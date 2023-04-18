#!/bin/bash

# get the download link from the issue body
link=$(echo $1 | grep -o 'https://.*')

# download and extract the resource pack
wget -O pack.zip $link
unzip pack.zip
rm pack.zip

# create output directory
mkdir -p output

# loop through all item icons
for file in $(find . -name '*.png'); do
  filename=$(basename $file)
  extension="${filename##*.}"
  filename="${filename%.*}"

  # convert to 2D
  convert -flatten -resize 32x32 "$file" "output/$filename.png"
done

# compress and upload result
tar -czvf icons.tar.gz output
rm -rf output
mkdir output
mv icons.tar.gz output/
