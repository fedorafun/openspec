Name: deepin-udis86
Version: 1.72
Release:        4
Summary:Deepin-wine

License: None
URL:https://www.deepin.org
Source0:https://community-packages.deepin.com/deepin/pool/non-free/u/udis86/udis86_%{version}-%{release}_i386.deb

BuildRequires: tar
Requires: tar

%description


%prep
ar -x %{SOURCE0} 
tar xf data.tar.xz 


%build




%install
mv %{_builddir}/usr %{buildroot}


%check


%files
/usr/bin/udcli
/usr/include/libudis86/*
/usr/include/udis86.h
/usr/lib/libudis86.so
/usr/lib/libudis86.so.0
/usr/lib/libudis86.so.0.0.0
/usr/share/doc/udis86/*



%changelog

