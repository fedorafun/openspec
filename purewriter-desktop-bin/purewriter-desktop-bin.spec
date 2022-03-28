Name:           purewriter-desktop-bin
Version:        1.5.2
Release:        1%{?dist}
Summary:        Never loss content editor & Markdown

License:        Unknown
URL:            https://writer.drakeet.com/desktop
Source0:        https://github.com/PureWriter/desktop/releases/download/1.5.2/PureWriter-1.5.2-Linux-amd64.deb
Source1:        purewriter-desktop-launcher.sh
Source2:        purewriter-desktop.desktop
Source3:        purewriter.png

BuildRequires:  javapackages-tools
Requires:       java-11-openjdk

%description
%{summary}.

%prep
ar x %{S:0}
tar -xf data.tar.xz

%install
%{__install} -Dm644 opt/pure-writer/lib/app/app.so -t %{buildroot}%{_javadir}/purewriter-desktop
%{__install} -Dm755 %{S:1} %{buildroot}%{_bindir}/purewriter-desktop
%{__install} -Dm644 %{S:2} %{buildroot}%{_datadir}/applications/purewriter-desktop.desktop
%{__install} -Dm644 %{S:3} %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/purewriter.png

%files
%license opt/pure-writer/share/doc/copyright
%{_javadir}/purewriter-desktop
%{_bindir}/purewriter-desktop
%{_datadir}/applications/purewriter-desktop.desktop
%{_datadir}/icons/hicolor/512x512/apps/purewriter.png

%post
/usr/bin/echo "******************************"
/usr/bin/echo "*  访问[https://fedora.fun]  *"
/usr/bin/echo "*     帮助我们变得更好！     *"
/usr/bin/echo "******************************"

%postun
/usr/bin/echo "******************************"
/usr/bin/echo "*  访问[https://fedora.fun]  *"
/usr/bin/echo "*     帮助我们变得更好！     *"
/usr/bin/echo "******************************"

%changelog
* Mon Mar 28 2022 OneToroto <onetoroto@hotmail.com> - 1.5.2-1
- First build.
