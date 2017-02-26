from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
document = Document()


paragraph = document.add_paragraph('GUTS')
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

run = document.add_paragraph().add_run('                                Guts')
font = run.font
font.size = Pt(25)

nome = raw_input ("Digite o nome: ")
p = document.add_paragraph('Nome: ')
p.add_run(nome)

endereco = raw_input ("Digite o endereco: ")
p = document.add_paragraph('Endereco: ')
p.add_run( endereco )

data = raw_input ("Digite a data do envento ")
p = document.add_paragraph('Data: ')
p.add_run( data )

email = raw_input ("Digite o email: ")
p = document.add_paragraph('Email: ')
p.add_run( email )

telefone = raw_input ("Digite o telefone: ")

p = document.add_paragraph('Telefone: ')
p.add_run( telefone )

celular = raw_input ("Digite o celular ")
p = document.add_paragraph('Celular: ')
p.add_run( celular )

tipofesta = raw_input ("Digite o tipo de festa: ")
p = document.add_paragraph('Tipo de festa: ')
p.add_run( tipofesta )

numeropessoas = raw_input ("Digite o ncmero de pessoas: ")
p = document.add_paragraph('Ncmero de pessoas: ')
p.add_run( numeropessoas )


espaco = raw_input ("Digite o Espaco/local: ")
p = document.add_paragraph('Espaco/Local: ')
p.add_run( espaco )



document.save('Guts.docx')
