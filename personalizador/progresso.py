"""Módulo para simular uma barra de progresso usando a biblioteca Rich."""
from rich.progress import track
import time

def simular_carregamento(texto):
    """
    Simula o processamento de um conteúdo exibindo uma barra de progresso animada.
    
    Parâmetros:
        texto (str): O conteúdo (texto ou nome de arquivo) a ser 'processado'.
    """
    # Mensagem informativa inicial
    print(f"Iniciando processamento: {texto[:30]}...")

    # A função 'track' cria a barra de progresso automaticamente sobre um loop.
    # range(10) significa que a barra será preenchida em 10 etapas.
    for etapa in track(range(10), description="[cyan]Trabalhando..."):
        # O time.sleep simula o tempo que o computador levaria para processar algo
        time.sleep(0.3) 
        
    print("Processamento concluído!")