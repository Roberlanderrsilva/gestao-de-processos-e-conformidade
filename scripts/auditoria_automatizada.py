import pandas as pd
import os

def analisar_matriz(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return

    df = pd.read_csv(caminho_arquivo)
    df.columns = df.columns.str.strip()
    
    coluna_alvo = None
    for nome in ['Nivel_Risco', 'Nível_Risco', 'Nivel de Risco', 'Nível de Risco']:
        if nome in df.columns:
            coluna_alvo = nome
            break
    
    if not coluna_alvo:
        print(f"Erro: Coluna de Risco não encontrada. Colunas: {df.columns.tolist()}")
        return

    print("-" * 50)
    print("📊 RELATÓRIO DE AUDITORIA DE CONFORMIDADE DIGITAL")
    print("-" * 50)

    resumo = df[coluna_alvo].value_counts()
    for nivel, qtd in resumo.items():
        status = "🔴 CRÍTICO" if "Crítico" in str(nivel) else "🟡 ALTO" if "Alto" in str(nivel) else "🟢 MODERADO"
        print(f"{status}: {qtd} pontos identificados.")

    print("-" * 50)
    print("✅ Auditoria finalizada com sucesso via Python.")

if __name__ == "__main__":
    # Verifique se o nome da pasta e do arquivo CSV está correto abaixo:
    analisar_matriz('documentos-conformidade/auditoria_detalhada_software.csv')
