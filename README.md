Overview
========

    ├── icons
    │   ├── crystal
    │   │   ├── 22x22/apps
    │   │   ├── 32x32/apps
    │   │   └── 48x48/apps
    │   ├── hicolor
    │   │   ├── scalable/apps
    │   │   ├── 16x16/apps
    │   │   ├── 22x22/apps
    │   │   ├── 32x32/apps
    │   │   ├── 48x48/apps
    │   │   ├── 64x64/apps
    │   │   └── 256x256/apps
    │   └── oxygen
    │       ├── 22x22/apps
    │       ├── 32x32/apps
    │       ├── 48x48/apps
    │       └── 64x64/apps
    ├── package
    ├─────────────────────── openSUSE
    └── SLE                  │
        ├── animations       ├── animations
        ├── testpage         ├── testpage
        ├── wizard           │   (see below)
        ├── wmconfig         ├── wmconfig
        └── worldmap         └── worldmap

Icons
-----

Add new icons to `icons/hicolor`. Adding scalable sources is required, because icons are generated with convert.sh script.

Wizard
------

This is the fancy YaST dialog layout used in the installation workflow.

The `openSUSE/wizard` counterpart to `SLE/wizard` lives
in the `yast` directory of the [openSUSE branding repository][branding].

[branding]: https://github.com/openSUSE/branding/tree/leap-15.1/yast

Generated Packages
==================
All icons will be stored in /usr/share/icons/.

yast2-branding-openSUSE
-----------------------
- icons /usr/share/icons/oxygen
- icons /usr/share/icons/hicolor
- icons /usr/share/icons/crystal
- /usr/share/YaST2/theme/current/icons is a link to /usr/share/icons/hicolor

yast2-branding-openSUSE-Oxygen
------------------------------
- Has no icons but pre-requires yast2-branding-openSUSE
- Moves link /usr/share/YaST2/theme/current/icons to /usr/share/icons/oxygen
  while installation (post script) and reset it while uninstallation
  (postun script)

yast2-theme-SLE
---------------
- icons /usr/share/icons/hicolor
- /usr/share/YaST2/theme/current/icons is a link to /usr/share/icons/hicolor