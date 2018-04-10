import utils
from PIL import Image

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

def mosaico(original_img=None, extras={'size':25}):
    p_size = extras.get('size')
    img = original_img.copy()
    img = utils.toImage(img)
    img = img.resize( (int(img.size[0]/p_size), int(img.size[1]/p_size)), Image.NEAREST)
    img = img.resize((img.size[0]*p_size, img.size[1]*p_size), Image.NEAREST)
    img = utils.toCV2(img)
    return img

def rgb_component(original_img=None, extras={}):
    extras.update(utils.rgb_component_aux())
    r = extras.get('r')
    g = extras.get('g')
    b = extras.get('b')
    img = original_img.copy()
    if img.any():
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                img[i,j] = [b,g,r]
        return img
    return None

def quitar_marca_de_agua(original_img=None, extras={}):
    img = original_img.copy()
    if img.any():
        high_contrast_image = high_contrast(img, extras)
        grey_scale_image = grey_scale(img, extras)
        height, width, channels = img.shape
        for i in range(0, height):
            for j in range(0,width):
                b = int(img[i,j][0])
                g = int(img[i,j][1])
                r = int(img[i,j][2])
                if r > g + 10 and r > b + 10:
                    pix_grey = grey_scale_image[i,j]
                    pix_hc = high_contrast_image[i,j]
                    if (pix_grey[0] < pix_hc[0] and
                       pix_grey[1] < pix_hc[1] and
                       pix_grey[2] < pix_hc[2]):
                        img[i,j] = pix_hc
                    else:
                        img[i,j] = pix_grey
        return img
    return None

def m_a_color(original_img=None, extras={}):
    img = original_img.copy()
    mos_img = mosaico(img)
    html = utils.write_html(mos_img)
    print html
    # exit(0)
    return mos_img

def att(original_img=None, extras={'morsa':True}):
    img = original_img.copy()
    if img.any():
        img = high_contrast(img, extras) #Pasamos a blanco y negro
        height, width, channels = img.shape
        for i in range(0, width):
            for j in range(0, height, 9): #Recorremos de 9 pixeles en 9 pixeles a lo largo
                p1, p2, p3 = img[i,j], img[i,j + 1], img[i,j + 2]
                p4, p5, p6 = img[i,j + 3], img[i,j + 4], img[i,j + 5]
                p7, p8, p9 = img[i,j + 6], img[i,j + 7], img[i,j + 8]

                print p1,p2,p3,p4,p5,p6,p7,p8,p9
                exit()
