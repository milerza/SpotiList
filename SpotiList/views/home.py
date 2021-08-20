import tkinter as tk
from models.models import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.primeiroContainer = tk.Frame(self.master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = tk.Frame(self.master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = tk.Frame(self.master,width=1000, height=600, highlightbackground="gray", highlightthickness=1)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.fontePadrao = ("Arial", "10")
        self.titulo = tk.Label(self.primeiroContainer, text="SpotiList")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()

        self.cadastro_album = tk.Button(self.segundoContainer,width=20)
        self.cadastro_album["text"] = "Cadastrar Álbum"
        self.cadastro_album["command"] = self.go_to_cadastrar_album
        self.cadastro_album.pack(side="left")

        self.pesquisa_album = tk.Button(self.segundoContainer,width=20)
        self.pesquisa_album["text"] = "Pesquisar Álbum"
        self.pesquisa_album["command"] = self.go_to_pesquisar_album
        self.pesquisa_album.pack(side="left")

        self.pesquisa_musica = tk.Button(self.segundoContainer,width=20)
        self.pesquisa_musica["text"] = "Pesquisar Música"
        self.pesquisa_musica["command"] = self.go_to_pesquisar_musica
        self.pesquisa_musica.pack(side="left")

        self.gerar_playlist= tk.Button(self.segundoContainer,width=20)
        self.gerar_playlist["text"] = "Gerar Playlist"
        self.gerar_playlist["command"] = self.go_to_playlist
        self.gerar_playlist.pack(side="left")

        self.quit = tk.Button(self.segundoContainer,width=20, text="Sair", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    #funcao para criar a Tela de cadastro do Album
    def go_to_cadastrar_album(self):
        print("Vá para cadastrar album")
        #limpando a tela do app
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()



        #recriando a tela
        self.terceiroContainer = tk.Frame(self.master, width=1000, height=600)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.albumlabel = tk.Label(self.terceiroContainer,width=80, text="Cadastrar Álbum \n")
        self.albumlabel["font"] = ("Arial", "15", "bold")
        self.albumlabel.pack(side="top")

        #campo titulo
        self.tituloLabel = tk.Label(self.terceiroContainer, text="    Título", font=self.fontePadrao)
        self.tituloLabel.pack(side="left")

        self.titulo_album = tk.Entry(self.terceiroContainer)
        self.titulo_album["width"] = 30
        self.titulo_album["font"] = self.fontePadrao
        self.titulo_album.pack(side="left")

        # campo ano de lancamento
        self.anoLabel = tk.Label(self.terceiroContainer, text="     Ano de Lançamento", font=self.fontePadrao)
        self.anoLabel.pack(side="left")

        self.ano_lancamento = tk.Entry(self.terceiroContainer)
        self.ano_lancamento["width"] = 20
        self.ano_lancamento["font"] = self.fontePadrao
        self.ano_lancamento.pack(side="left")

        #campo banda
        self.bandaLabel = tk.Label(self.terceiroContainer, text="     Banda/Artista", font=self.fontePadrao)
        self.bandaLabel.pack(side="left")

        self.banda = tk.Entry(self.terceiroContainer)
        self.banda["width"] = 30
        self.banda["font"] = self.fontePadrao
        self.banda.pack(side="left")

        #botao cadastrar album
        self.cd_album = tk.Button(self.quartoContainer, width=20)
        self.cd_album["text"] = "Cadastrar"
        self.cd_album["command"] = self.cadastrarAlbum
        self.cd_album.pack(side="bottom")

    def go_to_pesquisar_album(self):
        print("vá para pesquisar album")
        #limpando janela do app
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()

        #recriando console
        self.terceiroContainer = tk.Frame(self.master, width=1000, height=600)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        #titulo da tela
        self.pes_albumlabel = tk.Label(self.terceiroContainer, width=80, text="Pesquisar Álbum")
        self.pes_albumlabel["font"] = ("Arial", "15", "bold")
        self.pes_albumlabel.pack()

        #campo de pesquisa

        # campo pesquisar
        self.pesquisarAlbumLabel = tk.Label(self.terceiroContainer, text="Informe título, ano de lançamento \n ou banda do álbum", font=self.fontePadrao)
        self.pesquisarAlbumLabel.pack(side="left")

        self.campoPesquisaAlbum = tk.Entry(self.terceiroContainer)
        self.campoPesquisaAlbum["width"] = 30
        self.campoPesquisaAlbum["font"] = self.fontePadrao
        self.campoPesquisaAlbum.pack(side="left")

        #botao cadastrar album
        #chama a funcao que conecta com o bd
        self.bt_pesquisarAlbum = tk.Button(self.terceiroContainer, width=20)
        self.bt_pesquisarAlbum["text"] = "Pesquisar"
        self.bt_pesquisarAlbum["command"] = self.pesquisarAlbum
        self.bt_pesquisarAlbum.pack(side="bottom")

    def go_to_pesquisar_musica(self):
        print("vá para pesquisar músicas")
        #limpando a tela
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()

        #recriando containers
        self.terceiroContainer = tk.Frame(self.master, width=1000, height=600)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.pes_musicalabel = tk.Label(self.terceiroContainer, width=80, text="Pesquisar Música")
        self.pes_musicalabel["font"] = ("Arial", "15", "bold")
        self.pes_musicalabel.pack()

        # campo de pesquisa

        # campo pesquisar
        self.pesquisarMusicaLabel = tk.Label(self.terceiroContainer,
                                            text="Informe título da música\n ou banda ",
                                            font=self.fontePadrao)
        self.pesquisarMusicaLabel.pack(side="left")

        self.campoPesquisaMusica = tk.Entry(self.terceiroContainer)
        self.campoPesquisaMusica["width"] = 30
        self.campoPesquisaMusica["font"] = self.fontePadrao
        self.campoPesquisaMusica.pack(side="left")

        # botao cadastrar musica
        # chama a funcao que conecta com o bd
        self.bt_pesquisarmusica = tk.Button(self.terceiroContainer, width=20)
        self.bt_pesquisarmusica["text"] = "Pesquisar"
        self.bt_pesquisarmusica["command"] = self.pesquisarMusica
        self.bt_pesquisarmusica.pack(side="bottom")

    def go_to_playlist(self):
        print("vá para playlist!")
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()

        self.terceiroContainer = tk.Frame(self.master, width=1000, height=600)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.label_gerar_playlist = tk.Label(self.terceiroContainer, width=80, text="Gerar Playlist")
        self.label_gerar_playlist["font"] = ("Arial", "15", "bold")
        self.label_gerar_playlist.pack()

        # botao cadastrar musica
        # chama a funcao que conecta com o bd

        self.bt_gerarplaylis = tk.Button(self.terceiroContainer, width=20)
        self.bt_gerarplaylis["text"] = "Clique aqui para \n gerar Playlist"
        self.bt_gerarplaylis["command"] = self.gerarPlaylist
        self.bt_gerarplaylis.pack()

    def telaMusica(self):
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()

        self.terceiroContainer = tk.Frame(self.master, width=1000, height=600)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.label_cdMusicas = tk.Label(self.terceiroContainer, width=80, text="Músicas do álbum: " + self.album_titulo)
        self.label_cdMusicas["font"] = ("Arial", "15", "bold")
        self.label_cdMusicas.pack()

        # campos de cadastro de música
        # titulo
        self.labeltitulo_musica = tk.Label(self.terceiroContainer,
                                           text="Título",
                                           font=self.fontePadrao)
        self.labeltitulo_musica.pack(side="left")

        self.titulo_musica = tk.Entry(self.terceiroContainer)
        self.titulo_musica["width"] = 30
        self.titulo_musica["font"] = self.fontePadrao
        self.titulo_musica.pack(side="left")

        # duracao
        self.duracaoLabel = tk.Label(self.terceiroContainer,
                                     text="Duração(em segundos)",
                                     font=self.fontePadrao)
        self.duracaoLabel.pack(side="left")

        self.duracao = tk.Entry(self.terceiroContainer)
        self.duracao["width"] = 30
        self.duracao["font"] = self.fontePadrao
        self.duracao.pack(side="left")

        # favoritar
        self.favoritoLabel = tk.Label(self.terceiroContainer,
                                      text="Favorita?(S/N)",
                                      font=self.fontePadrao)
        self.favoritoLabel.pack(side="left")

        self.fav = tk.Entry(self.terceiroContainer)
        self.fav["width"] = 10
        self.fav["font"] = self.fontePadrao
        self.fav.pack(side="left")

        #notificacao sucesso
        self.sucesso = tk.Label(self.terceiroContainer, text="Album "+ self.album_titulo + " cadastrado com sucesso")
        self.sucesso["pady"] = 20
        self.sucesso.pack()

        # botao cadastrar musica
        # chama a funcao que conecta com o bd

        self.cd_musica = tk.Button(self.quartoContainer, width=20, fg="green")
        self.cd_musica["text"] = "Adicionar música ao álbum"
        self.cd_musica["command"] = self.cadastrarMusica
        self.cd_musica.pack(side="left")

        self.voltar = tk.Button(self.quartoContainer, width=20, text="Voltar para o início", fg="red")
        self.voltar["command"] = self.limparTela
        self.voltar.pack(side="left")

    def cadastrarAlbum(self):
        print("Funcao cadastrar album !")
        album = Album()
        album.id = ""
        album.titulo = self.titulo_album.get()
        album.ano_lancamento = self.ano_lancamento.get()
        album.nome_banda = self.banda.get()
        cadastro = album.cadastrar_album()

        print(cadastro)

        if cadastro == "sucesso":
            print("cadastrou")

            self.id = album.get_album_id(album.titulo,album.ano_lancamento,album.nome_banda)
            self.terceiroContainer.destroy()
            self.quartoContainer.destroy()
            self.album_titulo = album.titulo
            self.album_ano = album.ano
            self.album_banda= album.banda

            self.telaMusica()

        else:
            print("não cadastrou")

    def cadastrarMusica(self):
        #Verifica se entrou na funcao
        print("Funcao cadastrar musica!")

        #print(self.fav.get()) ##testando o favoritar

        musica = Musica()
        albumID= str(self.id)

        musica.id = ""
        musica.titulo = self.titulo_musica.get()
        musica.duracao = self.duracao.get()
        musica.favorito = self.fav.get()
        musica.album_id = albumID

        print(musica.album_id)
        #print(musica.duracao)

        cm = musica.cadastrar_musica()

        if cm == "sucesso":

            self.terceiroContainer.destroy()
            self.quartoContainer.destroy()

            self.telaMusica()

            self.cadastromusica = tk.Label(self.terceiroContainer,text="música cadastrada: " + musica.titulo)
            self.cadastromusica.pack(side="bottom")


        else:
            print("não cadastrou")
            print(cm)



    def pesquisarAlbum(self):
        print("Funcao pesquisar album !")
        self.quartoContainer.destroy()
        self.field = self.campoPesquisaAlbum.get()
        album = Album()
        pesquisa = album.pesquisar_album(self.field)

        for p in pesquisa:
            print(p)

        if pesquisa != "erro" and pesquisa != []:
            for p in pesquisa:
                print(p)
                self.quartoContainer = tk.Frame(self.master)
                self.quartoContainer["pady"] = 10
                self.quartoContainer.pack()

                self.respostas = tk.Label(self.quartoContainer, text="Álbum: "+p[1]+"     Ano: "+p[2]+"      Banda/Artista: "+p[3])
                self.respostas["font"] =("Arial","12")
                self.respostas.pack()
        elif pesquisa == "erro":
            self.quartoContainer = tk.Frame(self.master)
            self.quartoContainer["pady"] = 10
            self.quartoContainer.pack()

            self.erro = tk.Label(self.quartoContainer,text="Erro ao executar a busca!")
            self.erro["font"] = ("Arial","12")
            self.erro.pack()
        else:
            self.quartoContainer = tk.Frame(self.master)
            self.quartoContainer["pady"] = 10
            self.quartoContainer.pack()

            self.erro = tk.Label(self.quartoContainer, text="Nenhum resultado foi encontrado")
            self.erro["font"] = ("Arial", "12")
            self.erro.pack()


    def pesquisarMusica(self):
        print("Funcao pesquisar musica !")
        print("Funcao pesquisar album !")
        self.quartoContainer.destroy()
        self.field2 = self.campoPesquisaMusica.get()
        musica = Musica()
        pesquisa1 = musica.pesquisar_musica_titulo(self.field2)
        pesquisa2 = musica.pesquisar_musica_por_banda(self.field2)
        pesquisa = pesquisa1 + pesquisa2

        for p in pesquisa:
            print(p)

        if pesquisa != "erro" and pesquisa != []:
            for p in pesquisa:
                print(p)
                self.quartoContainer = tk.Frame(self.master)
                self.quartoContainer["pady"] = 10
                self.quartoContainer.pack()
                if p[2] == 'S' or p[2] == 's':
                    self.fav = "sim"
                elif p[2] == 'N' or p[2] == 'n':
                    self.fav = "Não"
                else:
                    self.fav = "-"

                self.respostas = tk.Label(self.quartoContainer,
                                          text="Título: " + p[0] + "     Duração: " + str(p[1]) +"    Favoritada: "+self.fav+ "      Banda/Artista: " + p[3])
                self.respostas["font"] = ("Arial", "12")
                self.respostas.pack()

        elif pesquisa == "erro":
            self.quartoContainer = tk.Frame(self.master)
            self.quartoContainer["pady"] = 10
            self.quartoContainer.pack()

            self.erro = tk.Label(self.quartoContainer, text="Erro ao executar a busca!")
            self.erro["font"] = ("Arial", "12")
            self.erro.pack()
        else:
            self.quartoContainer = tk.Frame(self.master)
            self.quartoContainer["pady"] = 10
            self.quartoContainer.pack()

            self.erro = tk.Label(self.quartoContainer, text="Nenhum resultado foi encontrado")
            self.erro["font"] = ("Arial", "12")
            self.erro.pack()

    def gerarPlaylist(self):
        print("Funcao gerar playlist!")
        musica = Musica()
        self.resultado = musica.pesquisar_todas_musicas()

        favoritadas = list()
        nao_favoritadas = list()
        for r in self.resultado:
            favorito = r[3]
            if favorito =='s' or favorito == 'S':
                favoritadas.append(r)
            elif favorito =='n' or favorito == 'N':
                nao_favoritadas.append(r)
            else:
                print("Erro na consulta. ID do objeto:"+str(r[0]))

        seg_fav = 0
        favoritadas.sort() #Embaralhando as músicas
        playlist_fav = list() #musicas favoritas da playlist

        while seg_fav < 1800:
            print("Entrei no looping")
            for f in favoritadas:
                seg_fav = seg_fav + int(f[2])
                print(seg_fav)
                playlist_fav.append(f)
            break

        numero_fav_playlist = len(playlist_fav) #conta o número de musicas favoritas na playlit
        print(numero_fav_playlist)
        seg_naofav = 0
        nao_favoritadas.sort()  # Embaralhando as músicas
        playlist_naofav = list()  # musicas  nao favoritas da playlist]
        # variavel contadora
        x = 1
        while seg_fav < 1800:
            print("Entrei no looping 2")
            for nf in nao_favoritadas:
                x += 1
                seg_naofav = seg_naofav + int(nf[2])
                print(seg_naofav)
                playlist_naofav.append(nf)
                if x > numero_fav_playlist:
                    break
            break

        playlist = playlist_fav + playlist_naofav
        playlist.sort()

        self.quartoContainer = tk.Frame(self.master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.titulo = tk.Label(self.quartoContainer, text="Playlist Gerada:")
        self.titulo["font"] = ("Arial", "15")
        self.titulo.pack()
        #variavel contadora de tempo da playlist
        duracao_total = 0

        for p in playlist:
            duracao_total = duracao_total + p[2]
            if p[2] == 'S' or p[3] == 's':
                self.fav = "Sim"
            elif p[2] == 'N' or p[3] == 'n':
                self.fav = "Não"
            else:
                self.fav = "-"

            self.respostas = tk.Label(self.quartoContainer,
                                      text="Título: " + p[1] + "     Duração: " + str(p[2]) + "    Favoritada: " + self.fav )

            self.respostas["font"] = ("Arial", "12")
            self.respostas.pack()

        self.tempototal = tk.Label(self.quartoContainer, text="Duração da Playlist: "+str(duracao_total)+" segundos (max = 3600 (1 hots))")
        self.tempototal["font"] = ("Arial", "15")
        self.tempototal.pack()

        print("exibindo favoritadas")
        print(playlist_fav)
        print("exibindo nao favoritadas")
        print(playlist_naofav)
        print("exibindo playlist")
        print(playlist)

    def limparTela(self):
        self.terceiroContainer.destroy()
        self.quartoContainer.destroy()



#Gerar janela do programa
root = tk.Tk()
root.geometry('1200x800')
app = Application(master=root)
app.mainloop()