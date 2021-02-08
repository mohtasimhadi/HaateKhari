import cv2


def getCascade(action):
    switcher = {
        'Mouth': cv2.CascadeClassifier('knowYourself/CascadeFiles/haarcascade_mcs_mouth.xml'),
        'Nose': cv2.CascadeClassifier('knowYourself/CascadeFiles/haarcascade_mcs_nose.xml'),
        'Eye': cv2.CascadeClassifier('knowYourself/CascadeFiles/haarcascade_eye.xml'),
        'Face': cv2.CascadeClassifier('knowYourself/CascadeFiles/haarcascade_frontalface_default.xml'),
    }
    return switcher.get(action, "nothing")


def bodyPartDetection(image, action):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = getCascade(action)
    rects = cascade.detectMultiScale(gray, 1.7, 11)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return image
