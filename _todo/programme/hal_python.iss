; section non commentée
[Setup]
AppName=HalPython
AppVerName=HalPython 1.5.1162
AppPublisher=Xavier Dupré
AppPublisherURL=http://www.xavierdupre.fr/hal_python/hal_python_help_html/index.html
AppSupportURL=http://www.xavierdupre.fr/hal_python/hal_python_help_html/index.html
AppUpdatesURL=http://www.xavierdupre.fr/hal_python/hal_python_help_html/index.html
DefaultDirName={pf}/HalPython
DefaultGroupName=HalPython
OutputDir=D:\Dupre\_data\site\hal_python\executable
OutputBaseFilename=setup_HalPython_py25
Compression=lzma
SolidCompression=yes
VersionInfoVersion=1.0.0

[Code]

; cette fonction retourne le chemin d'installation de Python 2.5
; le résultat est vide si celui-ci n'a pas été installé
; le chemin est celui stocké dans la clé de registre 
;           HKLM\Software\Python\PythonCore\2.5\InstallPath
function GetPythonPath(Param: String): String;
begin
  Result := '';
  Result := ExpandConstant('{reg:HKLM\Software\Python\PythonCore\2.5\InstallPath,|}');
  if Result <> '' then
    Result := Result + '\pythonw.exe';
end;

; cette fonction retourne {win}\system32\msiexec.exe
; si Python 2.5 a été installé, vide sinon
function GetPythonPathExec(Param: String): String;
begin
  Result := GetPythonPath () ;
  if Result <> '' then
    Result := ExpandConstant('{win}\system32\msiexec.exe') ;
end;

; clés de registre
; mémorise le répertoire d'installation
; et le numéro de version
[Registry]
Root: HKLM; Subkey: "SOFTWARE\HalPython\InstallPath"; ValueType: string; ValueName: ""; 
        ValueData: "{app}"; Flags: uninsdeletekey
Root: HKLM; Subkey: "SOFTWARE\HalPython\Version"; ValueType: string; ValueName: ""; 
        ValueData: "1.5.1162"; Flags: uninsdeletekey

; icône sur le bureau
[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; 
     Flags: checkedonce

; fichiers
[Files]
; le module en question
Source: "..\hal_dll.dll"; DestDir: "{app}\hal_python";
Source: "..\hal_dll_ext.dll"; DestDir: "{app}\hal_python";
Source: "..\hal_dll_model.dll"; DestDir: "{app}\hal_python";
Source: "..\hal_python.dll"; DestDir: "{app}\hal_python";
Source: "..\wxwindows_old.dll"; DestDir: "{app}\hal_python";
Source: "..\boost_python.dll"; DestDir: "{app}\hal_python";
Source: "..\_graphviz_draw.exe"; DestDir: "{app}\hal_python";
Source: "..\_hal_script.exe"; DestDir: "{app}\hal_python";
Source: "..\hal_python.py"; DestDir: "{app}\hal_python";
Source: "..\install\__init__.py"; DestDir: "{app}\hal_python";
Source: "..\install\setup.py"; DestDir: "{app}";
Source: "..\_test\temp\hal_python.chm"; DestDir: "{app}";

; les fichiers annexes
Source: "hal_python.url"; DestDir: "{app}";    URL de l'application
Source: "pyscripter.chm"; DestDir: "{app}";    aide de l'éditeur PyScripter
Source: "PyScripter.exe"; DestDir: "{app}";    éditeur PyScripter
Source: "python-2.5.2.msi"; DestDir: "{app}";  installateur Python 2.5
Source: "sample.bat"; DestDir: "{app}";        fichier de commande
Source: "sample.py"; DestDir: "{app}";         exemple de programme

; création des icônes
[Icons]
Name: "{group}\PyScripter"; Filename: "{app}\PyScripter.exe"; WorkingDir: "{app}"
Name: "{group}\PyScripter Help"; Filename: "{app}\pyscripter.chm"; WorkingDir: "{app}"
Name: "{group}\Help"; Filename: "{app}\hal_python.chm"; WorkingDir: "{app}"
Name: "{group}\smallest sample with PyScripter"; Filename: "{app}\small_sample.bat"; WorkingDir: "{app}"
Name: "{group}\Website"; Filename: "{app}\hal_python.url"
Name: "{group}\uninstall"; Filename: "{uninstallexe}"; WorkingDir: "{app}"

[Run]
; installe Python 2.5 si GetPythonPathExec retourne un résultat non vide
; passe à l'instruction suivante sinon
Filename: "{code:GetPythonPathExec}"; Parameters: "/i ""{app}\python-2.5.2.msi"" /qr ALLUSERS=1"; 
          StatusMsg: "Installing Python 2.5..."; Flags: skipifdoesntexist
          
; installe le module  si GetPythonPath retourne un résultat non vide
; passe à l'instruction suivante sinon
; exécute en fait l'insttruction python setup.py install
Filename: "{code:GetPythonPath}"; Parameters:"setup.py install"; WorkingDir: "{app}"; 
          StatusMsg: "Installing HalPython for Python 2.5..."

; supprime l'installation de Python 2.5
Filename: "{cmd}"; Parameters: "/c del python-2.5.2.msi"; WorkingDir: "{app}";
