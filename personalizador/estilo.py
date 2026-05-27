"""Módulo para aplicar estilos coloridos ao texto."""
from rich.console import Console
from rich.text import Text

def imprimir_estilizado(texto):
    """Exibe o texto com cor azul e em negrito."""
    console = Console()
    # Criamos um objeto de texto com um estilo específico
    texto_estilizado = Text(texto, style="bold blue")
    console.print(texto_estilizado)