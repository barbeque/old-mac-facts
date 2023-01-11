from PIL import Image
import os, sys
from optparse import OptionParser

usage = "usage: %prog [options] <32x32 image file>"
parser = OptionParser(usage=usage)
parser.add_option("-c", "--c-output", action="store_true", dest="generate_c", default=False, help="Generate a C-language header file definition for the icon")

(options, args) = parser.parse_args()

if len(args) < 1:
    parser.print_help()
    sys.exit(1)

# Load source image
im = Image.open(args[0])
# Scale to 32x32 if it isn't already
im = im.resize((32, 32))
# Convert to 1-bit colour
im = im.convert("1")

def padded_hex(byte):
    return "{:02x}".format(byte)

# Output the pixel data
def output_image(im):
    byte_count = 0
    for y in range(0, im.height):
        for x in range(0, im.width // 8):
            this_byte = 0
            for bit in range(0, 8):
                this_byte = (this_byte << 1) | (im.getpixel((x * 8 + bit, y)) & 0x01)
            print(padded_hex(this_byte), end = " ")
            byte_count += 1
    print() # newline to clear the screen
    assert(byte_count == 128)
    
output_image(im, options)

# Attempt to guess the mask as well (flood-fill then invert?)
