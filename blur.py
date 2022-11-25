"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

def main():
    """
    This program helps to blur the picture.
    """
    img = SimpleImage("images/smiley-face.png")
    img.show()

    blurred_img = blur(img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()

def blur(old_img):
    """
    :param img:old one with less blurring
    :return:img is new one with one more blurring
    """
    #  create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    # Loop over the picture
    for x in range(old_img.width):
        for y in range(old_img.height):
            #  get pixel of new_img at x,y
            pixel = new_img.get_pixel(x, y)
            o_img = old_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y ==0:
                # Get pixel at the top-left corner of the image.
                pixel_right = old_img.get_pixel(x , y+1)
                pixel_down = old_img.get_pixel(x+1, y)
                pixel_downandright = old_img.get_pixel(x + 1, y+1)
                pixel.red = (pixel_right.red + pixel_down.red + pixel_downandright.red + o_img.red) //4
                pixel.green = (pixel_right.green + pixel_down.green + pixel_downandright.green + o_img.green) // 4
                pixel.blue = (pixel_right.blue + pixel_down.blue + pixel_downandright.blue + o_img.blue) // 4

            elif x == 0 and y == old_img.width-1:
                # Get pixel at the top-right corner of the image.
                pixel_left = old_img.get_pixel(x, y - 1)
                pixel_down = old_img.get_pixel(x + 1, y)
                pixel_downandleft = old_img.get_pixel(x + 1, y - 1)
                pixel.red = (pixel_left.red + pixel_down.red + pixel_downandleft.red + o_img.red) // 4
                pixel.green = (pixel_left.green + pixel_down.green + pixel_downandleft.green + o_img.green) // 4
                pixel.blue = (pixel_left.blue + pixel_down.blue + pixel_downandleft.blue + o_img.blue) // 4

            elif x == old_img.height-1 and y == 0:
                # Get pixel at the bottom-left corner of the image
                pixel_right = old_img.get_pixel(x, y + 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandright = old_img.get_pixel(x - 1, y + 1)
                pixel.red = (pixel_right.red + pixel_up.red + pixel_upandright.red + o_img.red) // 4
                pixel.green = (pixel_right.green + pixel_up.green + pixel_upandright.green + o_img.green) // 4
                pixel.blue = (pixel_right.blue + pixel_up.blue + pixel_upandright.blue + o_img.blue) // 4

            elif x == old_img.width-1 and y == old_img.height-1:
                # Get pixel at the bottom-right corner of the image
                pixel_left = old_img.get_pixel(x, y - 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandleft = old_img.get_pixel(x - 1, y - 1)
                pixel.red = (pixel_left.red + pixel_up.red + pixel_upandleft.red + o_img.red) // 4
                pixel.green = (pixel_left.green + pixel_up.green + pixel_upandleft.green + o_img.green) // 4
                pixel.blue = (pixel_left.blue + pixel_up.blue + pixel_upandleft.blue + o_img.blue) // 4

            elif x == 0 and y != 0 and y !=old_img.width-1:
                # Get top edge's pixels (without two corners)
                pixel_right = old_img.get_pixel(x, y + 1)
                pixel_down = old_img.get_pixel(x + 1, y)
                pixel_downandright = old_img.get_pixel(x + 1, y + 1)
                pixel_left = old_img.get_pixel(x , y-1)
                pixel_downandleft = old_img.get_pixel(x+1 , y-1 )
                pixel.red = (pixel_right.red + pixel_down.red + pixel_downandright.red + pixel_left.red + pixel_downandleft.red + o_img.red) // 6
                pixel.green = (pixel_right.green + pixel_down.green + pixel_downandright.green + pixel_left.green+ pixel_downandleft.green + o_img.green) // 6
                pixel.blue = (pixel_right.blue + pixel_down.blue + pixel_downandright.blue+ pixel_left.blue + pixel_downandleft.blue + o_img.blue) // 6

            elif x == old_img.height-1 and y != 0 and y != old_img.width-1:
                # Get bottom edge's pixels (without two corners)
                pixel_right = old_img.get_pixel(x, y + 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandright = old_img.get_pixel(x - 1, y + 1)
                pixel_left = old_img.get_pixel(x, y - 1)
                pixel_upandleft = old_img.get_pixel(x - 1, y - 1)
                pixel.red = (pixel_right.red + pixel_up.red + pixel_upandright.red + pixel_left.red + pixel_upandleft.red + o_img.red) // 6
                pixel.green = (pixel_right.green + pixel_up.green + pixel_upandright.green + pixel_left.green+ pixel_upandleft.green + o_img.green) // 6
                pixel.blue = (pixel_right.blue + pixel_up.blue + pixel_upandright.blue+ pixel_left.blue + pixel_upandleft.blue + o_img.blue) // 6

            elif x != 0 and x != old_img.width-1 and y == 0:
                # Get left edge's pixels (without two corners)
                pixel_right = old_img.get_pixel(x, y + 1)
                pixel_down = old_img.get_pixel(x + 1, y)
                pixel_downandright = old_img.get_pixel(x + 1, y + 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandright = old_img.get_pixel(x - 1, y + 1)
                pixel.red = (pixel_right.red + pixel_down.red + pixel_downandright.red + pixel_up.red + pixel_upandright.red + o_img.red) // 6
                pixel.green = (pixel_right.green + pixel_down.green + pixel_downandright.green + pixel_up.green+ pixel_upandright.green + o_img.green) // 6
                pixel.blue = (pixel_right.blue + pixel_down.blue + pixel_downandright.blue+ pixel_up.blue + pixel_upandright.blue + o_img.blue) // 6

            elif x != 0 and x != old_img.width-1 and y == old_img.height-1:
                # Get right edge's pixels (without two corners)
                pixel_left = old_img.get_pixel(x, y - 1)
                pixel_down = old_img.get_pixel(x + 1, y)
                pixel_downandleft = old_img.get_pixel(x + 1, y - 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandleft = old_img.get_pixel(x - 1, y - 1)
                pixel.red = (pixel_left.red + pixel_down.red + pixel_downandleft.red + pixel_up.red + pixel_upandleft.red + o_img.red) // 6
                pixel.green = (pixel_left.green + pixel_down.green + pixel_downandleft.green + pixel_up.green+ pixel_upandleft.green + o_img.green) // 6
                pixel.blue = (pixel_left.blue + pixel_down.blue + pixel_downandleft.blue+ pixel_up.blue + pixel_upandleft.blue + o_img.blue) // 6

            else:
                # Inner pixels.
                pixel_left = old_img.get_pixel(x, y - 1)
                pixel_down = old_img.get_pixel(x + 1, y)
                pixel_downandleft = old_img.get_pixel(x + 1, y - 1)
                pixel_up = old_img.get_pixel(x - 1, y)
                pixel_upandleft = old_img.get_pixel(x - 1, y - 1)
                pixel_right = old_img.get_pixel(x, y + 1)
                pixel_downandright = old_img.get_pixel(x + 1, y + 1)
                pixel_upandright = old_img.get_pixel(x - 1, y + 1)
                pixel.red = (pixel_left.red + pixel_down.red + pixel_downandleft.red + pixel_up.red + pixel_upandleft.red + pixel_right.red + pixel_downandright.red + pixel_upandright.red + o_img.red) // 9
                pixel.green = (pixel_left.green + pixel_down.green + pixel_downandleft.green + pixel_up.green+ pixel_upandleft.green+ pixel_right.green+ pixel_downandright.green + pixel_upandright.green + o_img.green) // 9
                pixel.blue = (pixel_left.blue + pixel_down.blue + pixel_downandleft.blue+ pixel_up.blue + pixel_upandleft.blue+ pixel_right.blue+ pixel_downandright.blue + pixel_upandright.blue + o_img.blue) // 9
    return new_img


if __name__ == '__main__':
    main()
