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


def recognition(imagePath):
    resultPath = 'media/knowYourself/temp/'
    image = bodyPartDetection(cv2.resize(cv2.imread(imagePath), None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA),
                              'Face')
    cv2.imwrite(resultPath + 'Face.jpg', image)
    image = bodyPartDetection(cv2.resize(cv2.imread(imagePath), None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA),
                              'Nose')
    cv2.imwrite(resultPath + 'Nose.jpg', image)
    image = bodyPartDetection(cv2.resize(cv2.imread(imagePath), None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA),
                              'Eye')
    cv2.imwrite(resultPath + 'Eye.jpg', image)
    image = bodyPartDetection(cv2.resize(cv2.imread(imagePath), None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA),
                              'Mouth')
    cv2.imwrite(resultPath + 'Mouth.jpg', image)
