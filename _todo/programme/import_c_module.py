# coding: latin-1
"""
import d'un module C (un fichier), inclut la recompilation 
si le module a évolué depuis sa dernière compilation
"""

import os, sys, re

def _find_compiled_file (path, name) :
    """cherche un fichier compilé"""
    ver         = sys.version_info
    st          = "%d.%d" % ver [:2]
    name        = os.path.splitext (name) [0]
    exp         = re.compile (name + "[.]o$")
    file, rep   = [], []
    for r, d, f in os.walk (path) :
        if st not in r : continue
        for a in f : 
            if exp.search (a) :
                return r,a
    return None,None

def import_c_module (name, mingw = r"c:\MinGW\bin", cpp = True, remove = False, path = None) :
    """
    @ingroup SQLAppModels    
    import d'un module C
    @param      name        nom du module C (nom du fichier sans extension, sans chemin non plus)
    @param      mingw       emplacement du compilateur mingw
    @param      cpp         c++ file?
    @param      remove      remove the file first before compiling
    @param      path        if the file is not found, try to look into this folder
    @return                 objet module
    
    @warning    remove = True must be used when the module is compiled for the first time. 
                Otherwise, the module is already loaded and impossible to remove until Python is closed.
    """
    if os.path.splitext (name) [1] == "" : 
        if cpp : 
            name += ".cpp"
            ext   = "cpp"
        else : 
            name += ".c"
            ext   = "c"
    else :
        ext = os.path.splitext (name) [1] [1:]
        
    mfile   = name
    mod     = os.path.splitext (mfile) [0]
    if path != None :
            mypath  = os.path.normpath (os.path.realpath (path))
            allpath = [mypath, "."]
    else :  allpath = ["."]
        
    for p in sys.path :
        if p not in allpath : allpath.append (p)
    
    for path in allpath :
        whole = os.path.join (path, name)
        if os.path.exists (whole) :
            break
    else :
        path_tried = u"\n".join (allpath)
        raise ImportError ("unable to find file %s in any import path:\n%s" \
                                % (name, path_tried))
        
    if sys.platform == "win32" : fsec = mod + ".pyd"
    else :                       fsec = mod + ".so"
        
    if path not in sys.path :
        sys.path.append (path)
        
    comp = os.path.join (path, fsec)
    if not os.path.exists (comp) :
        cond = True 
        resa = "not found"
    else :
        if remove :
            os.remove (comp)
            cond = True
            resa = "remove"
        else :
            r,f     = _find_compiled_file (path, mfile)
            if f != None :
                wholeo  = os.path.join (r,f)
                datec   = os.path.getmtime (whole)
                date    = os.path.getmtime (wholeo)
                cond    = datec > date
                resa    = "date"
            else :
                cond = True
                resa = "f == None"
                
    if cond :
        mfile = mod

        file =  ("""
                # coding: latin-1
                from distutils.core import setup
                from distutils.core import Extension

                setup(name          = '%s',
                      version       = '0.1',
                      ext_modules   = [Extension('%s', ['%s.%s']), ],
                      url           = '',
                      author        = '',
                      author_email  = '...',
                      )
                """ % (mfile,mfile,mfile,ext)).replace ("                ", "")
        wr   = os.path.join (path, "setup.py")
        f = open (wr, "w")
        f.write (file)
        f.close ()
        
        env = os.getenv ("PATH")
        if mingw not in env : 
            os.putenv ("PATH", env + ";" + mingw)
        
        cwd = os.getcwd ()
        os.chdir (path)
        
        py = sys.executable.replace ("pythonw.exe", "python.exe")
        if sys.platform == "win32" :    
                cmd  = "%s setup.py build_ext --inplace -c mingw32" % (py)
        else :  cmd  = "%s setup.py build_ext --inplace" % (py)
        child_stdin, stdout, child_stderr = os.popen3 (cmd)
        res = stdout.read ()
        err = child_stderr.read ()
        stdout.close ()
        
        os.chdir (cwd)
        
        if len (err) > 0 :
            message  = "\nOUTPUT:\n" + res + "\n\n"
            message += "ERR:\n" + err
            if "error" in err :
                message += "unable to compile %s (resa %s)\n%s" % (name, resa, message)
                print (message)
                raise ImportError (message)
            else :
                print (message)
            
        mod = __import__ (mfile)
        return mod
    
    else :
        mfile   = mod
        mod     = __import__ (mfile)
        return mod
    
if __name__ == "__main__" :
    sample_module = import_c_module ("sample_module", cpp = True)
    print sample_module

    print sample_module.exemple("e")
    print sample_module.exemple2() 