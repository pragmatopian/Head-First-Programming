from tkinter import *
import pygame.mixer

app = Tk()
app.title("Head First Mix")

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()

def change_volume(volume):
    track.set_volume(float(volume))

track = mixer.Sound(sound_file)

track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)
track_button.pack(side = LEFT)

volume = DoubleVar()
volume_scale = Scale(variable = volume,
                     from_ = 0.0,
                     to = 1.0,
                     resolution = 0.1,
                     command = change_volume,
                     label = "Volume",
                     orient = HORIZONTAL)
volume_scale.pack(side = RIGHT)

def shutdown():
    track.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
