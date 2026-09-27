# 💻 Código da Aplicação

Esta pasta contém o código do Flow, o agente financeiro.

## O que tem aqui

```
src/
├── app.py              # Aplicação principal (Streamlit + Gemini API)
└── requirements.txt    # Dependências
```

## O que o `app.py` faz

1. **Carrega os dados** — lê os 4 arquivos da pasta `data/` (`transacoes.csv`, `orcamentos.json`, `perfil_usuario.json`, `historico_alertas.csv`)
2. **Monta o contexto** — formata esses dados num bloco de texto com o resumo financeiro do usuário (orçamento por categoria, transações recentes, alertas anteriores)
3. **Define o comportamento do Flow** — o `SYSTEM_PROMPT` com as regras de personalidade, tom de voz e limites do agente
4. **Chama a API do Gemini** — a função `perguntar()` envia o system prompt + contexto + pergunta do usuário pra API e retorna a resposta
5. **Exibe o chat** — usando `st.chat_input` e `st.chat_message`, o Streamlit renderiza a conversa numa interface simples

## Como Rodar

```bash
# Ativar o ambiente virtual (se ainda não tiver criado, veja o README principal)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Criar o arquivo .env com sua chave do Gemini (veja .env.example na raiz)

# Rodar a aplicação
streamlit run app.py
```

## Configuração necessária

Antes de rodar, crie um arquivo `.env` na raiz do projeto com:

```
GEMINI_API_KEY=sua_chave_aqui
```

Pegue sua chave gratuita em [aistudio.google.com/apikey](https://aistudio.google.com/apikey).