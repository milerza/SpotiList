#This is the models
from DB.ConfigureDB import Banco

class Album():
    def __init__(self,id=0,titulo="",ano="",banda=""):
        self.id_album = id
        self.titulo= titulo
        self.ano_lancamento = ano
        self.nome_banda = banda


    def cadastrar_album(self):
        #verificada
        # preciso retornar o ID AO CADASTRAR, OU CADASTRAR APENAS UM DO MESMO ÁLBUM
        banco = Banco()
        try:
            c = banco.connection.cursor()
            c.execute("insert into albuns(titulo,ano,nome_banda) "
                      "values ('"+self.titulo+"','"+self.ano_lancamento+"','"+self.nome_banda+"') ")
            banco.connection.commit()

            print('Álbum inserido com sucesso. ID do álbum:' )
            c.close()
            return "sucesso"

        except:
            return "erro"

    def todos_albuns(self):
        banco = Banco()
        try:
            c = banco.connection.cursor()
            c.execute("Select * from albuns")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()
            for r in rows:
                print(r)
            return rows
        except:
            return "erro"

    def pesquisar_album(self,field):
        banco = Banco()
        self.dado = field
        print(self.dado)

        try:
            c = banco.connection.cursor()
            c.execute("Select * from albuns where titulo LIKE '%"+self.dado+"%' or ano LIKE '%"+self.dado+"%'  or nome_banda LIKE '%"+self.dado+"%'  ")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()
            for r in rows:
                print(r)
            return rows

        except:
            return "erro"

    def get_album_id(self, titulo, ano, banda):
        banco = Banco()
        self.titulo = titulo
        self.ano = ano
        self.banda = banda
        print("valores para pegar o ID: "+self.titulo+" "+ self.banda+" "+self.ano)

        try:
            c = banco.connection.cursor()
            c.execute("Select id from albuns where titulo='"+self.titulo+"' and ano='"+self.ano+"' and nome_banda='"+self.banda+"'")
            rows = c.fetchone()
            banco.connection.commit()
            c.close()
            print(rows[0])
            return rows[0]

        except:
            return "erro"

    def get_id_album_per_banda(self, field):
        print("entrou na funcao pegar id")
        banco = Banco()
        self.campo = field

        try:
            c = banco.connection.cursor()
            c.execute("Select id from albuns where nome_banda LIKE '%"+self.campo+"%'")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()
            x = list()
            for r in rows:
                x += r[0]
                print(x)
            return rows

        except:
            return "erro"




class Musica(Album):
    def __init__(self, id=0, titulo="", duracao="", favorito="", album_id=""):
        super().__init__(id, titulo)
        self.id_musica = id
        self.titulo = titulo
        self.duracao = duracao
        self.favorito = favorito
        self.album_id = album_id

    def cadastrar_musica(self):
        banco = Banco()
        print(self.titulo)
        print(self.duracao)
        print(self.favorito)
        print(self.album_id)

        try:
            c = banco.connection.cursor()
            c.execute("insert into musicas (titulo, duracao, favorito, album) "
                      "values ('" + self.titulo + "','" + self.duracao + "','" + self.favorito + "','" + self.album_id +"')")
            banco.connection.commit()
            c.close()
            return "sucesso"

        except:
            return "erro"
    def pesquisar_todas_musicas(self):
        banco = Banco()
        try:
            c = banco.connection.cursor()
            c.execute("Select * from musicas")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()

            for r in rows:
                print(r)

            return rows

        except:
            return "erro"

    def pesquisar_musica_titulo(self, field):
        banco = Banco()
        album = Album()
        self.campodado = field
        self.ids_album = album.get_id_album_per_banda(self.campodado)
        print(self.ids_album)
        print("testando")
        print(self.campodado)

        try:
            c = banco.connection.cursor()
            c.execute(
                "Select musicas.titulo, musicas.duracao, musicas.favorito, albuns.nome_banda from musicas INNER JOIN albuns ON albuns.id=musicas.album and musicas.titulo LIKE '%" + self.campodado + "%'")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()
            print(rows)

            for r in rows:
                print(r)

            return rows

        except:
            return "erro"

    def pesquisar_musica_por_banda(self, field):
        banco = Banco()
        album = Album()
        self.entrada = field

        try:
            c = banco.connection.cursor()
            c.execute(
                "Select musicas.titulo, musicas.duracao, musicas.favorito, albuns.nome_banda from musicas INNER JOIN albuns ON albuns.id = musicas.album and albuns.nome_banda LIKE '%" +self.entrada+ "%'")
            rows = c.fetchall()
            banco.connection.commit()
            c.close()
            print(rows)

            for r in rows:
                print(r)

            return rows

        except:
            return "erro"


####----------------Testando cadastro de música

# musica = Musica(titulo="sonhos",duracao="125",favorito="N",album_id="2")
# cadastrar = musica.cadastrar_musica()
#
# print(cadastrar)
#
# ##----------- Testando função  de cadastro de album
# album = Album(titulo="biscoito", ano="2020", banda="Mariana")
# cadastro = album.cadastrar_album()
# print(cadastro)

###------ Testando funcao get_albuns_id
#albuns =Album()
#id = albuns.get_album_id("Positions", "2020", "Ariana")
#print(id)

###------testando funcao pesquisar_album
# print("Consulta dos álbuns cadastrados encontrada no arquivo models.py")
# albuns =Album()
# pesquisa= albuns.pesquisar_album("Ariana")
# print(pesquisa)
#
#

# ###-------------testando funcoes de pesquisar musicas
# musica =  Musica()
# todasmusicas = musica.pesquisar_todas_musicas()
# pm = musica.pesquisar_musica_titulo("Mandioca")
# pmn = musica.pesquisar_musica_por_banda("Ariana")
# print('testando musicas pelo titulo')
# print(pm)
# print('testando musicas pela banda')
# print(pmn)





