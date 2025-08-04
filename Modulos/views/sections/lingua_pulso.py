import flet as ft
from models.interrogatorio import Interrogatorio


def build_lingua_pulso(interrogatorio: Interrogatorio):
    campos = {
        "Cor da língua": ft.Dropdown(
            label="Cor da língua",
            options=[
                ft.dropdown.Option("Pálida"),
                ft.dropdown.Option("Vermelha"),
                ft.dropdown.Option("Vermelho-encarneada"),
                ft.dropdown.Option("Arroxeada"),
                ft.dropdown.Option("Normal")
            ]
        ),
        # ... outros campos da seção
        "Formato da língua": ft.Dropdown(
            label="Formato da língua",
            options=[
                ft.dropdown.Option("Fina"),
                ft.dropdown.Option("Inchada"),
                ft.dropdown.Option("Vermelho-encarneada"),
                ft.dropdown.Option("Arroxeada"),
                ft.dropdown.Option("Normal")
            ]
        ),
        "Pulso": ft.TextField(label="Pulso (frequência, profundidade, força, qualidade)")
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("11. Inspeção da língua e pulso", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("11. Inspeção da língua e pulso", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("11. Inspeção da língua e pulso", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Cor da língua"],
                # ... outros controles
                campos["Pulso"]
            ], spacing=10)
        ]
    )