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

# YaST Oxygen icons maintained by Martin Schlander <martin.schlander () gmail ! com>


Name:           yast2-theme
Version:        4.1.6
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
%if 0%{?is_opensuse}
BuildRequires:  yast2-qt-branding-openSUSE
%endif
BuildArch:      noarch
Summary:        YaST2 - Theme
License:        GPL-2.0-only
Group:          System/YaST
Url:            http://github.com/yast/yast-theme

%description
Contains the SUSE Linux theme for YaST2.

%if 0%{?is_opensuse}
%package -n yast2-branding-openSUSE
Summary:        YaST2 - Theme (openSUSE)
Group:          System/YaST
Provides:       yast2-branding = %{version}
Provides:       yast2_theme = %{version}
Conflicts:      otherproviders(yast2-branding)
Supplements:    packageand(yast2:branding-openSUSE)
Conflicts:      yast2-theme-SLE
PreReq:         /bin/ln
Requires:       hicolor-icon-theme
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}
Obsoletes:      yast2-theme-openSUSE < %{version}
Provides:       yast2-theme-openSUSE = %{version}

%description -n yast2-branding-openSUSE
This package contains the openSUSE theme for YaST2.


%package -n yast2-branding-openSUSE-Oxygen
Summary:        YaST2 - switcher into Oxygen icon theme
Group:          System/YaST
Supplements:    packageand(yast2:plasma5-session)
PreReq:         /bin/ln
PreReq:         yast2-branding-openSUSE = %{version}
Conflicts:      yast2-theme-SLE
Provides:       yast2-theme-openSUSE-Oxygen = %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}

%description -n yast2-branding-openSUSE-Oxygen
After installing this package, symbolic link for "current" theme 
will be changed "Oxygen". This package does not contains icons 
of the openSUSE theme for YaST2. Icons itself exist in 
yast2-branding-openSUSE package.


%else
%package SLE
Summary:        YaST2 - SLE Theme
Group:          System/YaST
Provides:       yast2_theme = %{version}
Conflicts:      yast2-theme-openSUSE
Conflicts:      yast2-theme-openSUSE-Oxygen
Conflicts:      yast2-branding-openSUSE
Conflicts:      yast2-branding-openSUSE-Oxygen
Obsoletes:      yast2-branding-openSUSE
Obsoletes:      yast2-branding-openSUSE-Oxygen
PreReq:         /bin/ln

%description SLE
This package contains the YaST2 theme for the SUSE Linux Enterprise
Family.
%endif

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%if 0%{?is_opensuse}
rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/SLE
mv $RPM_BUILD_ROOT%{yast_themedir}/openSUSE $RPM_BUILD_ROOT%{yast_themedir}/current

# let's take hicolor icons for yast
ln -s /usr/share/icons/hicolor $RPM_BUILD_ROOT%{yast_themedir}/current/icons

# install opensuse icewm style
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
cp openSUSE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/

cp -R "$RPM_BUILD_ROOT/%{yast_docdir}" "$RPM_BUILD_ROOT/%{yast_docdir}-openSUSE"
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/yast2-theme/
echo 'This file marks the package yast2-branding-openSUSE-Oxygen to be installed.'   > $RPM_BUILD_ROOT/usr/share/doc/packages/yast2-theme/yast2-branding-openSUSE-Oxygen.txt

%else
# install SLE icewm style
mkdir -p $RPM_BUILD_ROOT/etc/icewm/
cp SLE/wmconfig/* $RPM_BUILD_ROOT/etc/icewm/

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/openSUSE*
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
rm -rf "$RPM_BUILD_ROOT/%{_docdir}/yast2-theme"

mv $RPM_BUILD_ROOT%{yast_themedir}/SLE $RPM_BUILD_ROOT%{yast_themedir}/current

# let's take hicolor icons for yast
ln -s /usr/share/icons/hicolor $RPM_BUILD_ROOT%{yast_themedir}/current/icons

# remove KDE icons - they are incomplete and only interesting for openSUSE
rm -rf $RPM_BUILD_ROOT/usr/share/icons/{crystal,oxygen}
%endif

%fdupes $RPM_BUILD_ROOT%{yast_themedir}
%fdupes $RPM_BUILD_ROOT/usr/share/icons

%if 0%{?is_opensuse}

%post -n yast2-branding-openSUSE-Oxygen
if test -L %{yast_themedir}/current/icons ; then
  rm %{yast_themedir}/current/icons
fi
ln -s /usr/share/icons/oxygen %{yast_themedir}/current/icons

%postun -n yast2-branding-openSUSE-Oxygen
# yast2-branding-openSUSE is still there, so we have to reset the link to higcolor
if test -L %{yast_themedir}/current/icons ; then
  rm %{yast_themedir}/current/icons
fi
ln -s /usr/share/icons/hicolor %{yast_themedir}/current/icons

%files -n yast2-branding-openSUSE
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/current
%config %{_sysconfdir}/icewm
/usr/share/icons/*
%doc %{yast_docdir}-openSUSE

%files -n yast2-branding-openSUSE-Oxygen
%dir /usr/share/doc/packages/yast2-theme/
/usr/share/doc/packages/yast2-theme/yast2-branding-openSUSE-Oxygen.txt

%else

%files SLE
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/current
/usr/share/icons/hicolor/*/apps/*
%config %{_sysconfdir}/icewm
%endif

%changelog
