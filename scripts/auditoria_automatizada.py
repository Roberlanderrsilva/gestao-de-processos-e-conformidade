import pandas as pd
import os

def analisar_matriz(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return

    # Lendo a matriz de riscos que criamos
    df = pd.read_csv(caminho_arquivo)
    
    print("-" * 50)
    print("📊 RELATÓRIO DE AUDITORIA DE CONFORMIDADE DIGITAL")
    print("-" * 50)
    
    # Contando os níveis de risco
    resumo = df['Nivel_Risco'].value_counts()
    
    for nivel, qtd in resumo.items():
        status = "🔴 CRÍTICO" if nivel == "Crítico" else "🟡 ALTO" if nivel == "Alto" else "🟢 MODERADO"
        print(f"{status}: {qtd} pontos identificados.")

    print("-" * 50)
    print("✅ Auditoria finalizada com sucesso via Python.")

if __name__ == "__main__":
    analisar_matriz('documentos-conformidade/auditoria_detalhada_software.csv')
