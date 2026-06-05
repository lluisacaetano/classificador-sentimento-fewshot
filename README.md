# Classificador de Sentimento - Few-Shot

Trabalho da disciplina **(2026-1) FIC - Introdução a Agentes Inteligentes**

## Descrição

Script em Python que utiliza a API da OpenAI com técnica de **Few-Shot Prompting** para classificar o sentimento de reclamações de clientes.

### Funcionalidades:
- Recebe um texto de reclamação do cliente
- Usa prompt Few-Shot com exemplos para aumentar a precisão
- Retorna um JSON com o sentimento e resumo da reclamação

### Formato de Saída:
```json
{
  "sentimento": "positivo | negativo | neutro",
  "resumo": "Breve resumo da reclamação"
}
```

## Como Usar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key
Crie um arquivo `.env` baseado no `.env.example`:
```bash
cp .env.example .env
```

Edite o arquivo `.env` e insira sua chave da OpenAI:
```
OPENAI_API_KEY=sk-...
```

### 3. Executar
```bash
python main.py
```

## Exemplo de Uso

```
==================================================
  CLASSIFICADOR DE SENTIMENTO - FEW-SHOT
==================================================

Digite a reclamação do cliente:
> Comprei um notebook há 3 dias e ele parou de funcionar. Péssimo!

RESULTADO:
{
  "sentimento": "negativo",
  "resumo": "Cliente insatisfeito com defeito no produto recém-adquirido."
}
```

## Tecnologias

- Python 3.x
- OpenAI API (gpt-4o-mini)
- python-dotenv

