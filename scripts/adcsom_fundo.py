from moviepy.editor import *

# Pegando o Caminho para o vídeo e áudio
video_path = "videos_prontos/videocortado.mp4"
audio_path = "sons_de_fundo/ifloseitall.mp3"
output_path = "videos_prontos/video_com_audio.mp4"

# Carregando o vídeo e o áudio
video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)

# Adicionando o áudio ao vídeo
video = video.set_audio(audio)

# Salvando o vídeo com o áudio adicionado
video.write_videofile(output_path, codec='libx264', audio_codec='aac')