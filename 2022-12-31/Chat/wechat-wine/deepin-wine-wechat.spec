Name: deepin-wine-wechat
Version: 3.7.6.29
Release:        1%{?dist}
Summary: wine wechat

License: None 
URL: https://weixin.qq.com/
Source0: https://github.com/vufa/deepin-wine-wechat-arch/releases/download/v%{version}-1/deepin-wine-wechat-%{version}-1-x86_64.pkg.tar.zst
Source1: run.sh

Requires: p7zip wqy-microhei-fonts alsa-lib xwininfo  openal mpg123 mpg123-libs 

%description


%prep
tar xf %{SOURCE0}


%build


%install
rm %{_builddir}/opt/apps/com.qq.weixin.deepin/files/run.sh
cp %{SOURCE1} %{_builddir}/opt/apps/com.qq.weixin.deepin/files/
mv %{_builddir}/opt %{buildroot}
mv %{_builddir}/usr %{buildroot}
%check


%files
/opt/apps/com.qq.weixin.deepin/
/usr/share/applications/com.qq.weixin.deepin.desktop
/usr/share/icons/hicolor/16x16/apps/com.qq.weixin.deepin.svg
/usr/share/icons/hicolor/24x24/apps/com.qq.weixin.deepin.svg
/usr/share/icons/hicolor/32x32/apps/com.qq.weixin.deepin.svg
/usr/share/icons/hicolor/48x48/apps/com.qq.weixin.deepin.svg
/usr/share/icons/hicolor/64x64/apps/com.qq.weixin.deepin.svg

%changelog

