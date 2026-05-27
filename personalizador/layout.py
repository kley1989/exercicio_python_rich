"""Módulo para organizar o texto em layouts de tela."""
from rich.layout import Layout
from rich.console import Console

def exibir_no_topo(texto):
    """Exibe o texto em uma divisão na parte superior da tela."""
    console = Console()
    layout = Layout()

    # Dividimos a tela em topo e baixo
    layout.split_column(
        Layout(name="superior"),
        Layout(name="inferior")
    )
    
    # Colocamos o seu texto apenas na parte de cima
    layout["superior"].update(f"Conteúdo do Topo: {texto}")
    layout["inferior"].update("Parte de baixo vazia...")
    
    console.print(layout)
