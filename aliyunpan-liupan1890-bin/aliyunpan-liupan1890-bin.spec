Name:           aliyunpan-liupan1890-bin
Version:        2.12.05
%define BaseVersion 2.11.29
Release:        1
Summary:         阿里云盘小白羊版 阿里云盘PC版 aliyundriver
License:        None
Url:            https://github.com/electron/electron
Source0:        阿里小白羊版Linux v2.11.29.zip
Source1:        aliyunpan-liupan1890-launcher.sh
Source2:        aliyunpan-liupan1890.svg
Source3:        aliyunpan-liupan1890.desktop
Source4:        app.asar

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
cd %{_builddir}/%{name}-%{version}/
%define BUILD_DIR "$(pwd)/$(ls)/electron"

%build

%install
mkdir -p %{buildroot}/usr/lib/aliyunpan-liupan1890

cd %{BUILD_DIR}
rm resources/aria2c
cp resources/* %{buildroot}/usr/lib/aliyunpan-liupan1890/

ln -s /usr/bin/aria2c %{buildroot}/usr/lib/aliyunpan-liupan1890/

install -Dm755 %{SOURCE1} "%{buildroot}/usr/bin/aliyunpan-liupan1890"

install -Dm644 %{SOURCE2} -t "%{buildroot}/usr/share/icons/hicolor/scalable/apps/"
install -Dm644 %{SOURCE3} -t "%{buildroot}/usr/share/applications/"

if [ -d %{SOURCE4}]
    then install -Dm644 %{SOURCE4} %{buildroot}/usr/lib/aliyunpan-liupan1890/
fi

%post
%postun

%files
%{_bindir}/aliyunpan-liupan1890
/usr/lib/aliyunpan-liupan1890/
/usr/share/icons/hicolor/scalable/apps/*
/usr/share/applications/*

%changelog

