#import skimage.io as io
import os
from PIL import Image

def com(batches_path, patch_w, patch_h, step_w, step_h, output_path):
    items = os.listdir(batches_path)
    num = len(items)                    #图片个数
    last = items[num-1]
    last_name = last.split('.')[0]         #切分出图片的名字
    num_h = int(last_name.split('_')[0])
    num_w = int(last_name.split('_')[1])
    img_w = (num_w + 1) * step_w + patch_w
    img_h = (num_h + 1) * step_h + patch_h
    #print(img_w, img_h)
    image_new = Image.new('RGB', (img_w, img_h), (0,0,0))
    print(image_new.size)
    k = 0
    for i in range(num_h+1):
        for j in range(num_w+1):
            print(k)
            img_path = os.path.join(batches_path, items[k])
            img = Image.open(img_path)
            box = (j*step_w, i*step_h, j*step_w+patch_w, i*step_h + patch_h)
            print(box)
            image_new.paste(img, box)
            k = k+1
    image_new.save(output_path)
    image_new.show()
    print('img size', image_new.size)

def com_files(input_path, patch_w, patch_h, step_w, step_h, output_path):
    items = os.listdir(input_path)
    for filename in items:
        batches_path = os.path.join(input_path, filename)
        output_path_new = os.path.join(output_path, (filename+'.png'))
        com(batches_path, patch_w, patch_h, step_w, step_h, output_path_new)


if __name__ == "__main__":
    batches_path = 'D:\\pyProjects\\seg\\batches'
    output_path = 'D:\\pyProjects\\seg\\new_picture'
    com_files(batches_path, 500, 500, 200, 200, output_path)