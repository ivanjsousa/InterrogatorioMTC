import flet as ft
from utils.file_handling import save_interrogatorio_to_txt
from models.interrogatorio import Interrogatorio


def create_save_button(interrogatorio: Interrogatorio):
    return ft.ElevatedButton(
        "Salvar Interrogatório (TXT)",
        icon=ft.icons.SAVE,
        on_click=lambda e: save_interrogatorio_to_txt(interrogatorio, e.page),
        style=ft.ButtonStyle(
            padding=20,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        )
    )