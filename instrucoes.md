### 1. Create (or activate) venv
python -m venv <nome_env> #criar <br>
.\<nome_env>\Scripts\activate.bat #ativar

### 2. Install dependencies
pip install numpy pandas opencv-python matplotlib pillow scipy sklearn <br>
or pip install -r requirements.txt <br>
pip freeze > requirements.txt #output requirements.txt <br>

### 3. Image processing and ML intuition
- Read image (opencv)
- Convert to grayscale (opencv)
- Found face with cascade algorithm (opencv)
- Index, Structure and Normalize (numpy)
- Reduce dimensionality with PCA (sklearn)
- Apply ML model (sklearn)
- Output confidence score, bouding box of face and class (M/F) (sklearn)

#### 3.1 Open Images
- cv2.imread() -> np.array, cv2.imshow() #BGR
- plt.imread() -> np.array, plt.imshow() #RGB
- PIL.Image.open().toarray() #RGB
- r = im[:,:,0], b = im[:,:1], etc
- im.shape() -> return dimensions and channels
- plt.imshow(cmap='gray'), plt.show() #gray

#### 3.2 Convert to gray and pixels intuition
- gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
- pixels goes from 0 to 255
- if image is colored, it will be 3 channels
- For a colored image of 48x48, we have im.shape() == (48,48,3)
- For a grayscaled image of 48x48, we have im.shape() == (48,48)
- 0 -> Darker, 255 -> Lighter
- cv2.resize(im, (<new_shape>), cv2.INTER_AREA) #im, (h,w), flag
- INTER_AREA -> Fast and Ok, INTER_CUBIC -> Slow and Good

### 4. Detecting faces
- Read img
im = cv2.imread("<path>.extension") #.jpg, .png, .bmp
- Convert to grayscale
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
- Apply Cascade Classifier
haar = cv2.CascadeClassifier("<path>.xml")
aces = haar.detectMultiScale(gray, 1.3, 5)
print(faces) -> [[x1,y1,d1,d2]]
- Show result
cv2.rectangle(im, (x1, y1),(x1+d1, y1+d2), (0,255,0), 3)
plt.imshow(im)
- Crop face (if needed)
face_crop = im[x1:x1+d1, y1:y1+d2]
plt.imshow(face_crop)
cv2.imwrite('<name_of_image>')

### 5. Applying image processing to videos
cap = cv2.VideoCapture('<>.mp4')

haar = cv2.CascadeClassifier('<>'.xml)

def face_detect(im):
    gray = cv2.cvtColor(...)
    faces = haar.detectMultiScale(gray, 1.3, 5)
    
    for x,y,w,h in faces:
        cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,255), 3)
    
    return im

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    frame = face_detect(frame)
    
    cv2.imshow('object_detect', frame)
    if cv2.waitKey(20) == 27: #waitKey(FPS)
        break
    cv2.destroyAllWindows()
    cap.release()
    