# import the opencv library
import cv2
import torch
# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
img_counter = "analyze"  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    
    cv2.imshow('frame', frame)
    
    #same image
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))  
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    

    # Images
    img = frame  # or file, Path, PIL, OpenCV, numpy, list
    # Inference
    results = model(img)
    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()