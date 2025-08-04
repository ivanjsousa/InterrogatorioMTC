import flet as ft
from models.interrogatorio import Interrogatorio


def build_emocoes(interrogatorio: Interrogatorio):
    campos = {
        "Emoção predominante": ft.Dropdown(
            label="Emoção predominante",
            options=[
                ft.dropdown.Option("Raiva"),
                ft.dropdown.Option("Frustração"),
                ft.dropdown.Option("Preocupação"),
                ft.dropdown.Option("Medo"),
                ft.dropdown.Option("Tristeza"),
                ft.dropdown.Option("Alegria excessiva"),
                ft.dropdown.Option("Nenhuma em particular")
            ]
        ),
        "Situações de estresse frequentes": ft.TextField(
            label="Situações de estresse frequentes",
            multiline=True,
            min_lines=2
        ),
        "Ansiedade": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Ansiedade?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Estado emocional atual": ft.TextField(
            label="Estado emocional atual",
            multiline=True,
            min_lines=2
        )
    }

    for key, field in campos.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("8. Emoções predominantes", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("8. Emoções predominantes", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("8. Emoções predominantes", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Emoção predominante"],
                campos["Situações de estresse frequentes"],
                campos["Ansiedade"],
                campos["Estado emocional atual"]
            ], spacing=10)
        ]
    )