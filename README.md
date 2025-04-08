# 🌦️ Projeto: Análise de Dados Meteorológicos

## 💡 Disciplina: Lógica e Programação de Computadores  
**PUCRS – Fase 2**

---

## 📌 Descrição

Este programa foi desenvolvido para realizar análises meteorológicas a partir de dados reais de Porto Alegre (1961 a 2016). A aplicação foi feita em **Python**, com foco no processamento de arquivos CSV, visualização tabular alinhada e geração de gráficos.

---

## 📁 Estrutura do Projeto

- `clima.py` → Código-fonte principal e comentado.
- `dados.csv` → Arquivo de dados meteorológicos (pode ser outro, contanto que siga o mesmo formato).
- `README.md` → Este arquivo com instruções.
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

- ✅ Leitura de arquivos CSV com delimitador vírgula
- ✅ Autocomplete de caminho de arquivos no terminal (com `prompt_toolkit`)
- ✅ Visualização tabular com colunas alinhadas
- ✅ Exibição de dados por intervalo de datas e tipo de medição
- ✅ Mês mais chuvoso (acumulado de precipitação)
- ✅ Média de temperatura mínima (2006–2016) para um mês informado
- ✅ Gráfico com as médias de temperatura mínima
- ✅ Cálculo da média geral da temperatura mínima do mês

---

## 🧠 Formato esperado do CSV

O arquivo `.csv` deve conter os seguintes campos no cabeçalho:

```csv
data,precip,maxima,minima,um_relativa,vel_vento
```

Formato da data: `dd/mm/yyyy`  
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
- Curso: Análise e desenvolvimento de sistemas
- Universidade: PUCRS

---

## 📝 Observações

- O programa ignora automaticamente linhas com dados incompletos ou inválidos.
- Os caminhos para arquivos são tratados de forma **relativa**.
- As saídas em modo texto são apresentadas com colunas alinhadas para facilitar leitura.

---

### 🚀 Boas análises meteorológicas!
