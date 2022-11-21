# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
#images = convert_from_path('C:\Users\Admin\Desktop\IMMANUAL R\NAAC Overall Internship\Mech\3_7_1_1 _17-18 Mech.pdf')
images = convert_from_path('3_7_1_1_18-19 Mech.pdf', poppler_path=r"C:\Program Files (x86)\poppler-0.68.0_x86\poppler-0.68.0\bin")

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
