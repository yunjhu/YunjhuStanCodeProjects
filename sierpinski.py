"""
File: sierpinski.py
Name: Ashley
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	a recursion to draw sierpinski triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the level of the triangles
	:param length: the length of the triangle
	:param upper_left_x: the x-location of the triangle's left point
	:param upper_left_y: the y-location of the triangle's left point
	:return: triangle
	"""
	if order == 0:
		return
	else:
		line_up = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		window.add(line_up)
		line_left = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5*length, upper_left_y+0.866*length)
		window.add(line_left)
		line_rigjt = GLine(upper_left_x + 0.5 * length, upper_left_y + 0.866 * length, upper_left_x+length,upper_left_y)
		window.add(line_rigjt)
		# Upper left
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# Upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length / 2, upper_left_y)
		# Lower
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + 0.5*length*0.866)


if __name__ == '__main__':
	main()