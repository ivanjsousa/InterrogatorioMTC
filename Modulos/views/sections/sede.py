import flet as ft
from models.interrogatorio import Interrogatorio


def build_sede(interrogatorio: Interrogatorio):
    campos = {
        "Sente sede frequentemente": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Sente sede frequentemente?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Prefere bebidas": ft.Dropdown(
            label="Prefere bebidas",
            options=[
                ft.dropdown.Option("Quentes"),
                ft.dropdown.Option("Frias"),
                ft.dropdown.Option("Indiferente")
            ]
        ),
        "Quantidade de água ingerida": ft.TextField(label="Quantidade de água ingerida")
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("5. Sede", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("5. Sede", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("5. Sede", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Sente sede frequentemente"],
                campos["Prefere bebidas"],
                campos["Quantidade de água ingerida"]
            ], spacing=10)
        ]
    )