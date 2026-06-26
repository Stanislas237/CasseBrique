#define MyAppName "Casse Brique"
#define MyAppVersion "1.0"
#define MyAppPublisher "Stan.co"
#define MyAppExeName "Casse Brique.exe"

[Setup]
AppId={{BreakOut-Setup}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

AppPublisherURL=https://portfolio-stanco.web.app/
AppSupportURL=https://portfolio-stanco.web.app/contact.html
AppUpdatesURL=https://t.me/boost/unity_engine_stan_co

VersionInfoVersion=1.0
VersionInfoCompany=Stan.co
VersionInfoDescription=Casse Brique Installer
VersionInfoProductName=Casse Brique
VersionInfoProductVersion=1.0

ArchitecturesInstallIn64BitMode=x64compatible

PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog

DefaultDirName={autopf}\Casse Brique
DefaultGroupName=Casse Brique

OutputDir=Setup
OutputBaseFilename=CasseBriqueSetup

Compression=lzma2
SolidCompression=yes
LZMAUseSeparateProcess=yes
LZMADictionarySize=65536

WizardStyle=modern

SetupIconFile=blast.ico

WizardImageFile=Banner.bmp
WizardSmallImageFile=blast.bmp

LicenseFile=welcome.txt

DisableProgramGroupPage=yes

UninstallDisplayIcon={app}\{#MyAppExeName}

[Tasks]
Name: "desktopicon"; Description: "Create a Desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]

; Game files
Source: "Casse Brique.exe"; DestDir: "{app}"

; Music
Source: "font.wav"; Flags: dontcopy

[Icons]
Name: "{group}\Casse Brique"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\Casse Brique"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch Casse Brique"; Flags: nowait postinstall skipifsilent

[Code]

function sndPlaySound(lpszSoundName: string; uFlags: LongWord): LongBool;
  external 'sndPlaySoundW@winmm.dll stdcall';

procedure InitializeWizard();
begin
  ExtractTemporaryFile('font.wav');
  sndPlaySound(ExpandConstant('{tmp}\font.wav'), $0001 or $0008);
end;

procedure DeinitializeSetup();
begin
  sndPlaySound('',0);
end;