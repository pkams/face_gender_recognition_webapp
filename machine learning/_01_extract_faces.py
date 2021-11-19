import glob
import cv2
import os
from tqdm import tqdm

def extract_face(im, cascade_file):
    # Gray
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Cascade
    cascade = cv2.CascadeClassifier(cascade_file)
    # Face detection
    face = cascade.detectMultiScale(gray, 1.3, 5)
    return face

def draw_face(im, cascade_file):
    face = extract_face(im, cascade_file)
    # Draw rectangle
    for (x,y,w,h) in face:
        cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,0), 3)
    return im

def crop_face(im, cascade_file):
    face = extract_face(im, cascade_file)
    (x,y,w,h) = face[0]
    im_cropped = im[y:y+h, x:x+w]
    return im_cropped

if __name__ == '__main__':

    # Loading files
    cascade_file = '../model/haarcascade_frontalface_default.xml'
    im = cv2.imread('data/male_000281.jpg')

    # 1. Example image
    # Drawing bouding box
    im_detected = draw_face(im.copy(), cascade_file)
    cv2.imshow('Detected face', im_detected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Crop face
    im_cropped = crop_face(im, cascade_file)
    cv2.imshow('Cropped face', im_cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2. Iterating over all files
    female_list = glob.glob('data/female/*.jpg', recursive=True)
    male_list = glob.glob('data/male/*.jpg', recursive=True)
    all_list = female_list + male_list
    errors = 0
    for image in tqdm(all_list):
        try:
            new_path = image.replace('data/', 'data/cropped/')
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            im = cv2.imread(image)
            im_cropped = crop_face(im, cascade_file)
            cv2.imwrite(new_path, im_cropped)
        except:
            errors+=1
            #print(f"Can't find any face in the image {image}")

    print('Total errors: ', errors)

