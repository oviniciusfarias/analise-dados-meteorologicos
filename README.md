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
- `requirements.txt` → Lista de dependências do projeto.

---

## ▶️ Como Executar

### 1. Pré-requisitos

- Ter o Python 3 instalado.

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

**Ativar ambiente virtual:**

- Windows:
  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o programa

```bash
python clima.py
```

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
- Curso: Análise e desenvolvimento de software
- Universidade: PUCRS

---

## 📝 Observações

- O programa ignora automaticamente linhas com dados incompletos ou inválidos.
- Todos os caminhos para arquivos são tratados de forma **relativa**, conforme exigido no enunciado.
- O código está documentado com comentários e funções separadas para facilitar leitura e manutenção.

---

### 🚀 Bons estudos e boas análises meteorológicas!
