Name: cutefish-terminal
Version: 0.7
Release:        1%{?dist}
Summary: A terminal emulator for Cutefish.

License:  GPLv3
URL: https://github.com/cutefishos/terminal#third-party-code
Source0: https://codeload.github.com/cutefishos/terminal/zip/refs/heads/main

BuildRequires: cmake 
BuildRequires: qt5-qtbase-devel qt5-qtx11extras-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
Requires: cutefish-ui 

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

