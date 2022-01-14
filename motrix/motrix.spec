Name:           motrix
Version:        1.6.11
Release:        2
Summary:        A full-featured download manager.
License:        MIT
Url:            https://github.com/agalwood/Motrix
Source0:        https://github.com/agalwood/Motrix/archive/refs/tags/v%{version}.tar.gz
Source1:        motrix-launcher.sh
Source2:        motrix.desktop
Source3:        motrix.xml
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  yarnpkg
# for patch
BuildRequires:  wget

Requires:       electron11

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none

%description
A full-featured download manager.

%prep
%setup -q -n Motrix-%{version} -a 0
%define BUILD_DIR %{_builddir}/Motrix-%{version}/

%build
cd %{BUILD_DIR}
# patch time
rm yarn.lock package.json
wget https://raw.githubusercontent.com/agalwood/Motrix/51b1be7bbc85f0df9206a0d6e571a95b22e2a2a7/package.json
wget https://raw.githubusercontent.com/agalwood/Motrix/51b1be7bbc85f0df9206a0d6e571a95b22e2a2a7/yarn.lock
# real build
yarn
yarn run build:dir

%install
mkdir -p "%{buildroot}/usr/bin"
cd "%{BUILD_DIR}"
install -Dm644 release/linux-unpacked/resources/app.asar -t "%{buildroot}/usr/lib/motrix/"
cp -r release/linux-unpacked/resources/engine "%{buildroot}/usr/lib/motrix/"
install -Dm644 static/512x512.png "%{buildroot}/usr/share/icons/hicolor/512x512/apps/motrix.png"
install -Dm755 %{SOURCE1} "%{buildroot}/usr/bin/motrix"
install -Dm644 %{SOURCE2} "%{buildroot}/usr/share/applications/motrix.desktop"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/mime/packages/motrix.xml"

%post
%postun

%files
%{_bindir}/motrix
/usr/lib/motrix
/usr/share/applications/motrix.desktop
/usr/share/icons/hicolor/512x512/apps/motrix.png
/usr/share/mime/packages/motrix.xml

%changelog

