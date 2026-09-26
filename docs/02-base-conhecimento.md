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
- Nome: Pedro
- Perfil: Costuma gastar mais no fim de semana
- Meta: Reduzir gastos com delivery

Orçamento de Outubro:
- Lazer: R$ 300 (usado: R$ 310 — estourado)
- Alimentação/iFood: R$ 250 (usado: R$ 240)
- Feira/Mercado: R$ 400 (usado: R$ 150)

Últimas transações:
- 12/10: iFood - R$ 45
- 13/10: Cinema - R$ 60
- 15/10: Mercado - R$ 80

Alertas anteriores:
- 10/10: Avisado sobre proximidade do limite de lazer
```
