import flet as ft
from models.interrogatorio import Interrogatorio
from views.components.save_button import create_save_button
from views.sections import (
    identificacao, historico_saude, sono, apetite_digestao, sede,
    evacuacao_urina, saude_reprodutiva, emocoes, termorregulacao,
    dor, lingua_pulso, estacoes_horarios, interpretacao
)


def main_layout(page: ft.Page):
    interrogatorio = Interrogatorio()

    # Criar todas as seções
    sections = [
        identificacao.build_identificacao(interrogatorio),
        historico_saude.build_historico_saude(interrogatorio),
        sono.build_sono(interrogatorio),
        apetite_digestao.build_apetite_digestao(interrogatorio),
        sede.build_sede(interrogatorio),
        evacuacao_urina.build_evacuacao_urina(interrogatorio),
        saude_reprodutiva.build_saude_reprodutiva(interrogatorio),
        emocoes.build_emocoes(interrogatorio),
        termorregulacao.build_termorregulacao(interrogatorio),
        dor.build_dor(interrogatorio),
        lingua_pulso.build_lingua_pulso(interrogatorio),
        estacoes_horarios.build_estacoes_horarios(interrogatorio),
        interpretacao.build_interpretacao(interrogatorio)
    ]

    # Botão de salvar
    btn_salvar = create_save_button(interrogatorio)

    # Layout principal
    page.add(
        ft.Column([
            ft.Text("📋 Interrogatório MTC", size=24, weight=ft.FontWeight.BOLD),
            *sections,
            ft.Divider(),
            btn_salvar
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
    )