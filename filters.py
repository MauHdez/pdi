def identity(original_img=None, extras={}):
    img = original_img.copy()
    return img

def grey_scale(original_img=None, extras={}):
    img = original_img.copy()
    if img.any():
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                grey = (int(img[i,j][0]) + int(img[i,j][1]) + int(img[i,j][2])) / 3
                img[i,j] = [grey,grey,grey]
        return img
    return None

def brightness(original_img=None, extras={}):#, brightness = 127):
    img = original_img.copy()
    if img.any():
        brightness = extras.get("brightness")
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):

                b = int(img[i,j][0])
                new_b = b + brightness
                if new_b > 255:
                    new_b = 255
                elif new_b < 0:
                    new_b = 0

                g = int(img[i,j][1])
                new_g = g + brightness
                if new_g > 255:
                    new_g = 255
                elif new_g < 0:
                    new_g = 0

                r = int(img[i,j][2])
                new_r = r + brightness
                if new_r > 255:
                    new_r = 255
                elif new_r < 0:
                    new_r = 0

                img[i,j] = [new_b,new_g,new_r]
        return img
    return None

def one_channel(original_img=None, extras={}):#, channel = 'R'):
    img = original_img.copy()
    if img.any():
        channel = extras.get('channel')
        if channel not in ["R","G","B"]:
            return None
        height, width, channels = img.shape
        if channel == "R":
            for i in range(0, height):
                for j in range(0,width):
                    img[i,j] = [0,0,img[i,j][2]]
            return img
        elif channel == "G":
            for i in range(0, height):
                for j in range(0,width):
                    img[i,j] = [0,img[i,j][1],0]
            return img
        elif channel == "B":
            for i in range(0, height):
                for j in range(0,width):
                    img[i,j] = [img[i,j][0],0,0]
            return img
    return None

def high_contrast(original_img=None, extras={}):
    img = original_img.copy()
    if extras.get('morsa'):
        img = grey_scale(original_img=img, extras=extras)
    if img.any():
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                b = 0 if int(img[i,j][0]) <= 127 else 255
                g = 0 if int(img[i,j][1]) <= 127 else 255
                r = 0 if int(img[i,j][2]) <= 127 else 255
                img[i,j] = [b,g,r]
        return img
    return None

def inverse(original_img=None, extras={}):
    img = original_img.copy()
    if img.any():
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                b = int(img[i,j][0])
                new_b = 255 - b
                if new_b > 255:
                    new_b = 255
                elif new_b < 0:
                    new_b = 0

                g = int(img[i,j][1])
                new_g = 255 - g
                if new_g > 255:
                    new_g = 255
                elif new_g < 0:
                    new_g = 0

                r = int(img[i,j][2])
                new_r = 255 - r
                if new_r > 255:
                    new_r = 255
                elif new_r < 0:
                    new_r = 0

                img[i,j] = [new_b,new_g,new_r]
        return img
    return None
# 
# def mosaico(original_img=None, extras={}):
#     img = original_img.copy()
#     if img.any():
#         height, width, channels = img.shape
#         for i in range(0, height):
#             for j in range(0,width):
#                 if i < height-3 and j < width-3:
#
#         return img
#     return None
