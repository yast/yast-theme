Overview
========

    ├── icons
    │   ├── breeze
    │   │   └── apps
    │   │       ├── 32
    │   │       ├── 48
    │   │       └── 64
    │   ├── breeze-dark
    │   │   └── apps
    │   │       ├── 32
    │   │       ├── 48
    │   │       └── 64
    │   ├── crystal
    │   │   ├── 22x22/apps
    │   │   ├── 32x32/apps
    │   │   └── 48x48/apps
    │   ├── hicolor
    │   │   └── scalable/apps
    │   └── oxygen
    │       ├── 22x22/apps
    │       ├── 32x32/apps
    │       ├── 48x48/apps
    │       └── 64x64/apps
    ├── package
    ├─────────────────────── openSUSE
    └── SLE                  │
        ├── animations       ├── animations
        ├── wizard           │   (see below)
        ├── wmconfig         ├── wmconfig
        └── worldmap         └── worldmap

Icons
-----

The only icons in hicolor here are pattern-* for yast-packager. Other icons are
shipped with the module that uses them.

Oxygen and Crystal themes are still shipped, but pretty much deprecated due to
lack of maintenance.

Wizard
------

This is the fancy YaST theme used in the Qt installation workflow.

The `openSUSE/wizard` counterpart to `SLE/wizard` lives
in the `yast` directory of the [openSUSE branding repository][branding].

[branding]: https://github.com/openSUSE/branding/tree/leap-15.1/yast

Generated Packages
==================
All icons will be stored in /usr/share/icons/.

yast2-theme
---------------
- icons /usr/share/icons/hicolor

yast2-theme-oxygen
-----------------------
- icons /usr/share/icons/oxygen

yast2-theme-crystal
-----------------------
- icons /usr/share/icons/crystal
