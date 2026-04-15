import pygame
import os

class MusicPlayer:

    def __init__(self):

        pygame.mixer.init()

        self.folder = "music/sample_tracks"

        self.playlist = [
            "track1.wav",
            "track2.wav"
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