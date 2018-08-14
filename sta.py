from PIL import Image
import os


def standard(input_dir, output_dir):
    filename_list = os.listdir(input_dir)
    for filename in filename_list:
        im = Image.open(os.path.join(input_dir, filename))
        size = im.size
        im = im.resize((4*size[0], 4*size[1]), Image.BICUBIC)
        im.save(os.path.join(output_dir, filename))

if __name__ == "__main__":
    input_dir = 'D:\\DIV2K\\DIV2K_train_LR_unknown\\X4'
    output_dir = 'G:\\DIV2K\\unknown\\X4'
    standard(input_dir, output_dir)

