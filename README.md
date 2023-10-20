Overview
========

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
- `/usr/share/icons/hicolor`

yast2-theme-oxygen
-----------------------
- `/usr/share/icons/oxygen`

yast2-theme-breeze
-----------------------
- `/usr/share/icons/breeze`
- `/usr/share/icons/breeze-dark`

## Building the SLE Installation Theme

The SLE (SUSE Linux Enterprise) installation theme files are built from the
`*.scss` sources in the `src/` subdirectory. If you change any of the source
files then regenerate the files (see below) and commit the changes to Git
as well.

The Git repository contains the generated files to simplify the package build
and testing the changes in a real installation.

### Pre-Requisities

- Install npm: `sudo zypper install npm-default`
- Go to the `src/` subdirectory.
- Install the SASS processor and the tools: `npm ci`
  - The NPM packages are installed into the `node_modules` subdirectory

### Building the QSS and CSS Files

- Run `rake generate`
- This generates all `theme/SLE/wizard/*.qss` and `theme/SLE/wizard/*.css`
  files.

## Updating the NPM Packages

The `npm ci` command installs the NPM packages exactly in the versions specified
in the `package-lock.json` file.

If you want to update the packages to the latest semver compatible version then
run command `npm install`.

If you want to update the packages to a newer, possibly incompatible version,
then edit the `package.json` file and run `npm install`. Carefully check the
built result.

In all cases do not forget to commit the changes in both `package.json` and
`package-lock.json` files to git.

### Sources

- `src/scss/components/*.scss` - style definition split into logical groups
- `src/scss/theme-vars/*.scss` - color definitions for each theme, some
  shared settings
- `src/scss/*.scss` - the main files, these are rendered to the final QSS files


### Linting

This package uses the [Stylelint](https://github.com/stylelint/stylelint) tool
for linting with the [stylelint-config-standard-scss](
https://github.com/stylelint-scss/stylelint-config-standard-scss)
default configuration.

Because the Qt style sheet supports only a subset of the CSS features and some
values or settings are a bit different than in full CSS some checks were disabled
or the settings were adjusted. See the [`src/.stylelintrc.yml`](
https://github.com/yast/yast-theme/blob/master/src/.stylelintrc.yml) configuration
file.

You can find the descriptions of the Stylelint rules in the
[documentation](https://stylelint.io/user-guide/rules/list).

- Run `npx gulp lint` to start the linter.
- This will check whether the files are valid and well formatted.

## Testing in Installation

The `Rakefile` has been adapted to support the `yupdate` tool, that allows
patching the installer directly from GitHub or from a local Git checkout (see
the [documentation](
https://github.com/yast/yast-installation/blob/master/doc/yupdate.md)).

*Do not forget to regenerate the theme files if you touch any `*.scss`
source file!*
