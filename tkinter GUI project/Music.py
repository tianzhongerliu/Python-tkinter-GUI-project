import os
import threading
import time
import tkinter.messagebox
from tkinter import filedialog
import tkinter as tk
from mutagen.mp3 import MP3
from pygame import mixer


playPhoto = None
stopPhoto = None
pausePhoto = None
rewindPhoto = None
mutePhoto = None
volumePhoto = None

muted = False
playlist = []
paused = False

def music_run(window):
    root = tk.Toplevel(window)

    # Create the menubar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Create the submenu

    subMenu = tk.Menu(menubar, tearoff=0)

    # playlist - contains the full path + filename
    # playlistbox - contains just the filename
    # Fullpath + filename is required to play the music inside play_music load function

    def browse_file():
        global filename_path
        filename_path = filedialog.askopenfilename()
        add_to_playlist(filename_path)

        mixer.music.queue(filename_path)


    def add_to_playlist(filename):
        filename = os.path.basename(filename)
        index = 0
        playlistbox.insert(index, filename)
        playlist.insert(index, filename_path)
        index += 1


    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open", command=browse_file)
    subMenu.add_command(label="Exit", command=root.destroy)


    def about_us():
        tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python Tkinter by @attreyabhatt')


    subMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us", command=about_us)

    mixer.init()  # initializing the mixer

    root.title("Melody")
    root.iconbitmap(r'images/melody.ico')

    # Root Window - StatusBar, LeftFrame, RightFrame
    # LeftFrame - The listbox (playlist)
    # RightFrame - TopFrame,MiddleFrame and the BottomFrame

    leftframe = tk.Frame(root)
    leftframe.pack(side='left', padx=30, pady=30)

    playlistbox = tk.Listbox(leftframe)
    playlistbox.pack()

    addBtn = tk.Button(leftframe, text="+ Add", command=browse_file)
    addBtn.pack(side='left')


    def del_song():
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        playlistbox.delete(selected_song)
        playlist.pop(selected_song)


    delBtn = tk.Button(leftframe, text="- Del", command=del_song)
    delBtn.pack(side='left')

    rightframe = tk.Frame(root)
    rightframe.pack(pady=30)

    topframe = tk.Frame(rightframe)
    topframe.pack()

    lengthlabel = tk.Label(topframe, text='Total Length : --:--')
    lengthlabel.pack(pady=5)

    currenttimelabel = tk.Label(topframe, text='Current Time : --:--', relief='groove')
    currenttimelabel.pack()


    def show_details(play_song):
        file_data = os.path.splitext(play_song)

        if file_data[1] == '.mp3':
            audio = MP3(play_song)
            total_length = audio.info.length
        else:
            a = mixer.Sound(play_song)
            total_length = a.get_length()

        # div - total_length/60, mod - total_length % 60
        mins, secs = divmod(total_length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        lengthlabel['text'] = "Total Length" + ' - ' + timeformat

        t1 = threading.Thread(target=start_count, args=(total_length,))
        t1.start()


    def start_count(t):
        global paused
        # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
        # Continue - Ignores all of the statements below it. We check if music is paused or not.
        current_time = 0
        while current_time <= t and mixer.music.get_busy():
            if paused:
                continue
            else:
                mins, secs = divmod(current_time, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
                time.sleep(1)
                current_time += 1


    def play_music():
        global paused

        if paused:
            mixer.music.unpause()
            paused = False
        else:
            try:
                stop_music()
                time.sleep(1)
                selected_song = playlistbox.curselection()
                selected_song = int(selected_song[0])
                play_it = playlist[selected_song]
                mixer.music.load(play_it)
                mixer.music.play()
                show_details(play_it)
            except:
                tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')


    def stop_music():
        mixer.music.stop()


    def pause_music():
        global paused
        paused = True
        mixer.music.pause()


    def rewind_music():
        play_music()


    def set_vol(val):
        volume = float(val) / 100
        mixer.music.set_volume(volume)
        # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,

    def mute_music():
        global muted
        if muted:  # Unmute the music
            mixer.music.set_volume(0.7)
            volumeBtn.configure(image=volumePhoto)
            scale.set(70)
            muted = False
        else:  # mute the music
            mixer.music.set_volume(0)
            volumeBtn.configure(image=mutePhoto)
            scale.set(0)
            muted = True


    middleframe = tk.Frame(rightframe)
    middleframe.pack(pady=30, padx=30)

    global playPhoto
    playPhoto = tk.PhotoImage(file='images/play.gif')
    playBtn = tk.Button(middleframe, image=playPhoto, command=play_music)
    playBtn.grid(row=0, column=0, padx=10)

    global stopPhoto
    stopPhoto = tk.PhotoImage(file='images/stop.gif')
    stopBtn = tk.Button(middleframe, image=stopPhoto, command=stop_music)
    stopBtn.grid(row=0, column=1, padx=10)

    global pausePhoto
    pausePhoto = tk.PhotoImage(file='images/pause.gif')
    pauseBtn = tk.Button(middleframe, image=pausePhoto, command=pause_music)
    pauseBtn.grid(row=0, column=2, padx=10)

    # Bottom Frame for volume, rewind, mute etc.

    bottomframe = tk.Frame(rightframe)
    bottomframe.pack()

    global rewindPhoto
    rewindPhoto = tk.PhotoImage(file='images/rewind.gif')
    rewindBtn = tk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
    rewindBtn.grid(row=0, column=0)

    global mutePhoto
    global volumePhoto
    mutePhoto = tk.PhotoImage(file='images/mute.gif')
    volumePhoto = tk.PhotoImage(file='images/volume.gif')
    volumeBtn = tk.Button(bottomframe, image=volumePhoto, command=mute_music)
    volumeBtn.grid(row=0, column=1)

    scale = tk.Scale(bottomframe, from_=0, to=100, orient='horizontal', command=set_vol)
    scale.set(70)  # implement the default value of scale when music player starts
    mixer.music.set_volume(0.7)
    scale.grid(row=0, column=2, pady=15, padx=30)


    def on_closing():
        stop_music()
        root.destroy()


    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

