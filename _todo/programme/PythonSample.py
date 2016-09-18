import sys
if "PythonSample" not in sys.modules :
    PythonSample = imp.load_dynamic ('PythonSample', PythonSample.dll) 
    sys.modules ["PythonSample"]  = PythonSample