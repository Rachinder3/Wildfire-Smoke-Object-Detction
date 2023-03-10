from datetime import datetime
from PIL import Image
from io import BytesIO
import re, time, base64
import cv2
import matplotlib.pyplot as plt
import time



current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"



def base64_2_img(img, path):
    """
    arguements:
        img: image in base 64 format
    
        path: path to store the image
    
    """
    try:
        # ensuring img is string
        if type(img) == bytes:
            img = img.decode("utf-8")
        
        
            
            
        
        base64_data = re.sub('^data:image/.+;base64,', '', img)
        
        byte_data = base64.b64decode(base64_data)
        
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        img.save(path)
        #cv2.imwrite(filename=path, img=img)
            
            
    except Exception as e:
        print(str(e))
        
        
def image_2_base64(path):
    '''
    arguements: 
        path: path of the image
        
    returns:
        image in base 64 format
    
    '''
    
    try:
        image = open(path,'rb')
        image_read = image.read()
        image_64_encode = base64.b64encode(image_read)
        image.close()
        return image_64_encode
    
        
    
    except Exception as e:
        print(str(e))
        
        
# def play_video(video_path):
    
#     cap = cv2.VideoCapture(video_path)

#     # cap = cv2.VideoCapture(0)

#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



#     if cap.isOpened() == False:
#         print("Error file not found")


#     while cap.isOpened():
#         ret, frame = cap.read()

#         if ret == True:
#             time.sleep(1/10)
    
    
    
    
    
#             img = cv2.resize(frame,(1024,640))
    
    
    
    
#             cv2.imshow('Camera feed', img)
    
#             if cv2.waitKey(10) & 0xFF == ord('q'):
#                 break
#         else:
#             break
#     cap.release()
#     cv2.destroyAllWindows()
        
            
        
    
    
    
    