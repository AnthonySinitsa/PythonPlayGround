from gimpfu import *

def save_as_r16(image, drawable, filename):
    width = image.width
    height = image.height
    with open(filename, 'wb') as file:
        for y in range(height):
            for x in range(width):
                # Get grayscale value of pixel (x, y)
                grayscale_value = pdb.gimp_drawable_get_pixel(drawable, x, y)[0]
                # Convert grayscale value to 16-bit format if needed
                pixel_value_16bit = grayscale_value * 256  # Example conversion, adjust as needed
                # Write pixel_value_16bit to binary file
                file.write(pixel_value_16bit.to_bytes(2, byteorder='little'))  # Write 16-bit little-endian

# Register the script with GIMP
register(
    "python-fu-save-as-r16",
    "Save image as .r16 file",
    "Save image pixels as 16-bit binary file",
    "Author Name",
    "Author Name",
    "2024",
    "<Image>/File/Save as .r16",
    "*",
    [
        (PF_FILE, "filename", "Output filename", "output.r16"),
    ],
    [],
    save_as_r16
)

main()
