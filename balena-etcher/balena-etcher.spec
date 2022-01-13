Name:           balena-etcher
Version:        1.7.3
Release:        1
Summary:        Flash OS images to SD cards & USB drives, safely and easily.
License:        ASL 2.0
Url:            https://github.com/balena-io/etcher
Source0:        https://github.com/balena-io/etcher/archive/refs/tags/v%{version}.tar.gz
Source1:        balena-etcher-electron.sh
Source2:        balena-etcher-electron.desktop
BuildRequires:  clang
BuildRequires:  nodejs
BuildRequires:  npm

Requires:       electron12
Requires:       libusb

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none
AutoReqProv: no

%description
Flash OS images to SD cards & USB drives, safely and easily.

%prep
%setup -q -n etcher-%{version} -a 0
%define BUILD_DIR %{_builddir}/etcher-%{version}/

%build
cd %{BUILD_DIR}
npm ci
npm run webpack
npm prune --production

%install
%define _appdir %{buildroot}/usr/lib/balena-etcher

cd %{BUILD_DIR}
install -d "%{_appdir}"

install package.json "%{_appdir}"
cp -a {lib,generated,node_modules} "%{_appdir}"
install -D assets/icon.png "%{_appdir}/assets/icon.png"
install -D lib/gui/app/index.html "%{_appdir}/lib/gui/app/index.html"

install -Dm755 %{SOURCE1} "%{buildroot}/usr/bin/balena-etcher-electron"
install -Dm644 %{SOURCE2} "%{buildroot}/usr/share/applications/balena-etcher-electron.desktop"

for size in 16x16 32x32 48x48 128x128 256x256 512x512; do
  install -Dm644 "assets/iconset/${size}.png" "%{buildroot}/usr/share/icons/hicolor/${size}/apps/balena-etcher-electron.png"
done

%post
%postun

%files
%{_bindir}/balena-etcher-electron
/usr/lib/balena-etcher
/usr/share/applications/balena-etcher-electron.desktop
/usr/share/icons/hicolor/*/apps/balena-etcher-electron.png
%changelog

