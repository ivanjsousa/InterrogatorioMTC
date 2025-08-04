import flet as ft
from models.interrogatorio import Interrogatorio


def build_dor(interrogatorio: Interrogatorio):
    campos = {
        "Localização": ft.TextField(label="Localização"),
        "Tipo": ft.Dropdown(
            label="Tipo de dor",
            options=[
                ft.dropdown.Option("Pontada"),
                ft.dropdown.Option("Peso"),
                ft.dropdown.Option("Queimação"),
                ft.dropdown.Option("Formigamento"),
                ft.dropdown.Option("Cólica"),
                ft.dropdown.Option("Outro")
            ]
        ),
        "Intensidade (0 a 10)": ft.Slider(
            min=0,
            max=10,
            divisions=10,
            label="Intensidade (0 a 10): {value}"
        ),
        "Frequência": ft.TextField(label="Frequência"),
        "Fatores agravantes / aliviantes": ft.TextField(
            label="Fatores agravantes / aliviantes",
            multiline=True,
            min_lines=2
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("10. Dor", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("10. Dor", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("10. Dor (se houver)", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Localização"],
                campos["Tipo"],
                campos["Intensidade (0 a 10)"],
                campos["Frequência"],
                campos["Fatores agravantes / aliviantes"]
            ], spacing=10)
        ]
    )