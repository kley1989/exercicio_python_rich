import argparse
import os
# Importamos os módulos que criamos dentro do pacote personalizador [4]
from personalizador import painel, estilo, progresso, layout

def principal():
    # 1. Configuração do Interpretador de Argumentos (CLI) [5, 6]
    parser = argparse.ArgumentParser(description="Sistema Personalizador de Texto")

    # Argumento posicional obrigatório: o texto ou o caminho do arquivo [2]
    parser.add_argument('entrada', help="Texto simples ou o caminho de um arquivo .txt")

    # Opção para avisar que a entrada é um arquivo [2, 7]
    parser.add_argument('-a', '--arquivo', action='store_true', 
                        help="Ative esta opção se estiver passando um caminho de arquivo")

    # Opção para escolher o módulo [2]
    parser.add_argument('-m', '--modulo', 
                        choices=['painel', 'estilo', 'progresso', 'layout'],
                        help="Escolha o módulo: painel, estilo, progresso ou layout")

    # Opção para escolher a função (opcional, dependendo da sua implementação) [2]
    parser.add_argument('-f', '--funcao', help="Nome da função específica do módulo")

    # Captura os argumentos digitados no terminal [5]
    args = parser.parse_args()

    # 2. Lógica para Processar a Entrada (Texto ou Arquivo) [1]
    conteudo = args.entrada
    if args.arquivo:
        # Verifica se o arquivo realmente existe no computador
        if os.path.exists(args.entrada):
            with open(args.entrada, 'r', encoding='utf-8') as f:
                conteudo = f.read()
        else:
            print(f"Erro: O arquivo '{args.entrada}' não foi encontrado.")
            return

    # 3. Estrutura de Seleção Múltipla (Match-Case) [3, 8]
    # Aqui o Python decide qual módulo do seu pacote chamar
    match args.modulo:
        case 'painel':
            painel.criar_painel(conteudo)
        case 'estilo':
            estilo.imprimir_estilizado(conteudo)
        case 'progresso':
            progresso.simular_carregamento(conteudo)
        case 'layout':
            layout.exibir_no_topo(conteudo)
        case _:
            # Caso o usuário não passe um módulo, apenas imprime o texto [3]
            print(f"Modo padrão (sem formatação):\n{conteudo}")

if __name__ == "__main__":
    principal()