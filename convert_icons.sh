#!/bin/bash

# Install Pillow
pip install pillow

# Check if the input and output directories exist, create them if they don't
if [ ! -d "input" ]; then
  echo "Error: input directory does not exist"
  exit 1
fi
if [ ! -d "output" ]; then
  mkdir output
fi

# Define the function to convert an image
function convert_image {
  # Get the input and output filenames
  input_file="$1"
  output_file="$2"
  # Load the image and convert it to a 2D icon
  python - <<END
from PIL import Image

input_image = Image.open("$input_file")
output_image = input_image.crop((0, 0, 16, 16))
output_image.save("$output_file")
END
}

# Loop over all files in the input directory
for input_file in input/*.png; do
  # Get the filename without the extension
  filename=$(basename "$input_file" .png)
  # Convert the image and save it to the output directory
  convert_image "$input_file" "output/$filename.png"
done
