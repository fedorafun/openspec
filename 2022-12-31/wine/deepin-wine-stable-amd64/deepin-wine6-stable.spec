Name: deepin-wine6-stable 
Version: 6.0.0.24
Release: 1
Summary:Deepin wine6 stable 

License: None
URL: https://deepin-wine.org
Source0: https://com-store-packages.uniontech.com/appstore/pool/appstore/d/deepin-wine6-stable/deepin-wine6-stable_%{version}-%{release}_amd64.deb
Source1:https://com-store-packages.uniontech.com/appstore/pool/appstore/d/deepin-wine6-stable/deepin-wine6-stable-amd64_%{version}-%{release}_amd64.deb
Source2:https://com-store-packages.uniontech.com/appstore/pool/appstore/d/deepin-wine6-stable/deepin-wine6-stable-i386_%{version}-%{release}_i386.deb
BuildRequires: tar
Requires: alsa-lib dbus ffmpeg p7zip-plugins, libncurses.so.5, curl, libudis86.so.0 

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog

