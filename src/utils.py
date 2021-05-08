import png

def GetPNGData(imagefile):
    png_image = png.Reader(filename=imagefile)

    image_data = png_image.read()
    image_properties = image_data[3]

    # grab the image pixel data from index 2
    # the full image in row0: [R,G,B,R...], row1: [R,G,B,R,...] format
    return list(image_data[2]), image_properties