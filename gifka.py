

import cv2


h = 11      # height
w = 6       # width
x1 = 1
y1 = 2
x2 = 8
y2 = 2
x3 = 18
y3 = 2
x4 = 25
y4 = 2




img = cv2.imread('background.png')
d1 = img[y1:y1 + h, x1:x1 + w]
d2 = img[y2:y2 + h, x2:x2 + w]
d3 = img[y3:y3 + h, x3:x3 + w]
d4 = img[y4:y4 + h, x4:x4 + w]

for i in range(1, 4):
    d1[:, :, :] = 0                                             # h, w, channel - clear image
    di = cv2.imread('./digits/{}.png'.format(i))
    d1 += di

    for j in range(0, 10):
        d2[:, :, :] = 0
        di = cv2.imread('./digits/{}.png'.format(j))
        d2 += di

        for k in range(0, 6):
            d3[:, :, :] = 0
            di = cv2.imread('./digits/{}.png'.format(k))
            d3 += di

            for l in range(0, 10):
                d4[:, :, :] = 0
                di = cv2.imread('./digits/{}.png'.format(l))
                d4 += di

                img[5, 15] = [255, 255, 255]
                img[10, 15] = [255, 255, 255]
                cv2.imwrite('./data/im{}{}{}{}.png'.format(i, j, k, l), img)

                # break on 30:00
                if i == 3: break
            if i == 3: break
        if i == 3: break


"""
img = cv2.imread('2000.png')
img2 = img[2:13, 1:7]
img2[0, 0] = [0, 255, 0]
cv2.imwrite('im.png', img2)
#cv2.imshow('img', img)
#cv2.waitKey(0)

img = cv2.imread('background.png')
d1 = img[y1:y1 + h, x1:x1 + w]
d2 = img[y2:y2 + h, x2:x2 + w]
d3 = img[y3:y3 + h, x3:x3 + w]
d4 = img[y4:y4 + h, x4:x4 + w]

for i in range(1, 4):
    img[:, :, :] = 0             # h, w, channel - clear image
    di = cv2.imread('./digits/{}.png'.format(i))
    d1 += di
    d2 += di
    d3 += di
    d4 += di
    img[5, 15] = [255, 255, 255]
    img[10, 15] = [255, 255, 255]
    img3 = img.copy()
    #img[:, :, 2] = 0
    #img[:, :, 1] = 0
    #img[:, :, 0] = 0
    #img[:, :, :] = 0  # h, w, channel - clear image
    cv2.imwrite('im2.png', img)
"""




