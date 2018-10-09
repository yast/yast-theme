#! /bin/bash
for x in 16 22 32 48 64 256
do
  mkdir -p ${x}x${x}/apps
  for name in `grep -v '^#' new-icons.txt`
  do
    inkscape -z --export-png ${x}x${x}/apps/${name}.png scalable/apps/${name}.svg -w ${x} 1> /dev/null
    optipng -o7 ${x}x${x}/apps/${name}.png 1> /dev/null
  done
done
