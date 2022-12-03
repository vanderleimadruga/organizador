"""
Módulo __main__.py
Requisitos: Este módulo contém a função principal.
Autor: Vanderlei dos Santos Madruga
Data: 03/12/2022
Versão: 0.0.3
"""

# Importação de módulos.

import model
import view

# Definição de funções.

# Função principal.

def main():
    """
    Função principal.
    """

    # Chamada de função de saída.
    view.inicio() # Apresentação inicial.

    # Chamada de função de entrada.
    pasta_origem = view.caminho_pasta() # Recebe do usuário o caminho da pasta.

    # Chamada de função de processamento.
    lista_arquivos = model.lista_arquivos(pasta_origem) # Cria a lista de arquivos.

    # Chamada de função de saída.
    if len(lista_arquivos) == 0: # Verifica se a lista contém algum arquivo.
        print("\nA pasta não contém arquivos para organização.\n")
    else:
        view.mostra_arquivos(lista_arquivos) # Mostra na tela a lista de arquivos.
    
    # Chamada de função de processamento.
    model.cria_pasta(pasta_origem) # Crias as pastas predefinidas.

    # Chamada de função de processamento.
    model.move_arquivo(lista_arquivos, pasta_origem) # Organiza os arquivos.

    # Chamada de função de saída.
    view.fim() # Apresentação final.

if __name__ == "__main__": # Verifica se o código atual é o principal; o que está em execução. Se for, o executa.
    main()