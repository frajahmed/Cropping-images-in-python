from PIL import Image
import os, glob
import cv2
import time

# #####Erste Methode###########
# im = Image.open('1.jpg')    #bilde name
# im.show()   #bilder unbearbeitet zeigen
# cropped = im.crop((800,450,1330,750)) #auf x von 800 bis 1330 und auf y von 450 bis 750
# cropped.show()  #finish bilder zeigen
# cropped.save('1-1.jpg')


###########zweite Methode################


sizes=[(710,361,1258,795), (711, 362, 1259, 796)
]
a=1
for filename in glob.glob(r"C:\Users\ahmed\OneDrive\Desktop\Masterarbeit\Programme\Frontal or not Model\*jpg"):
    for i in sizes:
        new = Image.new('RGB', (1100, 1100), color='white')
        img=Image.open(filename)
        imm=img.crop(box=(i))
        imm1 = imm.resize((1000, 1000))
        new.paste(imm1, (350, 50))
        new.save("Data-Training"+"_"+str(a)+".jpg")
        a+=1