import flet as ft
from models.interrogatorio import Interrogatorio


def build_interpretacao(interrogatorio: Interrogatorio):
    campos = {
        "Hipótese de padrão energético": ft.TextField(
            label="Hipótese de padrão energético",
            multiline=True,
            min_lines=2
        ),
        "Indicação de tratamento": ft.TextField(
            label="Indicação de tratamento",
            multiline=True,
            min_lines=3
        )
    }

    for key, field in campos.items():
        field.on_change = lambda e, k=key: interrogatorio.update_section("Interpretação final", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("Interpretação final", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Hipótese de padrão energético"],
                campos["Indicação de tratamento"]
            ], spacing=10)
        ]
    )