def identity(img = None, extras = {}):
    return img

def grey_scale(img = None, extras = {}):
    print '1grey_scale'
    if img.any():
        print '2haygrey_scale'
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                grey = (int(img[i,j][0]) + int(img[i,j][1]) + int(img[i,j][2])) / 3
                img[i,j] = [grey,grey,grey]
        return img
    print '3nohaygrey_scale'
    return None

def brightness(img = None, extras = {}):#, brightness = 127):
    print '1brightness'
    if img.any():
        print '2haybrightness'
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
    print '3nohaybrightness'
    return None

def one_channel(img = None, extras = {}):#, channel = 'R'):
    print '1one_channel'
    if img.any():
        print '2hayone_channel'
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
    print '3nohayone_channel'
    return None

def high_contrast(img = None, extras = {}):
    print '1high_contrast'
    if img.any():
        print '2hayhigh_contrast'
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                b = 0 if int(img[i,j][0]) <= 127 else 255
                g = 0 if int(img[i,j][1]) <= 127 else 255
                r = 0 if int(img[i,j][2]) <= 127 else 255
                img[i,j] = [b,g,r]
        return img
    print '3nohayhigh_contrast'
    return None
