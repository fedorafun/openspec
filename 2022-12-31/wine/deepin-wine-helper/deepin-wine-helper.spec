Name: deepin-wine-helper
Version: 5.1.42
Release:        1
Summary: "Deepin Wine Helper"

License: None
URL: http://www.deepin.org
Source0:https://community-store-packages.deepin.com/appstore/pool/appstore/d/%{name}/%{name}_%{version}-%{release}_i386.deb

BuildRequires: tar 
Requires: tar 

%description


%prep
ar -x %{SOURCE0}
tar xf data.tar.xz
rm -r %{_builddir}/etc


%build




%install
mv %{_builddir}/opt/ %{buildroot}
mv %{_builddir}/usr/ %{builddir}


%check


%files
/opt/deepinwine/




%changelog

