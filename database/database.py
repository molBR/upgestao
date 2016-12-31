import sqlite3

class Database(object):
    dbConnect = None
    dbCursor = None

    def __init__(self,loc):
        if(loc==1):
            self.dbConnect = sqlite3.connect('GutsDados.db')
        else:
            self.dbConnect = sqlite3.connect('database/GutsDados.db')
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
            valor_inic varchar(100) NOT NULL,
            data_inser varchar(100) NOT NULL,
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
        x = self.dbCursor.fetchall()
        return x

    def selectProdutoDoces(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 1')
        return self.dbCursor.fetchall()

    def selectProdutoSalgados(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 2')
        return self.dbCursor.fetchall()

    def selectProdutoMassas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 3')
        return self.dbCursor.fetchall()

    def selectProdutoBebidas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 4')
        return self.dbCursor.fetchall()

    def selectProdutoOutros(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 5')
        return self.dbCursor.fetchall()

    def selectCategoria(self):
        self.dbCursor.execute('SELECT * FROM Categoria ORDER BY id')
        print self.dbCursor.fetchone()

    def ContadorProduto(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        x = self.dbCursor.fetchall()
        return int((len(x)+1))

    def selectProdutoId(self, id):
        value = [id]
        self.dbCursor.execute('SELECT * FROM Produto WHERE id = ?', value)
        return self.dbCursor.fetchone()

    def selectProdutoOnlyId(self):
        self.dbCursor.execute('SELECT id FROM Produto ORDER BY id')
        return self.dbCursor.fetchall()

    def ExistsProduto(self,id):
        value = [id]
        self.dbCursor.execute('SELECT id FROM Produto WHERE id = ?', value)
        data = self.dbCursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True

    def deleteGivenId(self,id):
        print id
        value = [id]
        self.dbCursor.execute('DELETE FROM Produto WHERE id = ?',value)
        self.dbConnect.commit()


    def close(self):
        self.dbCursor.close()
