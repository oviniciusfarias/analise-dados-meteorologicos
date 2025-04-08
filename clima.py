import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Solicita ao usuário o nome do arquivo CSV e verifica se ele existe na pasta
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

def solicitar_arquivo_csv():
    completer = PathCompleter(file_filter=lambda name: name.endswith('.csv'))
    while True:
        nome_arquivo = prompt("Digite o nome do arquivo CSV: ", completer=completer)
        if nome_arquivo.endswith('.csv') and os.path.exists(nome_arquivo):
            return nome_arquivo
        else:
            print(f"Arquivo '{nome_arquivo}' não encontrado. Tente novamente.")

# Lê o arquivo CSV e transforma os dados em uma lista de dicionários
def carregar_dados(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # Corrigido para usar ponto e vírgula como separador
        for linha in leitor:
            try:
                if not linha['data'] or not linha['precip'] or not linha['maxima'] or not linha['minima']:
                    continue
                dados.append({
                    'data': datetime.strptime(linha['data'], '%d/%m/%Y'),
                    'precipitacao': float(linha['precip']) if linha['precip'] else None,
                    'temp_max': float(linha['maxima']) if linha['maxima'] else None,
                    'temp_min': float(linha['minima']) if linha['minima'] else None,
                    'umidade': float(linha['um_relativa']) if linha['um_relativa'] else None,
                    'vento': float(linha['vel_vento']) if linha['vel_vento'] else None
                })
            except ValueError:
                continue  # Ignora erros de conversão
    return dados

# Visualiza dados com base em um intervalo de datas e tipo escolhido
def visualizar_intervalo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim, tipo):
    inicio = datetime(ano_inicio, mes_inicio, 1)
    from calendar import monthrange
    fim_dia = monthrange(ano_fim, mes_fim)[1]
    fim = datetime(ano_fim, mes_fim, fim_dia)

    print(f"\nExibindo dados de {inicio.strftime('%m/%Y')} a {fim.strftime('%m/%Y')}:")
    
    cabecalhos = {
        1: f"{'Data':>10} | {'Precipitação':>13} | {'Temp Máx':>8} | {'Temp Mín':>8} | {'Umidade':>7} | {'Vento':>5}",
        2: f"{'Data':>10} | {'Precipitação':>13}",
        3: f"{'Data':>10} | {'Temp Máx':>8} | {'Temp Mín':>8}",
        4: f"{'Data':>10} | {'Umidade':>7} | {'Vento':>5}"
    }
    print(cabecalhos[tipo])

    for d in dados:
        if inicio <= d['data'] <= fim:
            if tipo == 1:
                print(f"{d['data'].strftime('%d/%m/%Y'):>10} | {d['precipitacao']:>13.1f} | {d['temp_max']:>8.1f} | {d['temp_min']:>8.1f} | {d['umidade']:>7.1f} | {d['vento']:>5.1f}")
            elif tipo == 2:
                print(f"{d['data'].strftime('%d/%m/%Y'):>10} | {d['precipitacao']:>13.1f}")
            elif tipo == 3:
                print(f"{d['data'].strftime('%d/%m/%Y'):>10} | {d['temp_max']:>8.1f} | {d['temp_min']:>8.1f}")
            elif tipo == 4:
                print(f"{d['data'].strftime('%d/%m/%Y'):>10} | {d['umidade']:>7.1f} | {d['vento']:>5.1f}")

# Retorna o mês/ano com maior volume de precipitação
def mes_mais_chuvoso(dados):
    chuva_por_mes = {}
    for d in dados:
        chave = (d['data'].year, d['data'].month)
        if d['precipitacao'] is not None:
            chuva_por_mes[chave] = chuva_por_mes.get(chave, 0) + d['precipitacao']
    mais_chuvoso = max(chuva_por_mes.items(), key=lambda x: x[1])
    print(f"\nMês mais chuvoso: {mais_chuvoso[0][1]}/{mais_chuvoso[0][0]} com {mais_chuvoso[1]:.2f} mm")

# Calcula a média da temperatura mínima para um mês de 2006 a 2016
def medias_temp_min(dados, mes):
    medias = {}
    for ano in range(2006, 2017):
        valores = [d['temp_min'] for d in dados if d['data'].year == ano and d['data'].month == mes and d['temp_min'] is not None]
        chave = f"{mes}/{ano}"
        if valores:
            medias[chave] = sum(valores) / len(valores)
        else:
            medias[chave] = None
    return medias

# Plota um gráfico com as médias de temperatura mínima
def grafico_medias(medias, mes):
    chaves = list(medias.keys())
    valores = [v for v in medias.values() if v is not None]
    chaves_validas = [k for k in chaves if medias[k] is not None]

    plt.figure(figsize=(10, 5))
    plt.bar(chaves_validas, valores, color='skyblue')
    plt.xlabel('Ano')
    plt.ylabel('Temperatura mínima média (°C)')
    plt.title(f'Média da temperatura mínima - Mês {mes:02d} (2006-2016)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Calcula a média geral das temperaturas mínimas
def media_geral(medias):
    valores = [v for v in medias.values() if v is not None]
    if valores:
        media = sum(valores) / len(valores)
        print(f"\nMédia geral da temperatura mínima: {media:.2f} °C")
    else:
        print("\nNão há dados suficientes para calcular a média geral.")

# Função principal com menu interativo
def main():
    arquivo = solicitar_arquivo_csv()
    dados = carregar_dados(arquivo)

    while True:
        print("\nMenu:")
        print("1. Visualizar intervalo de dados")
        print("2. Exibir mês mais chuvoso")
        print("3. Médias da temperatura mínima de um mês (2006-2016)")
        print("4. Gráfico das médias da temperatura mínima (2006-2016)")
        print("5. Média geral da temperatura mínima (2006-2016)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                mes_inicio = int(input("Mês inicial (1-12): "))
                ano_inicio = int(input("Ano inicial: "))
                mes_fim = int(input("Mês final (1-12): "))
                ano_fim = int(input("Ano final: "))
                tipo = int(input("Tipo (1-todos, 2-precipitação, 3-temperatura, 4-umidade/vento): "))
                visualizar_intervalo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim, tipo)
            except:
                print("Entrada inválida.")
        elif opcao == '2':
            mes_mais_chuvoso(dados)
        elif opcao == '3':
            mes = int(input("Informe o número do mês (1-12): "))
            medias = medias_temp_min(dados, mes)
            for k, v in medias.items():
                if v is not None:
                    print(f"{k}: {v:.2f} °C")
                else:
                    print(f"{k}: sem dados")
        elif opcao == '4':
            mes = int(input("Informe o número do mês (1-12): "))
            medias = medias_temp_min(dados, mes)
            grafico_medias(medias, mes)
        elif opcao == '5':
            mes = int(input("Informe o número do mês (1-12): "))
            medias = medias_temp_min(dados, mes)
            media_geral(medias)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Garante que o programa só execute quando rodado diretamente
if __name__ == "__main__":
    main()
