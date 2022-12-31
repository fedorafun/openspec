Name: fedorafun-non-free
Version: 1
Release: 1
Summary: fedorafun non-free repo
License: None
URL: https://www.github.com/fedorafun
Source0: fedorafun-non-free.repo

%description
Fedorafun non-free repo
%prep



%build



%install
mkdir -p %{_builddir}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/yum.repos.d/
install -D %{SOURCE0}  %{buildroot}/etc/yum.repos.d/



%check


%files
/etc/yum.repos.d/fedorafun-non-free.repo


%changelog

