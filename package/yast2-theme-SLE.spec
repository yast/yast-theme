#
# spec file for package yast2-theme
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           yast2-theme-SLE
Version:        3.1.9
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-theme-%{version}.tar.bz2

Group:	        System/YaST
License:        GPL-2.0
BuildRequires:	pkg-config update-desktop-files hicolor-icon-theme fdupes
BuildRequires:  yast2-devtools >= 3.1.10
BuildArchitectures: noarch
Requires:	hicolor-icon-theme
Summary:	YaST2 - SLE Theme
Group:		System/YaST
Provides:	yast2_theme = %{version}
Provides:       yast2-theme-NLD = 0.4.5
Obsoletes:      yast2-theme-NLD <= 0.4.5
Conflicts:      yast2-theme-openSUSE
Conflicts:      yast2-theme-openSUSE-any
PreReq:		/bin/ln

%description
This package contains the YaST2 theme for the SUSE Linux Enterprise
Family.

%prep
%setup -n yast2-theme-%{version}

%build
%yast_build

%install
%yast_install

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/openSUSE*
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
# ghost file (not packed in RPM but listed)
#
# make icons available to GNOME control center (hicolor theme)
# (bug #166008)
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/64x64/apps

for dir in 22x22 32x32 48x48 64x64; do
    cd $RPM_BUILD_ROOT/%{yast_themedir}/SLE/icons/$dir/apps
    icons=$(ls *.png)
    cd $RPM_BUILD_ROOT/usr/share/icons/hicolor/$dir/apps
    for icon in $icons; do
        [ -e $icon ] || ln -s %{yast_themedir}/SLE/icons/$dir/apps/$icon .
    done
done

%fdupes $RPM_BUILD_ROOT%{yast_themedir}


%files
%defattr(-,root,root)
%{yast_themedir}/SLE
/usr/share/icons/hicolor/*/apps/*
