from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image
import base64
import paho.mqtt.client as mqtt


def view():
    s = BytesIO()
    c.capture(s,'png')
    image = Image.open(s)
    return image
    
def calc_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    b = scale = len(histogram)
    for index in range(0,scale):
        ratio = histogram[index]/pixels
        b += ratio * (-scale + index)
    return 1 if b == 255 else b/scale

if __name__ == '__main__':
    c = PiCamera()
    c.resolution = (640,320)
    c.exposure_mode = 'off'
    c.start_preview()
    client = mqtt.Client()
    client.connect("masterpi.local")
    p = view()
    
    # publish brightness
    brightness = calc_brightness(p)
    #brightness = round(brightness,4)
    print(brightness)
    client.publish("garage/brightness",brightness)
    
    # publish 