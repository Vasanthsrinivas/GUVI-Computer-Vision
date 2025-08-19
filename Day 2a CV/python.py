import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Bird image.jpeg")
median = cv2.medianBlur(img,5)
plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.show()