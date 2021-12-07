import os
import cv2

def write_info(website, text, images = []):
    full_path = os.path.join('outputs', website)

    if not os.path.isdir(full_path):
        os.mkdir(full_path)

    file_name = f"{website}.txt"

    f = open(os.path.join(full_path, file_name), 'wb')

    f.write(text)

    if images != []:
        for idx,img in enumerate(images):

            img_name = f'{website}_{idx}.png'
            img_path_folder = os.path.join(full_path, 'img')

            if not os.path.isdir(img_path_folder):
                os.mkdir(img_path_folder)

            img_path = os.path.join(img_path_folder,website)

            if not os.path.isdir(img_path):
                os.mkdir(img_path)
            
            img_path_file = os.path.join(img_path, img_name)
            
            cv2.imwrite(img_path_file, img)


