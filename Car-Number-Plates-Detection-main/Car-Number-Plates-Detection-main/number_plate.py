import cv2
import pytesseract
import socket
harcascade = "model/haarcascade_russian_plate_number.xml"
HOST = '192.168.243.70'
PORT = 8479



def capture():
    cap = cv2.VideoCapture(0)

    cap.set(3, 640) # width
    cap.set(4, 480) #height

    min_area = 500
    count = 0

    while True:
        success, img = cap.read()

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x,y,w,h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y+h, x:x+w]
                cv2.imshow("ROI", img_roi)
    
                # if text:
                #     cap.release()

    
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results",img)
            cv2.waitKey(500)
            count += 1
            cap.release()
            while True:
                img = cv2.imread('plates/scaned_img_0.jpg')
                gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                thresh =cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
                noise= cv2.medianBlur(thresh,5)
                text = pytesseract.image_to_string(thresh)
                print(text)
                server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                server.bind((HOST,PORT))

                server.listen(5)

                while True:
                    communication_socket, address = server.accept()
                    # waiting for connection
                    print("connected to the address")
                    # var = "wats up"
                    communication_socket.send(text.encode('utf-8'))
                    print(text)
                    communication_socket.close()
                    print("connection closed")

capture()

# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind((HOST,PORT))

# server.listen(5)

# while True:
#     communication_socket, address = server.accept()
#                     # waiting for connection
#     print("connected to the address")
#                     # var = "wats up"
#     text = "abcd"
#     communication_socket.send(text.encode('utf-8'))
#     print(text)
#     communication_socket.close()
#     print("connection closed")