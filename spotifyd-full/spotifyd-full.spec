Name:   spotifyd-full
Version: 0.3.3
Release:        1%{?dist}
Summary: A spotify playing daemon (all features enabled)
BuildArch: aarch64 x86_64
License: GPLv3
URL: https://github.com/Spotifyd/spotifyd
Source0: https://github.com/Spotifyd/spotifyd/archive/refs/tags/v%{version}.tar.gz


BuildRequires: rust-libdbus-sys-devel   dbus dbus-devel 
BuildRequires:  alsa-lib-devel cargo git 
BuildRequires: openssl-devel
BuildRequires: portaudio pulseaudio-libs  portaudio portaudio-devel
Requires:  pulseaudio-libs portaudio 
AutoReqProv: no

%description
Spotifyd streams music just like the official client, but is more lightweight and supports more platforms. Spotifyd also supports the Spotify Connect protocol, which makes it show up as a device that can be controlled from the official clients.

%prep
tar xf %{SOURCE0}


%build
cd %{_builddir}/spotifyd-%{version}
cargo build --release --all-features


%install
 install -D -m 755 %{_builddir}/spotifyd-%{version}/target/release/spotifyd %{buildroot}/usr/bin/spotifyd
 install -D -m 644  %{_builddir}/spotifyd-%{version}/contrib/spotifyd.service  %{buildroot}/usr/lib/systemd/user/spotifyd.service
 rm -rf  %{_builddir}/*

%check


%files
/usr/lib/systemd/user/spotifyd.service
/usr/bin/spotifyd


%changelog

