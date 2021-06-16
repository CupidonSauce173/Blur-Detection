# Python-Image-Blur-Detection

## Installation

### Getting the script from github
Install manually: 
1. Clone the repository and unpack it via winrar or any zip manager and copy the files into a directory for the script.
Install via git:
1. git clone https://github.com/CupidonSauce173/Blur-Detection.git

### Installing the dependencies
This script require few modules, tqdm, imutils and cv2. Use the package manager PIP : https://pip.pypa.io/en/stable/ to install all dependencies.
1. Install tqdm
```bash
pip install tqdm
```
2. Install imutils
```bash
pip install imutils
```
3. Install cv2
```bash
pip install opencv-python
```

## How to run
First, create an "images" folder next to the script if you wish to use default values.
Second, put all the images you want in the 'images' folder or any other folder you wish. Then, run 
```bash
python detect_blur.py --images images
```
## Usage
There are few arguments you can put to customize your experience.
```
--images <directory_path>, leave it to 'images' if you put all your images in the provided images folder, or else, use something like --images "path/to/folder".
--threshold <int value>, leave it for a default value of 100 (100%). This let you set the maximum amount of blur an image can have before being flagged as blurry.
--output_file_name <file name>, leave it for a default value of "results.txt". This let you customize the output file of the script at the end of the process.

--images => --i
--threshold => --t
--output_file_name => --o

examples of commands
python detect_blur.py --i E:\turcot_images --t 20 --o "image_result.txt"
```

## Notes
There will be a progress bar to show you how many images you process per second and also to show you where the script is.

## Little explaination of why I did this
This project helped the project Turcot with analysing which pictures were blurry from drone they used to do the cartography of the whole sector. In my system, it can process around 2.1 pictures / second (pictures of 5472x3648 pixels and of around 4.5mb - 6.5mb).




