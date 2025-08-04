import flet as ft
from datetime import datetime
import json
import os


def main(page: ft.Page):
    page.title = "Interrogatório Medicina Tradional Chinesa"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # Dados do interrogatório
    interrogatorio = {
        "identificacao": {},
        "historico_saude": {},
        "sono": {},
        "apetite_digestao": {},
        "sede": {},
        "evacuacao_urina": {},
        "saude_reprodutiva": {},
        "emocoes": {},
        "termorregulacao": {},
        "dor": {},
        "lingua_pulso": {},
        "estacoes_horarios": {}
    }

    # Função para salvar os dados
    def save_data(e):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"interrogatorio_mtc_{timestamp}.json"

        if not os.path.exists("dados_interrogatorio"):
            os.makedirs("dados_interrogatorio")

        with open(f"dados_interrogatorio/{filename}", "w", encoding="utf-8") as f:
            json.dump(interrogatorio, f, ensure_ascii=False, indent=4)

        page.snack_bar = ft.SnackBar(ft.Text("Dados salvos com sucesso!"))
        page.snack_bar.open = True
        page.update()

    # Seção 1: Identificação
    nome = ft.TextField(label="Nome", width=400)
    idade = ft.TextField(label="Idade", width=150, input_filter=ft.NumbersOnlyInputFilter())
    sexo = ft.Dropdown(
        label="Sexo",
        width=150,
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
            ft.dropdown.Option("Outro"),
        ]
    )
    estado_civil = ft.TextField(label="Estado civil", width=200)
    profissao = ft.TextField(label="Profissão", width=300)
    queixa_principal = ft.TextField(label="Queixa principal (CP)", multiline=True, min_lines=2)
    queixas_secundarias = ft.TextField(label="Queixas secundárias", multiline=True, min_lines=2)
    inicio_queixas = ft.TextField(label="Início da(s) queixa(s)")
    fatores_agravantes = ft.TextField(label="Fatores agravantes/aliviantes", multiline=True, min_lines=2)

    def update_identificacao(e):
        interrogatorio["identificacao"] = {
            "nome": nome.value,
            "idade": idade.value,
            "sexo": sexo.value,
            "estado_civil": estado_civil.value,
            "profissao": profissao.value,
            "queixa_principal": queixa_principal.value,
            "queixas_secundarias": queixas_secundarias.value,
            "inicio_queixas": inicio_queixas.value,
            "fatores_agravantes": fatores_agravantes.value
        }

    for field in [nome, idade, sexo, estado_civil, profissao, queixa_principal,
                  queixas_secundarias, inicio_queixas, fatores_agravantes]:
        field.on_change = update_identificacao

    secao_identificacao = ft.ExpansionTile(
        title=ft.Text("1. Identificação", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                ft.Row([nome, idade, sexo]),
                ft.Row([estado_civil, profissao]),
                queixa_principal,
                queixas_secundarias,
                inicio_queixas,
                fatores_agravantes
            ], spacing=10)
        ]
    )

    # Seção 2: Histórico de Saúde
    doencas_anteriores = ft.TextField(label="Doenças anteriores", multiline=True, min_lines=2)
    cirurgias = ft.TextField(label="Cirurgias", multiline=True, min_lines=2)
    medicamentos = ft.TextField(label="Uso de medicamentos (quais e há quanto tempo)", multiline=True, min_lines=2)
    alergias = ft.TextField(label="Alergias", multiline=True, min_lines=2)
    historico_familiar = ft.TextField(label="Histórico familiar relevante", multiline=True, min_lines=2)

    def update_historico_saude(e):
        interrogatorio["historico_saude"] = {
            "doencas_anteriores": doencas_anteriores.value,
            "cirurgias": cirurgias.value,
            "medicamentos": medicamentos.value,
            "alergias": alergias.value,
            "historico_familiar": historico_familiar.value
        }

    for field in [doencas_anteriores, cirurgias, medicamentos, alergias, historico_familiar]:
        field.on_change = update_historico_saude

    secao_historico_saude = ft.ExpansionTile(
        title=ft.Text("2. Histórico de Saúde", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                doencas_anteriores,
                cirurgias,
                medicamentos,
                alergias,
                historico_familiar
            ], spacing=10)
        ]
    )

    # Seção 3: Sono
    dificuldade_dormir = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Dificuldade para dormir?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    acorda_noite = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Acorda durante a noite?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    horas_acorda = ft.TextField(label="Que horas?", visible=False)
    sonha_muito = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Sonha muito?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    sono_reparador = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Sono reparador?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )

    def toggle_horas_acorda(e):
        horas_acorda.visible = (acorda_noite.value == "sim")
        page.update()

    acorda_noite.on_change = toggle_horas_acorda

    def update_sono(e):
        interrogatorio["sono"] = {
            "dificuldade_dormir": dificuldade_dormir.value,
            "acorda_noite": acorda_noite.value,
            "horas_acorda": horas_acorda.value if acorda_noite.value == "sim" else None,
            "sonha_muito": sonha_muito.value,
            "sono_reparador": sono_reparador.value
        }

    for field in [dificuldade_dormir, acorda_noite, sonha_muito, sono_reparador, horas_acorda]:
        if hasattr(field, 'on_change'):
            field.on_change = update_sono
        else:
            field.on_blur = update_sono

    secao_sono = ft.ExpansionTile(
        title=ft.Text("3. Sono", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                dificuldade_dormir,
                acorda_noite,
                horas_acorda,
                sonha_muito,
                sono_reparador
            ], spacing=10)
        ]
    )

    # Seção 4: Apetite e digestão
    apetite = ft.Dropdown(
        label="Apetite",
        options=[
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("aumentado"),
            ft.dropdown.Option("diminuído")
        ]
    )
    preferencia_comida = ft.Dropdown(
        label="Gosta de comidas frias ou quentes?",
        options=[
            ft.dropdown.Option("frias"),
            ft.dropdown.Option("quentes"),
            ft.dropdown.Option("indiferente")
        ]
    )
    sabor_boca = ft.Dropdown(
        label="Sente sabor na boca?",
        options=[
            ft.dropdown.Option("nenhum"),
            ft.dropdown.Option("metálico"),
            ft.dropdown.Option("amargo"),
            ft.dropdown.Option("doce"),
            ft.dropdown.Option("azedo"),
            ft.dropdown.Option("salgado")
        ]
    )
    peso_estomago = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Sensação de peso no estômago?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    plenitude = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Sensação de plenitude mesmo com pouca comida?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )

    def update_apetite_digestao(e):
        interrogatorio["apetite_digestao"] = {
            "apetite": apetite.value,
            "preferencia_comida": preferencia_comida.value,
            "sabor_boca": sabor_boca.value,
            "peso_estomago": peso_estomago.value,
            "plenitude": plenitude.value
        }

    for field in [apetite, preferencia_comida, sabor_boca, peso_estomago, plenitude]:
        if hasattr(field, 'on_change'):
            field.on_change = update_apetite_digestao
        else:
            field.on_blur = update_apetite_digestao

    secao_apetite_digestao = ft.ExpansionTile(
        title=ft.Text("4. Apetite e digestão", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                apetite,
                preferencia_comida,
                sabor_boca,
                peso_estomago,
                plenitude
            ], spacing=10)
        ]
    )

    # Seção 5: Sede
    sede_frequente = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Sente sede frequentemente?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    preferencia_bebida = ft.Dropdown(
        label="Prefere bebidas quentes ou frias?",
        options=[
            ft.dropdown.Option("quentes"),
            ft.dropdown.Option("frias"),
            ft.dropdown.Option("indiferente")
        ]
    )
    modo_beber = ft.Dropdown(
        label="Bebe água em grandes quantidades ou em pequenos goles?",
        options=[
            ft.dropdown.Option("grandes quantidades"),
            ft.dropdown.Option("pequenos goles"),
            ft.dropdown.Option("moderadamente")
        ]
    )

    def update_sede(e):
        interrogatorio["sede"] = {
            "sede_frequente": sede_frequente.value,
            "preferencia_bebida": preferencia_bebida.value,
            "modo_beber": modo_beber.value
        }

    for field in [sede_frequente, preferencia_bebida, modo_beber]:
        if hasattr(field, 'on_change'):
            field.on_change = update_sede
        else:
            field.on_blur = update_sede

    secao_sede = ft.ExpansionTile(
        title=ft.Text("5. Sede", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                sede_frequente,
                preferencia_bebida,
                modo_beber
            ], spacing=10)
        ]
    )

    # Seção 6: Evacuação e urina
    frequencia_evacuacao = ft.TextField(label="Frequência das evacuações")
    caracteristicas_fezes = ft.Dropdown(
        label="Fezes",
        options=[
            ft.dropdown.Option("ressecadas"),
            ft.dropdown.Option("moles"),
            ft.dropdown.Option("com muco"),
            ft.dropdown.Option("com sangue"),
            ft.dropdown.Option("normais")
        ]
    )
    gases = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Gases / distensão abdominal?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    caracteristicas_urina = ft.Dropdown(
        label="Urina",
        options=[
            ft.dropdown.Option("clara"),
            ft.dropdown.Option("escura"),
            ft.dropdown.Option("turva"),
            ft.dropdown.Option("normal")
        ]
    )
    frequencia_urina = ft.TextField(label="Frequência urinária")
    dor_urina = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Dor ou ardência ao urinar?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )

    def update_evacuacao_urina(e):
        interrogatorio["evacuacao_urina"] = {
            "frequencia_evacuacao": frequencia_evacuacao.value,
            "caracteristicas_fezes": caracteristicas_fezes.value,
            "gases": gases.value,
            "caracteristicas_urina": caracteristicas_urina.value,
            "frequencia_urina": frequencia_urina.value,
            "dor_urina": dor_urina.value
        }

    for field in [frequencia_evacuacao, caracteristicas_fezes, gases,
                  caracteristicas_urina, frequencia_urina, dor_urina]:
        if hasattr(field, 'on_change'):
            field.on_change = update_evacuacao_urina
        else:
            field.on_blur = update_evacuacao_urina

    secao_evacuacao_urina = ft.ExpansionTile(
        title=ft.Text("6. Evacuação e urina", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                frequencia_evacuacao,
                caracteristicas_fezes,
                gases,
                caracteristicas_urina,
                frequencia_urina,
                dor_urina
            ], spacing=10)
        ]
    )

    # Seção 7: Saúde Reprodutiva
    # Controles para mulheres
    idade_menarca = ft.TextField(label="Idade da menarca", visible=False)
    duracao_ciclo = ft.TextField(label="Duração do ciclo (em dias)", visible=False)
    duracao_fluxo = ft.TextField(label="Duração do fluxo", visible=False)
    cor_sangue = ft.Dropdown(
        label="Cor do sangue",
        options=[
            ft.dropdown.Option("vermelho vivo"),
            ft.dropdown.Option("escuro"),
            ft.dropdown.Option("pálido"),
            ft.dropdown.Option("com coágulos")
        ],
        visible=False
    )
    colicas = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Cólicas menstruais?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ]),
        visible=False
    )
    tpm = ft.TextField(label="TPM (sintomas)", multiline=True, min_lines=2, visible=False)
    anticoncepcionais = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Uso de anticoncepcionais?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ]),
        visible=False
    )
    gravidezes_abortos = ft.TextField(label="Gravidezes / abortos", visible=False)

    # Controles para homens
    libido = ft.Dropdown(
        label="Libido",
        options=[
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("baixa"),
            ft.dropdown.Option("alta")
        ],
        visible=False
    )
    erecao = ft.Dropdown(
        label="Ereção",
        options=[
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("fraca"),
            ft.dropdown.Option("ausente")
        ],
        visible=False
    )
    ejaculacao = ft.Dropdown(
        label="Ejaculação",
        options=[
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("precoce"),
            ft.dropdown.Option("retardada")
        ],
        visible=False
    )

    def toggle_saude_reprodutiva(e):
        is_female = (sexo.value == "Feminino")
        is_male = (sexo.value == "Masculino")

        # Controles femininos
        idade_menarca.visible = is_female
        duracao_ciclo.visible = is_female
        duracao_fluxo.visible = is_female
        cor_sangue.visible = is_female
        colicas.visible = is_female
        tpm.visible = is_female
        anticoncepcionais.visible = is_female
        gravidezes_abortos.visible = is_female

        # Controles masculinos
        libido.visible = is_male
        erecao.visible = is_male
        ejaculacao.visible = is_male

        page.update()

    # Atualizar visibilidade inicial
    sexo.on_change = toggle_saude_reprodutiva

    def update_saude_reprodutiva(e):
        if sexo.value == "Feminino":
            interrogatorio["saude_reprodutiva"] = {
                "idade_menarca": idade_menarca.value,
                "duracao_ciclo": duracao_ciclo.value,
                "duracao_fluxo": duracao_fluxo.value,
                "cor_sangue": cor_sangue.value,
                "colicas": colicas.value,
                "tpm": tpm.value,
                "anticoncepcionais": anticoncepcionais.value,
                "gravidezes_abortos": gravidezes_abortos.value
            }
        elif sexo.value == "Masculino":
            interrogatorio["saude_reprodutiva"] = {
                "libido": libido.value,
                "erecao": erecao.value,
                "ejaculacao": ejaculacao.value
            }
        else:
            interrogatorio["saude_reprodutiva"] = {}

    for field in [idade_menarca, duracao_ciclo, duracao_fluxo, cor_sangue, colicas,
                  tpm, anticoncepcionais, gravidezes_abortos, libido, erecao, ejaculacao]:
        if hasattr(field, 'on_change'):
            field.on_change = update_saude_reprodutiva
        else:
            field.on_blur = update_saude_reprodutiva

    secao_saude_reprodutiva = ft.ExpansionTile(
        title=ft.Text("7. Saúde Reprodutiva", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                ft.Text("Esta seção será preenchida de acordo com o sexo selecionado na Identificação."),
                # Controles femininos
                idade_menarca,
                duracao_ciclo,
                duracao_fluxo,
                cor_sangue,
                colicas,
                tpm,
                anticoncepcionais,
                gravidezes_abortos,
                # Controles masculinos
                libido,
                erecao,
                ejaculacao
            ], spacing=10)
        ]
    )

    # Seção 8: Emoções predominantes (com múltiplas escolhas via Checkbox)
    checkbox_emocoes = [
        ft.Checkbox(label="Raiva"),
        ft.Checkbox(label="Frustração"),
        ft.Checkbox(label="Preocupação"),
        ft.Checkbox(label="Medo"),
        ft.Checkbox(label="Tristeza"),
        ft.Checkbox(label="Alegria excessiva"),
        ft.Checkbox(label="Nenhuma em particular")
    ]

    situacoes_estresse = ft.TextField(label="Situações de estresse frequentes", multiline=True, min_lines=2)

    ansiedade = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Ansiedade?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )

    estado_emocional = ft.TextField(label="Estado emocional nos últimos meses", multiline=True, min_lines=2)

    def update_emocoes(e=None):
        emocoes_selecionadas = [cb.label for cb in checkbox_emocoes if cb.value]
        interrogatorio["8. Emoções predominantes"] = {
            "Emoções predominantes": ", ".join(emocoes_selecionadas),
            "Situações de estresse": situacoes_estresse.value,
            "Ansiedade": ansiedade.value,
            "Estado emocional atual": estado_emocional.value
        }

    # Adiciona evento aos campos
    for field in checkbox_emocoes + [situacoes_estresse, ansiedade, estado_emocional]:
        if hasattr(field, 'on_change'):
            field.on_change = update_emocoes
        else:
            field.on_blur = update_emocoes

    secao_emocoes = ft.ExpansionTile(
        title=ft.Text("8. Emoções predominantes", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                ft.Text("Selecione as emoções predominantes:"),
                ft.Column(checkbox_emocoes, spacing=5),
                situacoes_estresse,
                ansiedade,
                estado_emocional
            ], spacing=10)
        ]
    )

    # Seção 9: Termorregulação e sudorese
    sensacao_termica = ft.Dropdown(
        label="Sente muito frio ou muito calor?",
        options=[
            ft.dropdown.Option("muito frio"),
            ft.dropdown.Option("muito calor"),
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("alternância")
        ]
    )
    suor_espontaneo = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Suor espontâneo? (sem esforço físico)"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    suor_noturno = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Suor noturno?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )
    odor_suor = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Suor com odor forte?"),
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="não", label="Não")
        ])
    )

    def update_termorregulacao(e):
        interrogatorio["termorregulacao"] = {
            "sensacao_termica": sensacao_termica.value,
            "suor_espontaneo": suor_espontaneo.value,
            "suor_noturno": suor_noturno.value,
            "odor_suor": odor_suor.value
        }

    for field in [sensacao_termica, suor_espontaneo, suor_noturno, odor_suor]:
        if hasattr(field, 'on_change'):
            field.on_change = update_termorregulacao
        else:
            field.on_blur = update_termorregulacao

    secao_termorregulacao = ft.ExpansionTile(
        title=ft.Text("9. Termorregulação e sudorese", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                sensacao_termica,
                suor_espontaneo,
                suor_noturno,
                odor_suor
            ], spacing=10)
        ]
    )

    # Seção 10: Dor
    localizacao_dor = ft.TextField(label="Localização")
    tipo_dor = ft.Dropdown(
        label="Tipo de dor",
        options=[
            ft.dropdown.Option("pontada"),
            ft.dropdown.Option("peso"),
            ft.dropdown.Option("queimação"),
            ft.dropdown.Option("formigamento"),
            ft.dropdown.Option("cólica"),
            ft.dropdown.Option("outro")
        ]
    )
    intensidade_dor = ft.Slider(min=0, max=10, divisions=10, label="Intensidade (0 a 10): {value}")
    frequencia_dor = ft.TextField(label="Frequência")
    fatores_dor = ft.TextField(label="O que agrava ou alivia?", multiline=True, min_lines=2)

    def update_dor(e):
        interrogatorio["dor"] = {
            "localizacao": localizacao_dor.value,
            "tipo": tipo_dor.value,
            "intensidade": intensidade_dor.value,
            "frequencia": frequencia_dor.value,
            "fatores": fatores_dor.value
        }

    for field in [localizacao_dor, tipo_dor, frequencia_dor, fatores_dor]:
        if hasattr(field, 'on_change'):
            field.on_change = update_dor
        else:
            field.on_blur = update_dor

    intensidade_dor.on_change = update_dor

    secao_dor = ft.ExpansionTile(
        title=ft.Text("10. Dor (se houver)", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                localizacao_dor,
                tipo_dor,
                intensidade_dor,
                frequencia_dor,
                fatores_dor
            ], spacing=10)
        ]
    )

    # Seção 11: Inspeção da língua e pulso
    cor_lingua = ft.Dropdown(
        label="Cor da língua",
        options=[
            ft.dropdown.Option("pálida"),
            ft.dropdown.Option("avermelhada"),
            ft.dropdown.Option("arroxeada"),
            ft.dropdown.Option("normal")
        ]
    )
    saburra = ft.Dropdown(
        label="Saburra",
        options=[
            ft.dropdown.Option("branca"),
            ft.dropdown.Option("amarela"),
            ft.dropdown.Option("espessa"),
            ft.dropdown.Option("ausente")
        ]
    )
    umidade_lingua = ft.Dropdown(
        label="Umidade",
        options=[
            ft.dropdown.Option("seca"),
            ft.dropdown.Option("úmida"),
            ft.dropdown.Option("normal")
        ]
    )
    forma_lingua = ft.Dropdown(
        label="Forma da língua",
        options=[
            ft.dropdown.Option("normal"),
            ft.dropdown.Option("inchada"),
            ft.dropdown.Option("fissurada"),
            ft.dropdown.Option("com marcas de dentes")
        ]
    )
    pulso = ft.TextField(label="Pulso (descrição)")

    def update_lingua_pulso(e):
        interrogatorio["lingua_pulso"] = {
            "cor_lingua": cor_lingua.value,
            "saburra": saburra.value,
            "umidade": umidade_lingua.value,
            "forma": forma_lingua.value,
            "pulso": pulso.value
        }

    for field in [cor_lingua, saburra, umidade_lingua, forma_lingua, pulso]:
        if hasattr(field, 'on_change'):
            field.on_change = update_lingua_pulso
        else:
            field.on_blur = update_lingua_pulso

    secao_lingua_pulso = ft.ExpansionTile(
        title=ft.Text("11. Inspeção da língua e pulso (se aplicável)", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                cor_lingua,
                saburra,
                umidade_lingua,
                forma_lingua,
                pulso
            ], spacing=10)
        ]
    )

    # Seção 12: Estações e horários de piora
    estacao_piora = ft.Dropdown(
        label="Os sintomas pioram em alguma estação do ano?",
        options=[
            ft.dropdown.Option("primavera"),
            ft.dropdown.Option("verão"),
            ft.dropdown.Option("outono"),
            ft.dropdown.Option("inverno"),
            ft.dropdown.Option("não"),
            ft.dropdown.Option("todas")
        ]
    )
    horario_piora = ft.TextField(label="Horário específico de manifestação dos sintomas")

    def update_estacoes_horarios(e):
        interrogatorio["estacoes_horarios"] = {
            "estacao_piora": estacao_piora.value,
            "horario_piora": horario_piora.value
        }

    for field in [estacao_piora, horario_piora]:
        if hasattr(field, 'on_change'):
            field.on_change = update_estacoes_horarios
        else:
            field.on_blur = update_estacoes_horarios

    secao_estacoes_horarios = ft.ExpansionTile(
        title=ft.Text("12. Estações e horários de piora", weight=ft.FontWeight.BOLD),
        controls=[
            ft.Column([
                estacao_piora,
                horario_piora
            ], spacing=10)
        ]
    )

    # Botão de salvar
    btn_salvar = ft.ElevatedButton(
        "Salvar Interrogatório",
        icon=ft.icons.SAVE,
        on_click=save_data,
        style=ft.ButtonStyle(
            padding=20,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        )
    )

    # Layout principal
    page.add(
        ft.Column([
            ft.Text("📋 Interrogatório na MTC", size=24, weight=ft.FontWeight.BOLD),
            secao_identificacao,
            secao_historico_saude,
            secao_sono,
            secao_apetite_digestao,
            secao_sede,
            secao_evacuacao_urina,
            secao_saude_reprodutiva,
            secao_emocoes,
            secao_termorregulacao,
            secao_dor,
            secao_lingua_pulso,
            secao_estacoes_horarios,
            ft.Divider(),
            btn_salvar
        ], spacing=20)
    )


# Iniciar o app
ft.app(target=main)
