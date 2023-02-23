from PIL import Image
import numpy as np
import os
import json

"""
      Apply a 2-value mask to the image
"""

jsonPath = 'xxx.json'
imgRoot = ' '

if __name__ == "__main__":
    with open(jsonPath) as jsonFile:            
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    for instance_json in jsonObject:
        mask_path = instance_json['mask']
        mask_path = os.path.join(imgRoot, mask_path)
        img_path = instance_json['img']
        img_path = os.path.join(imgRoot, img_path)

        path_split = img_path.split('/')
        file_index = len(path_split) - 1
        path_split[7] = 'masked'
        sep = '/'
        save_path = sep.join(path_split)
        del path_split[file_index]
        save_father_path = sep.join(path_split)
        if not os.path.exists(save_father_path):
                os.makedirs(save_father_path) 
        else:
            pass
        print(save_path)

        img=Image.open(img_path).convert('RGB')
        img_mat = np.array(img)

        mask=Image.open(mask_path)
        mask_mat = np.array(mask)
        mask_mat = np.expand_dims(mask_mat, 2)

        if img_mat.shape[0] != mask_mat.shape[0]:
            continue

        binary_mask = mask_mat != 0
        masked_img = binary_mask * img_mat
        if img_mat.shape[2] == 2:
            new = Image.fromarray(masked_img, mode='I')
        else:
            new = Image.fromarray(masked_img, mode='RGB')
        new.save(save_path)

            





