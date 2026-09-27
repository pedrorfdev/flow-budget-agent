# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | 	Analisar os gastos por categoria e identificar padrões (ex: gasto recorrente com iFood) |
| `orcamentos.json` | JSON | Definir o limite mensal de cada categoria, base para os alertas de estouro |
| `perfil_usuario.json` | JSON | Personalizar o tom das respostas e entender metas financeiras do usuário |
| `historico_alertas.csv` | CSV | 	Evitar repetir o mesmo alerta e dar contexto sobre avisos anteriores |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os arquivos mockados originais (perfil_investidor.json e produtos_financeiros.json) foram adaptados, já que o Flow não lida com investimentos ou produtos bancários — o foco é controle de orçamento e hábitos de consumo. perfil_investidor.json virou perfil_usuario.json (dados comportamentais e metas), e produtos_financeiros.json virou orcamentos.json (limites definidos por categoria de gasto). historico_atendimento.csv foi renomeado para historico_alertas.csv, guardando o histórico de avisos que o Flow já deu, e não atendimentos.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON são carregados no início da sessão e injetados no contexto do prompt como parte do system prompt, simulando uma base de conhecimento estática por sessão.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados de orçamento e transações vão direto no system prompt, resumidos por categoria (total gasto x limite definido). O histórico de alertas é consultado antes de gerar uma nova resposta, pra evitar repetir o mesmo aviso duas vezes na mesma conversa.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Usuário:
- Nome: João Silva
- Perfil de gasto: impulsivo em lazer e delivery, organizado com contas fixas
- Objetivo: Reduzir gastos com iFood e aumentar uso da feira/mercado

Orçamento de Outubro/2025:
- iFood: R$ 200,00 (usado: R$ 324,30 — ESTOURADO em 62%)
- Lazer: R$ 300,00 (usado: R$ 334,90 — ESTOURADO em 12%)
- Mercado: R$ 500,00 (usado: R$ 275,00 — dentro do limite)
- Transporte: R$ 350,00 (usado: R$ 295,00 — dentro do limite)
- Moradia: R$ 1.500,00 (usado: R$ 1.380,00 — dentro do limite)
- Saúde: R$ 250,00 (usado: R$ 188,00 — dentro do limite)

Últimas transações:
- 22/10: iFood - Sushi - R$ 74,00
- 20/10: Academia - R$ 99,00
- 18/10: Show/Ingresso - R$ 120,00
- 16/10: iFood - Açaí - R$ 29,90
- 14/10: iFood - Lanche - R$ 38,00

Alertas anteriores nesse mês:
- 14/10: Avisado que estava a 90% do limite de iFood (usuário respondeu)
- 18/10: Avisado que estava próximo do limite de lazer (usuário respondeu)
- 02/10: Sugerido trocar iFood pela feira (usuário não respondeu)
```
