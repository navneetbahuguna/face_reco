import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

def getImageWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faces = []
    Ids = []
    for imagepath in imagePaths:
        faceImg = Image.open(imagepath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(faceNp)
        print (ID)
        Ids.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
    return Ids, faces
Ids, faces = getImageWithId(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
