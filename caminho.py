import glob
import shutil
from random import sample

caminho_origem_normal = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Data\\train\\NORMAL\\*'
caminho_origem_normal2 = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Data\\test\\NORMAL\\*'
caminho_origem_covid19 = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Data\\train\\COVID19\\*'
caminho_origem_covid19_2 = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Data\\test\\COVID19\\*'
caminho_destino_treino = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Imagens Utilizadas\\train'
caminho_destino_teste = 'D:\\Trabalhos\\Processamento digital de imagens\\Imagens Para PRJ\\Imagens Utilizadas\\test'

arquivos_normal = glob.glob(caminho_origem_normal)
arquivos_normal2 = glob.glob(caminho_origem_normal2)
arquivos_covid19 = glob.glob(caminho_origem_covid19)
arquivos_covid19_2 = glob.glob(caminho_origem_covid19_2)
print(len(arquivos_covid19))
imagens_sorteadas_normal = sample(range(0,len(arquivos_normal)),400)
imagens_sorteadas_normal2 = sample(range(0,len(arquivos_normal2)),100)
imagens_sorteadas_covid19 = sample(range(0,len(arquivos_covid19)),400)
imagens_sorteadas_covid19_2 = sample(range(0,len(arquivos_covid19_2)),100)

""" 
print(len(arquivos_normal))
print(len(arquivos_normal2))
print(len(arquivos_covid19))
print(len(arquivos_covid19_2 ))
print(len(imagens_sorteadas_normal))
print(len(imagens_sorteadas_normal2))
print(len(imagens_sorteadas_covid19))
print(len(imagens_sorteadas_covid19_2)) """
caminho_destino_teste_covid = caminho_destino_teste + '\\COVID19'
caminho_destino_teste_normal = caminho_destino_teste + '\\NORMAL'
caminho_destino_treino_covid = caminho_destino_treino + '\\COVID19'
caminho_destino_treino_normal = caminho_destino_treino + '\\NORMAL'

for i in imagens_sorteadas_normal:
    shutil.copy(arquivos_normal[i], caminho_destino_treino_normal)

for i in imagens_sorteadas_normal2:
    shutil.copy(arquivos_normal2[i], caminho_destino_teste_normal)

for  j in imagens_sorteadas_covid19:
    shutil.copy(arquivos_covid19[j], caminho_destino_treino_covid)

for j in imagens_sorteadas_covid19_2:
    shutil.move(arquivos_covid19_2[j], caminho_destino_teste_covid)