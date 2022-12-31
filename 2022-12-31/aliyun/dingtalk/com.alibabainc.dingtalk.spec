Name:       com.alibabainc.dingtalk
Version:   1.2.0.132
Release:    1
Summary:    钉钉
License:    None
URL:        https://gov.dingtalk.com
Packager:   zhullyb
Source0:    https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/com.alibabainc.dingtalk_%{version}_amd64.deb
Source1:    com.alibabainc.dingtalk.desktop
Source2:    libk5crypto.so.3

# DebSource & pkgvere can be get here: https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/linux_dingtalk_update.json

# Requires: bubblewrap

%define _build_id_links none

AutoReqProv: no

%description

%prep
ar x %{SOURCE0}
tar -xf data.tar.xz

%install

mkdir -p %{buildroot}/opt/apps/com.alibabainc.dingtalk/
cp -R opt/apps/com.alibabainc.dingtalk/files/ %{buildroot}/opt/apps/com.alibabainc.dingtalk/
rm %{buildroot}/opt/apps/com.alibabainc.dingtalk/files/*-Release.*/libm.so.6
install -Dm644 %{SOURCE1} -t %{buildroot}/usr/share/applications/
install -Dm644 %{SOURCE2} -t %{buildroot}/opt/apps/com.alibabainc.dingtalk/files/*-Release.*/
# process /usr/bin/dingtalk
mkdir -p %{buildroot}/usr/bin/
echo '#!/bin/bash -e
cd /opt/apps/com.alibabainc.dingtalk/files/*-Release*/
LD_LIBRARY_PATH=/opt/apps/com.alibabainc.dingtalk/files/*-Release.*:$LD_LIBRARY_PATH ./com.alibabainc.dingtalk' > %{buildroot}/usr/bin/dingtalk
chmod +x %{buildroot}/usr/bin/dingtalk

%pre

%post

%preun

%postun

%files
/usr/bin/dingtalk
/usr/share/applications/com.alibabainc.dingtalk.desktop
/opt/apps/com.alibabainc.dingtalk/
