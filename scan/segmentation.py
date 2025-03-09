import cv2
import document_scan as ds
import os


im_dir = "jot-it/scan/scanned/"
im_file_path = "jot-it/yetanother.png"
interactive_mode = False

scanner = ds.DocScanner(interactive_mode)

valid_formats = [".jpg", ".jpeg", ".jp2", ".png", ".bmp", ".tiff", ".tif"]

get_ext = lambda f: os.path.splitext(f)[1].lower()

new_img = scanner.scan(im_file_path)

cv2.imshow('contour', new_img)
cv2.waitKey()