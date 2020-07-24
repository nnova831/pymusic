import winsound as ws
import tkinter as tk
import os, threading

'''
PLAY_SOUNDS
-Nicholas Olgado

this script is a simple GUI that takes user input to play a tone.

the first entry is the tone frequency, as a sine wave.
the second entry is the tone duration, in seconds. This number can be a decimal.
'''

#TO DO: gui doesn't scale

project_dir = os.path.dirname(__file__)

def ws_thread():
    FREQ = int(e_tone.get())

    if FREQ < 37:
        print('value not in range')
        FREQ = 37
    if FREQ > 32767:
        print('value not in range')
        FREQ = 32767

    DUR = int(float(e_dur.get()) * 1000)
    x = threading.Thread(target=ws.Beep, args=(FREQ,DUR))
    x.start()

window = tk.Tk()
window.title("Tone Generator")
window.geometry("250x100")

play = tk.Button(window, text = 'Play Sound!', command = ws_thread)

tone_text = tk.Label(window, text="Tone (Freq, Hz)")
dur_text = tk.Label(window, text="Duration (seconds)")

e_tone = tk.Entry(window)
e_dur = tk.Entry(window)

tone_text.grid(column = 0, row = 0)
dur_text.grid(column = 0, row = 1)
e_tone.grid(column = 1, row = 0)
e_dur.grid(column = 1, row = 1)
play.grid(column = 0, row = 2, columnspan = 2)

window.mainloop()