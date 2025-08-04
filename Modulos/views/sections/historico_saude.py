import flet as ft
from models.interrogatorio import Interrogatorio


def build_historico_saude(interrogatorio: Interrogatorio):
    campos = {
        "Doenças anteriores": ft.TextField(label="Doenças anteriores", multiline=True, min_lines=2),
        "Cirurgias": ft.TextField(label="Cirurgias", multiline=True, min_lines=2),
        "Uso de medicamentos": ft.TextField(label="Uso de medicamentos", multiline=True, min_lines=2),
        "Alergias": ft.TextField(label="Alergias", multiline=True, min_lines=2),
        "Histórico familiar relevante": ft.TextField(label="Histórico familiar relevante", multiline=True, min_lines=2)
    }

    for key, field in campos.items():
        field.on_change = lambda e, k=key: interrogatorio.update_section("2. Histórico de Saúde", k, e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("2. Histórico de Saúde", weight=ft.FontWeight.BOLD),
        controls=[ft.Column(list(campos.values()), spacing=10)]
    )