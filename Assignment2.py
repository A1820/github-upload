import numpy as np
import cv2 # OpenCV

# Assigning Variables
drawing = False
ix,iy = -1,-1


# Defining Functions
def draw_rectangle (event,x,y,flags,param):
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing= True
        ix,iy =x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing==True:
             cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1) # Allows to draw solid rectangle while dragging the mouse
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1) # Stops the drawing


# Opening Of Image
img = np.zeros((512,512,3)) # Blank black image

cv2.namedWindow(winname='back')

cv2.setMouseCallback('back',draw_rectangle)

while True:
    cv2.imshow('back',img) #Shows both the image and the rectangle being drawn
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()
