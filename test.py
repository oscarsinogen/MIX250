# MÅL for prosjekt:
#
# 1: Få til ansiktsgjenkjenning
# 2: Få til -..- på BT sin forside
# 3: Eksportert bildedata til annen fil.
# 4: Lage UI for representering av ett dataelement

%matplotib as matplotlib

from google.colab import files
file = files.upload()

from google.colab.patches import cv2_imshow
import cv2
from google.colab import files

def get_input():
  uploaded = files.upload()
  for file_name in uploaded.keys():
    return file_name

def estimate_happiness(photo_name):
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  img = cv2.imread(photo_name)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  print(faces)

def show_results(happiness_level, photo_name):
  img = cv2.imread(photo_name, cv2.IMREAD_UNCHANGED)
  cv2_imshow(img)
  #for (x,y,w,h) in faces:
   # cv2.rectangle(img, (x, y), (x+w, y+h),(0, 255, 0), 2)
  #cv2_imshow(img)
  print(f'He/she is {happiness_level}')

input_photo = 'cruz2003.jpg'
happiness_level = estimate_happiness(input_photo)
show_results(happiness_level, input_photo)
