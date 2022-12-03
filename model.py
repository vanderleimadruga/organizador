"""
Módulo model.py
Requisitos: Este módulo agrega as funções de processamento.
Autor: Vanderlei dos Santos Madruga
Data: 03/12/2022
Versão: 0.0.7
"""

# Importação de módulos.

import os
import shutil

# Definição de funções.

# Funções de processamento.

def cria_pasta(caminho_pasta):
    """
    Função que cria as pastas Documentos e Planilhas; não permite escolha ao usuário.
    """
    if not os.path.exists(os.path.join(caminho_pasta, "Documentos")): # Verifica se a pasta já existe.
        os.mkdir(os.path.join(caminho_pasta, "Documentos")) # Cria a pasta se ela não existe.
    if not os.path.exists(os.path.join(caminho_pasta, "Planilhas")):
        os.mkdir(os.path.join(caminho_pasta, "Planilhas"))

def lista_arquivos(caminho_pasta):
    """
    Função que retorna uma lista somente de arquivos.
    """
    lista = []
    conteudo = os.listdir(caminho_pasta) # Cria uma lista com todo o conteúdo da pasta (arquivos e pastas).
    for elemento in conteudo:
        if os.path.isfile(os.path.join(caminho_pasta, elemento)): # Verifica se o elemento é um arquivo.
            lista.append(elemento)
    return lista

def tipo_arquivo(nome_arquivo):
    """
    Função que retorna a extensão do arquivo no formato ".ext".
    """
    indice = nome_arquivo.rfind(".") # Procura da direita para a esquerda o ponto da extensão e retorna sua posição.
    extensao = str.lower(nome_arquivo[indice:]) # Faz o fatiamento do nome do arquivo e retorna a extensão; normaliza para minúsculas.
    return extensao

def move_arquivo(lista_arquivos, caminho_origem):
    """
    Organiza os arquivos movendo-os para as pastas predefinidas a partir
    da idenficação do tipo de arquivo pela sua extensão. Ignora arquivos 
    com outras extensões não tratadas.
    """
    tipo_documentos = [".doc", ".docx", ".docm" ".dotx", ".dotm", ".odt", ".ott"]
    tipo_planilhas = [".xls", ".xlsx", ".xlsm" ".xlsb", ".xltx", ".ods", ".ots"]
    pasta_documentos = "Documentos"
    pasta_planilhas = "Planilhas"
    print("Processando os arquivos...\n")
    for arquivo in lista_arquivos:
        if tipo_arquivo(arquivo) in tipo_documentos:
            origem = os.path.join(caminho_origem, arquivo)
            destino = os.path.join(caminho_origem, pasta_documentos, arquivo)
            shutil.move(origem, destino)
            print(f"O arquivo {arquivo} foi movido para a pasta {pasta_documentos}.")
        elif tipo_arquivo(arquivo) in tipo_planilhas:
            origem = os.path.join(caminho_origem, arquivo)
            destino = os.path.join(caminho_origem, pasta_planilhas, arquivo)
            shutil.move(origem, destino)
            print(f"O arquivo {arquivo} foi movido para a pasta {pasta_planilhas}.")
        else:
            print(f"O arquivo {arquivo} não necessita ser movido.")
    print("\nTodos os arquivos foram processados.")