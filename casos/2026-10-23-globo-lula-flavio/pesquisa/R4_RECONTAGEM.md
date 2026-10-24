# R4 (recontagem): etiquetas dos checadores no debate da Globo, refeitas do zero

Debate do 2º turno entre Lula (PT) e Flávio Bolsonaro (PL), TV Globo, sexta-feira 23/10/2026. Recontagem feita em 24/10/2026, perto das 15h20 (horário de Brasília).

**Pergunta.** O R4 anterior (`R4_CHECAGENS_E_MOMENTOS.md`) concluiu que, em todos os checadores que usam etiqueta de falso, Flávio teve mais falas marcadas como falsas que Lula. Esta recontagem refaz tudo sem usar aquele arquivo como fonte e responde se a conclusão estava certa.

**Como foi feito.**
- Cada página foi baixada com `curl` (cabeçalho de navegador) e convertida em texto por um script próprio que só tira as tags. As etiquetas foram contadas no texto bruto, por script e conferidas uma a uma. Não foi usado resumo automático.
- O candidato de cada fala saiu da estrutura da própria página: seção "FLÁVIO BOLSONARO (PL)" / "LULA (PT)" no g1, a linha de autoria embaixo de cada aspa na Lupa, "O que Lula disse" / "O que Flávio disse" no Estadão, as seções e o nome no título de cada item no Terra e no UOL. Depois, cada fala foi conferida pelo conteúdo, para pegar fala atribuída ao candidato errado.
- No Aos Fatos, as etiquetas não estão no HTML. Elas vêm de uma API pública que a própria página chama (`/api/escriba/177500de-f763-4f91-894c-981086c9bbe3/`, achada no JavaScript da página). O JSON traz a transcrição, e cada checagem traz o campo `selo` junto do trecho checado.
- "Falsa" aqui é só a etiqueta máxima de cada checador: #FAKE (g1), FALSO (Lupa, Estadão, Terra, UOL) e `falso` (Aos Fatos). INSUSTENTÁVEL, ENGANOSO, EXAGERADO e "não é bem assim" **não** entram como falsa.
- Mesma régua para os dois. Este arquivo não diz quem ganhou o debate nem quem "mentiu mais". Cada checador escolhe quais falas checa, então a contagem mede a seleção dele, não todas as falas do debate.

---

## 1. Resultado em uma tabela

| Checador | Flávio: falas checadas | Flávio: falsas | Lula: falas checadas | Lula: falsas | Bate com o R4 anterior? |
|---|---|---|---|---|---|
| Fato ou Fake (g1) | 30 | **6** #FAKE | 24 falas (25 selos) | **3** #FAKE | ❌ não: o R4 tinha Flávio 29 e 5 #FAKE. A página ganhou uma checagem nova no sábado (24) |
| Agência Lupa | 27 | **6** FALSO | 16 | **2** FALSO | ✅ sim, etiqueta por etiqueta |
| Estadão Verifica | 22 | **5** falso | 22 | **2** falso | ⚠️ em parte: falsas iguais; o total subiu de 21 para 22 nos dois (página atualizada às 14h20 de 24/10) |
| Terra (com Aos Fatos) | 12 | **3** FALSO | 7 | **0** | ✅ sim, etiqueta por etiqueta |
| Aos Fatos | 23 | **8** falso | 23 | **1** falso | 🆕 o R4 não conseguiu ler as etiquetas; agora lidas na API |
| UOL Confere | 19 | **7** FALSO | 13 | **1** FALSO | 🆕 o R4 recebeu 403; agora a página abriu |

**Nos 6 checadores, Flávio tem mais falas marcadas como falsas que Lula.** Isso vale também em proporção das falas checadas e por minuto de fala (§3).

---

## 2. Checador por checador

### 2.1 Fato ou Fake (g1)

URL: https://g1.globo.com/fato-ou-fake/eleicoes/noticia/2026/10/23/veja-o-que-e-fato-ou-fake-nas-falas-de-flavio-bolsonaro-e-lula-no-debate-da-globo-no-2o-turno-das-eleicoes-2026.ghtml
Cabeçalho da página: "23/10/2026 22h15 Atualizado 24/10/2026".

| | Falas | #FATO | #NÃOÉBEMASSIM | #FAKE |
|---|---|---|---|---|
| Flávio | 30 | 12 | 12 | 6 |
| Lula | 24 falas, 25 selos | 15 (uma grafada "#/FATO") | 7 | 3 |

Lula tem 25 selos em 24 falas porque uma fala recebeu dois: *"A declaração de Lula sobre ter acabado com a fome em 2012 #NÃOÉBEMASSIM."* e *"A declaração de Lula sobre 33 milhões de pessoas passando fome ao voltar é #FATO."*

Os 6 #FAKE de Flávio (fala resumida, selo copiado da página):
1. vídeo de Bolsonaro suspirando não era deboche: "A declaração é #FAKE."
2. TCU apontou mais de 11.500 obras paralisadas no atual governo: "A declaração é #FAKE."
3. Lula não atualizou a tabela SUS: "A declaração é #FAKE."
4. governo diz que ladrão de celular não tem que ser preso por "uma cervejinha": "A declaração é #FAKE:"
5. "Eu vou criar a Casa da Mulher Brasileira": "A declaração é #FAKE."
6. **(nova)** relatório da PF diria que não há dinheiro público no filme sobre Bolsonaro: "A declaração é #FAKE. Veja o porque:". O texto da checagem diz: *"A Polícia Federal informou neste sábado (24) que a declaração de Flávio 'não procede'"*. Foi essa checagem, publicada no sábado, que faltou no R4 anterior.

Os 3 #FAKE de Lula:
1. "O Tigrinho foi criado por vocês [governo Jair Bolsonaro] em 2022."
2. "Eles [governo de Jair Bolsonaro] gastaram quase 30% a mais do que nós [no cartão corporativo]."
3. "A economia não crescia acima de 3% desde que eu deixei a Presidência, em 2010."

Atribuição: as 30 falas da seção de Flávio são de Flávio e as 24 da seção de Lula são de Lula, conferidas pelo conteúdo. Nenhuma fala trocada de candidato.

### 2.2 Agência Lupa

URL: https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/
Página: "Atualizado: 24/10/2026 02:28" (`dateModified` 2026-10-24T05:28:56+00:00).

| | Falas | VERDADEIRO | FALTA CONTEXTO | EXAGERADO | INSUSTENTÁVEL | SUBESTIMADO | FALSO |
|---|---|---|---|---|---|---|---|
| Flávio | 27 | 5 | 8 | 5 | 3 | 0 | **6** |
| Lula | 16 | 8 | 3 | 1 | 0 | 2 | **2** |

Cada fala tem uma linha de autoria logo abaixo, e a etiqueta vem em seguida. Exemplo copiado: *"Flávio Bolsonaro (PL), candidato à Presidência, em debate no dia 23 de outubro de 2026 na Globo"* → *"FALSO"*.

FALSO de Flávio (6): barra de chocolate de 120 g para 80 g; o "vídeo real" de Bolsonaro suspirando; "Ele [Lula] é o pai do Tigrinho"; ladrão de celular e "cervejinha"; juro real perto de 20% no Plano Safra; "Eu vou criar a casa da mulher brasileira".
FALSO de Lula (2): economia sem crescer acima de 3% desde 2010; "O 'tigrinho' foi criado por vocês [governo Bolsonaro] em 2022".
A fala da PF sobre o filme recebeu **INSUSTENTÁVEL** na Lupa, não FALSO.

### 2.3 Estadão Verifica

URL: https://www.estadao.com.br/estadao-verifica/debate-tv-globo-checagem-tempo-real-ao-vivo/
`dateModified` 2026-10-24T14:20:09-03:00.

| | Falas | verdadeiro | falta contexto | exagerado | enganoso | impreciso | subestimado | inconclusivo | falso |
|---|---|---|---|---|---|---|---|---|---|
| Flávio | 22 | 4 | 5 | 1 | 4 | 3 | 0 | 0 | **5** |
| Lula | 22 | 8 | 4 | 3 | 2 | 1 | 1 | 1 | **2** |

Formato copiado: *"O que Flávio disse: que Jair Bolsonaro não debochou de pessoas com falta de ar."* → *"O Estadão Verifica checou e concluiu que: é falso."*

Diferença para o R4 anterior: entraram duas checagens depois da contagem dele, uma de cada lado, e nenhuma é falso:
- Flávio: *"que 1 milhão de crianças aguardam vaga em creche"* → "é exagerado".
- Lula: *"que milhões de trabalhadores sofrem acidentes de trabalho"* → "é verdadeiro".

falso de Flávio (5): "pai do tigrinho"; 11,5 mil obras paralisadas; meta de esgoto de 2033 jogada para 2050; Bolsonaro não debochou de quem tinha falta de ar; ladrão de celular e "cervejinha".
falso de Lula (2): "há fotos de Flávio com Daniel Vorcaro"; Jair Bolsonaro é o "pai do tigrinho".

### 2.4 Terra (checagem consolidada, Terra e Aos Fatos)

URL: https://www.terra.com.br/noticias/eleicoes/flavio-x-lula-na-globo-confira-a-checagem-sobre-as-declaracoes-do-ultimo-debate,0c0522294d9719e823d66bf9ef74f6f3v9zi67zf.html
Página: "24 out 2026 - 01h21 (atualizado às 01h36)".

| | Falas | VERDADEIRO | ENGANOSO | FALTA CONTEXTO | NÃO É BEM ASSIM | SUBESTIMADO | FALSO |
|---|---|---|---|---|---|---|---|
| Flávio | 12 | 4 | 3 | 1 | 1 | 0 | **3** |
| Lula | 7 | 3 | 2 | 0 | 1 | 1 | **0** |

FALSO de Flávio, copiado: *"FALSO: Flávio Bolsonaro disse que Jair Bolsonaro não debochou de pessoas com falta de ar"*, *"FALSO: Flávio disse que o governo Lula jogou a meta de 90% de atendimento de esgoto, que era para 2033, para 2050"*, *"FALSO: "Ele é o pai do Tigrinho, ele é o pai do Cassino online, ele criou, ele liberou" - Flávio Bolsonaro"*.

Registro sem juízo: as etiquetas do Terra não coincidem com os selos do Aos Fatos na API (por exemplo, R$ 600 do Bolsa Família: ENGANOSO no Terra, `nao_e_bem_assim` no Aos Fatos), e o texto dos itens do Terra repete a forma de escrever do Estadão ("Flávio disse que o ex-presidente Jair Bolsonaro definiu que todas as concessões de rodovias teriam pedágio zero para motociclistas"). O Terra está contado como fonte separada, como no R4 anterior.

### 2.5 Aos Fatos (lido na API, não no resumo)

URL da matéria: https://www.aosfatos.org/noticias/checamos-flavio-bolsonaro-lula-debate-globo/
URL dos dados: https://www.aosfatos.org/api/escriba/177500de-f763-4f91-894c-981086c9bbe3/ (o componente `EscribaClient` da página busca `/api/escriba/${escribaId}/` a cada 10 segundos).

O JSON tem 311 trechos de transcrição e 60 anotações do tipo `comment`. 46 têm `selo` e texto de checagem; 14 não têm `selo` nem texto (rascunho sem publicação) e ficaram de fora. Os 46 batem com as duas listas da matéria: "Veja o que checamos de Flávio Bolsonaro" (23 itens) e "Veja o que checamos de Lula" (23 itens). O Aos Fatos usa três selos: `verdadeiro`, `falso` e `nao_e_bem_assim`.

| | Falas | verdadeiro | nao_e_bem_assim | falso |
|---|---|---|---|---|
| Flávio | 23 | 5 | 10 | **8** |
| Lula | 23 | 18 | 4 | **1** |

Exemplo copiado do JSON: `"speaker":"Flávio Bolsonaro"`, trecho *"Aquele vídeo dele suspirando e ele fala que estava debochando das pessoas que estavam sem ar. É mentira."*, `"selo": "falso"`.

`falso` de Flávio (8): 11.500 obras paralisadas (TCU); vídeo de Bolsonaro com falta de ar; não fez nada pela dívida das Santas Casas; "pai do Tigrinho"; "troca de tiros" no caso Ana Clara; ladrão de celular e "cervejinha"; "Eu vou criar a Casa da Mulher Brasileira"; relatório da PF sobre o filme.
`falso` de Lula (1): *"Vocês perceberam que a economia não crescia acima de 3% desde que eu deixei a Presidência em 2010?"*

Atribuição: o campo `speaker` só aparece no primeiro trecho de cada vez que alguém fala; nos trechos seguintes vem vazio. Por isso o candidato de cada checagem foi conferido pelo conteúdo e pela lista da matéria. Exemplo: a checagem *"nós herdamos seis mil obras paradas"* (Lula, `verdadeiro`) e a seguinte, *"Nós instalamos mais de 21.300 pontos de internet"* (Flávio, `verdadeiro`), estão em trechos sem `speaker`. Nenhuma checagem com `falso` ficou com o candidato em dúvida.

Observação sem juízo: a fala de Lula sobre as 6 mil obras tem `selo: verdadeiro` no Aos Fatos, embora o texto diga que eram 8.603; na Lupa, no Estadão, no Terra e no UOL ela é SUBESTIMADO.

### 2.6 UOL Confere

URL: https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm
`dateModified` 2026-10-24T17:31:44.000Z. Desta vez a página respondeu 200 com cabeçalho de navegador (no R4 anterior, 403).

| | Falas | VERDADEIRO | ENGANOSO | EXAGERADO | SUBESTIMADO | INSUSTENTÁVEL | FALSO |
|---|---|---|---|---|---|---|---|
| Flávio | 19 | 3 | 8 | 0 | 0 | 1 | **7** |
| Lula | 13 | 7 | 1 | 3 | 1 | 0 | **1** |

A página tem uma seção "FLÁVIO BOLSONARO" e outra "LULA"; cada item começa com a etiqueta em maiúsculas e ponto, por exemplo: *"FALSO. Não é verdade que a Polícia Federal tenha publicado um relatório com as alegações de Flávio."*

FALSO de Flávio (7): 11.500 obras paralisadas; ladrão de celular e "cervejinha"; redução de quantidade dos produtos; vídeo de Bolsonaro com falta de ar; relatório da PF sobre "Dark Horse"; enchentes no RS ("não entregou nem 30%"); Cracolândia.
FALSO de Lula (1): crescimento acima de 3% desde 2010.
A página tem errata: *"A primeira versão deste texto afirmava que o governo de Sergio Massa na Argentina registrou inflação de 211,4% em 2023."* (item de Flávio, que segue VERDADEIRO).

---

## 3. A conta em proporção e por tempo de fala

Os checadores checaram mais falas de Flávio, e Flávio falou mais (O Tempo, §5: 48min02s contra 43min35s). Então a contagem absoluta pode inflar o lado de quem fala mais. A conta abaixo tira esse efeito de duas formas.

| Checador | Flávio: falsas ÷ checadas | Lula: falsas ÷ checadas | Flávio: falsas por 10 min de fala | Lula: falsas por 10 min de fala |
|---|---|---|---|---|
| g1 | 6 ÷ 30 = 20,0% | 3 ÷ 24 = 12,5% | 1,25 | 0,69 |
| Lupa | 6 ÷ 27 = 22,2% | 2 ÷ 16 = 12,5% | 1,25 | 0,46 |
| Estadão | 5 ÷ 22 = 22,7% | 2 ÷ 22 = 9,1% | 1,04 | 0,46 |
| Terra | 3 ÷ 12 = 25,0% | 0 ÷ 7 = 0% | 0,62 | 0 |
| Aos Fatos | 8 ÷ 23 = 34,8% | 1 ÷ 23 = 4,3% | 1,67 | 0,23 |
| UOL | 7 ÷ 19 = 36,8% | 1 ÷ 13 = 7,7% | 1,46 | 0,23 |

Tempo de fala usado: Flávio 48,03 min e Lula 43,58 min (O Tempo). Nas três réguas (número, proporção e tempo), Flávio fica acima nos 6 checadores. Somar os checadores não faz sentido, porque a mesma fala aparece em vários.

---

## 4. Algum placar com Flávio tendo MENOS falsas que Lula?

**Não encontrei nenhum.** Foram 12 buscas, com Revista Oeste, Gazeta do Povo, Jovem Pan, Pleno News, "quem mentiu mais", plataformas com IA e críticas aos checadores. Todos os placares achados e lidos no texto bruto põem Flávio com mais falsas:

| Quem publicou | URL | Método | Números (copiados) |
|---|---|---|---|
| Revista Fórum (linha de esquerda) | https://revistaforum.com.br/politica/placar-checagem-forum-debate-globo/ | checagem própria: 7 agentes de IA sobre a transcrição, todo texto lido por editor antes de publicar | "Das 17 falas de Flávio Bolsonaro checadas e publicadas, 13 foram classificadas como enganosas, 3 como falsas e 1 como verdadeira." / "Das 12 falas de Lula checadas e publicadas, 11 foram confirmadas" (a 12ª: "não é bem assim") |
| Mais Novela | https://www.maisnovela.com.br/tv/quem-mentiu-mais-no-debate-globo.phtml | soma Aos Fatos e Lupa sem repetir fala, contando só "falso" | "Flávio Bolsonaro: 18 falas falsas" / "Lula: 3 falas falsas". ⚠️ Diz que o Aos Fatos checou 26 falas de Flávio e lista como falsas falas que não estão nas 23 checagens do Aos Fatos na API (por exemplo, R$ 7 bilhões em viagens, que é do debate da Band). Número não confiável |
| "quemmentiu?" (via Mais Novela) | não localizada | plataforma de checagem, não oficial | "Para Flávio, foram 127 checagens, com 16 fatos, 57 fakes, 50 imprecisos e 4 sem provas." / "Para Lula, foram 83 checagens, com 63 fatos, 5 fakes, 14 imprecisos e 1 sem provas." |
| checagemaovivo.org (via Mais Novela e Correio da Manhã) | https://checagemaovivo.org/ (hoje só mostra "Muito obrigado por acompanhar"; o placar não está mais no ar) | gerado por IA durante a transmissão | Correio da Manhã: "foram analisadas 63 declarações de Lula e 103 de Bolsonaro [...] Lula, 58 declarações foram classificadas como factuais e cinco como 'não é bem assim'. Já no caso de Bolsonaro, oito foram consideradas factuais, 54 falsas, 37 imprecisas" (https://cmjornal.pt/mundo/detalhe/detetor-de-mentiras-analisa-debate-entre-lula-da-silva-e-flavio-bolsonaro-e-aponta-dezenas-de-declaracoes-falsas) |
| Vermelho (linha de esquerda) | https://vermelho.org.br/2026/10/24/checagens-do-debate-da-globo-confirmam-lula-e-verdadeiro-e-flavio-e-falso/ | resume UOL, Lupa, Aos Fatos e g1 | UOL com "12 declarações do presidente e 18 do senador" (versão anterior da página; hoje são 13 e 19) |
| Rádio Capital FM | https://capitalfmradio.com.br/quem-mentiu-mais-no-debate-da-globo-flavio-teve-mais-declaracoes-falsas-do-que-lula-dizem-agencias/ | resume Lupa, g1, UOL e Estadão | "cinco declarações de Flávio foram classificadas como falsas, contra duas de Lula" (Lupa). ⚠️ A página da Lupa tem 6 FALSO de Flávio; o resumo do Estadão dela ("uma declaração classificada como falsa") cobre só 9 checagens |

Veículos de linha conservadora: a Revista Oeste publicou sobre o debate (avaliação de independentes, estudo qualitativo, "Flávio muda o tom"), mas nenhuma das buscas trouxe placar de checagem dela. Gazeta do Povo: só a matéria anterior ao debate sobre a checagem da Globo. Jovem Pan e Pleno News: nada encontrado. O texto da Oeste "Lula espalha mais fake news contra Flávio" (https://revistaoeste.com/politica/lula-espalha-mais-emfake-news-em-contra-flavio/) é de 11/10/2026 e trata de um ato na Avenida Paulista, não do debate.

Limite: a busca na web vê pouco das últimas 24 horas. Não achar não prova que não exista.

---

## 5. O Tempo: "68 ataques diretos e um pedido de desculpas"

URL: https://www.otempo.com.br/eleicoes/2026/presidentes/2026/10/24/debate-da-globo-entre-flavio-e-lula-tem-68-ataques-diretos-e-um-pedido-de-desculpas-veja-os-dados
Publicada em 24/10/2026, 10h32 (`dateModified` 10:39:36). Autor: Wallace Graciano.

| Medida | Flávio | Lula | Trecho copiado |
|---|---|---|---|
| Ataques diretos | 34 | 34 | "identificamos ao menos 34 intervenções de Flávio e 34 de Lula como ataques diretos" |
| Ataques indiretos | 1 | 1 | "Outras duas falas trazem críticas indiretas, sem imputação direta nova, uma de cada candidato" |
| Sem ataque | 5 no total (não separa por candidato) | | "As cinco restantes foram classificadas como manifestações sem ataque" |
| Palavras | 9.237 (58,6%) | 6.528 (41,4%) | "foram contabilizadas 9.237 palavras nas falas atribuídas a Flávio (58,6% do total) e 6.528 nas de Lula (41,4%), somando 15.765" |
| Tempo de fala | 48min02s | 43min35s | "foram contabilizados 48min02s de fala para Flávio e 43min35s para Lula, uma diferença de 4min27s" |
| Tempo disponível | até 48min30s | até 46min30s | "havia até 46min30s disponíveis para Lula e até 48min30s para Flávio" |
| Direitos de resposta | 11 pedidos: 3 aceitos, 8 negados | 1 pedido, aceito | "Flávio acumulou 11 pedidos, dos quais três foram aceitos e oito rejeitados. Lula apresentou um pedido, que foi concedido." |
| Pedido de desculpas | 1 (de Flávio a Lula) | 0 | "Flávio respondeu: 'te peço desculpa de verdade', formulação repetida duas vezes na mesma intervenção" (depois de Lula reclamar de ser chamado de "nove dedos") |
| Nome do adversário dito | "Lula" 56 vezes | "Flávio" 6 vezes | "Flávio pronunciou a palavra exata 'Lula' 56 vezes, enquanto Lula usou 'Flávio' seis vezes" |
| "Google" | 3 | 10 | "A palavra 'Google' apareceu dez vezes nas falas de Lula e três nas de Flávio" |
| "dívida" | 19 | 14 | "'dívida' foi mencionada 19 vezes por Flávio e 14 por Lula" |
| "SUS" | 12 | 7 | "O termo 'SUS' teve 12 ocorrências no registro do senador e sete no do presidente" |
| Esquivas nas 12 respostas iniciais | 2 | 3 | Lula: saneamento, dívida pública (contrapergunta sobre o Banco Central), saídas temporárias e facções. Flávio: salário mínimo sem os reajustes do PT; ensino integral (propostas só na tréplica) |
| Respostas parciais | 1 (SUS) | 1 (endividamento e preço dos alimentos) | "As respostas parciais ocorreram na discussão sobre SUS [...] e no endividamento" |

Outros números da matéria: 12 pedidos de direito de resposta anunciados por César Tralli, "quatro concedidas e oito negadas"; no bloco livre, "houve 20 intervenções alternadas entre Lula e Flávio, equivalentes a 19 passagens de palavra".

Método, copiado: *"contagem automatizada de palavras e expressões, com separação manual das falas de candidatos e mediação. 'Ataque direto' é uma intervenção com crítica explícita à conduta, honestidade, capacidade ou ações do adversário [...] Os indicadores de ataques são classificação editorial"*. A matéria diz: *"Os resultados não estabelecem um vencedor."* Fonte complementar citada por ela: Agência Lupa.

---

## 6. Conclusão

**O levantamento anterior estava certo na conclusão e parcialmente errado nos números.**

- ✅ **Certo:** em todos os checadores com etiqueta de falso, Flávio tem mais falas marcadas como falsas que Lula. A recontagem confirma isso nos 4 checadores que o R4 tinha lido e em mais 2 que ele não conseguiu ler (Aos Fatos, pela API, e UOL Confere). Também vale em proporção das falas checadas e por minuto de fala.
- ❌ **g1:** Flávio tem hoje 30 falas e **6 #FAKE**, não 29 e 5. A checagem que faltava (o relatório da PF sobre o filme) foi publicada no sábado (24), depois da contagem anterior. Lula segue com 24 falas, 25 selos e 3 #FAKE.
- ⚠️ **Estadão:** as falsas não mudaram (5 e 2), mas o total passou de 21 para **22** nos dois, por duas checagens publicadas depois, nenhuma falsa.
- ✅ **Lupa e Terra:** batem etiqueta por etiqueta.
- 🆕 **Aos Fatos:** Flávio 23 = 8 falso, 10 não é bem assim, 5 verdadeiro; Lula 23 = 1 falso, 4 não é bem assim, 18 verdadeiro.
- 🆕 **UOL Confere:** Flávio 19 = 7 falso, 8 enganoso, 3 verdadeiro, 1 insustentável; Lula 13 = 1 falso, 1 enganoso, 3 exagerado, 1 subestimado, 7 verdadeiro.
- **Fala atribuída ao candidato errado:** nenhuma foi encontrada, nem no R4 anterior nem nas páginas.
- **Placar com Flávio tendo menos falsas que Lula:** não foi encontrado nenhum.

Arquivos baixados e o JSON do Aos Fatos ficaram fora do repositório, na pasta temporária da sessão.
