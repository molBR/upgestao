import sqlite3

class Database(object):
    dbConnect = None
    dbCursor = None

    def __init__(self):
        self.dbConnect = sqlite3.connect('GutsDados.db')
        self.dbCursor = self.dbConnect.cursor()


    def createDB(self):

        self.dbCursor.execute('''CREATE TABLE Categoria (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            data_inser INTEGER NOT NULL
        );''')

        self.dbCursor.execute('''CREATE TABLE Produto (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            valor_inic double(10000,2) NOT NULL,
            data_inser INTEGER NOT NULL,
            Id_Categoria INTEGER NOT NULL,
            FOREIGN KEY (Id_Categoria) REFERENCES Categoria(id)
       );''')

    def insertProduto(self, id, nome, valor_inic, data_inser):
        values = [id, nome, valor_inic, data_inser]
        self.dbCursor.execute( 'INSERT INTO Produto VALUES (id, nome, valor_inic, data_inser)', values)
        self.dbConnect.commit();

    def insertProduto(self, prod):
        values = [prod.getId(), prod.getNome(), prod.getValor_inic(),
         prod.getData_inser(),prod.getForeign_key()]

        self.dbCursor.execute( 'INSERT INTO Produto VALUES (?, ?, ?, ?,?)',values)
        self.dbConnect.commit()

    def insertCategoria(self, id, nome, valor_inic, data_inser):
        values = [id, nome, data_inser]

        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();

    def insertCategoria(self, categ):
        values = [categ.getId(), categ.getNome(), categ.getData_inser()]

        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();

    def selectProduto(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        print self.dbCursor.fetchone()

    def selectCategoria(self):
        self.dbCursor.execute('SELECT * FROM Categoria ORDER BY id')
        print self.dbCursor.fetchone()

    def close(self):
        self.dbCursor.close()
