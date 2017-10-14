# USAGE
# python image_diff.py --first images/original_01.png --second images/modified_01.png

#sudo apt-get install python-pip
#sudo apt-get install python-matplotlib python-numpy python-pil python-scipy
#sudo apt-get install build-essential cython
#sudo apt-get install python-skimage
#pip install -U scikit-image
#pip install -U opencv-python
#pip install -U imutils

# import the necessary packages
from skimage.measure import compare_ssim
import matplotlib.pyplot as plt
import argparse
import numpy
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
ap.add_argument("-s", "--second", required=True,
	help="second")
args = vars(ap.parse_args())

# load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
#cv2.imshow("Original", imageA)
#cv2.imshow("Modified", imageB)
#cv2.imshow("Diff", diff)
#cv2.imshow("Thresh", thresh)
#cv2.waitKey(0)

#plt.imshow(imageA,cmap='gray')
#plt.show()
#plt.imshow(imageB,cmap='gray')
#plt.show()
#plt.imshow(diff,cmap='gray')
#plt.show()
#plt.imshow(thresh,cmap='gray')
#plt.show()

if cnts:
	cv2.imwrite('img1diff.png',imageA)
	cv2.imwrite('img2diff.png',imageB)
else:
	print("No difference")

#plt.figure('Differences between the images')
#plt.subplot(211)
#plt.imshow(imageA)
#plt.subplot(212)
#plt.imshow(imageB)
#plt.show()
