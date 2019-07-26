import telnetlib
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab

host = "192.168.1.92"
port = 55443
timeout = 100

if __name__ == '__main__':
    with telnetlib.Telnet(host, port, timeout) as session:
        session.write(b"{ \"id\": 0, \"method\": \"set_power\", \"params\":[\"on\"]}\r\n")
        while True:
            image = ImageGrab.grab()
            # plt.imshow(image)
            colors = []
            sX = round(image.width *(1/15))
            eX =round(image.width *(14/15))
            sE = round(image.height *(1/15))
            eE = round(image.height *(14/15))
            for w in range(sX, eX, 200):
                for h in range(sE, eE, 200 ):
                    # plt.scatter(w, h, s=10) #print POINT
                    colors.append(image.getpixel((w, h)))
            mean = tuple(np.nanmedian(colors, axis=0))

            r = round(mean[0])
            g = round(mean[1])
            b = round(mean[2])
            print(r, g, b)
            yeeRGB = (r * 65536) + (g * 256) + b
            session.write(b"{\"id\": 0, \"method\": \"set_rgb\", \"params\": [" + str(yeeRGB).encode() + b"]}\r\n")
            time.sleep(0.3)
            # plt.show() #print image
            # time.sleep(0.5)

import atexit

def exit_handler():
    with telnetlib.Telnet(host, port, timeout) as session:
        session.write(b"{ \"id\": 0, \"method\": \"set_power\", \"params\":[\"off\"]}\r\n")

atexit.register(exit_handler)