import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


class Image:
    # threshold for SSIM
    similarity_threshold = 0.95  # Adjust as needed

    # Constructor
    def __init__(self, img):
        self.img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    # CompareTo
    def compareTo(self, other):
        other_img = cv2.imread(other, cv2.IMREAD_GRAYSCALE)

        # The cv2.SSIM() function returns the SSIM score and a map of
        # local SSIM values (which you can ignore if you're only interested
        # in the overall similarity score).
        ssim_score = ssim(self.img, other_img)

        # The closer the SSIM score is to 1, the more similar the two images are.
        if ssim_score >= Image.similarity_threshold:
            print("Images are similar.")
        else:
            print("Images are not similar.")
