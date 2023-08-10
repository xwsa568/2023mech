import cv2

class WebcamCamera :
    def __init__(self, camera_index=0) :
        self.cam = cv2.VideoCapture(camera_index)
    
    def take_photo(self) :
        ret, frame = self.cam.read() 

        if ret : 
            return frame
        else :
            print("Unable to take picture.")
    
    def release(self) :
        self.capture.release()

