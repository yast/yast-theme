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


Name:           yast2-theme
Version:        3.1.9
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:	        System/YaST
License:        GPL-2.0
BuildRequires:	pkg-config update-desktop-files hicolor-icon-theme fdupes yast2-qt-branding-openSUSE
BuildRequires:  yast2-branding-openSUSE
BuildRequires:  yast2-devtools >= 3.1.10
BuildArchitectures: noarch
Summary:	YaST2 - Theme
%description
Contains the SuSE Linux theme for YaST2.

%package openSUSE
Summary:	YaST2 - Theme (openSUSE)
Group:		System/YaST
Provides:	yast2_theme = %{version}
Provides:	yast2-theme-UnitedLinux
Provides:	yast2-theme-openSUSE-any
Conflicts:      yast2-theme-SLE
PreReq:		/bin/ln
Requires:	hicolor-icon-theme

%package openSUSE-Crystal
Summary:	YaST2 - Theme (openSUSE)
Group:		System/YaST
Provides:	yast2_theme = %{version}
Provides:	yast2-theme-openSUSE-any
Conflicts:      yast2-theme-SLE
PreReq:		/bin/ln yast2-theme-openSUSE

%package openSUSE-Oxygen
Summary:	YaST2 - Theme (openSUSE)
Group:		System/YaST
Provides:	yast2_theme = %{version}
Provides:	yast2-theme-openSUSE-any
Conflicts:      yast2-theme-SLE
PreReq:		/bin/ln yast2-theme-openSUSE
Conflicts:      yast2-theme-openSUSE-Crystal

%description openSUSE
This package contains the openSUSE theme for YaST2.

%description openSUSE-Crystal
This package contains the openSUSE theme for YaST2.

%description openSUSE-Oxygen
This package contains the openSUSE theme for YaST2.


%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

rm -rf $RPM_BUILD_ROOT/%{yast_themedir}/SLE

cp -R "$RPM_BUILD_ROOT/%{yast_docdir}" "$RPM_BUILD_ROOT/%{yast_docdir}-openSUSE"
rm -rf "$RPM_BUILD_ROOT/%{yast_docdir}"
# ghost file (not packed in RPM but listed)
cd $RPM_BUILD_ROOT/%{yast_themedir}/
rm -rf openSUSE-current
ln -sn openSUSE openSUSE-current
#
# make icons available to GNOME control center (hicolor theme)
# (bug #166008)
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/256x256/apps

for dir in 22x22 32x32 48x48 64x64 256x256; do
    cd $RPM_BUILD_ROOT/%{yast_themedir}/openSUSE-current/icons/$dir/apps
    icons=$(ls *.png)
    cd $RPM_BUILD_ROOT/usr/share/icons/hicolor/$dir/apps
    for icon in $icons; do
        ln -s %{yast_themedir}/current/icons/$dir/apps/$icon .
    done
done
filelist=$(mktemp /tmp/fileListXXXXXX)
cd $RPM_BUILD_ROOT%{yast_themedir}/openSUSE
files=$(find . -type f)
tfiles=$(cd %{yast_themedir}/openSUSE && find wizard -type f)
files="$files $tfiles"
for subtheme in Crystal Oxygen ; do
  cd $RPM_BUILD_ROOT%{yast_themedir}/openSUSE-$subtheme
  for file in $files; do
    mkdir -p $(dirname "$file") || true
    if ! test -f "$file"; then
     ln -s %{yast_themedir}/openSUSE/$file $file
    fi
  done
done

%fdupes $RPM_BUILD_ROOT%{yast_themedir}


%post openSUSE
cd %{yast_themedir}
if ! test -d openSUSE-Crystal && ! test -d openSUSE-Oxygen; then
  ln -snf openSUSE openSUSE-current
fi

%post openSUSE-Crystal
cd %{yast_themedir}
ln -snf openSUSE-Crystal openSUSE-current

%post openSUSE-Oxygen
cd %{yast_themedir}
ln -snf openSUSE-Oxygen openSUSE-current

%files openSUSE
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/openSUSE
/usr/share/icons/hicolor/*/apps/*
%doc %{yast_docdir}-openSUSE
# ghost file (not packed in RPM but listed)
# remove the file when removing the RPM
%ghost %{yast_themedir}/openSUSE-current

%files openSUSE-Crystal
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/openSUSE-Crystal

%files openSUSE-Oxygen
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/openSUSE-Oxygen
