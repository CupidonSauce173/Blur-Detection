# USAGE
# python detect_blur.py --images images
# python detect_blur.py --images <folder_name>
import os
import sys
import argparse
try:
    import cv2
except ImportError:
    sys.exit("""Dependency 'cv2' is missing. Please install it with : pip install opencv-python""")
try:
    from imutils import paths
except ImportError:
    sys.exit("""Dependency 'imutils' is missing. Please install it with : pip install imutils""")
try:
    from tqdm import tqdm
except:
    sys.exit("""Dependency 'tqdm' is missing. Please install it with : pip install tqdm""")

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
ap.add_argument("-o", "--output_file_name", type=str, default="results.txt",
    help="set a custom output file name for the results.")
args = vars(ap.parse_args())
results_name = args["output_file_name"]
image_list = list(paths.list_images(args["images"]))
results_file = open(results_name, "w")
  
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

def process_images(index):
        image = cv2.imread(image_list[index])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = round(variance_of_laplacian(gray), 3)
        text = "Not Blurry"
        if fm < args["threshold"]:
            text = "Blurry"
        results_file.write(image_list[index].replace("images\\", ""))
        results_file.write(" SCORE : {} {}\n".format(fm, text))
        results_file.write("\n")


folder = args['images']
count = 0
for base, dirs, files in os.walk(folder):
    for Files in files:
        count += 1
print("Total files: " + str(count))
print("Starting to process the images...")
for i in tqdm(range(count)):
    process_images(i)
results_file.close()
print("All images has been processed with success. Please review  your " + results_name + " for more information.")
