Name: icalingua++
Version:2.5.3
Release:        1%{?dist}
Summary: A Linux client for QQ and more 

License: AGPL
URL:  https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0: https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v%{version}/icalingua-%{version}.x86_64.rpm
Source1: 
BuildRequires: nodejs-electron13-bin
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

