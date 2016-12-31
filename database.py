# coding=utf-8
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

        # Não há verificação de integridade nas foreign keys. Ou seja, é possível usar um valor de id_Categoria não existente.
        self.dbCursor.execute('''CREATE TABLE Produto (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            valor_inic double(10000,2) NOT NULL,
            data_inser INTEGER NOT NULL,
            id_Categoria INTEGER NOT NULL,
            nome_Categoria varchar(500) NOT NULL,
            FOREIGN KEY (id_Categoria) REFERENCES Categoria(id),
            FOREIGN KEY (nome_Categoria) REFERENCES Categoria(nome)
       );''')

    #INSERTS
    def insertProduto(self, id, nome, valor_inic, data_inser, id_Categoria, nome_Categoria):
        values = [id, nome, valor_inic, data_inser, id_Categoria, nome_Categoria]
        self.dbCursor.execute('INSERT INTO Produto VALUES (id, nome, valor_inic, '
                              'data_inser, id_Categoria, nome_Categoria)', values)
        self.dbConnect.commit();

    def insertProduto(self, prod):
        values = [prod.getId(), prod.getNome(), prod.getValor_inic(),
                  prod.getData_inser(), prod.getId_Categoria(), prod.getNome_Categoria()]
        self.dbCursor.execute('INSERT INTO Produto VALUES (?, ?, ?, ?, ?, ?)', values)
        self.dbConnect.commit()

    def insertCategoria(self, id, nome, valor_inic, data_inser):
        values = [id, nome, data_inser]
        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();

    def insertCategoria(self, categ):
        values = [categ.getId(), categ.getNome(), categ.getData_inser()]
        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();

    #SELECTS
    def selectProdutoAll(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        return self.dbCursor.fetchall()

    def selectProdutoId(self, id):
        value = [id]
        self.dbCursor.execute('SELECT * FROM Produto WHERE id = ?', value)
        return self.dbCursor.fetchall()

    def selectCategoriaAll(self):
        self.dbCursor.execute('SELECT * FROM Categoria ORDER BY id')
        return self.dbCursor.fetchall()

    def close(self):
        self.dbCursor.close()
