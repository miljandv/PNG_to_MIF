import sys
from PIL import Image

header = """

DEPTH =  """

header_2 = """;
WIDTH = 15;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT
BEGIN\n"""

if (len(sys.argv) > 2):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    im = Image.open(input_filename)

    f = open(output_filename, 'w');

    print("> Image size: ")
    print(im.size)
    print("")
    w = im.size[0]
    h = im.size[1]

    print("> Writing to file: "+ output_filename)

    f.write(header)
    f.write(str(h*w))
    f.write(header_2)

    index = 0;


    for x in range(0, h):
        for y in range(0, w):
            r = im.getpixel((y,x))[0] & 248
            g = im.getpixel((y,x))[1] & 248
            b = im.getpixel((y,x))[2] & 248

            total = int(r/16)<<8 | int(g/16) << 4 | int(b/16);

            hexa = hex(total)

            f.write(hex(index)[2:] + ":\t"+hexa[2:]+";\n")

            index += 1

    f.write("END;")

    print(">>> DONE");

else:
    print("Invalid number of arguments")