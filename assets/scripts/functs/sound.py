import os
import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()  # Inicializa o mixer do pygame
        self.next_audio = ""

    def add_to_playlist(self, audio_file):
        # Verifica se o arquivo de áudio existe
        audio_path = f"assets/sound/{audio_file}.mp3"
        if not os.path.exists(audio_path):
            print(f"Arquivo {audio_path} não encontrado.")
            return

        # Se não houver música tocando, inicia a próxima música da lista
        if not pygame.mixer.music.get_busy(): self.next_audio = audio_path
        else: self.next_audio = audio_path

        self.play_next(audio_path)
   
    def play_next(self, audio_path):
        # Verifica se há mais músicas na playlist para tocar
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
