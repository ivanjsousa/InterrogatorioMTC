import flet as ft
from models.interrogatorio import Interrogatorio


def build_termorregulacao(interrogatorio: Interrogatorio):
    campos = {
        "Sente muito frio ou muito calor": ft.Dropdown(
            label="Sente muito frio ou muito calor?",
            options=[
                ft.dropdown.Option("Muito frio"),
                ft.dropdown.Option("Muito calor"),
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Alternância")
            ]
        ),
        "Suor espontâneo": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Suor espontâneo?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Suor noturno": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Suor noturno?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Odor do suor": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Odor do suor?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("9. Termorregulação e sudorese", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("9. Termorregulação e sudorese", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("9. Termorregulação e sudorese", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Sente muito frio ou muito calor"],
                campos["Suor espontâneo"],
                campos["Suor noturno"],
                campos["Odor do suor"]
            ], spacing=10)
        ]
    )