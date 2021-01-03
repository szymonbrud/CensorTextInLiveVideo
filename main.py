import cv2
import pytesseract

# settings
isUsingLiveCamera = True
pathToImages = '1.png'
wordsToCensored = ['Hello', 'oder']

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def liveCameraUse():
    capture = cv2.VideoCapture(0)

    while True:
        success, img = capture.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        censor(img)


def photoCensure():
    img = cv2.imread(pathToImages)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    censor(img)


def censor(img):
    hImg, wImg, _ = img.shape

    words = pytesseract.image_to_data(img)

    for x, w in enumerate(words.splitlines()):
        if x != 0:
            w = w.split()

            left, top, width, height = int(
                w[6]), int(w[7]), int(w[8]), int(w[9])

            if len(w) == 12:
                censure = False

                for censureWord in wordsToCensored:
                    if censureWord in w[11]:
                        censure = True

                if censure:
                    print(f'{w[11]} is censure: {censure}')

                    cv2.rectangle(img, (left, top), (left + width,
                                                     top + height), (100, 100, 255), -1)

    cv2.imshow('result', img)
    cv2.waitKey(113)


if isUsingLiveCamera:
    liveCameraUse()
else:
    photoCensure()
