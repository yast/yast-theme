#! /bin/bash
for x in 16 22 32 48 64 256
do
  mkdir -p ${x}x${x}/apps
  for name in `ls scalable/apps/ | grep ".svg" | sed 's/.svg//g'`
  do
    inkscape -z --export-png ${x}x${x}/apps/${name}.png scalable/apps/${name}.svg -w ${x} 2> /dev/null 1> /dev/null
  done
done
