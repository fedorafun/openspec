Name: termius
Version: 7.37.0
Release: 1
Summary: ssh
License: None
URL: https://termius.com/
Source0: https://www.termius.com/download/linux/Termius.deb
Source1: termius-app.desktop
Packager: llozi
Requires: gtk3   libnotify   nss  libXScrnSaver libXtst xdg-utils at-spi2-core libuuid libappindicator libappindicator-gtk3 libsecret

AutoReqProv: no

%description

%prep
ar -x %{SOURCE0}
tar -xf data.tar.xz

%install
mkdir -p %{buildroot}
cp -R ~/rpmbuild/BUILD/opt %{buildroot}
cp -R ~/rpmbuild/BUILD/usr %{buildroot}
rm -rf  %{buildroot}/usr/share/doc
rm -rf %{buildroot}/usr/share/applications/termius-app.desktop
cp %{SOURCE1} %{buildroot}/usr/share/applications/

%pre

%post

%preun

%postun

%files
/opt/Termius/
/usr/share/applications/termius-app.desktop
/usr/share/icons/hicolor/


