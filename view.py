"""
Módulo view.py
Requisitos: Este módulo agrega as funções de entrada e saída.
Autor: Vanderlei dos Santos Madruga
Data: 03/12/2022
Versão: 0.0.4
"""

# Definição de funções.

# Funções de entrada.

def caminho_pasta():
    """
    Função que recebe do usuário o nome da pasta que contém os arquivos a serem organizados.
    """
    caminho_pasta = input("Digite o caminho da pasta (sem aspas): ")
    return caminho_pasta
   
def nomeia_pasta():
    """
    Função que recebe do usuário o nome da pasta que será criada para organizar os arquivos. *** NÃO IMPLEMENTADA ***
    """
    pass

# Funções de saída.

def inicio():
    """
    Apresentação inicial do programa.
    """
    print("""\nPROGRAMA ORGANIZADOR
    \nOrganiza os arquivos de documentos e de planinhas em pastas respectivas.
    \nInforme o caminho completo no formato C:\\Users\\Usuário\\Pasta, por exemplo.
    """)

def fim():
    """
    Apresentação final do programa.
    """
    print("\nO PROGRAMA ORGANIZADOR foi executado com sucesso.\n")

def mostra_arquivos(lista_arquivos):
    """
    Função que mostra na tela os arquivos a serem organizados.
    """
    print(f"\nA pasta contém os seguintes arquivos:\n")
    for arquivo in lista_arquivos:
        print(arquivo)
    print()