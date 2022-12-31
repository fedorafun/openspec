Name: xiaomitool
Version: 20.7.28 
Release:        1%{?dist}
Summary: Modding of Xiaomi devices made easy for everyone
Packager: llozi
License: None
URL:https://www.xiaomitool.com/V2/
Source0:https://github.com/francescotescari/XMT/releases/download/v%{version}/XMT2*Linux*%{version}.run
Source1:xiaomitool
Source2:xiaomitool.appdata.xml
Source3:xiaomitool.desktop
Source4:xiaomitool.menu
Source5:xiaomitool.xml

AutoReqProv: no

%description


%prep



%build



%install
sh %{SOURCE0} --noexec --keep --nox11

mkdir -p %{buildroot}/opt

mv XiaoMiTool-V2 %{buildroot}/opt

mkdir -p %{buildroot}/usr/bin

mkdir -p %{buildroot}/usr/share/appdata

mkdir %{buildroot}/usr/share/applications

mkdir -p %{buildroot}/usr/share/gnome-control-center/default-apps

mkdir -p %{buildroot}pkgdir/usr/share/menu


install -m755 %{SOURCE1} %{buildroot}/usr/bin

install -m644 %{SOURCE2} %{buildroot}/usr/share/appdata

install -m644 %{SOURCE3} %{buildroot}/usr/share/applications

install -m644 %{SOURCE5} %{buildroot}/usr/share/gnome-control-center/default-apps

install -m644 %{SOURCE4} %{buildroot}/usr/share/menu

rm -rf BUILDROOT
rm -rf %{BUILD}/*
%check


%files
/opt/XiaoMiTool-V2/XiaoMiTool.jar
   /opt/XiaoMiTool-V2/bin/java
   /opt/XiaoMiTool-V2/bin/jrunscript
   /opt/XiaoMiTool-V2/bin/keytool
   /opt/XiaoMiTool-V2/conf/logging.properties
   /opt/XiaoMiTool-V2/conf/net.properties
   /opt/XiaoMiTool-V2/conf/sdp/sdp.conf.template
   /opt/XiaoMiTool-V2/conf/security/java.policy
   /opt/XiaoMiTool-V2/conf/security/java.security
   /opt/XiaoMiTool-V2/conf/security/policy/README.txt
   /opt/XiaoMiTool-V2/conf/security/policy/limited/default_US_export.policy
   /opt/XiaoMiTool-V2/conf/security/policy/limited/default_local.policy
   /opt/XiaoMiTool-V2/conf/security/policy/limited/exempt_local.policy
   /opt/XiaoMiTool-V2/conf/security/policy/unlimited/default_US_export.policy
   /opt/XiaoMiTool-V2/conf/security/policy/unlimited/default_local.policy
   /opt/XiaoMiTool-V2/conf/sound.properties
   /opt/XiaoMiTool-V2/lib/classlist
   /opt/XiaoMiTool-V2/lib/javafx-swt.jar
   /opt/XiaoMiTool-V2/lib/javafx.properties
   /opt/XiaoMiTool-V2/lib/jexec
   /opt/XiaoMiTool-V2/lib/jrt-fs.jar
   /opt/XiaoMiTool-V2/lib/jspawnhelper
   /opt/XiaoMiTool-V2/lib/jvm.cfg
   /opt/XiaoMiTool-V2/lib/libavplugin-54.so
   /opt/XiaoMiTool-V2/lib/libavplugin-56.so
   /opt/XiaoMiTool-V2/lib/libavplugin-57.so
   /opt/XiaoMiTool-V2/lib/libavplugin-ffmpeg-56.so
   /opt/XiaoMiTool-V2/lib/libavplugin-ffmpeg-57.so
   /opt/XiaoMiTool-V2/lib/libavplugin-ffmpeg-58.so
   /opt/XiaoMiTool-V2/lib/libawt.so
   /opt/XiaoMiTool-V2/lib/libawt_headless.so
   /opt/XiaoMiTool-V2/lib/libawt_xawt.so
   /opt/XiaoMiTool-V2/lib/libdecora_sse.so
   /opt/XiaoMiTool-V2/lib/libfontmanager.so
   /opt/XiaoMiTool-V2/lib/libfxplugins.so
   /opt/XiaoMiTool-V2/lib/libglass.so
   /opt/XiaoMiTool-V2/lib/libglassgtk2.so
   /opt/XiaoMiTool-V2/lib/libglassgtk3.so
   /opt/XiaoMiTool-V2/lib/libgstreamer-lite.so
   /opt/XiaoMiTool-V2/lib/libj2pkcs11.so
   /opt/XiaoMiTool-V2/lib/libjava.so
   /opt/XiaoMiTool-V2/lib/libjavafx_font.so
   /opt/XiaoMiTool-V2/lib/libjavafx_font_freetype.so
   /opt/XiaoMiTool-V2/lib/libjavafx_font_pango.so
   /opt/XiaoMiTool-V2/lib/libjavafx_iio.so
   /opt/XiaoMiTool-V2/lib/libjavajpeg.so
   /opt/XiaoMiTool-V2/lib/libjawt.so
   /opt/XiaoMiTool-V2/lib/libjfxmedia.so
   /opt/XiaoMiTool-V2/lib/libjfxwebkit.so
   /opt/XiaoMiTool-V2/lib/libjimage.so
   /opt/XiaoMiTool-V2/lib/libjli.so
   /opt/XiaoMiTool-V2/lib/libjsig.so
   /opt/XiaoMiTool-V2/lib/libjsound.so
   /opt/XiaoMiTool-V2/lib/liblcms.so
   /opt/XiaoMiTool-V2/lib/libmlib_image.so
   /opt/XiaoMiTool-V2/lib/libnet.so
   /opt/XiaoMiTool-V2/lib/libnio.so
   /opt/XiaoMiTool-V2/lib/libprefs.so
   /opt/XiaoMiTool-V2/lib/libprism_common.so
   /opt/XiaoMiTool-V2/lib/libprism_es2.so
   /opt/XiaoMiTool-V2/lib/libprism_sw.so
   /opt/XiaoMiTool-V2/lib/libsplashscreen.so
   /opt/XiaoMiTool-V2/lib/libsunec.so
   /opt/XiaoMiTool-V2/lib/libverify.so
   /opt/XiaoMiTool-V2/lib/libzip.so
   /opt/XiaoMiTool-V2/lib/modules
   /opt/XiaoMiTool-V2/lib/psfont.properties.ja
   /opt/XiaoMiTool-V2/lib/psfontj2d.properties
   /opt/XiaoMiTool-V2/lib/security/blacklisted.certs
   /opt/XiaoMiTool-V2/lib/security/cacerts
   /opt/XiaoMiTool-V2/lib/security/default.policy
   /opt/XiaoMiTool-V2/lib/security/public_suffix_list.dat
   /opt/XiaoMiTool-V2/lib/server/libjsig.so
   /opt/XiaoMiTool-V2/lib/server/libjvm.so
   /opt/XiaoMiTool-V2/lib/tzdb.dat
   /opt/XiaoMiTool-V2/res/tmp/.instance.lock
   /opt/XiaoMiTool-V2/res/tmp/logs/xmt2log_1573743348259.txt
   /opt/XiaoMiTool-V2/res/tmp/logs/xmt2log_1573743418868.txt
   /opt/XiaoMiTool-V2/res/tmp/settings.app
   /opt/XiaoMiTool-V2/res/tools/adb
   /opt/XiaoMiTool-V2/res/tools/fastboot
   /opt/XiaoMiTool-V2/res/tools/libc++.so
   /usr/bin/xiaomitool
   /usr/share/appdata/xiaomitool.appdata.xml
   /usr/share/applications/xiaomitool.desktop
   /usr/share/gnome-control-center/default-apps/xiaomitool.xml
   /usr/share/menu





%changelog

