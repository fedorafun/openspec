Name:TencentMeeting
Version: 3.10.0.400
Release: 1
Summary:  Wemeet - Tencent Video Conferencing
License: None
URL: https://meeting.tencent.com/download-center.html
Source0: wemeet-bin-%{version}-%{release}-x86_64.pkg.tar.zst
Requires:  nss libX11 desktop-file-utils pulseaudio-libs 
Requires:  patchelf bubblewrap 
Requires:  qt5-qtwebengine qt5-qtx11extras

AutoReqProv: no

%description
Global cross-border video conferencing just got better! Wemeet breaks down borders, providing smooth, secure, and reliable cloud-based video conferencing  across over 100 countries around the world.
 Easily schedule or join meetings with crystal clear audio and HD video quality. And effectively collaborate across global teams through instant messaging, screen and document sharing, and much more!
%prep
tar xf %{SOURCE0}


%pre


%build

%install
mv %{_builddir}/opt %{buildroot}
mv %{_builddir}/usr %{buildroot}


%post

%preun

%postun

%files
/opt/wemeet/
/usr/share/applications/wemeetapp.desktop
/usr/bin/wemeet
/usr/lib/wemeet/*
/usr/share/icons/hicolor/128x128/apps/wemeetapp.png
/usr/share/icons/hicolor/16x16/apps/wemeetapp.png
/usr/share/icons/hicolor/256x256/apps/wemeetapp.png
/usr/share/icons/hicolor/32x32/apps/wemeetapp.png
/usr/share/icons/hicolor/64x64/apps/wemeetapp.png
/usr/share/icons/hicolor/scalable/apps/wemeet.svg
