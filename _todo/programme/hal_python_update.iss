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
OutputBaseFilename=setup_HalPython_update_py25
Compression=lzma
SolidCompression=yes
VersionInfoVersion=1.0.0

[Code]
function GetPythonPath(Param: String): String;
begin
  Result := '';
  Result := ExpandConstant('{reg:HKLM\Software\Python\PythonCore\2.5\InstallPath,|}');
  if Result <> '' then
    Result := Result + '\pythonw.exe';
end;

function GetHalPythonPath(Param: String): String;
begin
  Result := '';
  Result := ExpandConstant ('{reg:HKLM\Software\HalPython\InstallPath,|}') ;
end;

function InitializeSetup(): Boolean;
begin
  Result := True ;
  MsgBox (GetPythonPath (''), mbConfirmation, MB_OK) ;
  MsgBox (GetHalPythonPath (''), mbConfirmation, MB_OK) ;
  if GetPythonPath ('') = '' then begin
    MsgBox('Python 2.5 has not been installed. You should download 
            the complete Setup with Python 2.5 included instead of updating.', mbError, MB_OK) ;
    Result := False ;
  end else if GetHalPythonPath ('') = '' then begin
    MsgBox('HalPython for Python 2.5 has not been installed. 
            You should download the complete Setup with Python 2.5 included instead of updating.', 
            mbError, MB_OK) ;
    Result := False ;
  end
end;

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; 
      Flags: checkedonce

[Files]
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
Source: "hal_python.url"; DestDir: "{app}";
Source: "small_sample.bat"; DestDir: "{app}";
Source: "sample.py"; DestDir: "{app}";
Source: "..\_test\temp\hal_python.chm"; DestDir: "{app}";

[Registry]
Root: HKLM; Subkey: "SOFTWARE\HalPython\InstallPath"; ValueType: string; ValueName: ""; 
      ValueData: "{app}"; Flags: uninsdeletekey
Root: HKLM; Subkey: "SOFTWARE\HalPython\Version"; ValueType: string; ValueName: ""; 
      ValueData: "1.5.1162"; Flags: uninsdeletekey

[Icons]
Name: "{group}\PyScripter"; Filename: "{app}\PyScripter.exe"; WorkingDir: "{app}"
Name: "{group}\PyScripter Help"; Filename: "{app}\pyscripter.chm"; WorkingDir: "{app}"
Name: "{group}\Help"; Filename: "{app}\hal_python.chm"; WorkingDir: "{app}"
Name: "{group}\smallest sample with PyScripter"; Filename: "{app}\small_sample.bat"; WorkingDir: "{app}"
Name: "{group}\Website"; Filename: "{app}\hal_python.url"
Name: "{group}\uninstall"; Filename: "{uninstallexe}"; WorkingDir: "{app}"

[Run]
Filename: "{code:GetPythonPath}"; Parameters:"setup.py install"; WorkingDir: "{app}"; 
     StatusMsg: "Installing HalPython for Python 2.5..."
