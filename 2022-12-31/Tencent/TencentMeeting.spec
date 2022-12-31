Name:TencentMeeting
Version: 3.10.0.400
Release: 2
Summary:  Wemeet - Tencent Video Conferencing
License: None
URL: https://meeting.tencent.com/download-center.html
Source0: TencentMeeting_0300000000_%{version}_x86_64_default.publish.deb
Source1: wemeetapp.sh
Requires:  nss libX11 desktop-file-utils pulseaudio-libs 
Requires:  patchelf bubblewrap 
Requires:  qt5-qtwebengine qt5-qtx11extras

AutoReqProv: no

%description
Global cross-border video conferencing just got better! Wemeet breaks down borders, providing smooth, secure, and reliable cloud-based video conferencing  across over 100 countries around the world.
 Easily schedule or join meetings with crystal clear audio and HD video quality. And effectively collaborate across global teams through instant messaging, screen and document sharing, and much more!


%prep
ar -x %{SOURCE0}
tar xf data.tar.xz
cd ${builddir}/usr/share/applications
    sed -i 's|^Exec=.*|Exec=wemeet %u|g;s|^Icon=.*|Icon=wemeet|g' ${_pkgname}app.desktop
    sed -i '$i Comment=Tencent Meeting Linux Client\nComment[zh_CN]=腾讯会议Linux客户端\nKeywords=wemeet;tencent;meeting;' \
        "${_builddir}/usr/share/applications/wemeetapp.desktop"

cd ${srcdir}/opt/${_pkgname}

    for res in {16,32,64,128,256}
    do
        mkdir -p ${_builddir}/usr/share/icons/hicolor/${res}x${res}/apps;
        mv icons/hicolor/${res}x${res}/mimetypes/%{name}/app.png \
            %{_builddir}/usr/share/icons/hicolor/${res}x${res}/apps/${_pkgname}app.png;
    done



%pre


%build




%install



%post

%preun

%postun

%files
/opt/wemeet/
/usr/share/applications/wemeetapp.desktop




