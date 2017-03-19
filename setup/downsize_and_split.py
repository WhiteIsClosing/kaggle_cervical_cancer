import os, sys
# from scipy.misc import imread,imresize,imsave    # I have scipy 0.19.0
from PIL import Image

### Downsize image such that min(width, height) = 512 px * 3 color ###
def resize(img_path):
    try:
        img = Image.open(img_path)
        img.thumbnail((512,512), Image.ANTIALIAS)
        return img
    except IOError:
        print "cannot create thumbnail for '%s'" % img_path

### Decide whether the image gets saved to train or valid ###
### There is better ways to implement this, but since only run once ###
def save_train_img_to_path(img_path, img, typ):
    img_name = os.path.basename(img_path) 
    if(typ not in ["Type_1", "Type_2", "Type_3"]):
        sys.exit("Invalid typ argument")
    valid = open(typ + ".txt").read().split()
    if(img_name in valid):
        new_path = os.path.join("../data/valid", typ, img_name)
    else:
        new_path = os.path.join("../data/train", typ, img_name)
    img.save(new_path, "JPEG")

### Decide whether the additional image gets saved to train or valid ###
def save_addl_img_to_path(img_path, img, typ):
    img_name = os.path.basename(img_path) 
    if(typ not in ["Type_1", "Type_2", "Type_3"]):
        sys.exit("Invalid typ argument")
    valid = open(typ + ".additional.txt").read().split()
    if(img_name in valid):
        new_path = os.path.join("../data/additional/valid", typ, img_name)
    else:
        new_path = os.path.join("../data/additional/train", typ, img_name)
    img.save(new_path, "JPEG")

### train
def process_train():
    for typ in ["Type_1", "Type_2", "Type_3"]:
        for f in os.listdir(os.path.join("../download/train/", typ)):
            if f.endswith("jpg"):
                impath = os.path.join("../download/train/", typ, f)
                print "processing " + impath
                try:
                    img = resize(impath)
                    save_train_img_to_path(impath, img, typ)
                except IOError:
                    print "Training IO Error."

### test 
def process_test():
    for f in os.listdir(os.path.join("../download/test/")):
        if f.endswith("jpg"):
            impath = os.path.join("../download/test/", f)
            print "processing " + impath
            try:
                img = resize(impath)
                img.save(os.path.join("../data/test/unknown/", os.path.basename(impath)), "JPEG")
            except IOError:
                print "Testing IO Error."

### additional 
def process_additional():
    for typ in ["Type_1", "Type_2", "Type_3"]:
        for f in os.listdir(os.path.join("../download/additional/", typ)):
            if f.endswith("jpg"):
                impath = os.path.join("../download/additional/", typ, f)
                print "processing " + impath
                try:
                    img = resize(impath)
                    try:
                        save_addl_img_to_path(impath, img, typ)
                    except:
                        pass
                except IOError:
                    print "Additional IO Error."

### main ###
if __name__ == "__main__":
    ### loop through image and process
    # process_train()
    # process_test()
    process_additional()
