Overview
--------

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
        ├── control-center   ├── control-center
        ├── desktops         │   (?)
        ├── testpage         ├── testpage
        ├── wallpapers       │   (?)
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

[branding]: https://github.com/openSUSE/branding/tree/13.2/yast
