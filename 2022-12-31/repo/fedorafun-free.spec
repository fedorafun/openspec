Name: fedorafun-free
Version: 1
Release:        1
Summary: fedorafun free repo
License: None
URL: https://www.github.com/fedorafun
Source0: fedorafun-free.repo

%description
Fedorafun free repo
%prep



%build



%install
mkdir -p %{_builddir}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/yum.repos.d/
install -D %{SOURCE0}  %{buildroot}/etc/yum.repos.d/



%check


%files
/etc/yum.repos.d/fedorafun-free.repo


%changelog

