import Image, webcolors
from sys import argv, exit

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        actual_name = webcolors.rgb_to_name(requested_colour)
        return actual_name
    except ValueError:
        closest_name = closest_colour(requested_colour)
        return closest_name

def main():
    if len(argv) == 1:
        print "Please provide an image file"
        exit(0)

    im = Image.open(argv[1])
    pix = im.load()

    hash_tags = ""
    insta_colors_tags = []
    for w in range(im.size[0]):
        for h in range(im.size[1]):
            color_name = get_colour_name(pix[w,h]).capitalize()
            if color_name not in insta_colors_tags:
                insta_colors_tags.append(color_name)
            hash_tags += "#PixelAt%dx%dIs%s " % (w, h, color_name) 

    insta_hash_tags = ""
    for color in insta_colors_tags:
        insta_hash_tags += "#Insta%s " % color
    
    print insta_hash_tags + " " + hash_tags


if __name__ == "__main__":
    main()