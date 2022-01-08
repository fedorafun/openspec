Name:           nodejs-electron11-bin
Version:        11.5.0
Release:        1
Summary:        Build cross-platform desktop apps with JavaScript, HTML, and CSS
License:        MIT
Url:            https://github.com/electron/electron
Source0:        https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-linux-x64.zip
Source1:        electron-launcher.sh
Source2:        https://raw.githubusercontent.com/electron/electron/main/LICENSE

BuildRequires:  bsdtar

Provides:       nodejs-electron11 electron11

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
install -dm755 "${RPM_BUILD_ROOT}/usr/lib/electron11"
bsdtar -xf %{SOURCE0} -C "${RPM_BUILD_ROOT}/usr/lib/electron11"

chmod u+s "${RPM_BUILD_ROOT}/usr/lib/electron11/chrome-sandbox"

install -Dm755 %{SOURCE1} "${RPM_BUILD_ROOT}/usr/bin/electron11"
%post
%postun

%files
%license LICENSE
%{_bindir}/electron11
/usr/lib/electron11/

%changelog

