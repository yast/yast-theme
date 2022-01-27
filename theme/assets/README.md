# Building the YaST Installation Theme

## Pre-Requisities

- Install npm: `sudo zypper install npm-default`
- Install the SASS processor and the tools: `npm install`
  - The NPM packages are installed into the `node_modules` subdirectory

## Build the CSS File

- Run `npx gulp`
- This generates both CSS themes:
  - `theme/SLE/wizard/installation.qss` (the default dark theme)
  - `theme/SLE/wizard/installation-light.qss` (the alternative light theme)