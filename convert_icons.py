import os
import zipfile
from urllib.request import urlretrieve
from io import BytesIO
from PIL import Image

# URL of the Minecraft resource pack
resource_pack_url = input()

# Download the resource pack and extract the assets
with zipfile.ZipFile(BytesIO(urlretrieve(resource_pack_url)[0]), 'r') as zip_ref:
    zip_ref.extractall('./resource_pack')

# Create the output directory if it doesn't exist
output_dir = './converted_icons'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all the item textures and convert them to 2D
for root, dirs, files in os.walk('./resource_pack/assets/minecraft/textures/item'):
    for file in files:
        if file.endswith('.png'):
            # Load the 3D icon image
            image_3d = Image.open(os.path.join(root, file))

            # Get the top face of the 3D icon and rotate it to face the camera
            image_2d = image_3d.crop((8, 0, 16, 8)).rotate(45, expand=True)

            # Resize the image to 32x32 and save it as a PNG file
            image_2d = image_2d.resize((32, 32))
            image_2d.save(os.path.join(output_dir, file))
            
# Create a ZIP archive of the converted icons
with zipfile.ZipFile('./output.zip', 'w') as zip_file:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            zip_file.write(os.path.join(root, file), file)
