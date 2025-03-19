Name:           ProtonUp-Qt
Version:        2.11.1
Release:        1%{?dist}
Summary:        Install and manage Proton-GE for Steam and Wine-GE for Lutris with this graphical user interface.
License:        GPLv3
URL:            https://davidotek.github.io/protonup-qt


%global _pkgname ProtonUp-Qt
%global appimage_file %{_pkgname}-%{version}-x86_64.AppImage

# Source settings
# Source0:        https://github.com/DavidoTek/ProtonUp-Qt/releases/download/v%{version}/%{appimage_file}
Source0:        protonup-qt.desktop
Source1:        protonup-qt



BuildRequires:  fuse wget
Requires:       fuse

%description
%{summary}

%prep
wget https://github.com/DavidoTek/ProtonUp-Qt/releases/download/v%{version}/%{appimage_file}
echo "Extracting icons from AppImage..."
chmod 755 %{appimage_file}
./%{appimage_file} --appimage-extract > /dev/null

%install
mkdir -p %{buildroot}%{_optir}/protonup-qt
install -Dm 0755 %{appimage_file} %{buildroot}%{_optir}/protonup-qt/%{appimage_file}
install -Dm 0755 %{SOURCE1} %{buildroot}%{_bindir}/protonup-qt
install -Dm 0644 %{SOURCE0} %{buildroot}%{_datadir}/applications/protonup-qt.desktop

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
if [ -d "squashfs-root/usr/share/icons/hicolor" ]; then
  find squashfs-root/usr/share/icons/hicolor -depth -print | cpio -pdm %{buildroot}%{_datadir}/icons/hicolor
fi

# Remove extracted squashfs-root
rm -rf squashfs-root

%files
%license COPYING
%{_bindir}/protonup-qt
%{_datadir}/applications/protonup-qt.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_optir}/protonup-qt/*

%changelog
%autochangelog
