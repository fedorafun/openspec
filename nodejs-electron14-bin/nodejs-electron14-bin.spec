Name:           nodejs-electron14-bin
Version:        14.2.3
Release:        1
Summary:        Build cross-platform desktop apps with JavaScript, HTML, and CSS
License:        MIT
Url:            https://github.com/electron/electron
Source0:        https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-linux-x64.zip
Source1:        electron14-launcher.sh
Source2:        https://raw.githubusercontent.com/electron/electron/main/LICENSE

BuildRequires:  bsdtar

Provides:       nodejs-electron14 electron14

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none

AutoReqProv: no

%description
Build cross-platform desktop apps with JavaScript, HTML, and CSS

%prep
cp ${RPM_SOURCE_DIR}/LICENSE ${RPM_BUILD_DIR}/LICENSE

%build

%install
cd "$RPM_SOURCE_DIR"
install -dm755 "${RPM_BUILD_ROOT}/usr/lib/electron14"
bsdtar -xf %{SOURCE0} -C "${RPM_BUILD_ROOT}/usr/lib/electron14"

chmod u+s "${RPM_BUILD_ROOT}/usr/lib/electron14/chrome-sandbox"

install -Dm755 %{SOURCE1} "${RPM_BUILD_ROOT}/usr/bin/electron14"
%post
%postun

%files
%license LICENSE
%{_bindir}/electron14
/usr/lib/electron14/

%changelog

