import flet as ft
from models.interrogatorio import Interrogatorio


def build_evacuacao_urina(interrogatorio: Interrogatorio):
    campos = {
        "Frequência das evacuações": ft.TextField(label="Frequência das evacuações"),
        "Características das fezes": ft.Dropdown(
            label="Características das fezes",
            options=[
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Ressecada"),
                ft.dropdown.Option("Mole"),
                ft.dropdown.Option("Com muco"),
                ft.dropdown.Option("Com sangue")
            ]
        ),
        "Gases / distensão abdominal": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Gases / distensão abdominal?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Cor e aspecto da urina": ft.Dropdown(
            label="Cor e aspecto da urina",
            options=[
                ft.dropdown.Option("Clara"),
                ft.dropdown.Option("Escura"),
                ft.dropdown.Option("Turva"),
                ft.dropdown.Option("Normal")
            ]
        ),
        "Frequência urinária": ft.TextField(label="Frequência urinária"),
        "Dor ou ardência ao urinar": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Dor ou ardência ao urinar?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("6. Evacuação e urina", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("6. Evacuação e urina", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("6. Evacuação e urina", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Frequência das evacuações"],
                campos["Características das fezes"],
                campos["Gases / distensão abdominal"],
                campos["Cor e aspecto da urina"],
                campos["Frequência urinária"],
                campos["Dor ou ardência ao urinar"]
            ], spacing=10)
        ]
    )