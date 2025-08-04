import matplotlib.pyplot as plt

# Dados das regiões e siglas
regions = {
    "HX": "Hélice – relacionada a órgãos genitais, pontos externos, calor",
    "AH": "Anti-hélice – relacionada à coluna vertebral e articulações centrais",
    "SF": "Escafa – relacionada a membros superiores (ombro, cotovelo, punho)",
    "TF": "Fossa triangular – relacionada a membros inferiores (quadril, joelho, tornozelo)",
    "TG": "Trago – associada a garganta, nariz e sistema endócrino",
    "AT": "Antitrago – relacionada a cabeça, cérebro, sistema nervoso e neurológico",
    "CO": "Concha – associada a órgãos internos (pulmão, coração, fígado, estômago etc.)",
    "LO": "Lóbulo – relacionada a cabeça e sentidos (olhos, boca, mente, emoções)"
}

# Criar figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
ax.set_title("Mapa das Regiões Auriculares com Funções Terapêuticas", fontsize=14, weight='bold')

# Inserir as regiões como uma tabela visual
table_data = [[sigla, nome] for sigla, nome in regions.items()]
table = ax.table(cellText=table_data, colLabels=["Sigla", "Região e Função"], cellLoc='left', colWidths=[0.1, 0.9], loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2)

plt.tight_layout()
plt.show()
