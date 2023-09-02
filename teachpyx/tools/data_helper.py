import os
import zipfile
from typing import List
from urllib.request import urlopen


def decompress_zip(filename, dest: str, verbose: bool = False) -> List[str]:
    """
    Unzips a zip file.

    :param filename: file to process
    :param dest: destination
    :param verbose: verbosity
    :return: return the list of decompressed files
    """
    try:
        fp = zipfile.ZipFile(filename, "r")
    except zipfile.BadZipFile as e:
        raise RuntimeError(f"Unable to unzip {filename!r}") from e
    files = []
    for info in fp.infolist():
        if not os.path.exists(info.filename):
            data = fp.read(info.filename)
            tos = os.path.join(dest, info.filename)
            if not os.path.exists(tos):
                finalfolder = os.path.split(tos)[0]
                if not os.path.exists(finalfolder):
                    if verbose:
                        print(f"creating folder {finalfolder!r}")
                    os.makedirs(finalfolder)
                if not info.filename.endswith("/"):
                    with open(tos, "wb") as u:
                        u.write(data)
                    files.append(tos)
                    if verbose:
                        print(f"unzipped {info.filename!r} to {tos!r}")
            elif not tos.endswith("/"):
                files.append(tos)
        elif not info.filename.endswith("/"):
            files.append(info.filename)
    return files


def download_and_unzip(
    url: str, dest: str = ".", timeout: int = 10, verbose: bool = False
) -> List[str]:
    """
    Downloads a file and unzip it.

    :param url: url
    :param dest: destination folder
    :param timeout: timeout
    :param verbose: display progress
    :return: list of unzipped files
    """
    filename = url.split("/")[-1]
    dest_zip = os.path.join(dest, filename)
    if not os.path.exists(dest_zip):
        if verbose:
            print(f"downloads into {dest_zip!r} from {url!r}")
        with urlopen(url, timeout=timeout) as u:
            content = u.read()
        with open(dest_zip, "wb") as f:
            f.write(content)
    elif verbose:
        print(f"already downloaded {dest_zip!r}")

    return decompress_zip(dest_zip, dest, verbose=verbose)
