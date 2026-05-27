"""Módulo para criar painéis de texto estilizados."""
from rich.panel import Panel
from rich.console import Console

def criar_painel(texto):
    """Exibe o texto dentro de um painel colorido."""
    console = Console()
    painel = Panel(texto, title="Meu Painel", style="bold magenta")
    console.print(painel)