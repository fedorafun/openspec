Name: Gtk-Chat
Version: 0.0.1
Release:        1%{?dist}
Summary: A Gtk application for Chatting with your friends
License: GPL v3.0
URL: https://gitlab.com/weiliang1503/gtk-chat
Source0: https://gitlab.com/weiliang1503/gtk-chat/-/archive/master/gtk-chat-master.tar.gz

BuildRequires: meson  libsoup-devel gcc wget vala ninja-build
BuildRequires: json-glib-devel
Requires: gtk4

%description
A Gtk application for Chatting with your friends


%prep
wget https://gitlab.com/weiliang1503/gtk-chat/-/archive/master/gtk-chat-master.tar.gz
%autosetup  %{SOURCE0}

%build
cd gtk-chat-master
meson build 
build && ninja


%install
mkdir  %{buildroot}/usr
mkdir  %{buildroot}/usr/bin
mkdir  %{buildroot}/usr/share
mkdir  %{buildroot}/usr/applications
install -D -m     %{_builddir}/gtk-chat/build/gtk-chat


%check


%files
%license
%doc


%changelog

