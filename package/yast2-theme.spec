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
Version:        4.1.2
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
Conflicts:      yast2-theme-SLE
Requires:       yast2-branding-openSUSE = %{version}
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

# remove unneeded icons
pushd $RPM_BUILD_ROOT/usr/share/icons/hicolor
rm -rf 256x256
rm 16x16/apps/pattern-enlightenment.png
rm 16x16/apps/pattern-lxde.png
rm 16x16/apps/yast-gray-dot.png
rm 16x16/apps/yast-green-dot.png
rm 16x16/apps/yast-red-dot.png
rm 16x16/apps/yast-yellow-dot.png
rm 22x22/apps/pattern-enlightenment.png
rm 22x22/apps/pattern-lxde.png
rm 22x22/apps/yast-gray-dot.png
rm 22x22/apps/yast-green-dot.png
rm 22x22/apps/yast-red-dot.png
rm 22x22/apps/yast-yellow-dot.png
rm 32x32/apps/pattern-enlightenment.png
rm 32x32/apps/pattern-lxde.png
rm 48x48/apps/pattern-enlightenment.png
rm 48x48/apps/pattern-lxde.png
rm 48x48/apps/yast-gray-dot.png
rm 48x48/apps/yast-green-dot.png
rm 48x48/apps/yast-red-dot.png
rm 48x48/apps/yast-yellow-dot.png
rm 64x64/apps/apparmor_app_armor.png
rm 64x64/apps/bootdisk_create.png
rm 64x64/apps/defaultgroup.png
rm 64x64/apps/gnome.png
rm 64x64/apps/kde.png
rm 64x64/apps/keyboardlayout.png
rm 64x64/apps/ktip.png
rm 64x64/apps/msg_error.png
rm 64x64/apps/msg_info.png
rm 64x64/apps/msg_warning.png
rm 64x64/apps/pattern-enlightenment.png
rm 64x64/apps/pattern-lxde.png
rm 64x64/apps/pixie.png
rm 64x64/apps/printer2.png
rm 64x64/apps/route.png
rm 64x64/apps/samba_setup.png
rm 64x64/apps/SuSEmenu.png
rm 64x64/apps/system.png
rm 64x64/apps/tdsl.png
rm 64x64/apps/user_add.png
rm 64x64/apps/user_system.png
rm 64x64/apps/www.png
rm 64x64/apps/yast-addon.png
rm 64x64/apps/yast-autoyast.png
rm 64x64/apps/yast-backup.png
rm 64x64/apps/yast-bluetooth.png
rm 64x64/apps/yast-bootloader.png
rm 64x64/apps/yast-ca_mgm.png
rm 64x64/apps/yast-cd-creator.png
rm 64x64/apps/yast-cd_update.png
rm 64x64/apps/yast-checkmedia.png
rm 64x64/apps/yast-common_cert.png
rm 64x64/apps/yast-controller.png
rm 64x64/apps/yast-create-new-vm.png
rm 64x64/apps/yast-dasd.png
rm 64x64/apps/yast-dhcp-server.png
rm 64x64/apps/yast-disk.png
rm 64x64/apps/yast-dns.png
rm 64x64/apps/yast-dns-server.png
rm 64x64/apps/yast-dsl.png
rm 64x64/apps/yast-firewall.png
rm 64x64/apps/yast-ftp.png
rm 64x64/apps/yast-hardware.png
rm 64x64/apps/yast-heartbeat.png
rm 64x64/apps/yast-high_availability.png
rm 64x64/apps/yast-host.png
rm 64x64/apps/yast-http-server.png
rm 64x64/apps/yast-hwinfo.png
rm 64x64/apps/yast-inetd.png
rm 64x64/apps/yast-inst-mode.png
rm 64x64/apps/yast-instserver.png
rm 64x64/apps/yast-iscsi-client.png
rm 64x64/apps/yast-iscsi-server.png
rm 64x64/apps/yast-isdn.png
rm 64x64/apps/yast-isns.png
rm 64x64/apps/yast-joystick.png
rm 64x64/apps/yast-kdump.png
rm 64x64/apps/yast-kerberos.png
rm 64x64/apps/yast-keyboard.png
rm 64x64/apps/yast-kiwi.png
rm 64x64/apps/yast-lan.png
rm 64x64/apps/yast-ldap-browser.png
rm 64x64/apps/yast-ldap.png
rm 64x64/apps/yast-ldap-server.png
rm 64x64/apps/yast-license.png
rm 64x64/apps/yast-live-install.png
rm 64x64/apps/yast-lvm_config.png
rm 64x64/apps/yast-mail.png
rm 64x64/apps/yast-mail-server.png
rm 64x64/apps/yast-messages.png
rm 64x64/apps/yast-misc.png
rm 64x64/apps/yast-mouse.png
rm 64x64/apps/yast-network_devices.png
rm 64x64/apps/yast-network.png
rm 64x64/apps/yast-network_services.png
rm 64x64/apps/yast-nfs.png
rm 64x64/apps/yast-nfs_server.png
rm 64x64/apps/yast-nis.png
rm 64x64/apps/yast-nis_server.png
rm 64x64/apps/yast-ntp-client.png
rm 64x64/apps/yast-online_update.png
rm 64x64/apps/yast-powertweak.png
rm 64x64/apps/yast-printer.png
rm 64x64/apps/yast-product-registration.png
rm 64x64/apps/yast-proxy.png
rm 64x64/apps/yast-release-notes.png
rm 64x64/apps/yast-remote.png
rm 64x64/apps/yast-restore.png
rm 64x64/apps/yast-routing.png
rm 64x64/apps/yast-samba-client.png
rm 64x64/apps/yast-samba-server.png
rm 64x64/apps/yast-scanner.png
rm 64x64/apps/yast-security.png
rm 64x64/apps/yast-slp-server.png
rm 64x64/apps/yast-software.png
rm 64x64/apps/yast-sound.png
rm 64x64/apps/yast_source.png
rm 64x64/apps/yast-ssh-server.png
rm 64x64/apps/yast-sudoers.png
rm 64x64/apps/yast-support.png
rm 64x64/apps/yast-sw_single.png
rm 64x64/apps/yast-sw_source.png
rm 64x64/apps/yast-sysconfig.png
rm 64x64/apps/yast-system.png
rm 64x64/apps/yast-tftp-server.png
rm 64x64/apps/yast-timezone.png
rm 64x64/apps/yast-tv.png
rm 64x64/apps/yast-uml.png
rm 64x64/apps/yast-update.png
rm 64x64/apps/yast-vdisk.png
rm 64x64/apps/yast-vendor.png
rm 64x64/apps/yast-virtualisation.png
rm 64x64/apps/yast-vm-domain0-setup.png
rm 64x64/apps/yast-vm-install.png
rm 64x64/apps/yast-vm-management.png
rm 64x64/apps/yast-wol.png
rm 64x64/apps/yast-x11.png
rm 64x64/apps/yast-yast-language.png
rm 64x64/apps/yast-zfcp.png

popd

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
