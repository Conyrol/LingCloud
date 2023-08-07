# chuck_belong maker
import os
import json
import zipfile

root_path = "/root/data/mutimodel_dataset/data_split/coco"

def list_files_in_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        file_list = zip_file.namelist()
    return file_list

zip_file_dict = {}

image_path = os.path.join(root_path, 'image')
for check_name in os.listdir(image_path):
    if '.zip' in check_name:
        zip_file_list = list_files_in_zip(os.path.join(image_path, check_name))
        for file_name in zip_file_list:
            zip_file_dict[file_name] = check_name

with open(os.path.join(root_path, 'raw_json/chunk_belong.json'), 'w') as f:
    f.write(json.dumps(zip_file_dict))