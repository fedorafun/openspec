%define HOME %{HOME} 

Name: hmcl
Version: 3.5.3
Release:      1
Summary:play minecraft on Fedora

License: GPLv3+
URL:https://hmcl.huangyuhui.net/
Source0:https://raw.githubusercontent.com/zxc3123857948/fedora-spec/main/hmcl/sources/hmcl
Source1:https://github.com/zxc3123857948/fedora-spec/blob/main/%{NAME}/sources/jar/%{version}/HMCL-%{version}.jar
Source2:https://github.com/zxc3123857948/fedora-spec/blob/main/hmcl/sources/hmcl.png
Source3:https://raw.githubusercontent.com/zxc3123857948/fedora-spec/main/hmcl/sources/hmcl.desktop

AutoReqProv: no
Requires: java-17 javafx

%description
play Minecraft on Fedora!!

%prep

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/${HOME}/.local/share/hmcl/
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icon

install -D -m 777 %{SOURCE0} %{buildroot}/usr/bin

install -D  %{SOURCE1} %{buildroot}/${HOME}/.local/share/hmcl/

cp %{SOURCE2}  %{buildroot}/usr/share/icon
cp %{SOURCE3}  %{buildroot}/usr/share/applications
rm -rf  %{_builddir}/*



%files
/usr/bin/hmcl
/usr/share/applications/hmcl.desktop
/usr/share/icon/hmcl.png
/%{HOME}/.local/share/hmcl/


%changelog

