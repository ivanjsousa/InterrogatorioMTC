import flet as ft
from models.interrogatorio import Interrogatorio


def build_saude_reprodutiva(interrogatorio: Interrogatorio):
    # Controles para mulheres
    campos_mulheres = {
        "Idade da menarca": ft.TextField(label="Idade da menarca", visible=False),
        "Duração do ciclo": ft.TextField(label="Duração do ciclo (dias)", visible=False),
        # ... outros campos femininos
    }

    # Controles para homens
    campos_homens = {
        "Libido": ft.Dropdown(
            label="Libido",
            options=[
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Baixa"),
                ft.dropdown.Option("Alta")
            ],
            visible=False
        ),
        # ... outros campos masculinos
    }

    def toggle_controles_sexo():
        is_female = (interrogatorio.sexo_value == "Feminino")
        for campo in campos_mulheres.values():
            campo.visible = is_female
        for campo in campos_homens.values():
            campo.visible = not is_female
        if hasattr(toggle_controles_sexo, 'page'):
            toggle_controles_sexo.page.update()

    # Configura eventos para todos os campos
    for key, field in {**campos_mulheres, **campos_homens}.items():
        if hasattr(field, 'on_change'):
            field.on_change = lambda e, k=key: interrogatorio.update_section("7. Saúde Reprodutiva", k, e.control.value)
        else:
            field.on_blur = lambda e, k=key: interrogatorio.update_section("7. Saúde Reprodutiva", k, e.control.value)

    # Atualiza visibilidade inicial
    toggle_controles_sexo()

    return ft.ExpansionTile(
        title=ft.Text("7. Saúde Reprodutiva", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                ft.Text("Esta seção será preenchida de acordo com o sexo selecionado na Identificação."),
                *campos_mulheres.values(),
                *campos_homens.values()
            ], spacing=10)
        ]
    )