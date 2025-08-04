import flet as ft
from models.interrogatorio import Interrogatorio


def build_identificacao(interrogatorio: Interrogatorio):
    campos = {
        "Nome": ft.TextField(label="Nome", width=400),
        "Idade": ft.TextField(label="Idade", width=150, input_filter=ft.NumbersOnlyInputFilter()),
        "Sexo": ft.Dropdown(
            label="Sexo",
            width=150,
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Feminino"),
                ft.dropdown.Option("Outro"),
            ]
        ),
        # ... outros campos
    }

    def update_sexo(e):
        interrogatorio.set_sexo(e.control.value)

    campos["Sexo"].on_change = update_sexo

    for key, field in campos.items():
        if key != "Sexo":
            field.on_change = lambda e, k=key: interrogatorio.update_section(
                "1. Identificação", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("1. Identificação", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                ft.Row([campos["Nome"], campos["Idade"], campos["Sexo"]]),
                # ... outros controles
            ], spacing=10)
        ]
    )