#
# spec file for package yast2-theme
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-theme
Version:        3.1.26
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  yast2-qt-branding-openSUSE
BuildArch:      noarch
Summary:        YaST2 - Theme
License:        GPL-2.0
Group:          System/YaST

%description
Contains the SuSE Linux theme for YaST2.

%package openSUSE
Summary:        YaST2 - Theme (openSUSE)
Group:          System/YaST
Provides:       yast2_theme = %{version}
Conflicts:      yast2-theme-SLE
PreReq:         /bin/ln
Requires:       hicolor-icon-theme
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}
Provides:       yast2-theme-openSUSE-Crystal = %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}
Provides:       yast2-theme-openSUSE-Oxygen = %{version}

%description openSUSE
This package contains the openSUSE theme for YaST2.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

# install opensuse icewm style
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
cp openSUSE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/SLE

cp -R "$RPM_BUILD_ROOT/%{yast_docdir}" "$RPM_BUILD_ROOT/%{yast_docdir}-openSUSE"
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
# ghost file (not packed in RPM but listed)

#
# make icons available to GNOME control center (hicolor theme)
# (bug #166008)
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/256x256/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/scalable/apps

for dir in 22x22 32x32 48x48 64x64 256x256 scalable; do
    cd $RPM_BUILD_ROOT/%{yast_themedir}/openSUSE/icons/$dir/apps
    icons=$(find -name '*.png' -o -name '*.svg' 2>/dev/null)
    cd $RPM_BUILD_ROOT/usr/share/icons/hicolor/$dir/apps
    for icon in $icons; do
        ln -s %{yast_themedir}/openSUSE/icons/$dir/apps/$icon .
    done
done
%fdupes $RPM_BUILD_ROOT%{yast_themedir}

%files openSUSE
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/openSUSE
%config %{_sysconfdir}/icewm
/usr/share/icons/hicolor/*/apps/*
%doc %{yast_docdir}-openSUSE

%changelog
