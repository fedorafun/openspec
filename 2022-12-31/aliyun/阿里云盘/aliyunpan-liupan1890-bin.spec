Name:           aliyunpan-liupan1890-bin
Version:        2.12.05
Release:        3
Summary:         阿里云盘小白羊版 阿里云盘PC版 aliyundriver
License:        None
Url:            https://github.com/liupan1890/aliyunpan
Source0:        aliyunpan-liupan1890-%{version}-1-x86_64.pkg.tar.zst

Recommends:     mpv
Requires:       electron12
Requires:       aria2

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none

AutoReqProv: no

%description
 阿里云盘小白羊版 阿里云盘PC版 aliyundriver

%prep
%autosetup -c %{name}

%build

%install
cp -a %{_builddir}/%{name}-%{version}/usr %{buildroot}/
install -Dm644 %{buildroot}/usr/share/icons/* -t %{buildroot}/usr/share/icons/hicolor/scalable/apps/
rm %{buildroot}/usr/share/icons/aliyunpan-liupan1890.svg

%post
%postun

%files
%{_bindir}/aliyunpan-liupan1890
/usr/lib/aliyunpan-liupan1890/
/usr/share/icons/hicolor/scalable/apps/*
/usr/share/applications/*

%changelog

