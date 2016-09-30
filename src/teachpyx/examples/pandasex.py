# -*- coding: utf-8 -*-
"""
@file
@brief Quelques exemples autour de `pandas <http://pandas.pydata.org/>`_.
"""
import numpy
from pandas import Index


def pandas_fillna(df, by, hasna=None):
    """
    replace the nan value for something not nan

    @param      df      dataframe
    @param      by      list of columns for which we need to replace nan
    @param      hasna   None or list of columns for which we need to replace NaN
    @return             list of values chosen for each column, new dataframe (new copy)
    """
    df = df.copy()
    rep = {}
    for c in by:
        if hasna is not None and c not in hasna:
            continue
        if df[c].dtype in (str, bytes, object):
            se = set(df[c].dropna())
            val = se.pop()
            if isinstance(val, str):
                cst = "²"
            elif isinstance(val, bytes):
                cst = b"_"
            else:
                raise TypeError(
                    "Unable to determine a constant for type='{0}' dtype='{1}'".format(val, df[c].dtype))
            val += cst
            while val in se:
                val += "²"
            df[c].fillna(val, inplace=True)
            rep[c] = val
        else:
            dr = df[c].dropna()
            mi = abs(dr.min())
            ma = abs(dr.max())
            val = ma + mi
            if val <= ma:
                raise ValueError(
                    "Unable to find a different value for column '{0}': min={1} max={2}".format(val, mi, ma))
            df[c].fillna(val, inplace=True)
            rep[c] = val
    return rep, df


def pandas_groupby_nan(df, by, axis=0, as_index=False, **kwargs):
    """
    Does a groupby by keeping missing values.

    @param      df          dataframe
    @param      by          column or list of columns
    @param      axis        only 0 is allowed
    @param      as_index    should be False
    @param      kwargs      other parameters sent to
                            `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_
    @return                 groupby results

    See `groupby and missing values <http://pandas-docs.github.io/pandas-docs-travis/groupby.html#na-and-nat-group-handling>`_.

    .. faqref::
        :title: pandas.Dataframe.groupby does not consider missing values
        :tag: pandas

        Tout est dans le notebook :ref:`pandasgroupbyrst`.
    """
    if axis != 0:
        raise NotImplementedError("axis should be 0")
    if as_index:
        raise NotImplementedError("as_index must be False")
    if isinstance(by, tuple):
        raise TypeError("by should be of list not tuple")
    if not isinstance(by, list):
        by = [by]
    hasna = {}
    for b in by:
        h = df[b].isnull().values.any()
        if h:
            hasna[b] = True
    if len(hasna) > 0:
        rep, df_copy = pandas_fillna(df, by, hasna)
        res = df_copy.groupby(by, axis=axis, as_index=as_index, **kwargs)
        if len(by) == 1:
            for b in by:
                fnan = rep[b]
                if fnan in res.grouper.groups:
                    res.grouper.groups[numpy.nan] = res.grouper.groups[fnan]
                    del res.grouper.groups[fnan]
                new_val = list((numpy.nan if b == fnan else b)
                               for b in res.grouper.result_index)
                res.grouper.groupings[0]._group_index = Index(new_val)
                res.grouper.groupings[0].obj[b].replace(
                    fnan, numpy.nan, inplace=True)
                if isinstance(res.grouper.groupings[0].grouper, numpy.ndarray):
                    res.grouper.groupings[0].grouper = numpy.array(new_val)
                else:
                    raise NotImplementedError("Not implemented for type: {0}".format(
                        type(res.grouper.groupings[0].grouper)))
                res.grouper._cache[
                    'result_index'] = res.grouper.groupings[0]._group_index
        else:
            raise NotImplementedError("index={0}\ngroups={1}".format(res.grouper.result_index,
                                                                     res.grouper.groups))
        return res
    else:
        return df.groupby(by, axis=axis, **kwargs)
