import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Solicita ao usuário o nome do arquivo CSV e verifica se ele existe na pasta
def solicitar_arquivo_csv():
  while True:
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: dados.csv)").strip()
    if not nome_arquivo.endswith('.csv'):
      print("Por favor, insira um arquivo com extensão .csv")
      continue
    if os.path.exists(nome_arquivo):
      return nome_arquivo
    else:
      print(f"Arquivo '{nome_arquivo}' não encontrado. Tente novamente.")

# Lê o arquivo CSV e transforma os dados em uma lista de dicionários
def carregar_dados(nome_arquivo):
  dados = []
  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
      try:
        # Ignora linhas com campos obrigatórios ausentes
        if not linha['Data'] or not linha['Precipitacao'] or not linha['TempMaxima'] or not linha['TempMinima']:
          continue
        dados.append({
          'data': datetime.strptime(linha['Data'], '%Y-%m-%d'),
          'precipitacao': float(linha['Precipitacao']) if linha['Precipitacao'] else None,
          'temp_max': float(linha['TempMaxima']) if linha['TempMaxima'] else None,
          'temp_min': float(linha['TempMinima']) if linha['TempMinima'] else None,
          'umidade': float(linha['UmidadeRelativa']) if linha['UmidadeRelativa'] else None,
          'vento': float(linha['VelocidadeVento']) if linha['VelocidadeVento'] else None
        })
      except ValueError:
        continue # Ignora erros de conversão
  return dados

# Visualiza dados com base em um intervalo de datas e tipo escolhido
def visualizar_intervalo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim, tipo):
  inicio = datetime(ano_inicio, mes_inicio, 1)
  fim = datetime(ano_fim, mes_fim, 28)

  print(f"\nExibindo dados de {inicio.strftime('%m/%Y')} a {fim.strftime('%m/%Y')}:")

  cabecalhos = {
    1: "Data | Precipitação | Temp Máx | Temp Mín | Umidade | Vento",
    2: "Data | Precipitação",
    3: "Data | Temp Máx | Temp Mín",
    4: "Data | Umidade | Vento"
  }

  print(cabecalhos[tipo])

  for d in dados:
    if inicio <= d['data'] <= fim:
      if tipo == 1:
        print(f"{d['data'].strftime('%Y-%m-%d')} | {d['precipitacao']} | {d['temp_max']} | {d['temp_min']} | {d['umidade']} | {d['vento']}")
      elif tipo == 2:
        print(f"{d['data'].strftime('%Y-%m-%d')} | {d['precipitacao']}")
      elif tipo == 3:
        print(f"{d['data'].strftime('%Y-%m-%d')} | {d['temp_max']} | {d['temp_min']}")
      elif tipo == 4:
        print(f"{d['data'].strftime('%Y-%m-%d')} | {d['umidade']} | {d['vento']}")

# Retorna o mês/ano com maior volume de precipitação
def mes_mais_chuvoso(dados):
  chuva_por_mes = {}
  for d in dados:
    chave = (d['data'].year, d['data'].month)
    if d['precipitacao'] is not None:
      chuva_por_mes[chave] = chuva_por_mes.get(chave, 0) + d['precipitacao']
  mais_chuvoso = max(chuva_por_mes.items(), key=lambda x: x[1])
  print(f"\nMês mais chuvoso: {mais_chuvoso[0][1]}/{mais_chuvoso[0][0]} com {mais_chuvoso[1]:.2f} mm")

# Calculaa média de tempera mínima para um mês de 2006 a 2016
def medias_temp_min(dados, mes):
  medias = {}
  for ano in range(2006, 2017):
    valores = [d['temp_min'] for d in dados if d['data'].year == ano and d['data'].month == mes and d['temp_min'] is not None]
    chave = f"{mes:02d}/{ano}"
    if valores:
      medias[chave] = sum(valores) / len(valores)
    else:
      medias[chave] = None
  return medias

# Plota um gráfico de barras com as médias de temperatura mínima
def grafico_medias(medias, mes):
  meses = [f"{mes:02d}/{ano}" for ano in range(2006, 2017)]
  valores = [medias.get(mes, None) for mes in meses]

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
def media_geral(medidas):
  valores = [v for v in medias.values() if v is not None]
  if valores:
    media = sum(valores) / len(valores)
    print(f"Média geral das temperaturas mínimas: {media:.2f} °C")
  else:
    print("Não há dados suficientes para calcular a média geral.")

# Função principal com menu interativo
def main():
  arquivo = solicitar_arquivo_csv()
  dados = carregar_dados(arquivo)

  while True:
    print("\nMenu:")
    print("1. Visualizar intervalo de dados")
    print("2. Exibir mês mais chuvoso")
    print("3. Médias da temperatura mínima de um mês (2006-2016)")
    print("4. Gráfico de médias de temperatura mínima")
    print("5. Média geral da temperatura mínima")
    print("0. Sair")

    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '0':
      print("Saindo...")
      break
    elif opcao == '1':
      try:
        mes_inicio = int(input("Mês inicial (1-12): "))
        ano_inicio = int(input("Ano inicial: "))
        mes_fim = int(input("Mês final (1-12): "))
        ano_fim = int(input("Ano final: "))
        tipo = int(input("Tipo (1-todos, 2-precipitação, 3-temperatura, 4-umidade/vento): "))
        visualizar_intervalo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim, tipo)
      except:
        print("Erro ao visualizar intervalo de dados. Verifique os valores inseridos.")
    elif opcao == '2':
      mes_mais_chuvoso(dados)
    elif opcao == '3':
      mes = int(input("Inform e o mês (1-12): "))
      medias = medias_temp_min(dados, mes)
      for k, v in medias.items():
        if v is not None:
          print(f"{k}: {v:.2f} °C")
        else:
          print(f"{k}: sem dados")
    elif opcao == '4':
      mes = int(input("Informe o mês (1-12): "))
      medias = medias_temp_min(dados, mes)
      grafico_medias(medias, mes)
    elif opcao == '5':
      mes = int(input("Informe o mês (1-12): "))
      medias = medias_temp_min(dados, mes)
      media_geral(medias)
    else:
      print("Opção inválida. Tente novamente.")
      
# Garante que o programa só execute se for chamado diretamente
if __name__ == "__main__":
  main()
