import os
import pygame
import tkinter as tk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.music_folder_path = 'sound'
        self.buttons = {}
        self.current_audio = None
        self.song_order = [
            "Beautiful - Heathers.wav",
            "Candy Store - Heathers.wav",
            "Fight for Me - Heathers.wav",
            "call.wav",
            "Big Fun - Heathers.wav",
            "Me Inside of Me - Heathers.wav",
            "Our Love Is God - Heathers.wav",
            "Seventeen - Heathers.wav",
            "Shine A Light - Heathers.wav",
            "Lifeboat - Heathers.wav",
            "Shine A Light (Reprise) - Heathers.wav",
            "Kindergarten Boyfriend - Heathers.wav",
            "Yo Girl - Heathers.wav",
            "Meant to Be Yours - Heathers.wav",
            "Dead Girl Walking (Reprise) - Heathers.wav",
            "I Am Damaged - Heathers.wav",
            "Seventeen (Reprise) - Heathers.wav",
            "Heathers Musical Curtain Call.wav"
        ]

        self.init_gui()
        self.load_music_files()

    def init_gui(self):
        self.root.title("Heathers Soundboard")
        self.root.configure(bg='#252525')
        self.root.geometry("800x500")

        self.main_frame = tk.Frame(self.root, bg='#252525')
        self.main_frame.pack(fill='both', expand=True)

        self.button_frame = tk.Frame(self.main_frame, bg='#252525')
        self.button_frame.pack(side=tk.LEFT, fill='y')

        self.scrollbar = tk.Scrollbar(self.button_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.button_frame, bg='#252525', yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = tk.Frame(self.canvas, bg='#252525')
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.control_frame = tk.Frame(self.main_frame, bg='#252525')
        self.control_frame.pack(side=tk.RIGHT, fill='both', expand=True)

        self.create_control_menu()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def load_music_files(self):
        audio_files = [f for f in os.listdir(self.music_folder_path) if f.endswith('.wav')]
        sorted_files = sorted(audio_files, key=lambda x: self.song_order.index(x))

        for file in sorted_files:
            self.buttons[file] = os.path.join(self.music_folder_path, file)
            button = tk.Button(self.scrollable_frame, text=file, command=lambda path=self.buttons[file]: self.play_audio(path), bg='#1f1f1f', fg='white', font=('Arial', 10))
            button.pack(pady=2, fill='x')

    def create_control_menu(self):
        self.play_pause_button = tk.Button(self.control_frame, text="▶", command=self.toggle_play_pause, bg='#1f1f1f', fg='white', font=('Arial', 20))
        self.play_pause_button.pack(pady=10)

        self.replay_button = tk.Button(self.control_frame, text="↺", command=self.replay_audio, bg='#1f1f1f', fg='white', font=('Arial', 20))
        self.replay_button.pack(pady=10)

        self.current_song_label = tk.Label(self.control_frame, text="", bg='#252525', fg='white', font=('Arial', 12))
        self.current_song_label.pack(pady=20)

    def play_audio(self, path):
        if self.current_audio and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        self.play_pause_button.config(text="⏸")

        self.current_audio = path
        self.current_song_label.config(text=os.path.basename(path))

    def toggle_play_pause(self):
        if pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() > 0:
                if pygame.mixer.music.get_pos() == pygame.mixer.Sound(self.current_audio).get_length():
                    self.replay_audio()
                else:
                    pygame.mixer.music.pause()
                    self.play_pause_button.config(text="▶")
            else:
                pygame.mixer.music.unpause()
                self.play_pause_button.config(text="⏸")
        else:
            self.play_audio(self.current_audio)

    def replay_audio(self):
        if self.current_audio and pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.current_audio)
            pygame.mixer.music.play()
            self.play_pause_button.config(text="⏸")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    music_player.run()
