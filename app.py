import openpyxl
from pil import Image, ImageDraw, ImageFont
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['sheet1']

for indice,linha in enumerate (sheet_alunos.iter_rows(min_row=2,max_row=2)):
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    data_inicio = linha[3].value
    data_final = linha[4].value
    carga_Horaria = linha[5].value 
    data_emissao = linha[6].value
    input('')

    fonte_nome = ImageFont.truetype('./tahoma.ttf')
    fonte_nome = ImageFont.truetype('./tahomabd.ttf')

    Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(Image)

    desenhar.text((200,600),nome_participante,fill='black',font=fonte_nome)

    Image.save(f'./(indice)(nome_participante)certificado_padrao.png')