import flet as ft
from models.interrogatorio import Interrogatorio


def build_estacoes_horarios(interrogatorio: Interrogatorio):
    campos = {
        "Piora no dia quente ou no frio": ft.Dropdown(
            label="Piora no dia quente ou no frio?",
            options=[
                ft.dropdown.Option("Dia quente"),
                ft.dropdown.Option("Dia frio"),
                ft.dropdown.Option("Não piora"),
                ft.dropdown.Option("Ambos")
            ]
        ),
        "Horário de piora": ft.Dropdown(
            label="É pior pela manhã, tarde ou a noite?",
            options=[
                ft.dropdown.Option("Manhã"),
                ft.dropdown.Option("Tarde"),
                ft.dropdown.Option("Noite"),
                ft.dropdown.Option("Não varia")
            ]
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("12. Estações e horários de piora", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("12. Estações e horários de piora", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("12. Estações e horários de piora", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Piora no dia quente ou no frio"],
                campos["Horário de piora"]
            ], spacing=10)
        ]
    )