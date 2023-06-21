from PIL import Image

img = Image.open('크롤링\lenna.png')

area = (100, 100, 320, 320)
CropImage = img.crop(area)

img.show()
CropImage.show()

# 큰 이미지의 파일의 썸네일 이미지 생성:thumbnail() 호출
# 속도향상을 위해서 썸네일을 사용한다.

from PIL import Image

img = Image.open('크롤링\lenna.png')

size = (64,64)
img.thumbnail(size)
img.save('크롤링\lenna-thumb.png')
img.show()


#이미지 회전 및 resize
from PIL import Image

img = Image.open('크롤링\lenna.png')
img2 = img.resize((300,300))
img2.save('크롤링\lenna_300.png')

img3 = img.rotate(90)
img3.save('크롤링\lenna_rotate.png')
img3.show()

#이미지 회전 및 flip

from PIL import Image

img = Image.open('크롤링\lenna.png')
mirrorImage = img.transpose(Image.FLIP_LEFT_RIGHT) # y축을 기준으로 x값 이동
mirrorImage.save('크롤링\lenna_mirror.png')
mirrorImage.show()

updownImage = img.transpose(Image.FLIP_TOP_BOTTOM) # x 축을 기준으로 y값 이동
updownImage.save('크롤링\lenna_updown.png')
updownImage.show()

#이미지 필터링
from PIL import Image, ImageFilter

img = Image.open('크롤링\lenna.png')
contourImage = img.filter(ImageFilter.CONTOUR)
contourImage.save('크롤링\lenna_contour.png')
contourImage.show()

blurImage = img.filter(ImageFilter.BLUR)
blurImage.save('크롤링\lenna_blur.png')
blurImage.show()

#이미지에서 R,G,B 분리
#(red, green, blue) = split()메소드 사용

from PIL import Image

new_york = Image.open('크롤링\newyork.jpg')
print(new_york.mode)

# 이미지의 R,G,B를 분리
r, g, b = new_york.split()

r.save('newyork_r.jpg')
g.save('newyork_g.jpg')
b.save('newyork_b.jpg')


