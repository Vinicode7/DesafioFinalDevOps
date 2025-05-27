# relatorio.py
from openpyxl import Workbook
from datetime import datetime
import os

# Criar pasta se não existir
os.makedirs("relatorios", exist_ok=True)

# Criar workbook
wb = Workbook()
ws = wb.active
ws.title = "Relatório de Exemplo"

# Cabeçalho
ws.append(["ID", "Nome", "Data"])

# Dados falsos
dados = [
    [1, "Relatório gerado via GitHub Actions", datetime.now().strftime("%d/%m/%Y %H:%M")],
    [2, "Outro registro", datetime.now().strftime("%d/%m/%Y %H:%M")]
]

# Adiciona os dados
for linha in dados:
    ws.append(linha)

# Salvar na pasta "relatorios"
wb.save("relatorios/relatorio.xlsx")

print("✅ Relatório gerado com sucesso!")
