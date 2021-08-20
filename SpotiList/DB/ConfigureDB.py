import sqlite3

class Banco():
    def __init__(self):
        self.connection = sqlite3.connect("SpotList.db")
        self.createAlbumTable()
        self.createMusicaTable()

    def createAlbumTable(self):

        cursor = self.connection.cursor()
        cursor.execute("Create TABLE if not exists albuns(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                       "titulo VARCHAR(100) NOT NULL, "
                       "ano VARCHAR(4) NOT NULL, "
                       "nome_banda VARCHAR(100) NOT NULL )")
        self.connection.commit()
        cursor.close()



    def createMusicaTable(self):
        cursor = self.connection.cursor()
        cursor.execute("Create TABLE if not exists musicas(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                       "titulo VARCHAR(100) NOT NULL, "
                       "duracao INT NOT NULL, "
                       "favorito CHAR(1) NOT NULL ,"
                       "album varchar(200) NOT NULL)")
        self.connection.commit()
        cursor.close()


