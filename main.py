from rembg import remove
from PIL import Image as i
input=i.open("images.jpeg")
output=remove(input)
output.save("output.png")