import cv2
import joblib
import numpy as np

def find_faces_and_gender(im, cascade_file, pca_file, model_file):
    # OpenCV step
    im_copy = im.copy()
    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray, 1.3, 5)
    (x,y,w,h) = face[0]
    cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,0), 3)
    crop = im_copy[y:y+h, x:x+w]
    crop_gray = gray[y:y+h, x:x+w]
    crop_resized = cv2.resize(crop_gray, (100,100))

    # PCA step
    norm = crop_resized / 255.0
    flat = norm.flatten()
    pca = joblib.load(pca_file)
    feat = pca.transform(flat.reshape(1,-1))
    #print(feat.shape)

    # Model step
    model = joblib.load(model_file)
    pred = model.predict(feat)
    pred_proba = model.predict_proba(feat)
    inf = ['Male' if pred == 0 else 'Female'][0]
    confidence = pred_proba[0][np.argmax(pred_proba[0])]

    return inf, confidence, face[0], crop

def draw_face_and_gender(im, inf, confidence, coord, crop):
    (x,y,w,h) = coord
    text = f'{inf} - {round(confidence,2)}'
    cv2.putText(im, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #cv2.imshow('cropped face', crop)
    return im

if __name__ == '__main__':
    cascade_file = '../model/haarcascade_frontalface_default.xml'
    im_file = '../data/male_000281.jpg'
    model_file = '../model/best_model.joblib'
    pca_file = '../model/pcafeat_model.joblib'

    im = cv2.imread(im_file)
    inf, confidence, coord, crop = find_faces_and_gender(im, cascade_file, pca_file, model_file)
    result = draw_face_and_gender(im, inf, confidence, coord, crop)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
