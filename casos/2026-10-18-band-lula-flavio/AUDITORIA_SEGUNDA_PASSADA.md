# Segunda passada: o que foi conferido e o que mudou

**19/out/2026.** Pedido de Gabriel: conferir de novo o passo a passo e o resultado da primeira rodada, corrigir o que estivesse errado e registrar tudo. A conferência foi feita pela IA, em passada separada, relendo a transcrição integral (privada) nos trechos usados pelo relatório e no confronto livre inteiro, e consultando de novo as fontes externas das quatro ações C. **Não houve escuta humana do áudio** nem revisão de um segundo analista. A primeira leitura fica preservada no histórico do Git (commit `33d31e4`).

## 1. O que foi conferido e se manteve

| Ponto do relatório | Onde | Resultado da conferência |
|---|---|---|
| Pergunta de saúde pediu acesso **e** dinheiro | 54:01–54:43 | Mantido. A mediadora cita 4% do PIB contra 6% e pergunta "como ampliar o atendimento e de onde vem o dinheiro". |
| Nenhum dos dois apontou fonte de recursos para o SUS na resposta à pergunta comum | 54:49–56:52 e 56:55–59:42 | Mantido. Flávio fala de prontuário, telemedicina e do futuro ministro; Lula fala da pandemia, da suspeita de privatização e do que já fez. Nenhum cita fonte de financiamento. |
| Saída temporária: Flávio contra, Lula a favor com condições | 60:21–61:47 e 61:51–63:14 | Mantido. Lula defende saída com bom comportamento "para ver a família" e exclui crime hediondo, estupro e violência contra a mulher. |
| Dívidas: Flávio com carência de 6 meses (pessoa física) e 1 ano (jurídica) | 73:56–75:27 | Mantido, e acrescentado: ele promete que a parcela de 100 a 200 reais cairia para 20 a 30. |
| Dívidas: Lula com MP, leilão, desconto e Pix | 100:11–100:41 e 103:20–103:43 | Mantido. Ele fala em "até 300 bilhões", desconto "de até 92%" e um Pix "que não é empréstimo". |
| Segurança: endurecimento penal e vigilância × coordenação por PEC | 04:36–06:38 e 06:43–08:32 | Mantido. |

## 2. Classificações corrigidas

| ID | Antes | Depois | Por quê |
|---|---|---|---|
| C11, terras raras | N | **D** | Flávio contesta a premissa no início da resposta (91:30) e, na tréplica, descreve o Escudo das Américas (94:50–95:24). A regra do pré-registro conta contestação da premissa como resposta direta, e foi assim que C6 já tinha sido marcado. |
| C12, "vítimas ou bandidos" | N | **P** | A pergunta junta castração química, maioridade penal e pena mínima por roubo de celular. Lula trata o celular (bloqueio do aparelho, 99:47–100:10) e deixa os outros dois. Um de três é parcial, a mesma régua de C10. |

Com isso, nos confrontos estruturados, cada candidato fica com uma resposta direta e uma parcial (`RESPOSTAS.json`).

## 3. O confronto livre estava incompleto

A primeira tabela tinha 8 núcleos do confronto livre. Relendo o bloco inteiro (12:33–43:37) pela mesma regra (pergunta explícita ao adversário, com conteúdo novo, fora pergunta retórica e repetição), a IA encontrou **mais 16**, de C13 a C28, com a classe de cada resposta. O confronto livre passa a ter **24 núcleos: 14 perguntas de Lula a Flávio e 10 de Flávio a Lula**.

| Respostas no confronto livre | D | P | N | I | Total |
|---|---:|---:|---:|---:|---:|
| Flávio (respondendo a Lula) | 5 | 4 | 4 | 1 | 14 |
| Lula (respondendo a Flávio) | 2 | 2 | 6 | 0 | 10 |

⚠️ **Estes números não se comparam entre os dois.** As perguntas são diferentes, o banco de tempo deixava cada um escolher quanto responder, e quem pergunta mais dá mais oportunidades ao outro. A tabela existe para mostrar o inventário completo, não para dizer quem respondeu melhor.

**O que se pode concluir, e vale para os dois:** a IA marcou o tipo de cada pergunta antes de olhar a resposta. No confronto livre, **15 das 24 perguntas foram sobre conduta ou acusação** (de Flávio a Lula, 7 de 10; de Lula a Flávio, 8 de 14) e 9 sobre política ou posição. Nos confrontos estruturados, em que cada um tinha uma pergunta e tempo fixo, **as 4 perguntas foram sobre política pública**. Quando o formato deixou livre, os dois levaram o debate para acusação.

A atribuição de quem pergunta foi feita pelo conteúdo e pelo vocativo ("Lula", "o seu pai"), porque a transcrição não tem falante. Pode mudar com a escuta.

## 4. A pergunta de economia ficou cortada

Na pergunta de 08:44, a transcrição pula do fim da formulação (09:11) para a resposta de Lula (09:15), e a resposta dele tem só uns 40 segundos de texto num tempo de 2 minutos. O trecho perdido é o mesmo nas leituras automáticas. A classificação M2a (P e P) foi mantida com o aviso que já existia; ela só muda com a escuta. **Nenhum achado do relatório depende dessa pergunta.**

## 5. Os detalhes de cada proposta, que a primeira rodada não tinha anotado

O pré-registro (§2, A) pedia, para cada compromisso, cinco campos marcados como presentes só quando há palavras na fala: mecanismo, instituição responsável, prazo ou meta, recurso ou custo e condição legal. A primeira rodada não preencheu esses campos. A segunda passada preencheu os 31, com o tempo de cada detalhe, em [`anotacoes/DETALHES_COMPROMISSOS.csv`](anotacoes/DETALHES_COMPROMISSOS.csv); a recontagem está em [`resultados/DETALHES.json`](resultados/DETALHES.json).

| Campo presente na fala | Flávio (18) | Lula (13) |
|---|---:|---:|
| mecanismo de execução | 9 | 9 |
| instituição responsável | 4 | 3 |
| prazo ou meta numérica | 7 | 5 |
| recurso ou custo | 1 | 1 |
| condição legal | 5 | 3 |

**O achado que vale para os dois:** das 31 propostas, **nenhuma veio com o próprio custo**. Só 2 citaram algum valor em dinheiro, uma de cada lado: Flávio, um "espaço no orçamento de mais de 200 bilhões" para ajudar a pagar dívidas (11:06), e Lula, os 725 bilhões **já investidos** na Nova Indústria Brasil (86:20). Nenhuma proposta trouxe os cinco campos; as mais detalhadas foram a do Ministério da Segurança e a do leilão de dívidas, de Lula, com quatro, e três de Flávio com três (leis antifacção, compra de dívidas e câmeras).

**Temas das propostas:** metade das propostas de Flávio é de segurança (9 de 18); as de Lula se espalham por economia (5 de 13), educação (3) e outros temas com uma cada. É contagem de unidades, não de importância.

Esta anotação foi feita **depois** de conhecidos os resultados da primeira rodada, pela regra do pré-registro, sem mudar a regra (emenda em `docs/EMENDAS.md`).

## 6. As durações usadas na seleção C misturavam outros assuntos

A seleção C foi publicada antes da pesquisa externa, e isso continua valendo: ninguém escolheu as quatro ações depois de saber o que as fontes diziam. Mas a regra era "maior tempo apresentando a ação", e alguns intervalos anotados incluíam outras coisas.

| Ação | Tempo anotado | O que entrou junto | Tempo sem o que não é da ação |
|---|---:|---|---:|
| F04, compra de dívidas | 168 s | solidariedade a Dani Marques (73:38–73:50) | ~157 s |
| F05, Ministério da Prosperidade e Caixa | 159 s | Bolsa Família (F15) e o adiamento de imposto (F17), contados duas vezes; conexão à internet e cruzamento com vagas de emprego | ~78 s no recorte estrito; ~105 s contando a parte do programa que ele disse passar pela Caixa |
| L09, leilão de dívidas | 74 s | o bloqueio de celular roubado (99:58–100:10) | ~61 s |
| L03, saída temporária | 71 s | fala cruzada no fim (63:14–63:21) | ~64 s |

**Consequência:** F04 continua a maior de Flávio com folga. A segunda dele depende de como se agrupa o programa da Caixa: no recorte estrito, F05 empata com F10 (câmeras, ~80 s) e F13 (maioridade penal, ~80 s). Do lado de Lula, L03 (~64 s), L09 (~61 s) e L11 (estatais, 58 s) ficam a poucos segundos um do outro, dentro do erro da marcação. **As quatro ações C ficam como uma amostra fixada antes das fontes, e o relatório deixa de dizer que são necessariamente as duas mais longas de cada um.** Os quatro estudos não foram trocados, porque trocar agora seria escolher depois de ver o resultado.

## 7. Fontes externas, conferidas de novo

Neste ambiente os sites do Planalto, do TSE e do Congresso não abriram (bloqueio de rede). As afirmações abaixo foram conferidas em pelo menos duas fontes independentes do ano, listadas em `docs/FONTES.md` (S19 a S29). Os textos oficiais da primeira rodada continuam como fonte primária.

| Ponto | O que se confirmou | O que mudou no relatório |
|---|---|---|
| MP 1.393/2026 | Publicada em 25/set/2026 (Desenrola 3.0); compra por leilão com deságio mínimo de 90%; teto de R$ 15 bilhões de custo para a União; **só dívidas de pessoa física com valor original abaixo de R$ 10 mil e de 720 a 1.645 dias de atraso**; parcelamento ainda depende do Conselho Monetário Nacional; acordos com devedores previstos para fevereiro de 2027 | O limite de R$ 10 mil e de atraso entrou no relatório. O anúncio do governo fala em renegociar até **R$ 150 bilhões** em dívidas (15 bilhões ÷ 10%), metade dos 300 bilhões falados no debate |
| Pix ao devedor | Nenhuma das fontes sobre a MP descreve depósito de dinheiro ao devedor | Mantido: o Pix não consta da medida consultada |
| Desconto ao devedor | O governo diz que o desconto será repassado; o texto fala em desconto de **até** o deságio obtido | A frase "o deságio não vira automaticamente desconto" foi trocada por "o desconto ao devedor é de até o obtido na compra, com condições ainda a definir" |
| MEI | A Fazenda anunciou a inclusão de dívidas bancárias de MEI no Desenrola 3.0 (S05) | Mantido: MEI não equivale a todas as empresas |
| Saída temporária | A Lei 14.843/2024 tirou a visita à família; o Congresso derrubou o veto em 28/mai/2024 (314 a 126 e 52 a 11); restou a saída para estudo no semiaberto. A ADI 7663 está no STF sem julgamento localizado | Acrescentado: o STF ainda pode julgar a ação |
| PEC 18/2025 | Aprovada na CCJ do Senado em 14/out/2026; retirada da pauta do plenário em 15/out; ainda sem votação em plenário na data desta passada | Status atualizado |
| Resolução TSE 23.755/2026 | Altera a Res. 23.610/2019 e inclui o §1º-C no art. 28, que proíbe provedores de IA de ranquear ou recomendar candidaturas, mesmo a pedido do usuário. O texto literal não pôde ser aberto aqui; o conteúdo foi conferido em três fontes independentes | Mantido o limite de `docs/LIMITE_ELEITORAL.md` |

## 8. O que esta passada não resolve

- Escuta humana integral do áudio e conferência de cada citação.
- Diarização conferida turno a turno; por isso não há tempo de fala por tema, só a estimativa por janelas já publicada (39:08 de Flávio, 35:20 de Lula, 19:38 incertos).
- O texto oficial da MP, da LEP e da resolução do TSE abertos diretamente nesta passada.
