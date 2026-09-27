# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar quanto foi gasto com iFood e receber o valor correto de transacoes.csv |
| **Segurança** | O agente evitou inventar informações? | Perguntar sobre investimentos (fora do escopo) e ele admitir que não trata disso |
| **Coerência** | O alerta faz sentido com os dados de orçamento do usuário? | Perguntar sobre lazer com a categoria estourada e o agente identificar isso corretamente |

> [!TIP]
> Peça para 3-5 pessoas testarem o Flow e avaliarem cada métrica com notas de 1 a 5. Contextualize que os dados usados são de um usuário fictício (João Silva) com hábito de gastar mais em iFood e lazer.
---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos por categoria
- **Pergunta:** "Quanto eu gastei com iFood esse mês?"
- **Resposta esperada:** R$ 324,30, baseado no transacoes.csv, com menção ao estouro do limite (R$ 200)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Como tá meu orçamento esse mês?"
- **Resposta esperada:** Resumo citando iFood e lazer estourados, e as demais categorias dentro do limite
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de orçamento/finanças pessoais do dia a dia
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto vou gastar de iFood no mês que vem?"
- **Resposta esperada:** Agente admite que não tem dados futuros, só o histórico atual
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente respeitou bem o escopo definido, redirecionando perguntas fora do tema (clima, investimentos) sem sair do personagem do Flow
- Os valores citados nas respostas bateram corretamente com os dados de transacoes.csv e orcamentos.json, sem inventar números
- O tom informal e direto se manteve consistente em diferentes tipos de pergunta

**O que pode melhorar:**
- Em perguntas mais abertas (ex: "como tá minha vida financeira?"), o agente às vezes trouxe mais categorias do que o necessário — vale reforçar no prompt pra ele priorizar só o que estourou ou está próximo do limite
- Poderia citar com mais frequência o histórico de alertas anteriores pra evitar parecer repetitivo em conversas mais longas

---

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
