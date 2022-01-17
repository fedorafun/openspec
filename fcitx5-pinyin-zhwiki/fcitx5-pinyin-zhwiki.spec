%define         _webslangver          20220101

Name:           fcitx5-pinyin-zhwiki
Version:        0.2.3.%{_webslangver}
Release:        1
Summary:        Fcitx 5 Pinyin Dictionary from zh.wikipedia.org
License:        GFDL
Url:            https://github.com/felixonmars/fcitx5-pinyin-zhwiki
Source0:        https://cloudflaremirrors.com/archlinux/community/os/x86_64/fcitx5-pinyin-zhwiki-1:%{version}-1-any.pkg.tar.zst

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
Fcitx 5 Pinyin Dictionary from zh.wikipedia.org

%prep
%autosetup -c %{name}
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build

%install
install -Dm644 %{BUILD_DIR}/usr/share/fcitx5/pinyin/dictionaries/zhwiki.dict -t %{buildroot}/usr/share/fcitx5/pinyin/dictionaries/

%post
%postun

%files
%license usr/share/licenses/fcitx5-pinyin-zhwiki/fdl-1.3.txt
/usr/share/fcitx5/pinyin/dictionaries/zhwiki.dict

%changelog

