from PIL import Image
import os
import time

start = time.clock()
def seg_picture(image, patch_w, patch_h, step_w, step_h, output_path):
    '''
    :param image: input image
    :param patch_w: patch_width
    :param patch_h: patch_height
    :param step_w: step_width
    :param step_h: step_height
    :param output_path: The directory of the patches storage
    '''
    size = image.size
    image_w = size[0]
    image_h = size[1]

    #print('old image\'s size is ', image_w, image_h)
    #块的个数
    num_w = (image_w - patch_w)//step_w + 1
    num_h = (image_h - patch_h)//step_h + 1

    # #补全
    # if (image_w - patch_w) % step_w != 0:
    #     num_w = num_w+1
    #     image_new = Image.new('RGB',(patch_w+num_w*step_w, image_h), (0, 0, 0))
    #     image_new.paste(image,(0, 0))
    #     image = image_new
    #     size = image.size
    #     image_w = size[0]
    #     image_h = size[1]
    #
    # if (image_h - patch_h) % step_h != 0:
    #     num_h = num_h + 1
    #     image_new = Image.new('RGB', (image_w, patch_h + num_h*step_h), (0, 0, 0))
    #     image_new.paste(image, (0, 0))              #拼接
    #     image = image_new
    # #image.show()

    #print("num_w: ", num_w)
    #print('num_h: ', num_h)
    #print('new image\'s size is ', image.size)

    #分块
    for i in range(num_h):
        for j in range(num_w):
            box = (j*step_w, i*step_h, j*step_h+patch_w, i*step_w+patch_h)   #tuple:(left, upper, right, lower)
            region = image.crop(box)
            region.save(os.path.join(output_path, (str(i)+'_'+str(j)+'.png')))

 #整个文件夹内图片的切分
def seg_file(input_path, patch_w, patch_h, step_w, step_h,output_path):
    filename_list = os.listdir(input_path)
    for filename in filename_list:
        image = Image.open(os.path.join(input_path, filename))
        name = filename.split('.')
        picture_name = name[0]
        output_path_new = os.path.join(output_path, picture_name)
        if not os.path.exists(output_path_new):
            os.mkdir(output_path_new)
       	    print(picture_name)
            seg_picture(image, patch_w, patch_h, step_w, step_h, output_path_new)


if __name__ == "__main__":
    input_path = 'G:\\DIV2K\\unknown\\X2'
    output_path = 'G:\\DIV2K\\64_48\\unknown_X2'
    seg_file(input_path, 64, 64, 48, 48, output_path)
    end = time.clock()
    print('Time: ', end-start) 
