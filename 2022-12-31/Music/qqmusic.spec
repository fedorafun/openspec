Name: qqmusic-bin
Version: 1.1.3
Release: 1%{?dist}
Summary: qqmusic for linux
License: None
URL: https://y.qq.com/download/download.html
Packager: llozi
Source0:  https://dldir1.qq.com/music/clntupate/linux/deb/qqmusic_%{version}_amd64.deb
Source1: qqmusic.desktop
Requires: gtk3,libXScrnSaver,nss

%define _build_id_links none

AutoReqProv: no

%description
Tencent QQMusic

%prep
ar x %{SOURCE0}
tar -xf data.tar.xz

%install
mkdir -p %{buildroot}
cp -R ~/rpmbuild/BUILD/opt %{buildroot}
cp -R ~/rpmbuild/BUILD/usr %{buildroot}
rm -rf  %{buildroot}/usr/share/doc
rm -rf %{buildroot}/usr/share/applications/qqmusic.desktop
cp %{SOURCE1} %{buildroot}/usr/share/applications/
%pre

%post

%preun

%postun

%files
/opt/qqmusic/
/usr/share/applications/
/usr/share/icons/hicolor/



