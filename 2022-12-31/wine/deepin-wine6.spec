Name:       deepin-wine6
Version:    1.0
Release:    2
Summary:    deepin-wine6 RPM repacking
Requires:   p7zip-plugins, libncurses.so.5, curl, libudis86.so.0
Group:      Applications/Emulators                         
License:    GPL
URL:        N/A

%description
deepin-wine6 packed in a single RPM on fedora x86-64 distros

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%install
cd %_builddir/deepin-wine6/
cp -r ./ %{buildroot}/

%files
%defattr (-,root,root)
/usr/share/*
/usr/bin/*
/opt/*

%changelog
* Thu Sep 16 2021 v21 - v1.0-2
- add some files missed
* Thu Sep 16 2021 v21 - v1.0-1
- first release
