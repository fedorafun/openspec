Name:       deepin-wine-all-in-one
Version:    1.0
Release:    2
Summary:    deepin-wine-all-in-one RPM repacking
Requires:    p7zip-plugins, libncurses.so.5, curl, libudis86.so.0
Group:      Applications/Emulators                         
License:    GPL
URL:        N/A

%description
Both deepin-wine_2.18-23 and deepin-wine_5.0-11 packed in a single RPM on fedora 32 x86-64 distros

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%install
cd %_builddir/deepin-wine/tmp_extract/
cp -r ./ %{buildroot}/

%files
%defattr (-,root,root)
/usr/lib/*
/usr/bin/*
/usr/share/*
/opt/*

%changelog
* Sat Oct 8 2020 v21 - 1.0-2 require(s) of libncurses.so.5, 
* some man page doc removed to prevent the confliction from occuring,
* both deepin-wine2.18-23 and deepin-wine5.0-11 packed in a single RPM.
- Update to 1.0-2
* Sat Oct 8 2020 v21 - 1.0-1 require(s) of libudis86.so.0 added
- Update to 1.0-1
