from rembg import remove as r
from PIL import Image as i
ig=i.open("images.jpeg")
output=r(ig)
output.save("output.png")