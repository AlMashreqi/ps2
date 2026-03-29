from ics_images import readImage, writeImage


def crop_image(image, x, y, w, h):
	if not image or not image[0]:
		raise ValueError("Image is empty")
	if w <= 0 or h <= 0:
		raise ValueError("Crop width and height must be > 0")
	if x < 0 or y < 0:
		raise ValueError("Top-left crop point must be inside image")

	img_h = len(image)
	img_w = len(image[0])
	if x >= img_w or y >= img_h:
		raise ValueError("Top-left crop point must be inside image")
	if x + w > img_w or y + h > img_h:
		raise ValueError("Crop goes outside image bounds")

	return [row[x:x+w] for row in image[y:y+h]]


def crop_and_resize(image, x, y, w, h, displayW, displayH):
	if displayW <= 0 or displayH <= 0:
		raise ValueError("Display width and height must be > 0")

	cropped = crop_image(image, x, y, w, h)
	out = [[(0, 0, 0) for _ in range(displayW)] for _ in range(displayH)]

	for out_y in range(displayH):
		src_y = int(out_y * h / displayH)
		if src_y >= h:
			src_y = h - 1
		for out_x in range(displayW):
			src_x = int(out_x * w / displayW)
			if src_x >= w:
				src_x = w - 1
			out[out_y][out_x] = cropped[src_y][src_x]

	return out


if __name__ == "__main__":
	image, width, height = readImage("in.png")

	x, y = 20, 20
	w, h = 120, 80
	cropped = crop_image(image, x, y, w, h)
	writeImage(cropped, "out_cropped.jpg")

	displayW, displayH = 240, 120
	stretched = crop_and_resize(image, x, y, w, h, displayW, displayH)
	writeImage(stretched, "out_cropped_resized.jpg")
