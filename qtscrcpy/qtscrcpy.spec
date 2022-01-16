Name:           qtscrcpy
Version:        1.8.1
Release:        1
Summary:        Android real-time display control software
License:        ASL-2.0
Url:            https://github.com/barry-ran/QtScrcpy
Source0:        https://github.com/barry-ran/QtScrcpy/archive/refs/tags/v%{version}.tar.gz
Source1:        qtscrcpy.desktop
Patch0:         qtscrcpy.pathfix.patch
BuildRequires:  qt5-qtx11extras-devel
Requires:       android-tools
Requires:       scrcpy

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
Android real-time display control software

%prep
%setup -q -n QtScrcpy-%{version}
%patch0
%define BUILD_DIR %{_builddir}/QtScrcpy-%{version}

%build
mkdir %{BUILD_DIR}/build
cd %{BUILD_DIR}/build
qmake-qt5 ../all.pro CONFIG+=qtquickcompiler
make qmake_all
sed -ie '/^CXXFLAGS/s/$/ -Wno-deprecated-declarations/' QtScrcpy/Makefile
make

%install
install -Dm755 %{BUILD_DIR}/output/release/QtScrcpy %{buildroot}/usr/bin/qtscrcpy
install -Dm644 %{S:1} -t %{buildroot}/usr/share/applications/
install -Dm644 %{BUILD_DIR}/backup/logo.png %{buildroot}/usr/share/pixmaps/qtscrcpy.png

install -Dm644 %{BUILD_DIR}/config/config.ini %{buildroot}/etc/qtscrcpy/config.ini
mkdir -p %{buildroot}/usr/share/qtscrcpy/keymap
mv %{BUILD_DIR}/keymap/* %{buildroot}/usr/share/qtscrcpy/keymap/


%post
%postun

%files
/etc/qtscrcpy/
%{_bindir}/qtscrcpy
/usr/share/applications/qtscrcpy.desktop
/usr/share/pixmaps/qtscrcpy.png
/usr/share/qtscrcpy/
/usr/share/qtscrcpy/keymap/
/usr/share/qtscrcpy/keymap/*

%changelog

