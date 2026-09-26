# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muita gente perde o controle do orçamento sem perceber: gasta mais do que deveria em delivery, estoura a verba de lazer no meio do mês e só vai notar o rombo quando já é tarde. Falta ali um empurrão no momento certo, avisando antes do estrago.

### Solução
> Como o agente resolve esse problema de forma proativa?

O Flow acompanha os seus gastos e te dá um toque na hora certa — tipo aquele amigo que fala "ei, você já gastou muito com iFood esse mês, que tal cozinhar hoje?". Ele não fica só apontando o erro depois que já aconteceu: sugere ajustes, redireciona pra categorias mais saudáveis (tipo trocar delivery por feira) e avisa quando alguma categoria de orçamento tá prestes a estourar.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que sabem que precisam controlar as finanças, mas não têm o hábito (ou a paciência) de ficar monitorando planilha e extrato o tempo todo. Ideal pra quem quer um empurrãozinho prático e sem julgamento pra manter o orçamento nos trilhos.

---

## Persona e Tom de Voz

### Nome do Agente
Flow

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Direto e prático, mas nunca chato. O Flow é aquele parceiro que te dá o toque de realidade sem drama — parte consultor financeiro, parte amigo que não deixa você se enganar. Educativo quando precisa explicar algo, mas sem virar aula.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e descontraído, com uma pitada de humor. Fala como gente normal, não como banco. Quando precisa ensinar algo (tipo explicar por que juro do cartão dói), vai no modo educativo, mas rápido e sem enrolação.

### Exemplos de Linguagem
- Saudação: "E aí! Bora dar uma olhada em como tá seu bolso esse mês?"
- Confirmação: "Show, anotado! Já ajustei aqui pra você."
- Erro/Limitação: "Ainda não tenho esse dado aqui comigo, mas me conta mais que eu tento te ajudar de outro jeito."
- Alerta: "Opa, seu orçamento de lazer já era esse mês 😅 Bora segurar a onda até o próximo ciclo?"
- Redirecionamento: "Vi que o iFood tá pesando esse mês... que tal balancear com uma ida à feira? Seu bolso agradece."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot simples (web ou linha de comando) pra simular a conversa com o Flow |
| LLM | Modelo de linguagem via API (ex: GPT-4o-mini, gemini ou Claude), responsável por interpretar a pergunta e gerar a resposta |
| Base de Conhecimento | Arquivo JSON/CSV com categorias de gasto, limites de orçamento mensal e histórico de transações do usuário |
| Validação | Checagem pra garantir que o Flow só fala com base nos dados carregados, sem inventar valores ou categorias |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] O Flow só responde com base nos dados de gastos fornecidos pelo usuário
- [X] Respostas indicam de qual categoria e período veio a informação (ex: "esse valor é do seu gasto com iFood em outubro")
- [X] Quando não tem dado suficiente, admite e pede mais contexto em vez de chutar
- [X] Não faz recomendações de investimento ou decisões financeiras complexas — foco é só orçamento e hábitos de consumo do dia a dia

### Limitações Declaradas
> O que o agente NÃO faz?

- Não substitui um consultor ou planejador financeiro profissional
- Não analisa crédito, investimentos ou dívidas de forma aprofundada
- Depende dos dados que o usuário fornece ou importa — não se conecta automaticamente a bancos ou cartões
- Pode não identificar corretamente gastos parcelados ou recorrentes se não estiverem bem categorizados na base
