#include <Python.h>
#include <stdio.h>

/** 
Une fois importe, le module definit deux fonctions :
    - exemple qui prend une chaine en argument et retourne 0
    - exemple2 qui leve une exception creee pour l'occasion 
*/



static PyObject* ExempleErreur;

static PyObject* exemple (PyObject* self, PyObject* args)
{
  const char* chaine;

  if (!PyArg_ParseTuple (args, "s", &chaine))
    return NULL;

  return Py_BuildValue("i", 2); 
}

static PyObject* exemple2(PyObject* self, PyObject* args)
{
  //const char* chaine ;

  PyErr_SetString (ExempleErreur, "Exemple de levée d'erreur") ;
  return NULL;
}

////////////////////////////////////////////////////
//////////// export des fonctions //////////////////
////////////////////////////////////////////////////

const char * module_name = "sample_module" ;
char buffer [100] ;

static PyMethodDef fonctions [] = {
  {"exemple",   exemple,    METH_VARARGS, "Un commentaire"},
  {"exemple2",  exemple2,   METH_VARARGS, "Une methode levant une exception"},
  {NULL, NULL, 0, NULL}
} ;

PyMODINIT_FUNC initsample_module(void)
{
  PyObject* m ;
  m = Py_InitModule (module_name, fonctions) ;
  
  
  sprintf (buffer, "%s.Exception", module_name) ;
  ExempleErreur = PyErr_NewException(buffer, NULL, NULL) ;
  Py_INCREF (ExempleErreur) ;
  PyModule_AddObject (m, "Exception", ExempleErreur) ;
}
