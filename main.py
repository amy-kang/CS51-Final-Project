import median, os
from image import Picture

IMAGE_DIRECTORY = "amy"
img_list = []
size_x = None
size_y = None

for f in os.listdir(IMAGE_DIRECTORY):
	img_list.append(Picture(filename = os.path.join(IMAGE_DIRECTORY, f)))

if img_list:
	size_x = img_list[0].width
	size_y = img_list[0].height

image = Picture(type = 'RGB', size = (size_x, size_y))

for y in range(size_y):
	for x in range(size_x):
		r_list = []
		g_list = []
		b_list = []
		for i in img_list:
			r, g, b = i.get_RGB_value((x,y))
			r_list.append(r)
			g_list.append(g)
			b_list.append(b)

		#rm = median.quick_select(r_list, len(r_list)/2)
		#gm = median.quick_select(g_list, len(g_list)/2)
		#bm = median.quick_select(b_list, len(b_list)/2)

		rm = median.get_median(r_list, len(r_list)/2)
		gm = median.get_median(g_list, len(g_list)/2)
		bm = median.get_median(b_list, len(b_list)/2)

		image.put_RGB_value((x,y),(rm,gm,bm))

image.save(IMAGE_DIRECTORY + '_output.png')

