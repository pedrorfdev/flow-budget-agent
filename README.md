# 💸 Flow — Seu Radar de Gastos

> Um agente financeiro que avisa **antes** do orçamento estourar, não depois.

## 🧠 O que é o Flow?

Todo mundo já passou por isso: o mês começa numa boa, mas no meio do caminho o iFood vira rotina, um role puxa outro, e quando vê, o orçamento de lazer já era 😅

O **Flow** é um agente de IA que acompanha seus gastos por categoria e te dá aquele toque na hora certa — tipo um amigo que entende de dinheiro e não fica te julgando. Ele te avisa quando uma categoria tá perto de estourar, mostra pra onde seu dinheiro tá indo, e sugere trocas mais saudáveis pro bolso (tipo trocar um iFood por uma ida à feira).

## 🎯 Problema que resolve

Gente que sabe que precisa controlar as finanças, mas não tem paciência (ou tempo) de ficar de olho em planilha e extrato o mês inteiro.

## ⚙️ Como funciona

1. O Flow lê seus dados de gastos e orçamento (arquivos mockados em `data/`)
2. Monta um contexto com tudo isso e injeta num prompt cuidadosamente construído pra evitar alucinação
3. Conversa com você via chat, sempre citando de onde tirou a informação
4. Roda tudo via API do Gemini — sem precisar instalar modelo local

## 🗂️ Estrutura do Repositório

```
📁 flow-budget-agent/
│
├── 📄 README.md
├── 📄 .env.example                   # Modelo de variáveis de ambiente
├── 📄 .gitignore
│
├── 📁 data/                          # Base de conhecimento do Flow
│   ├── transacoes.csv                # Histórico de transações
│   ├── orcamentos.json               # Limites de orçamento por categoria
│   ├── perfil_usuario.json           # Perfil e metas do usuário
│   └── historico_alertas.csv         # Alertas já enviados
│
├── 📁 docs/                          # Documentação do agente
│   ├── 01-documentacao-agente.md     # Caso de uso, persona, arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # System prompt e exemplos
│   ├── 04-metricas.md                # Avaliação e testes
│   └── 05-pitch.md                   # Roteiro do pitch
│
└── 📁 src/                           # Código da aplicação
    ├── app.py                        # Interface Streamlit + integração com Gemini
    └── requirements.txt              # Dependências
```

## 🚀 Como Rodar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/flow-budget-agent.git
cd flow-budget-agent/src

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Configure sua chave de API (veja .env.example)
# Crie um arquivo .env na raiz com: GEMINI_API_KEY=sua_chave_aqui

# Rode a aplicação
streamlit run app.py
```

Pegue sua chave gratuita do Gemini em [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

## 🛡️ Segurança e Anti-Alucinação

O Flow só responde com base nos dados carregados — nunca inventa valor, categoria ou recomendação de investimento. Quando não sabe algo, admite e redireciona. Mais detalhes em [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md).

## 📄 Documentação Completa

| Etapa | Arquivo |
|-------|---------|
| 1. Documentação do Agente | [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md) |
| 2. Base de Conhecimento | [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md) |
| 3. Prompts do Agente | [`docs/03-prompts.md`](./docs/03-prompts.md) |
| 4. Avaliação e Métricas | [`docs/04-metricas.md`](./docs/04-metricas.md) |
| 5. Pitch | [`docs/05-pitch.md`](./docs/05-pitch.md) |

---

Feito com ☕ e um pouco de desespero no fim do mês, por Pedro.