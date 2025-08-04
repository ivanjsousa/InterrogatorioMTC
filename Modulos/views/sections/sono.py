import flet as ft
from models.interrogatorio import Interrogatorio


def build_sono(interrogatorio: Interrogatorio):
    campos = {
        "Dificuldade para dormir": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Dificuldade para dormir?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Acorda durante a noite (horário)": ft.TextField(label="Que horas?", visible=False),
        "Sonha muito": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Sonha muito?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        ),
        "Sono reparador": ft.RadioGroup(
            content=ft.Column([
                ft.Text("Sono reparador?"),
                ft.Radio(value="Sim", label="Sim"),
                ft.Radio(value="Não", label="Não")
            ])
        )
    }

    def toggle_horas_acorda(e):
        campos["Acorda durante a noite (horário)"].visible = (e.control.value == "Sim")
        interrogatorio.update_section("3. Sono", "Dificuldade para dormir", e.control.value)
        e.page.update()

    campos["Dificuldade para dormir"].on_change = toggle_horas_acorda
    campos["Sonha muito"].on_change = lambda e: interrogatorio.update_section("3. Sono", "Sonha muito", e.control.value)
    campos["Sono reparador"].on_change = lambda e: interrogatorio.update_section("3. Sono", "Sono reparador", e.control.value)
    campos["Acorda durante a noite (horário)"].on_change = lambda e: interrogatorio.update_section("3. Sono", "Acorda durante a noite (horário)", e.control.value)

    return ft.ExpansionTile(
        title=ft.Text("3. Sono", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                campos["Dificuldade para dormir"],
                campos["Acorda durante a noite (horário)"],
                campos["Sonha muito"],
                campos["Sono reparador"]
            ], spacing=10)
        ]
    )