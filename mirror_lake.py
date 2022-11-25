"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    img = SimpleImage(filename)

    b_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            #正的上半部
            b_img_p1 = b_img.get_pixel(x, y)
            b_img_p1.red = img_p.red
            b_img_p1.green = img_p.green
            b_img_p1.blue = img_p.blue
            #反的下半部
            b_img_p2 = b_img.get_pixel(x, b_img.height-1-y)
            b_img_p2.red = img_p.red
            b_img_p2.green = img_p.green
            b_img_p2.blue = img_p.blue
    return b_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
