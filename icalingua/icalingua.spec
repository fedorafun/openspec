Name:           icalingua
Version:        2.4.5
Release:        1
Summary:        A Linux client for QQ and more
License:        AGPL-3.0
Url:            https://github.com/Icalingua/Icalingua
Source0:        https://github.com/Icalingua/Icalingua/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nodejs
BuildRequires:  clang
BuildRequires:  yarnpkg
Recommends:     ffmpeg

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none

%description
A Linux client for QQ and more

%prep
%autosetup -n Icalingua-%{version}
%define BUILD_DIR %{_builddir}/Icalingua-%{version}/icalingua

%build
cd %{BUILD_DIR}
export ELECTRON_MIRROR='https://npm.taobao.org/mirrors/electron/'
export SASS_BINARY_SITE='https://npm.taobao.org/mirrors/node-sass'
yarn
yarn run build:dir

%install
mkdir -p "%{buildroot}/opt/icalingua"
mkdir -p "%{buildroot}/usr/bin"
cd "%{BUILD_DIR}"
cp -a build/linux-unpacked/* "%{buildroot}/opt/icalingua"
cd "%{_builddir}/Icalingua-%{version}/pkgres"
install -Dm644 512x512.png "%{buildroot}/usr/share/icons/hicolor/512x512/apps/icalingua.png"
install -Dm644 icalingua.desktop "%{buildroot}/usr/share/applications/icalingua.desktop"
ln -s "/opt/icalingua/icalingua" "%{buildroot}/usr/bin/icalingua"

%post
%postun

%files
/opt/icalingua
/usr/bin/icalingua
/usr/share/applications/icalingua.desktop
/usr/share/icons/hicolor/512x512/apps/icalingua.png

%changelog
