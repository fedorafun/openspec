Name:		TouhouProject-Old
Release:	1.0
Version:	1.0
Summary:	NEC PC-98 danmaku STG by ZUN Soft, integrate by Zhaoym233
License:	BSD
URL:		https://zhaoym233.github.io/th_old/
Source0:	zun.hdi
Source1:	zh_tw.hdi
Source2:	dosbox-x.conf
Source3:	th-old.png
Source4:	th-old.desktop

%description
NEC PC-98 danmaku STG by ZUN Soft, integrate by Zhaoym233

%prep

%build

%install
mkdir -p %{buildroot}/usr/lib/th-old/
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/icons/th-old/
cp %{SOURCE0} %{buildroot}/usr/lib/th-old/
cp %{SOURCE1} %{buildroot}/usr/lib/th-old/
cp %{SOURCE2} %{buildroot}/usr/lib/th-old/
cp %{SOURCE3} %{buildroot}/usr/share/icons/th-old/
cp %{SOURCE4} %{buildroot}/usr/share/applications/
rm -rf {_builddir}/*
%check

%files
/usr/lib/th-old/dosbox-x.conf
/usr/lib/th-old/zun.hdi
/usr/lib/th-old/zh_tw.hdi
/usr/share/applications/th-old.desktop
/usr/share/icons/th-old/th-old.png

%changelog
