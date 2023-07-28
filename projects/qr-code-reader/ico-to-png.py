from PIL import Image

img = Image.open(r'C:\Users\yungng07\Downloads/scan.png')
img.save('icon.ico', format='ICO', sizes=[(64,64)])
