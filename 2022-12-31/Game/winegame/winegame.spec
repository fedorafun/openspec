Name: net.winegame.client-beta
Version: 0.5.10.2
Release: 1%{dist}
Summary: winegame
License: GPL-3.0+
URL:  https://winegame.net/
Packager: llozi
Source0: https://file.winegame.net/packages/debian/%{version}/net.winegame.client_%{version}_amd64.deb 
Requires:  python-gobject python3-pyyaml python-evdev  python-pillow  python-requests  python-dbus  python-distro   
Requires: python3-lxml python3-giacpy python3-setproctitle  python3-file-magic
Requires:gtk3 glib2 psmisc cabextract 
Requires:unzip  p7zip  tar  curl  wget aria2 
Requires:libXrandr  zenity 
Requires:mesa-demos vulkan-loader    vulkan-loader(x86-32)   vulkan-tools python3-lxml  
Requires:xorg-x11-xfs-utils collectd-notify_desktop 
Requires:glx-utils python3-distro  
Requires:fluid-soundfont-gs winetricks  gamemode

%description
The Sinicized and added Chinese source client based on 
lutris enables Chinese users to quickly download and install game!
%prep 
%build
ar x %{SOURCE0}
tar xf  data.tar.xz
%install
cp -R opt/ %{buildroot}   
cp -R usr/ %{buildroot}
%pre

%post

%preun

%postun

%files
/usr/share/
/opt/apps/net.winegame.client/
