Name: typora
Version: 1.0.3 
Release: 1
Summary: Markdown Editor
License: custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."
URL: https://typora.io/
Packager: llozi
Source0: https://typora.io/linux/typora_*_amd64.deb
Requires: libXScrnSaver

%define _build_id_links none

AutoReqProv: no

%description
a minimal Markdown reading & writing app. Change Log: (https://typora.io/windows/dev_release.html)

%prep
ar x %{SOURCE0}
tar -xf data.tar.xz

%install
cp -R ~/rpmbuild/BUILD/usr %{buildroot}

%pre

%post

%preun

%postun

%files
/usr/bin/typora
/usr/share/applications/typora.desktop
/usr/share/doc/typora/copyright
/usr/share/icons/hicolor/32x32/apps/typora.png
/usr/share/icons/hicolor/64x64/apps/typora.png
/usr/share/icons/hicolor/128x128/apps/typora.png
/usr/share/icons/hicolor/256x256/apps/typora.png
/usr/share/typora/
 /usr/share/lintian/overrides/typora
