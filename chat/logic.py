# chat/chatbot_logic.py
import json

def identificar_intencao(mensagem):
    """Identifica a intenção do usuário com base em palavras-chave."""
    mensagem = mensagem.lower()

    if "sustentabilidade" in mensagem:
        return "definicao_sustentabilidade"
    elif any(palavra in mensagem for palavra in ["dicas", "como ser mais sustentável", "o que posso fazer pelo meio ambiente"]):
        return "dicas_sustentabilidade"
    elif any(palavra in mensagem for palavra in ["leis climáticas", "legislação ambiental", "onde encontrar leis sobre o clima"]):
        return "leis_climaticas"
    elif any(palavra in mensagem for palavra in ["energias renováveis", "energia solar", "energia eólica", "o que são energias renováveis"]):
        return "energias_renovaveis"
    else:
        return "nao_entendi"

def buscar_resposta(intencao):
    """Busca a resposta correspondente na base de conhecimento."""
    with open("chat/knowledge_base.json", "r", encoding='utf-8') as f:
        knowledge = json.load(f)
    return knowledge.get(intencao, "Desculpe, não tenho informações sobre isso no momento.")

def obter_resposta(mensagem):
    """Função principal para obter a resposta do chatbot."""
    intencao = identificar_intencao(mensagem)
    resposta = buscar_resposta(intencao)
    return resposta