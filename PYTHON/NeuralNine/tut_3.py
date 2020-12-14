

"""
Fonte:
    https://www.youtube.com/watch?v=UM6YDJ2aalU

Canal:
    NeuralNine

Título:
    YouTube Downloader in Python

Instalar:
    pip install pytube
"""

# from pytube import YouTube
# from os import chdir, getlogin
#
# chdir(f'/home/{getlogin()}')
#
# "Link compatível (gera itags)"
# # v = YouTube('https://www.youtube.com/watch?v=sVnfv3-SeuU')
# # for formats in v.streams:
# #     print(formats.itag)
#
# "Link incompatível (não gera itags)"
# # v = YouTube('https://www.youtube.com/watch?v=vtyV8DXAYIU')
# # for formats in v.streams:
# #     print(formats.itag)
#
# url = 'https://www.youtube.com/watch?v=sVnfv3-SeuU'
# target_video = YouTube(url)  # criação do objeto
#
# for formats in target_video.streams:
#     print(formats.itag)
#
# def verificar_itags():
#     """
#     for parameters in target_video.streams:
#         print(parameters)
#
#     <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
#     <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
#     <Stream: itag="299" mime_type="video/mp4" res="1080p" fps="60fps" vcodec="avc1.64002a" progressive="False" type="video">
#     <Stream: itag="303" mime_type="video/webm" res="1080p" fps="60fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
#     <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="298" mime_type="video/mp4" res="720p" fps="60fps" vcodec="avc1.4d4020" progressive="False" type="video">
#     <Stream: itag="302" mime_type="video/webm" res="720p" fps="60fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
#     <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
#     <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">
#     <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">
#     <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">
#     <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
#     <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
#     <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">
#     <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">
#     """
#
# exec_download = target_video.streams.get_by_itag(160)  # inteiro que representa as características do vídeo
# print(f'======= INFO =======\nVídeo alvo: {url}\nStatus: baixando')
#
# exec_download.download(filename=f'vid')
# print(f'======= INFO =======\nVídeo alvo: {url}\nStatus: finalizado')

from pytube import YouTube

media_list = []
text = \
        """
        ========== BEM-VINDO ==========
        1. Insira a url de um ou múltiplos vídeos (um por vez)
        2. Caso todas as urls tenham sido inseridas, digite "download", para iniciar o seu download
        3. Insira as urls clicando na seta abaixo\n
        """
print(text)
while True:
    url = input('-----> ')
    if url == 'download':
        break
    media_list.append(url)

for i, video in enumerate(media_list):
    index = 0
    itags = [22, 299, 303, 136, 247, 298, 302, 135, 244, 134, 243, 133, 242, 160, 278, 140, 249, 250, 251]
    media_object = YouTube(video)
    while index < len(itags):
        try:
            media_format = media_object.streams.get_by_itag(itags[index])
            print(f"======= INFO =======\nVídeo alvo: {i}\nSTATUS: baixando")
            media_format.download()
            print(f"======= INFO =======\nVídeo alvo: {i}\nSTATUS: concluido")
            break
        except AttributeError:
            print(f'Download falhou com itag: {itags[index]}')
            index += 1
