#
# spec file for package yast2-theme
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.1.7
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools
BuildRequires:  rubygem(yast-rake)
%if 0%{?is_opensuse}
BuildRequires:  yast2-qt-branding-openSUSE
BuildRequires:  oxygen5-icon-theme
%endif

Requires:       hicolor-icon-theme

Provides:       yast2-branding = %{version}
Provides:       yast2_theme = %{version}
Provides:       yast2-theme = %{version}

Conflicts:      otherproviders(yast2-branding)
Conflicts:      otherproviders(yast2-theme)
Conflicts:      otherproviders(yast2_theme)

Obsoletes:      yast2-theme-openSUSE
Obsoletes:      yast2-theme-SLE
Obsoletes:      yast2-theme < %{version}
Obsoletes:      yast2-branding-openSUSE
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}

BuildArch:      noarch
Summary:        YaST2 - Theme
License:        GPL-2.0-only
Group:          System/YaST
Url:            http://github.com/yast/yast-theme

%description
Contains necessary theming resources to use YaST2.

%if 0%{?is_opensuse}
%package oxygen
Summary:        YaST2 - Oxygen icon theme
Group:          System/YaST
Supplements:    packageand(yast2:oxygen5-icon-theme)
PreReq:         yast2-branding = %{version}
Requires:       oxygen5-icon-theme
Provides:       yast2-theme-oxygen = %{version}
Obsoletes:      yast2-theme-oxygen < %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}

%description oxygen
Contains icons in KDE Oxygen style (from KDE Plasma 4).
%endif

%build

%install
%yast_install

# Distro specific config (should be moved to distro specific branding packages!)
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
%if 0%{?is_opensuse}
mv $RPM_BUILD_ROOT%{yast_themedir}/openSUSE $RPM_BUILD_ROOT%{yast_themedir}/current
cp theme/openSUSE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/
%else
rm -rf $RPM_BUILD_ROOT%{yast_icondir}/oxygen
mv $RPM_BUILD_ROOT%{yast_themedir}/SLE $RPM_BUILD_ROOT%{yast_themedir}/current
cp theme/SLE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/
%endif

# We only need current theme
rm -rf $RPM_BUILD_ROOT%{yast_themedir}/SLE $RPM_BUILD_ROOT%{yast_themedir}/openSUSE

# Clean out duplicates
%fdupes $RPM_BUILD_ROOT%{yast_themedir}
%fdupes $RPM_BUILD_ROOT/usr/share/icons

%pre
# CPIO can't remove links on its own
if test -L %{yast_themedir}/current ; then
  rm %{yast_themedir}/current
fi
# No longer used
if test -L %{yast_themedir}/current/icons ; then
  rm %{yast_themedir}/current/icons
fi

%files
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/current
%config %{_sysconfdir}/icewm
%{yast_icondir}/hicolor/*
%doc %{yast_docdir}
%license COPYING

%if 0%{?is_opensuse}
%files oxygen
%{yast_icondir}/oxygen/*
%endif

%changelog
