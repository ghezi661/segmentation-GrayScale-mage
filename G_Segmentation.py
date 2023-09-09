import cv2

image = cv2.imread('....jpeg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()