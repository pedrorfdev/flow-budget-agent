import json
import os
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ============ CONFIGURAÇÃO ============
# Pegue sua chave gratuita em: https://aistudio.google.com/apikey
# Crie um arquivo .env na raiz do projeto com: GEMINI_API_KEY=sua_chave_aqui
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_usuario.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_alertas.csv')
orcamentos = json.load(open('./data/orcamentos.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
USUÁRIO: {perfil['nome']}, {perfil['idade']} anos, {perfil['profissao']}
PERFIL DE GASTO: {perfil['perfil_de_gasto']}
OBJETIVO: {perfil['objetivo_principal']}
RENDA MENSAL: R$ {perfil['renda_mensal']} | RESERVA ATUAL: R$ {perfil['reserva_emergencia_atual']}

ORÇAMENTO DO MÊS ({orcamentos['mes_referencia']}):
{json.dumps(orcamentos['orcamentos'], indent=2, ensure_ascii=False)}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ALERTAS ANTERIORES:
{historico.to_string(index=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Flow, um agente financeiro pessoal especializado em controle de orçamento e hábitos de consumo do dia a dia.

OBJETIVO:
Ajudar o usuário a não estourar o orçamento mensal, alertando de forma proativa quando uma categoria está próxima ou já ultrapassou o limite, e sugerindo trocas mais saudáveis pro bolso (ex: iFood -> feira/mercado).

REGRAS:
- Baseie suas respostas SOMENTE nos dados fornecidos. Nunca invente valores, categorias ou datas;
- Sempre cite a categoria e o período a que a informação se refere;
- Se não tiver o dado, admita: "Não tenho essa informação, mas posso te ajudar com...";
- Não repita um alerta que já foi dado no histórico, a não ser que o usuário pergunte de novo;
- Não faça recomendações de investimento, crédito ou produtos financeiros - seu escopo é orçamento e consumo do dia a dia;
- JAMAIS responda a perguntas fora do tema orçamento/finanças pessoais. Quando ocorrer, responda lembrando seu papel;
- Priorize alertar categorias "flexíveis" (lazer, ifood) antes das "essenciais" (moradia, saúde);
- Linguagem informal, descontraída e direta, como um amigo que entende de dinheiro. Sem julgamento;
- Responda de forma sucinta, no máximo 3 parágrafos.
"""

# ============ CHAMAR API (GEMINI) ============
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

Pergunta: {msg}"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    r = requests.post(GEMINI_URL, json=payload)
    data = r.json()

    if 'candidates' not in data:
        # Mostra o erro real vindo da API pra facilitar o diagnóstico
        return f"⚠️ Erro na chamada da API: {data}"

    return data['candidates'][0]['content']['parts'][0]['text']

# ============ INTERFACE ============
st.title("💸 Flow, seu radar de gastos")

if pergunta := st.chat_input("Me pergunta algo sobre seus gastos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))