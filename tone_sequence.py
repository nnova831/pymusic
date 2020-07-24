import winsound as ws
import tkinter as tk
import numpy as np
import os, threading, time

'''
TONE_SEQUENCE
-Nicholas Olgado

this script is a simple GUI that takes user input to play a sequence of tones.
'''

project_dir = os.path.dirname(__file__)

sequence = [50, 100, 200, 400, 800]

time_ms = 1000
time_s = time_ms / 1000

for i in range(len(sequence)):
    print("{}".format(sequence[i]) + " Hz")
    x = threading.Thread(target=ws.Beep, args=(sequence[i],time_ms))
    x.start()
    time.sleep(time_s)
