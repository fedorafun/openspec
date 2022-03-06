Name: icalingua++
Version:2.5.3
Release:        1%{?dist}
Summary: A Linux client for QQ and more 

License: AGPL-3.0
URL:  https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0: https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v%{version}/icalingua-%{version}.x86_64.rpm
Source1:icalingua.desktop 
Source2:icalingua++_launcher
Requires:nodejs-electron13-bin

%description
 A Linux client for QQ and more

%prep
rpm2cpio %{SOURCE0} | cpio -div


%build




%install
mkdir -p %{buildroot}/usr/lib
mv %{_builddir}/opt/Icalingua++/resources/app.asar  %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/bin/
mv %{_builddir}/usr/share %{buildroot}/usr
install -D -m 755 %{SOURCE2} %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/icalingua.desktop
cp %{SOURCE1} %{buildroot}/usr/share/applications/


%check


%files
/usr/bin/icalingua++_launcher
/usr/lib/app.asar
/usr/share/applications/icalingua.desktop
/usr/share/icons/


%changelog

