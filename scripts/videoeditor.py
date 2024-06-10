from moviepy.editor import VideoFileClip

#pegando o caminho do video
clip = VideoFileClip("videos/videonature.mp4")

#pegando a duração total do video
duracao_total = clip.duration 

#cortando 18 segundo do video
clip_cortado = clip.subclip(18 - duracao_total, duracao_total)

#salvando o video na pasta videos prontos
clip_cortado.write_videofile("videos_prontos/videocortado.mp4")
