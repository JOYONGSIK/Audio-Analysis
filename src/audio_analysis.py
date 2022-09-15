import os
from turtle import color 
import numpy as np 

import librosa 
import librosa.display

import IPython.display as ipd
import matplotlib.pyplot as plt 


class AudioAnalysis:
    def __init__(self, audio_path: str = None):
        self.audio_path = audio_path
        
    def y_sr(self):
        y, sr = librosa.load(self.audio_path)
        return sr, len(y)/sr
        
    def play_music(self):
        y, sr = librosa.load(self.audio_path)
        return ipd.Audio(y=y, rate=sr)
    
    def music_2d_graph(self):
        y, sr = librosa.load(self.audio_path)
        
        plt.figure(figsize=(16, 6))
        librosa.display.waveshow(y=y, sr=sr)
        plt.savefig('result/2D_music_graph.jpg')
        return plt.close()
        
    def fourier_transform_graph(self):
        y, _ = librosa.load(self.audio_path)
        D = np.abs(librosa.stft(y=y, n_fft=2048, hop_length=512))
        print(D.shape)
        
        plt.figure(figsize=(16, 6))
        plt.plot(D)
        plt.savefig('result/fourier_transform_graph.jpg')
        return plt.close()
    
    def spectogram_graph(self):
        y, sr = librosa.load(self.audio_path)
        D = np.abs(librosa.stft(y=y, n_fft=2048, hop_length=512))
        DB = librosa.amplitude_to_db(D, ref=np.max)
        
        plt.figure(figsize=(16, 6))
        librosa.display.specshow(DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
        plt.colorbar()
        plt.savefig('result/spectogram_graph.jpg')
        return plt.close()
        
    def mel_spectogram_graph(self):
        y, sr = librosa.load(self.audio_path)
        S = librosa.feature.melspectrogram(y=y, sr=sr)
        S_DB = librosa.amplitude_to_db(S, ref=np.max)
        
        plt.figure(figsize=(16, 6))
        librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
        plt.colorbar()
        plt.savefig('result/mel_spectogram_graph.jpg')
        return plt.close()
        
    def audio_tempo(self):
        y, sr = librosa.load(self.audio_path)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return print(tempo)
    
    def zero_crossings(self):
        y, sr = librosa.load(self.audio_path)
        zero_crossings= librosa.zero_crossings(y=y, pad=False)
        return print(f'음 <-> 양 이동한 횟수 : {sum(zero_crossings)}')
    
    def harmonic_and_percussive_components(self):
        y, sr = librosa.load(self.audio_path)
        y_harm, y_perc = librosa.effects.hpss(y)
        
        plt.figure(figsize=(16, 6))
        plt.plot(y_harm, color='b')
        plt.plot(y_perc, color='r')
        plt.savefig('result/harmonic_and_percussive_components.jpg')
        return plt.close()