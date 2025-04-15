import flet as ft
from datetime import datetime
import os


def main(page: ft.Page):
    page.title = "Interrogatório MTC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 1000
    page.window_height = 800

    # Dados do interrogatório
    interrogatorio = {
        "1. Identificação": {},
        "2. Histórico de Saúde": {},
        "3. Sono": {},
        "4. Apetite e digestão": {},
        "5. Sede": {},
        "6. Evacuação e urina": {},
        "7. Saúde Reprodutiva": {},
        "8. Emoções predominantes": {},
        "9. Termorregulação e sudorese": {},
        "10. Dor": {},
        "11. Inspeção da língua e pulso": {},
        "12. Estações e horários de piora": {},
        "Interpretação final": {}
    }

    # Variável para controle do sexo
    sexo_value = None

    # Função para salvar em TXT
    def save_to_txt(e):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"interrogatorio_mtc_{timestamp}.txt"

            if not os.path.exists("dados_interrogatorio"):
                os.makedirs("dados_interrogatorio")

            with open(f"dados_interrogatorio/{filename}", "w", encoding="utf-8") as f:
                for section, content in interrogatorio.items():
                    f.write(f"\n{section}\n")
                    f.write("=" * 50 + "\n")
                    for key, value in content.items():
                        if value:  # Só escreve se tiver valor
                            f.write(f"{key}: {value}\n")

            page.snack_bar = ft.SnackBar(
                ft.Text(f"Dados salvos com sucesso em {filename}"),
                bgcolor=ft.colors.GREEN_400
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Erro ao salvar: {str(e)}"),
                bgcolor=ft.colors.RED_400
            )
            page.snack_bar.open = True
            page.update()

    # Seção 1: Identificação
    def build_identificacao():
        nonlocal sexo_value
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
            "Estado civil": ft.TextField(label="Estado civil", width=200),
            "Profissão": ft.TextField(label="Profissão", width=300),
            "Queixa principal (CP)": ft.TextField(label="Queixa principal (CP)", multiline=True, min_lines=2),
            "Queixas secundárias": ft.TextField(label="Queixas secundárias", multiline=True, min_lines=2),
            "Início da(s) queixa(s)": ft.TextField(label="Início da(s) queixa(s)"),
            "Fatores agravantes/aliviantes": ft.TextField(label="Fatores agravantes/aliviantes", multiline=True,
                                                          min_lines=2)
        }

        def update_sexo(e):
            nonlocal sexo_value
            sexo_value = e.control.value
            interrogatorio["1. Identificação"].update({"Sexo": e.control.value})
            page.update()

        campos["Sexo"].on_change = update_sexo

        for key, field in campos.items():
            if key != "Sexo":
                field.on_change = lambda e, k=key: interrogatorio["1. Identificação"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("1. Identificação", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    ft.Row([campos["Nome"], campos["Idade"], campos["Sexo"]]),
                    ft.Row([campos["Estado civil"], campos["Profissão"]]),
                    campos["Queixa principal (CP)"],
                    campos["Queixas secundárias"],
                    campos["Início da(s) queixa(s)"],
                    campos["Fatores agravantes/aliviantes"]
                ], spacing=10)
            ]
        )

    # Seção 2: Histórico de Saúde
    def build_historico_saude():
        campos = {
            "Doenças anteriores": ft.TextField(label="Doenças anteriores", multiline=True, min_lines=2),
            "Cirurgias": ft.TextField(label="Cirurgias", multiline=True, min_lines=2),
            "Uso de medicamentos": ft.TextField(label="Uso de medicamentos", multiline=True, min_lines=2),
            "Alergias": ft.TextField(label="Alergias", multiline=True, min_lines=2),
            "Histórico familiar relevante": ft.TextField(label="Histórico familiar relevante", multiline=True,
                                                         min_lines=2)
        }

        for key, field in campos.items():
            field.on_change = lambda e, k=key: interrogatorio["2. Histórico de Saúde"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("2. Histórico de Saúde", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column(list(campos.values()), spacing=10)
            ]
        )

    # Seção 3: Sono
    def build_sono():
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
            interrogatorio["3. Sono"].update({"Dificuldade para dormir": e.control.value})
            page.update()

        campos["Dificuldade para dormir"].on_change = toggle_horas_acorda

        campos["Sonha muito"].on_change = lambda e: interrogatorio["3. Sono"].update({"Sonha muito": e.control.value})
        campos["Sono reparador"].on_change = lambda e: interrogatorio["3. Sono"].update(
            {"Sono reparador": e.control.value})
        campos["Acorda durante a noite (horário)"].on_change = lambda e: interrogatorio["3. Sono"].update(
            {"Acorda durante a noite (horário)": e.control.value})

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

    # Seção 4: Apetite e digestão
    def build_apetite_digestao():
        campos = {
            "Apetite": ft.Dropdown(
                label="Apetite",
                options=[
                    ft.dropdown.Option("Normal"),
                    ft.dropdown.Option("Aumentado"),
                    ft.dropdown.Option("Diminuído")
                ]
            ),
            "Preferência por comidas": ft.Dropdown(
                label="Preferência por comidas",
                options=[
                    ft.dropdown.Option("Frias"),
                    ft.dropdown.Option("Quentes"),
                    ft.dropdown.Option("Indiferente")
                ]
            ),
            "Sabor na boca": ft.Dropdown(
                label="Sabor na boca",
                options=[
                    ft.dropdown.Option("Nenhum"),
                    ft.dropdown.Option("Metálico"),
                    ft.dropdown.Option("Amargo"),
                    ft.dropdown.Option("Doce"),
                    ft.dropdown.Option("Azedo"),
                    ft.dropdown.Option("Salgado")
                ]
            ),
            "Sensação de peso no estômago": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Sensação de peso no estômago?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ])
            ),
            "Plenitude com pouca comida": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Plenitude com pouca comida?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ])
            )
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["4. Apetite e digestão"].update({k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["4. Apetite e digestão"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("4. Apetite e digestão", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Apetite"],
                    campos["Preferência por comidas"],
                    campos["Sabor na boca"],
                    campos["Sensação de peso no estômago"],
                    campos["Plenitude com pouca comida"]
                ], spacing=10)
            ]
        )

    # Seção 5: Sede
    def build_sede():
        campos = {
            "Sente sede frequentemente": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Sente sede frequentemente?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ])
            ),
            "Prefere bebidas": ft.Dropdown(
                label="Prefere bebidas",
                options=[
                    ft.dropdown.Option("Quentes"),
                    ft.dropdown.Option("Frias"),
                    ft.dropdown.Option("Indiferente")
                ]
            ),
            "Quantidade de água ingerida": ft.TextField(label="Quantidade de água ingerida")
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["5. Sede"].update({k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["5. Sede"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("5. Sede", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Sente sede frequentemente"],
                    campos["Prefere bebidas"],
                    campos["Quantidade de água ingerida"]
                ], spacing=10)
            ]
        )

    # Seção 6: Evacuação e urina
    def build_evacuacao_urina():
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
                field.on_change = lambda e, k=key: interrogatorio["6. Evacuação e urina"].update({k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["6. Evacuação e urina"].update({k: e.control.value})

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

    # Seção 7: Saúde Reprodutiva
    def build_saude_reprodutiva():
        # Controles para mulheres
        campos_mulheres = {
            "Idade da menarca": ft.TextField(label="Idade da menarca", visible=False),
            "Duração do ciclo": ft.TextField(label="Duração do ciclo (dias)", visible=False),
            "Duração do fluxo": ft.TextField(label="Duração do fluxo (dias)", visible=False),
            "Cor do sangue": ft.Dropdown(
                label="Cor do sangue",
                options=[
                    ft.dropdown.Option("Vermelho vivo"),
                    ft.dropdown.Option("Escuro"),
                    ft.dropdown.Option("Pálido"),
                    ft.dropdown.Option("Com coágulos")
                ],
                visible=False
            ),
            "Cólicas menstruais": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Cólicas menstruais?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ]),
                visible=False
            ),
            "TPM": ft.TextField(label="TPM (sintomas)", multiline=True, min_lines=2, visible=False),
            "Uso de anticoncepcionais": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Uso de anticoncepcionais?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ]),
                visible=False
            ),
            "Gravidezes / abortos": ft.TextField(label="Gravidezes / abortos", visible=False)
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
            "Ereção": ft.Dropdown(
                label="Ereção",
                options=[
                    ft.dropdown.Option("Normal"),
                    ft.dropdown.Option("Fraca"),
                    ft.dropdown.Option("Ausente")
                ],
                visible=False
            ),
            "Ejaculação": ft.Dropdown(
                label="Ejaculação",
                options=[
                    ft.dropdown.Option("Normal"),
                    ft.dropdown.Option("Precoce"),
                    ft.dropdown.Option("Retardada")
                ],
                visible=False
            )
        }

        def toggle_controles_sexo():
            is_female = (sexo_value == "Feminino")
            is_male = (sexo_value == "Masculino")

            for campo in campos_mulheres.values():
                campo.visible = is_female
            for campo in campos_homens.values():
                campo.visible = is_male

            page.update()

        def update_campos(e, campo, secao):
            interrogatorio[secao].update({campo: e.control.value})

        # Configura eventos para campos femininos
        for key, field in campos_mulheres.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: update_campos(e, k, "7. Saúde Reprodutiva")
            else:
                field.on_blur = lambda e, k=key: update_campos(e, k, "7. Saúde Reprodutiva")

        # Configura eventos para campos masculinos
        for key, field in campos_homens.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: update_campos(e, k, "7. Saúde Reprodutiva")
            else:
                field.on_blur = lambda e, k=key: update_campos(e, k, "7. Saúde Reprodutiva")

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

    # Seção 8: Emoções predominantes
    def build_emocoes():
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
            "Situações de estresse frequentes": ft.TextField(label="Situações de estresse frequentes", multiline=True,
                                                             min_lines=2),
            "Ansiedade": ft.RadioGroup(
                content=ft.Column([
                    ft.Text("Ansiedade?"),
                    ft.Radio(value="Sim", label="Sim"),
                    ft.Radio(value="Não", label="Não")
                ])
            ),
            "Estado emocional atual": ft.TextField(label="Estado emocional atual", multiline=True, min_lines=2)
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["8. Emoções predominantes"].update(
                    {k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["8. Emoções predominantes"].update({k: e.control.value})

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

    # Seção 9: Termorregulação e sudorese
    def build_termorregulacao():
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
                field.on_change = lambda e, k=key: interrogatorio["9. Termorregulação e sudorese"].update(
                    {k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["9. Termorregulação e sudorese"].update(
                    {k: e.control.value})

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

    # Seção 10: Dor
    def build_dor():
        campos = {
            "Localização": ft.TextField(label="Localização"),
            "Tipo": ft.Dropdown(
                label="Tipo de dor",
                options=[
                    ft.dropdown.Option("Pontada"),
                    ft.dropdown.Option("Peso"),
                    ft.dropdown.Option("Queimação"),
                    ft.dropdown.Option("Formigamento"),
                    ft.dropdown.Option("Cólica"),
                    ft.dropdown.Option("Outro")
                ]
            ),
            "Intensidade (0 a 10)": ft.Slider(min=0, max=10, divisions=10, label="Intensidade (0 a 10): {value}"),
            "Frequência": ft.TextField(label="Frequência"),
            "Fatores agravantes / aliviantes": ft.TextField(label="Fatores agravantes / aliviantes", multiline=True,
                                                            min_lines=2)
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["10. Dor"].update({k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["10. Dor"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("10. Dor (se houver)", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Localização"],
                    campos["Tipo"],
                    campos["Intensidade (0 a 10)"],
                    campos["Frequência"],
                    campos["Fatores agravantes / aliviantes"]
                ], spacing=10)
            ]
        )

    # Seção 11: Inspeção da língua e pulso
    def build_lingua_pulso():
        campos = {
            "Cor da língua": ft.Dropdown(
                label="Cor da língua",
                options=[
                    ft.dropdown.Option("Pálida"),
                    ft.dropdown.Option("Avermelhada"),
                    ft.dropdown.Option("Arroxeada"),
                    ft.dropdown.Option("Normal")
                ]
            ),
            "Saburra": ft.Dropdown(
                label="Saburra",
                options=[
                    ft.dropdown.Option("Branca"),
                    ft.dropdown.Option("Amarela"),
                    ft.dropdown.Option("Espessa"),
                    ft.dropdown.Option("Ausente")
                ]
            ),
            "Umidade": ft.Dropdown(
                label="Umidade",
                options=[
                    ft.dropdown.Option("Seca"),
                    ft.dropdown.Option("Úmida"),
                    ft.dropdown.Option("Normal")
                ]
            ),
            "Forma da língua": ft.Dropdown(
                label="Forma da língua",
                options=[
                    ft.dropdown.Option("Normal"),
                    ft.dropdown.Option("Inchada"),
                    ft.dropdown.Option("Fissurada"),
                    ft.dropdown.Option("Com marcas de dentes")
                ]
            ),
            "Pulso": ft.TextField(label="Pulso (frequência, profundidade, força, qualidade)")
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["11. Inspeção da língua e pulso"].update(
                    {k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["11. Inspeção da língua e pulso"].update(
                    {k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("11. Inspeção da língua e pulso", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Cor da língua"],
                    campos["Saburra"],
                    campos["Umidade"],
                    campos["Forma da língua"],
                    campos["Pulso"]
                ], spacing=10)
            ]
        )

    # Seção 12: Estações e horários de piora
    def build_estacoes_horarios():
        campos = {
            "Piora no dia quente ou no frio": ft.Dropdown(
                label="Piora no dia quente ou no frio?",
                options=[
                    ft.dropdown.Option("Dia quente"),
                    ft.dropdown.Option("Dia frio"),
                    ft.dropdown.Option("Não piora"),
                    ft.dropdown.Option("Ambos")
                ]
            ),
            "Horário de piora": ft.Dropdown(
                label="É pior pela manhã, tarde ou a noite?",
                options=[
                    ft.dropdown.Option("Manhã"),
                    ft.dropdown.Option("Tarde"),
                    ft.dropdown.Option("Noite"),
                    ft.dropdown.Option("Não varia")
                ]
            )
        }

        for key, field in campos.items():
            if hasattr(field, 'on_change'):
                field.on_change = lambda e, k=key: interrogatorio["12. Estações e horários de piora"].update(
                    {k: e.control.value})
            else:
                field.on_blur = lambda e, k=key: interrogatorio["12. Estações e horários de piora"].update(
                    {k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("12. Estações e horários de piora", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Piora no dia quente ou no frio"],
                    campos["Horário de piora"]
                ], spacing=10)
            ]
        )

    # Seção de Interpretação final
    def build_interpretacao():
        campos = {
            "Hipótese de padrão energético": ft.TextField(label="Hipótese de padrão energético", multiline=True,
                                                          min_lines=2),
            "Indicação de tratamento": ft.TextField(label="Indicação de tratamento", multiline=True, min_lines=3)
        }

        for key, field in campos.items():
            field.on_change = lambda e, k=key: interrogatorio["Interpretação final"].update({k: e.control.value})

        return ft.ExpansionTile(
            title=ft.Text("Interpretação final", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Column([
                    campos["Hipótese de padrão energético"],
                    campos["Indicação de tratamento"]
                ], spacing=10)
            ]
        )

    # Botão de salvar
    btn_salvar = ft.ElevatedButton(
        "Salvar Interrogatório (TXT)",
        icon=ft.icons.SAVE,
        on_click=save_to_txt,
        style=ft.ButtonStyle(
            padding=20,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        )
    )

    # Layout principal
    page.add(
        ft.Column([
            ft.Text("📋 Interrogatório MTC", size=24, weight=ft.FontWeight.BOLD),
            build_identificacao(),
            build_historico_saude(),
            build_sono(),
            build_apetite_digestao(),
            build_sede(),
            build_evacuacao_urina(),
            build_saude_reprodutiva(),
            build_emocoes(),
            build_termorregulacao(),
            build_dor(),
            build_lingua_pulso(),
            build_estacoes_horarios(),
            build_interpretacao(),
            ft.Divider(),
            btn_salvar
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
    )


ft.app(target=main)
