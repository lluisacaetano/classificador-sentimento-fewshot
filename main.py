import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Carrega a API Key do arquivo .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def classificar_sentimento(texto_reclamacao: str) -> dict:
    # Prompt Few-Shot com exemplos para aumentar a precisão
    prompt = f"""Você é um analista de atendimento ao cliente.
Classifique o sentimento como: "positivo", "negativo" ou "neutro".
Retorne APENAS um JSON no formato: {{"sentimento": "...", "resumo": "..."}}

=== EXEMPLOS ===

Reclamação: "Estou muito decepcionado! Comprei um celular que chegou quebrado e ninguém resolve. Péssimo atendimento!"
{{"sentimento": "negativo", "resumo": "Cliente recebeu produto danificado e não obteve suporte adequado."}}

Reclamação: "O produto chegou no prazo e funciona bem. Porém, a embalagem estava amassada."
{{"sentimento": "neutro", "resumo": "Entrega no prazo e produto funcional, mas embalagem danificada."}}

Reclamação: "Quero agradecer pelo excelente atendimento! Problema resolvido rapidamente. Parabéns!"
{{"sentimento": "positivo", "resumo": "Cliente elogia a rapidez na resolução do problema."}}

=== CLASSIFICAR ===

Reclamação: "{texto_reclamacao}"
"""

    # Chama a API da OpenAI
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=200
    )

    # Extrai o texto da resposta
    texto_resposta = resposta.choices[0].message.content.strip()

    # Converte para JSON
    try:
        resultado = json.loads(texto_resposta)
    except:
        resultado = {"sentimento": "erro", "resumo": "Falha ao processar"}

    return resultado


def main():
    print("=" * 50)
    print("  CLASSIFICADOR DE SENTIMENTO - FEW-SHOT")
    print("=" * 50)

    # Recebe o texto de reclamação do cliente
    print("\nDigite a reclamação do cliente:")
    texto = input("> ")

    # Texto de exemplo caso o usuário não digite nada
    if not texto:
        texto = "Comprei um notebook há 3 dias e ele parou de funcionar. Péssimo!"
        print(f"(Usando exemplo: {texto})")

    # Classifica o sentimento
    resultado = classificar_sentimento(texto)

    # Exibe o resultado em JSON
    print("\nRESULTADO:")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
