%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name core

Name: cutefish-%{component_name}
Version: 0.8
Release: 1%{?dist}
License: GPLv3
Summary: System components, backend, and session files for Cutefish Desktop

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: polkit-devel polkit-qt5-1-devel libSM-devel
BuildRequires: pkgconfig(xorg-libinput) 
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-devel xcb-util-image-devel xcb-util-keysyms-devel libXtst-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-qtbase-devel qt5-qtx11extras-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: fishui-devel

Requires: pulseaudio-daemon
Requires: fishui

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
System components, backend, and session files for the Cutefish Desktop

%prep
%setup -qn %{component_name}-%{version}

%build
%{set_build_flags}
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%files
%{_bindir}/chotkeys
%{_bindir}/cupdatecursor
%{_bindir}/cutefish-cpufreq
%{_bindir}/cutefish-polkit-agent
%{_bindir}/cutefish-powerman
%{_bindir}/cutefish-screen-brightness
%{_bindir}/cutefish-session
%{_bindir}/cutefish-settings-daemon
%{_bindir}/cutefish-shutdown
%{_bindir}/cutefish-xembedsniproxy
%{_datadir}/cutefish-polkit-agent
%{_datadir}/cutefish-settings-daemon
%{_datadir}/cutefish-shutdown
%{_datadir}/polkit-1/actions/org.cutefish.brightness.pkexec.policy
%{_datadir}/polkit-1/actions/org.cutefish.cpufreq.pkexec.policy
%{_datadir}/xsessions/cutefish-xsession.desktop
%{_sysconfdir}/xdg/autostart/cutefish-polkit-agent.desktop
