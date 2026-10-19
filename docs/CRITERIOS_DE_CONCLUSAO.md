# Critérios de conclusão por tema

**19/out/2026, depois da segunda passada e depois de conhecidos os resultados** (emenda em `EMENDAS.md`). O autor pediu que cada achado feche com uma escolha clara e que o vídeo termine com uma conclusão. Este documento escreve como a escolha é feita, para que qualquer pessoa refaça a conta e discorde com o mesmo critério.

## 1. O que se escolhe, e o que não se escolhe

Escolhe-se, **por tema e por critério**, qual caminho apresentado no debate está mais perto de acontecer ou foi mais bem explicado, e diz-se **o nome de quem fica na frente naquele tema ou critério**, ou empate quando a conta empata. ⛔ Não se escolhe um vencedor do debate, não se soma tema e critério em placar geral e não se diz qual política é melhor para o país. Motivo jurídico: [`LIMITE_ELEITORAL.md`](LIMITE_ELEITORAL.md). Motivo de método: exequibilidade, explicação e resposta medem coisas diferentes, e o peso de cada uma é escolha de quem vota.

## 2. Os critérios

| Critério | Como se mede | Escala |
|---|---|---|
| **Exequibilidade** (proposta) | o instrumento que a proposta precisa, na fonte primária ou em 2 fontes do ano | **já vigente** (lei, MP ou ato em vigor) · **decisão do Executivo** sobre lei existente · **lei ordinária nova** · **emenda à Constituição** · **não demonstrado**; dentro do mesmo degrau, conta a fase da tramitação e se há despesa autorizada |
| **Explicação** (proposta) | os 5 detalhes de `DETALHES_COMPROMISSOS.csv` | número de detalhes presentes na fala |
| **Resposta** (candidato, só onde a pergunta é igual) | M1a a M4a de `OPORTUNIDADES.md` | D, P, N em base de 6 |
| **Congresso que toma posse em fev/2027** (dentro da exequibilidade) | composição pelos partidos que se declaram de direita, centro e esquerda (S32) | proposta que precisa de lei nova fica mais perto para quem está do lado da maioria das 2 casas; emenda à Constituição ainda depende de 3/5 (308 e 49), que nenhum grupo tem sozinho |
| **Dinheiro** (proposta), peso menor | custo dito na fala | presente ou ausente; no caso Band, ausente nas 31, então empata |
| ~~Uso do confronto livre~~ | tipo de cada pergunta feita ao outro | 🔧 v2 (19/out): **fora da conta**, a pedido do autor; segue como achado do formato no relatório, porque mede acusação e não proposta |

**Pesos, em ordem:** exequibilidade (com o fator Congresso) pesa mais; explicação e resposta vêm depois; dinheiro pesa menos. Não há número de peso nem soma: os pesos ordenam o que a fala diz primeiro e com mais destaque, e cada critério tem o seu resultado.

Exequibilidade **não** mede mérito nem efeito: uma proposta já vigente pode ser pior, e uma que exige emenda pode ser melhor. A frase de conclusão sempre diz isso.

## 2A. O Congresso de 2027, em números (S32)

| | Câmara (513) | Senado (81) |
|---|---:|---:|
| direita · centro · esquerda, pelos partidos que se declaram (projeto `congresso-e-governos-eleicoes-2026`, emenda 22) | **265** · 124 · 124 | **48** · 17 · 15 (+1) |
| outra contagem | Poder360, pela lista de partidos dele: 276 | Poder360, senador a senador: 49 |
| maioria absoluta | 257 | 41 |
| 3/5 para emenda à Constituição (CF, art. 60, §2º) | 308 | 49 |

Leitura: a direita tem, em tese, maioria nas 2 casas para lei nova se votar unida; para emenda à Constituição falta na Câmara (43 votos pela contagem do projeto) e fica no limite do Senado. Maioria contada por partido não é base garantida (S32, Correio da Manhã). A MP 1.393/2026 e a PEC 18/2025 podem ser votadas ainda pelo Congresso atual, antes de fevereiro.

## 3. A aplicação no caso Band (`casos/2026-10-18-band-lula-flavio/`)

| Tema | Caminho mais perto de acontecer | Por quê | Fontes |
|---|---|---|---|
| Saída temporária | **Flávio**, com folga (contra a saída) | a visita à família saiu da lei em 2024 (veto derrubado por 314 a 126 e 52 a 11); restabelecê-la, como o Lula defende, exige lei nova ou decisão do STF na ADI 7663, sem julgamento, e a lei nova passaria por um Congresso mais à direita que o que derrubou o veto | S06, S07, S23, S24 |
| Dívidas | **Lula** (leilão de carteiras) | a MP 1.393 está publicada, com teto de despesa de R$ 15 bi e chamamento previsto para novembro, e ainda precisa ser aprovada pelo Congresso; ela é menor do que o falado (cerca de R$ 150 bi em dívidas, não 300) e não tem Pix. A carência geral e a inclusão de empresas do Flávio exigem lei e dinheiro não indicados; a ferramenta de compra que ele precisaria já existe nessa mesma MP. O Congresso de 2027 facilitaria a lei nova do Flávio, e mesmo assim ele fica atrás, porque o que falta é a parte que ele acrescentou, sem dinheiro indicado | S02, S03, S04, S19 a S22 |
| Segurança | **Flávio** (a fronteira), com a PEC do Lula logo depois | o emprego das Forças Armadas na faixa de fronteira já tem base na LC 97/1999, art. 16-A, e depende só de decisão do Executivo (degrau 2); o ministério do Lula depende de uma emenda à Constituição (degrau 4) que já passou na Câmara (487 a 15 e 461 a 14) e na CCJ do Senado em 14/out, faltando o plenário; maioridade de 14 anos e castração química estão no mesmo degrau 4 sem tramitação, como o próprio Flávio disse (99:15); com o Congresso de 2027 esse caminho fica mais curto para ele, mas ainda faltam 43 votos na Câmara para os 3/5 | S14, S25, S26, S30, S31 |
| SUS | **empate por baixo** | nenhum dos 2 indicou a fonte de recursos pedida pela mediadora | `OPORTUNIDADES.md` M3b |

| Critério por candidato | Flávio | Lula | Leitura |
|---|---|---|---|
| Exequibilidade, por tema | 2 (saída temporária, segurança) | 1 (dívidas) | **Flávio**; SUS empata; o Congresso de 2027 pesa a favor do Flávio onde a proposta precisa de lei nova |
| Explicação: detalhes por proposta | 26 em 18 = **1,4**; "como fazer" 9 de 18 | 21 em 13 = **1,6**; "como fazer" 9 de 13 | **Lula**, um pouco; as 2 propostas mais detalhadas (4 de 5) são dele; o Flávio tem 3 com 3 |
| Resposta às 6 perguntas iguais (direta 2, em parte 1) | 1 direta + 3 em parte = **5** | 2 diretas + 1 em parte = **5** | **empate, 5 a 5**; os 2 sem resposta sobre o efeito da maioridade e o dinheiro do SUS |
| Dinheiro | 0 de 18 | 0 de 13 | **empate por baixo** |

**Conclusão por critério:** em exequibilidade, que pesa mais, o Flávio fica na frente em 2 temas e o Lula em 1, e o Congresso de 2027 pesa a favor do Flávio; em explicação, o Lula fica um pouco na frente; nas perguntas iguais, 5 a 5; no dinheiro, empate por baixo. ⛔ A soma desses resultados num vencedor do debate não é feita aqui (§1 e [`LIMITE_ELEITORAL.md`](LIMITE_ELEITORAL.md)); quem quiser somar tem os pesos e os números acima.

O uso do confronto livre (Flávio 7 de 10 perguntas de conduta, Lula 8 de 14) continua no relatório como achado do formato, fora desta conta.
