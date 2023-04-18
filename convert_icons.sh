#!/bin/bash

# Install necessary dependencies
sudo apt-get update
sudo apt-get install -y imagemagick

# Download and extract the resource pack
wget -O resources.zip $1
unzip -o resources.zip -d resources

# Loop through each item icon in the 3D assets directory
for file in resources/assets/minecraft/textures/item/*.png; do
  # Get the filename without extension
  filename=$(basename -- "$file")
  filename="${filename%.*}"

  # Convert the 3D icon to a 2D icon using ImageMagick
  convert "$file" -crop 64x64+0+96 "output/${filename}.png"
done

# Zip the output folder
zip -r output.zip output

# Clean up
rm -rf resources.zip resources output
