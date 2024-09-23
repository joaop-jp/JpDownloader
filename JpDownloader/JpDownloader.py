import tkinter as tk
from pytubefix import YouTube
from pytubefix import Playlist

def dwn_audio(): #baixa o audio
    url = entrada.get()
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True,output_path="d:/PROGRAMACAO/YtDownApp/Downloads")

def dwn_video(): #baixa o video
    url = entrada.get()
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path="d:/PROGRAMACAO/YtDownApp/Downloads")

def dwn_paudio(): #baixa playlist inteira em audio
    url = "url"
    pl = Playlist(url)
    for video in pl.pvideos:
        ys = video.streams.get_audio_only()
        ys.download(mp3=True,output_path="d:/PROGRAMACAO/YtDownApp/Downloads")

def dwn_pvideo(): #baixa playlist inteira em video
    url = "url"
    pl = Playlist(url)
    for video in pl.videos:
        ys = video.streams.get_highest_resolution()
        ys.download(output_path="d:/PROGRAMACAO/YtDownApp/Downloads")

def limpar_input():
    entrada.delete(0, tk.END)  # Limpa o conteúdo do campo de entrada
    
# Criar a janela principal
janela = tk.Tk()
janela.title("JP-YT-DOWNLOADER")
janela.geometry("500x450") # Definir o tamanho da janela largura x altura
janela.configure(bg="#020500")# Troca a cor de fundo da janela

# TEXTO DO APP
texto = "FAST YT DOWNLOADER"
texto2 = "paste url here"
label_texto = tk.Label(janela,bg="#020500", fg="#E7ECE6", text=texto, font=("Fixedsys", 24), padx=10, pady=10)
label_texto.pack(pady=20)

# Criar uma caixa de entrada
entrada = tk.Entry(janela, bg="#020500", fg="#E7ECE6", width=75)
label_texto2 = tk.Label(janela, bg="#020500", fg="#E7ECE6",text=texto2, font=("Fixedsys", 14), padx=10, pady=10)
entrada.pack(pady=1)
label_texto2.pack(pady=0)

# Criar um botão e associar a função `acao_botao`
botao = tk.Button(janela, bg="#020500", fg="#E7ECE6",font="Fixedsys", text="     AUDIO    ", command=dwn_audio)
botao.pack(pady=20)

# Criar um botão e associar a função `acao_botao`
botao = tk.Button(janela, bg="#020500",fg="#E7ECE6",font="Fixedsys", text="     VIDEO    ", command=dwn_video)
botao.pack(pady=20)

# Criar um botão e associar a função `acao_botao`
botao = tk.Button(janela, bg="#020500",fg="#E7ECE6",font="Fixedsys", text="AUDIO PLAYLIST", command=dwn_paudio)
botao.pack(pady=20)

# Criar um botão e associar a função `acao_botao`
botao = tk.Button(janela, bg="#020500",fg="#E7ECE6",font="Fixedsys", text="VIDEO PLAYLIST", command=dwn_pvideo)
botao.pack(pady=20)

# Cria um botão para limpar o campo de entrada
botao_limpar = tk.Button(janela, bg="#020500",fg="#E7ECE6",font="Fixedsys", text="CLEAR", command=limpar_input)
botao_limpar.pack(pady=20)

# Iniciar o loop da interface gráfica
janela.mainloop()