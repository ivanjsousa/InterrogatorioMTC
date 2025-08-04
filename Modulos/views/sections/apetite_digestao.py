import flet as ft
from models.interrogatorio import Interrogatorio


def build_apetite_digestao(interrogatorio: Interrogatorio):
    campos = {
        "Apetite": ft.Dropdown(
            label="Apetite",
            options=[
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Aumentado"),
                ft.dropdown.Option("Diminuído")
            ]
        ),
        "Preferência por comidas": ft.Dropdown(
            label="Preferência por comidas",
            options=[
                ft.dropdown.Option("Frias"),
                ft.dropdown.Option("Quentes"),
                ft.dropdown.Option("Indiferente")
            ]
        ),
        "Sabor na boca": ft.Dropdown(
            label="Sabor na boca",
            options=[
                ft.dropdown.Option("Nenhum"),
                ft.dropdown.Option("Metálico"),
                ft.dropdown.Option("Amargo"),
                ft.dropdown.Option("Doce"),
                ft.dropdown.Option("Azedo"),
                ft.dropdown.Option("Salgado")
            ]
        ),
        "Sensação de peso no estômago": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Sensação de peso no estômago?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Plenitude com pouca comida": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Plenitude com pouca comida?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("4. Apetite e digestão", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("4. Apetite e digestão", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("4. Apetite e digestão", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Apetite"],
                campos["Preferência por comidas"],
                campos["Sabor na boca"],
                campos["Sensação de peso no estômago"],
                campos["Plenitude com pouca comida"]
            ], spacing=10)
        ]
    )