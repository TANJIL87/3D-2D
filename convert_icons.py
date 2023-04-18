import os

import shutil

import requests

import zipfile

from io import BytesIO

from PIL import Image

# Define the input and output directories

input_dir = "resource_pack_folder"

output_dir = "output_folder"

# Get the resource pack URL from the GitHub issue

resource_pack_url = input("Enter the URL of the resource pack: ")

# Download the resource pack and extract it

response = requests.get(resource_pack_url)

zipfile_obj = zipfile.ZipFile(BytesIO(response.content))

zipfile_obj.extractall(input_dir)

# Loop through every directory and file in the input directory

for root, dirs, files in os.walk(input_dir):

    for filename in files:

        if filename.endswith(".png"):

            # Load the 3D Minecraft item icon as an image

            input_path = os.path.join(root, filename)

            image = Image.open(input_path)

            # Crop the top face of the item icon

            top_face = image.crop((40, 0, 72, 32))

            # Resize the top face to a 2D icon size

            icon_size = (32, 32)

            resized_icon = top_face.resize(icon_size)

            # Save the resized 2D icon as a PNG file in the output directory

            output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))

            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            resized_icon.save(output_path)

# Create a ZIP file of the output directory

shutil.make_archive(output_dir, "zip", output_dir)

# Print the download URL of the ZIP file

print(f"Download the output ZIP file at https://github.com/username/repo/releases/download/v1.0/output.zip")

# Clean up the extracted resource pack folder

shutil.rmtree(input_dir)

