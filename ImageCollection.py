import cv2
import os
import time
import uuid
WORKSPACE_PATH = 'D:\Project\Tensor\Tensorflow\workspace'

IMAGE_PATH = WORKSPACE_PATH+'\images\\collectedimage\\'

labels =['hello','thanks','yes','no','iloveyou']
#labels =['no']
number_img = 5
def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i >= 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

#print("before 1")
#cap = cv2.VideoCapture(1)
#print("before 2")
#cap = cv2.VideoCapture(2)
#print("before 3")
#cap = cv2.VideoCapture(3)
#print("before 4")
#cap = cv2.VideoCapture(4)
#print("before 5")
#cap = cv2.VideoCapture(5)

try:
     for label in labels:
        #os.mkdir ('D:\Project\Tensor\Tensorflow\workspace\images\\collectedimage\\'+label)
        cap= cv2.VideoCapture(1)
        print('Collecting Image for {}'.format(label))
        time.sleep(5)

        for imgno in range(number_img):
            ret,frame =cap.read()
            imagename=os.path.join(IMAGE_PATH,label,label+'-'+'{}.jpg'.format(str(uuid.uuid1())))
            print("saving in folder",imgno,imagename)
            cv2.imwrite(imagename,frame)
            cv2.imshow('frame',frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()

except Exception as e:
    # Code to handle other exceptions
    print(f"An unexpected error occurred: {e}")

