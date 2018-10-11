import cv2
import numpy as np
import csv
img=cv2.imread("Map.bmp")
imgg=cv2.resize(img,(600,600),interpolation=cv2.INTER_CUBIC)
imgg[np.where(imgg[:,:,2]>230)]=[255,255,255]
imgg[np.where(imgg[:,:,2]<230)]=[0,0,0]
cv2.imwrite('nicemap.jpg',imgg)
csvfile=open("AllBirdsv4.csv",encoding='ISO-8859-1')
reader=csv.reader(csvfile)
name=[]
i=0
for row in reader:
    if reader.line_num==1:
        continue
    if not row[1] in name:
        name.append(row[1])
        i=i+1
    try:
        x=int(row[6])
        y=int(row[7])
        #print(x, y)
        imgg[3*x-2:3*x+1,597-3*y:600-3*y]=[220,0,0]
    except:
        pass
    continue

cv2.imshow("img",imgg)
cv2.waitKey(0)




