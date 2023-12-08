import os
from PIL import Image, ImageChops, ImageStat

directory = "./base_screenshots"  # Replace with your directory path
png_files = [f for f in os.listdir(directory) if f.endswith('.png')]

print("Images to compare: " + str(png_files))

def is_image_blank(image):
    """Check if the image is blank (single color)"""
    extrema = image.convert("L").getextrema()
    return extrema[0] == extrema[1]

def rms_diff(image1, image2):
    """Calculate the root mean square error between two images"""
    diff = ImageChops.difference(image1, image2)
    h = ImageStat.Stat(diff).mean[0]
    return h

for filename in png_files:
    base_image = Image.open(os.path.join(directory, filename))
    test_image = Image.open(filename)

    # Check if any image is blank
    if is_image_blank(base_image) or is_image_blank(test_image):
        print(f"ERROR: {filename} is blank.")
        continue    

    # Ensure both images are the same size
    if base_image.size != test_image.size:
        test_image = test_image.resize(base_image.size)

    # Calculate RMS difference
    rms_error = rms_diff(base_image, test_image)
    if rms_error > 15:  # Threshold for error, can be adjusted
        print(f"ERROR: {filename} are different, RMS Error: {rms_error:.2f}")
    else:
        print(f"{filename} are identical.")

