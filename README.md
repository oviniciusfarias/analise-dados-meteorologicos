
# 🌦️ Projeto: Análise de Dados Meteorológicos

## 💡 Disciplina: Lógica e Programação de Computadores  
**PUCRS – Fase 2**

---

## 📌 Descrição

Este programa foi desenvolvido para realizar análises meteorológicas a partir de dados reais de Porto Alegre (1961 a 2016). A aplicação foi feita em **Python**, com foco no processamento de arquivos CSV e geração de estatísticas e gráficos informativos.

---

## 📁 Estrutura do Projeto

- `clima.py` → Código-fonte completo e comentado.
- `dados.csv` → Arquivo de dados meteorológicos (você pode renomear ou usar outro, desde que siga o mesmo formato).
- `README.md` → Este arquivo com instruções e informações do projeto.

---

## ▶️ Como Executar

### 1. Pré-requisitos

- Ter o Python 3 instalado.
- Ter o `matplotlib` instalado (para geração dos gráficos):
  ```bash
  pip install matplotlib
  ```

### 2. Execute o programa

Abra o terminal (cmd ou shell) e navegue até a pasta onde está o projeto. Em seguida, rode:

```bash
python clima.py
```

### 3. Informe o nome do arquivo CSV

Ao iniciar, o programa solicitará o nome do arquivo CSV:

```
Digite o nome do arquivo CSV (ex: dados.csv):
```

👉 Se o arquivo estiver na mesma pasta do `.py`, basta digitar `dados.csv`.  
👉 Se estiver em outro local, digite o caminho relativo (ex: `data/dados.csv`).

---

## 🧪 Funcionalidades

- ✅ Leitura e validação de dados meteorológicos a partir de arquivos CSV
- ✅ Visualização de dados filtrados por mês/ano e tipo de informação
- ✅ Identificação do mês mais chuvoso
- ✅ Cálculo da média da temperatura mínima de um determinado mês nos últimos 11 anos (2006–2016)
- ✅ Geração de gráfico de barras com as médias
- ✅ Cálculo da média geral da temperatura mínima para o mês escolhido

---

## 🧠 Formato esperado do CSV

O arquivo `.csv` deve conter os seguintes campos no cabeçalho:

```csv
Data,Precipitacao,TempMaxima,TempMinima,UmidadeRelativa,VelocidadeVento
```

Formato da data: `YYYY-MM-DD`  
Separador: vírgula (`,`)

---

## 📷 Exemplo de uso

```
Menu:
1. Visualizar intervalo de dados
2. Exibir mês mais chuvoso
3. Médias da temperatura mínima de um mês (2006-2016)
4. Gráfico das médias da temperatura mínima (2006-2016)
5. Média geral da temperatura mínima (2006-2016)
0. Sair
```

---

## 👨‍💻 Autor

- Nome: **Vinicius Farias**
- Curso: Engenharia de Software
- Universidade: PUCRS

---

## 📝 Observações

- O programa ignora automaticamente linhas com dados incompletos ou inválidos.
- Todos os caminhos para arquivos são tratados de forma **relativa**, conforme exigido no enunciado.
- O código está documentado com comentários e funções separadas para facilitar leitura e manutenção.

---

