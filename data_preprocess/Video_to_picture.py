import cv2



def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)

VideoCapture = cv2.VideoCapture("3.asf")

success, frame = VideoCapture.read()

i = 0
j = 0
timeF = 100

while success:
    i = i + 1
    if (i % timeF ==0):
        j = j + 1
        save_image(frame, './image1/image3_', j)
        print('save image:', j)
    success, frame = VideoCapture.read()
