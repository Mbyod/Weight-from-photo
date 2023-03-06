import pytesseract
from pytesseract import Output
import cv2
from matplotlib import pyplot as pl

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lubkovda\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
img_path = r'images/44.png'
# img_path = r'images/8.jpg'
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#преобразуем изображение в серый а потом в бинарное(чб)

# img_blur = cv2.GaussianBlur(img, (7,7), 0)

img_gray =cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY) # серая пикча
_, img_binary = cv2.threshold(img_gray, 90, 225, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV) # в бинарку
# img_invert = 255 - img_binary # инверсия

# # #обводка
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# img_dilation = cv2.dilate(img_binary, rect_kernel, iterations = 3)




extracted_text = pytesseract.image_to_string(img_binary, lang="rus") # аи считывает текст с картинки
extracted_text1 = pytesseract.image_to_string(img_binary, lang="eng")

# data = pytesseract.image_to_data(img_gray, lang='eng', output_type=pytesseract.Output.DICT)
#data = pytesseract.image_to_data(img_gray, lang='rus', output_type=pytesseract.Output.DICT)
#data = pytesseract.image_to_boxes(img_gray, lang='rus')

word='кг'
word1='kg'
for weight_rus in extracted_text.split('\n'):
    if word in weight_rus:
        print(weight_rus)
for weight_eng in extracted_text1.split('\n'):
    if word1 in weight_eng:
        print(weight_eng)

# print(extracted_text,extracted_text1)
cv2.imshow('img',img_binary)
cv2.waitKey(0)


# # ЖЕСТЬ
# data = pytesseract.image_to_data(img_gray, lang='rus')
#
# for i, element in enumerate(data.splitlines()):
#     if i == 0:
#
#         continue
#     element = element.split()
#     print(element)
#     try:
#         x, y, w, h =int(element[6]), int(element[7]),int(element[8]),int(element[9])
#         cv2.rectangle(img, (x, y),(w + x, h + y),(0, 0, 255),1 )
#         cv2.putText(img,element[11],(x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0),  1)
#
#     except IndexError:
#         print("Операция пропущена")




#print(extracted_text.strip())
