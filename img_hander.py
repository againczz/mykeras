import os
import shutil
from PIL import Image
width_step = 64
height_step = 48
img_path = "originIMG"
out_path = "D:\\work\\tfwork\\splitIMG2"
for root,dir,file in os.walk(img_path):
    for image_file in file:
        print(image_file)
        # dir_name = os.path.splitext(image_file)[0]
        # shutil.copyfile(os.path.join(img_path,image_file),os.path.join(out_path,dir_name))
        image_width, image_height = 640, 480
        width_start, height_start = 0, 0
        dir_name = os.path.splitext(image_file)[0]
        tmp_dir = os.path.join(out_path,dir_name)
        os.mkdir(tmp_dir)
        im_path = os.path.join(img_path,image_file)
        im = Image.open(im_path)
        im.save('%s/%s.jpg'% (tmp_dir,dir_name))
        count = 0
        while height_start < image_height:
            while width_start < image_width:
                count += 1
                cropedIm = im.crop((width_start,height_start,width_start+width_step,height_start+height_step))
                cropedIm.save('%s/%s%s.jpg'% (tmp_dir,dir_name,str(count)))
                width_start += width_step
            height_start += height_step
            width_start = 0
