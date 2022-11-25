"""
File: blur.py
Name:洪筠筑
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:old one with less blurring
    :return:img is new one with one more blurring
    """
    blurred = SimpleImage.blank(img.width, img.height)
    for y in range(img.width):
        for x in range(img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1,2,1):
                for j in range(-1, 2, 2):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x,pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return blurred


def main():
    """
    This program helps to blur the picture.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
