Name: icalingua
Version: 2.4.6
Release:        1%{?dist}
Summary:  A Linux client for QQ and more

License: AGPL-3.0
URL:https://github.com/Icalingua/Icalingua
Source0: icalingua.asar
Source1: icalingua.desktop
Source2: icalingua.png
Source3: icalingua
Requires: nodejs-electron13-bin

%description
A Linux client for QQ and more

%prep



%build



%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/icalingua
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p  %{buildroot}/usr/share/icons/icalingua
cp   %{SOURCE0} %{buildroot}/usr/lib/icalingua/
cp   %{SOURCE1} %{buildroot}/usr/share/applications/
cp   %{SOURCE2} %{buildroot}/usr/share/icons/icalingua/
cp   %{SOURCE3} %{buildroot}/usr/bin/
rm -rf {_builddir}/*
%check


%files
 /usr/bin/icalingua
   /usr/lib/icalingua/icalingua.asar
   /usr/share/icons/icalingua/icalingua.png
   /usr/share/applications/icalingua.desktop



%changelog

