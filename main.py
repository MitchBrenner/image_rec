from img_rec.Image import Image
import time

start = time.time()
img = Image("img1.png")
img.compareTo("img2.png")
end = time.time()

print("Time elapsed: ", end - start)
