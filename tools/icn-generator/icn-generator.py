from PIL import Image, ImageDraw
import os, sys
from optparse import OptionParser

usage = "usage: %prog [options] <32x32 image file>"
parser = OptionParser(usage=usage)
parser.add_option("-c", "--c-output", action="store_true", dest="generate_c", default=False, help="Generate a C-language header file definition for the icon")
parser.add_option("-b", "--blackout-mask", action="store_true", dest="generate_solid_mask", default=False, help="Generate an all-black, square mask")

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

def get_bytes_for_image(im):
    # get the apple format for ICN# (8 pixels per byte)
    # in an array of bytes
    output = []
    for y in range(0, im.height):
        for x in range(0, im.width // 8):
            this_byte = 0
            for bit in range(0, 8):
                this_byte = (this_byte << 1) | (im.getpixel((x * 8 + bit, y)) & 0x01)
            output.append(this_byte)
    return output

# Output the pixel data in raw hex
def output_image_hex(im, mask):
    def print_image_as_hex(i):
        bytes = get_bytes_for_image(i)
        assert(len(bytes) == 128)
        for i in range(0, len(bytes)):
            print(padded_hex(bytes[i]), end = " ")
        print() # put a newline between entries (remove this if it causes problems)

    print_image_as_hex(im)
    print_image_as_hex(mask)

def output_image_c(im, mask):
    # basically the same as the other code, but in C format
    im_bytes = get_bytes_for_image(im)
    mask_bytes = get_bytes_for_image(mask)
    appended = im_bytes + mask_bytes

    print(f'static const unsigned char icon[] = {{ /* {args[0]} */')
    # TODO: pretty print this so it's not just one big glob
    print('\t' + ', '.join([ "0x{:02x}".format(b) for b in appended ]))
    print('};')
    return

def generate_mask(im, solid_mask = False):
    if solid_mask:
        mask = Image.new('1', (32, 32))
        assert(32 == mask.width)
        colour = 0xff
        ImageDraw.floodfill(mask, (0,0), colour)
    else:
        mask = im.copy()
        # rough outline-based mask:
        #   for each line:
        #       draw black from the first black pixel
        #       to the last black pixel of the line
        for y in range(0, mask.height):
            # find the first black and last black pixel of this line
            first_black = -1
            last_black = -1
            for x in range(0, mask.width):
                if mask.getpixel((x, y)) == 0:
                    if first_black < 0:
                        first_black = x
                    last_black = x
            if first_black >= 0:
                # black out the assumed mask on this line
                for x in range(first_black, last_black):
                    mask.putpixel((x, y), 0)
    return mask

mask = generate_mask(im, options.generate_solid_mask)

if options.generate_c:
    output_image_c(im, mask)
else:
    output_image_hex(im, mask)

# Attempt to guess the mask as well (flood-fill then invert?)
