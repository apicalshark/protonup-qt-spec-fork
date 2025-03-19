Name:           ProtonUp-Qt
Version:        2.11.1
Release:        5%{?dist}
Summary:        Install and manage Proton-GE for Steam and Wine-GE for Lutris with this graphical user interface.
License:        GPLv3
URL:            https://davidotek.github.io/protonup-qt

%global _pkgname ProtonUp-Qt
%global appimage_file ProtonUp-Qt-%{version}-x86_64.AppImage

Source0:        protonup-qt.desktop
Source1:        protonup-qt
BuildRequires:  fuse wget
Requires:       fuse

%description
%{summary}

%prep
wget https://github.com/DavidoTek/ProtonUp-Qt/releases/download/v%{version}/ProtonUp-Qt-%{version}-x86_64.AppImage
cp %{appimage_file} %{appimage_file}.new
echo "Extracting icons from AppImage..."
chmod 755 %{appimage_file}
./%{appimage_file} --appimage-extract > /dev/null


%install
mkdir -p %{buildroot}%{_bindir}/protonup-qt-data
cp ProtonUp-Qt-%{version}-x86_64.AppImage.new %{buildroot}%{_bindir}/protonup-qt-data/ProtonUp-Qt-%{version}-x86_64.AppImage
chmod 0755 %{buildroot}%{_bindir}/protonup-qt-data/ProtonUp-Qt-%{version}-x86_64.AppImage
install -Dm 0755 %{SOURCE1} %{buildroot}%{_bindir}/protonup-qt
cd "squashfs-root/usr/share/icons"
find "." -type f -exec install -Dm644 "{}" "%{buildroot}%{_datadir}/icons/{}" \;
install -Dm 0644 %{SOURCE0} %{buildroot}%{_datadir}/applications/protonup-qt.desktop

%files
%{_bindir}/protonup-qt
%{_datadir}/applications/protonup-qt.desktop
%{_datadir}/icons/*
%{_bindir}/protonup-qt-data/ProtonUp-Qt-%{version}-x86_64.AppImage

%changelog
%autochangelog
