import flet as ft
from views.layout import main_layout


def main(page: ft.Page):
    # Configurações da página
    page.title = "Interrogatório MTC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 600
    page.window_height = 600

    # Carrega o layout principal
    main_layout(page)


if __name__ == "__main__":
    ft.app(target=main)
