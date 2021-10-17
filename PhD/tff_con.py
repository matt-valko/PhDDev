import os
from PIL import Image

yourpath = "~/Documents/Thesis_Data/"
for root, dirs, files in os.walk(yourpath, topdown=False):
    for dir in dirs:
        for name in files:
            print(os.path.join(root,dir, name))
            if os.path.splitext(os.path.join(root,dir, name))[1].lower() == ".tiff":
                if os.path.isfile(os.path.splitext(os.path.join(root,dir, name))[0] + ".jpg"):
                    print( "A jpeg file already exists for %s" % name)
                # If a jpeg is *NOT* present, create one from the tiff.
                else:
                    outfile = os.path.splitext(os.path.join(root, dir,name))[0] + ".jpg"
                    try:
                        im = Image.open(os.path.join(root, dir,name))
                        print ("Generating jpeg for %s" % name)
                        im.thumbnail(im.size)
                        im.save(outfile, "JPEG", quality=100)
                    except Exceptione:
                        print (e)