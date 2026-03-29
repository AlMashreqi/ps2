from ics_images import readImage, writeImage


def rotate_clock(image):
	"""
	Rotate a rectangular image 90 degrees clockwise.
	Input image is a 2-d list: image[row][col] = (R,G,B)
	Output size becomes (old_width x old_height).
	"""
	height = len(image)
	width = len(image[0])
	out = [[(0, 0, 0) for _ in range(height)] for _ in range(width)]

	for i in range(height):
		for j in range(width):
			out[j][height - 1 - i] = image[i][j]

	return out


def rotate_cclock(image):
	height = len(image)
	width = len(image[0])
	out = [[(0, 0, 0) for _ in range(height)] for _ in range(width)]

	for i in range(height):
		for j in range(width):
			out[width - 1 - j][i] = image[i][j]

	return out



if __name__ == "__main__":
	image, width, height = readImage("in.png")
	clockwise = rotate_clock(image)
	counterclockwise = rotate_cclock(image)
	writeImage(clockwise, "out_clockwise_90.jpg")
	writeImage(counterclockwise, "out_counterclockwise_90.jpg")
