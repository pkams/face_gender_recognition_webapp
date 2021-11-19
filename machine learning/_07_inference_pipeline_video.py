import cv2
from _06_inference_pipeline import find_faces_and_gender, draw_face_and_gender

if __name__ == '__main__':

    cascade_file = '../model/haarcascade_frontalface_default.xml'
    video_file = '../data/video.mp4'
    model_file = '../model/best_model.joblib'
    pca_file = '../model/pcafeat_model.joblib'

    cap = cv2.VideoCapture(video_file)

    while True:
        ret, frame = cap.read()

        if ret != True:
            break

        try:
            inf, confidence, coord, crop = find_faces_and_gender(frame, cascade_file, pca_file, model_file)
            frame = draw_face_and_gender(frame, inf, confidence, coord, crop)
        except:
            pass

        cv2.imshow('Video',frame)
        cv2.waitKey(10)

cv2.destroyAllWindows()
cap.release()