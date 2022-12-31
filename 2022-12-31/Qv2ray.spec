Name: qv2ray-git
Version: 3.0.0
Release:        1%{?dist}
Summary: A cross platform connection manager for V2Ray and other backends 
Packager: llozi

License:  GPLv3
URL: https://github.com/Shadowsocks-NET/Qv2ray
Source0: SingleApplication.tar.gz
Source1: QCodeEditor.tar.gz
Source2: qt-qrcode.tar.gz
Source3: libRoutingA.tar.gz
Source4: libqrencode.tar.gz
BuildRequires: cmake gcc git make 
BuildRequires: ninja-build qt6-qtbase  qt6-qtsvg
Requires: 

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

