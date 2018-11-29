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
Supplements:    (yast2 and oxygen5-icon-theme)
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
rake install DESTDIR=%{buildroot}

# Distro specific config (should be moved to distro specific branding packages!)
mkdir -p %{buildroot}/etc/icewm/
%if 0%{?is_opensuse}
mv %{buildroot}%{yast_themedir}/openSUSE %{buildroot}%{yast_themedir}/current
cp theme/openSUSE/wmconfig/* %{buildroot}/etc/icewm/
%else
mv %{buildroot}%{yast_themedir}/SLE %{buildroot}%{yast_themedir}/current
cp theme/SLE/wmconfig/* %{buildroot}/etc/icewm/
# SLE doesn't have oxygen5-icon-theme
rm -rf %{buildroot}%{yast_icondir}/oxygen
%endif

# We only need current theme
rm -rf %{buildroot}%{yast_themedir}/SLE %{buildroot}%{yast_themedir}/openSUSE

# Clean out duplicates
%fdupes %{buildroot}%{yast_themedir}
%fdupes %{buildroot}%{yast_icondir}

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
