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
Version:        3.1.35
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

%package -n yast2-branding-openSUSE
Summary:        YaST2 - Theme (openSUSE)
Group:          System/YaST
Provides:       yast2_theme = %{version}
Provides:       yast2-branding = %{version}
Conflicts:      otherproviders(yast2-branding)
Supplements:    packageand(yast2:branding-openSUSE)
Conflicts:      yast2-theme-SLE
PreReq:         /bin/ln
Requires:       hicolor-icon-theme
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}
Provides:        yast2-theme-openSUSE-Oxygen = %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}
Obsoletes:      yast2-theme-openSUSE < %{version}
Provides:       yast2-theme-openSUSE = %{version}

%description -n yast2-branding-openSUSE
This package contains the openSUSE theme for YaST2.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/SLE
mv $RPM_BUILD_ROOT%{yast_themedir}/openSUSE $RPM_BUILD_ROOT%{yast_themedir}/current

# let's take hicolor icons for yast
ln -s /usr/share/icons/hicolor $RPM_BUILD_ROOT%{yast_themedir}/current/icons

# install opensuse icewm style
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
cp openSUSE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/

cp -R "$RPM_BUILD_ROOT/%{yast_docdir}" "$RPM_BUILD_ROOT/%{yast_docdir}-openSUSE"
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
# ghost file (not packed in RPM but listed)

%fdupes $RPM_BUILD_ROOT%{yast_themedir}
%fdupes $RPM_BUILD_ROOT/usr/share/icons

%pre -n yast2-branding-openSUSE
# used to be a symlink, we need to remove it so rpm can update to the directory
if test -L %{yast_themedir}/current ; then
  rm %{yast_themedir}/current
fi

%files -n yast2-branding-openSUSE
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/current
%config %{_sysconfdir}/icewm
/usr/share/icons/*
%doc %{yast_docdir}-openSUSE

%changelog
