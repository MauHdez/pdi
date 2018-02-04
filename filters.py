def grey_scale(img = None):
    if img.any():
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                grey = (int(img[i,j][0]) + int(img[i,j][1]) + int(img[i,j][2])) / 3
                img[i,j] = [grey,grey,grey]
        return img
    return None

def brightness(img = None, brightness = 127):
    if img.any():
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

def one_channel(img = None, channel):
    if img.any():
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

def high_contrast(img = None):
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
