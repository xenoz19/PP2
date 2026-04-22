import pygame
import os

class MusicPlayer:

    def __init__(self):

        pygame.mixer.init()

        pygame.mixer.music.set_volume(1.0)

        self.folder = "music/sample_tracks"

        self.playlist = [
            "track1.mp3",
            "track2.mp3"
        ]

        self.backgrounds = [
            "images/background1.jpg",
            "images/background2.jpg"
        ]

        self.current = 0

    def load(self):

        path = os.path.join(
            self.folder,
            self.playlist[self.current]
        )

        pygame.mixer.music.load(path)

    def play(self):

        pygame.mixer.music.play()

    def stop(self):

        pygame.mixer.music.stop()

    def next(self):

        self.current = (
            self.current + 1
        ) % len(self.playlist)

        self.load()
        self.play()

    def previous(self):

        self.current = (
            self.current - 1
        ) % len(self.playlist)

        self.load()
        self.play()

    def get_background(self):

        return self.backgrounds[self.current]