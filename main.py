import image, median

IMAGE_DIRECTORY = "images" #change this later
img_list = []

for f in os.listdir(IMAGE_DIRECTORY):
	img_list.append(Image.init(os.path.join(IMAGE_DIRECTORY, f)))

for x in range(size_y):
	for y in range(size_x):
		r_list = []
		g_list = []
		b_list = []
		for i in img_list:
			r, g, b = i.getpixel((x,y))
			r
