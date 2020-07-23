import winsound as ws
import tkinter as tk
import logging, time, os
import threading

file_path = os.path.abspath(__file__)
project_dir = os.path.dirname(__file__)
logging_file_path = os.path.join(project_dir, 'LOG.txt')

FREQ = 0
DUR = 0

def play_sound(freq, dur):
    logging.info("Play Sound Thread Starting...")
    ws.Beep(freq, dur)
    logging.info("Play Sound Thread Finishing...")

def ws_thread():
    logging.info("Formatting inputs...")
    FREQ = int(e_tone.get())
    DUR = int(float(e_dur.get()) * 1000)
    logging.info("Button    : before creating thread")
    x = threading.Thread(target=play_sound, args=(FREQ,DUR))
    logging.info("Button    : before running thread")
    x.start()
    logging.info("Button    : wait for the thread to finish")
    # x.join()
    logging.info("Button    : all done")

format = "%(asctime)s: %(message)s"
logging.basicConfig(filename = logging_file_path, format=format, level=logging.INFO, datefmt="%H:%M:%S")

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