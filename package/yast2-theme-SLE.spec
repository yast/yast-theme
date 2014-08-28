#
# spec file for package yast2-theme-SLE
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


Name:           yast2-theme-SLE
Version:        3.1.29
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-theme-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
BuildArch:      noarch
Requires:       hicolor-icon-theme
Summary:        YaST2 - SLE Theme
License:        GPL-2.0
Group:          System/YaST
Provides:       yast2-theme-NLD = 0.4.5
Provides:       yast2_theme = %{version}
Obsoletes:      yast2-theme-NLD <= 0.4.5
Conflicts:      yast2-theme-openSUSE
Conflicts:      yast2-theme-openSUSE-any
PreReq:         /bin/ln

%description
This package contains the YaST2 theme for the SUSE Linux Enterprise
Family.

%prep
%setup -n yast2-theme-%{version}

%build
%yast_build

%install
%yast_install

# install SLE icewm style
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
cp SLE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/openSUSE*
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
rm -rf "$RPM_BUILD_ROOT/%{_docdir}/yast2-theme"

# remove KDE icons - they are incomplete and only interesting for openSUSE
rm -rf $RPM_BUILD_ROOT/usr/share/icons/{crystal,oxygen}

%fdupes $RPM_BUILD_ROOT%{yast_themedir}
%fdupes $RPM_BUILD_ROOT/usr/share/icons

%files
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/SLE
/usr/share/icons/hicolor/*/apps/*
%config %{_sysconfdir}/icewm

%changelog
