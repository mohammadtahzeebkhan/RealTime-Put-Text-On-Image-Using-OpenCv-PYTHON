#Demo
#https://youtu.be/rDJeeUr3oDA
import cv2

# read image
img = cv2.imread('img.jpg')

# show image
cv2.imshow('image', img)

#define the events for the
# mouse_click.
def mouse_click(event, x, y,flags, param):
	print(event)
	# to check if left mouse
	# button was clicked
	if event == cv2.EVENT_LBUTTONDOWN:
		
		# font for left click event
		font = cv2.FONT_HERSHEY_SIMPLEX
		youtube = 'SUBCRIBE'
		
		# display that left button
		# was clicked.
		cv2.putText(img, youtube, (x, y),
					font, 1,
					(25,5,255),
					2)
		cv2.imshow('image', img)
		
		
	# to check if right mouse
	# button was clicked
	print("PARADISE_HOPE.................. TESTING")
	if event == cv2.EVENT_RBUTTONDOWN:
		
		# font for right click event
		font = cv2.FONT_HERSHEY_SIMPLEX
		youtube_channel = 'PARADISE_HOPE'
		
		# display that right button
		# was clicked.
		cv2.putText(img, youtube_channel, (x, y),
					font, 1,
					(0, 0, 255),
					2)
		cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
print("TESTING")
cv2.waitKey(0)

# close all the opened windows.
cv2.destroyAllWindows()
