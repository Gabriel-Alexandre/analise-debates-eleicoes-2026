# R1 a R5 · Regras do debate e reação do mercado

Caso: debate do 2º turno entre Lula (PT) e Flávio Bolsonaro (PL) na TV Globo, 23/out/2026.
Coleta: 24/out/2026, entre ~10h40 e 11h20 (horário de Brasília), por WebSearch, WebFetch e `curl` (texto bruto da página).
Regra de número: só entra número conferido no texto da página (trecho copiado entre aspas). O que não foi conferido está marcado.

---

## 0. Correção de calendário que muda a Tarefa B

O pedido fala em "quinta 23/out" e "sexta 24/out". Pelo calendário, **23/out/2026 é sexta-feira e 24/out/2026 é sábado** (1º/out/2026 caiu numa quinta). Todas as fontes confirmam:

- BPMoney, 19/10: "nesta sexta-feira (23)". https://bpmoney.com.br/politica/debate-2-turno-lula-flavio-bolsonaro-tv-globo-sexta-23/
- Poder360, 24/10: publicado em "24.out.2026 (sábado) - 1h49", debate exibido na "6ª feira (23.out.2026)". https://www.poder360.com.br/poder-eleicoes-2026/debate-de-lula-e-flavio-na-globo-chega-a-30-pontos-de-audiencia/

Consequências para o relatório:

1. O debate começou às 21h20 de sexta, **depois do fechamento da B3**. O pregão de 23/out é **anterior** ao debate.
2. **Não há pregão em 24/out (sábado)** e o 2º turno é domingo, 25/out. O próximo pregão é segunda, 26/out, e ele vai misturar o debate com o **resultado da eleição**. Não existe, antes da eleição, um preço de Ibovespa, dólar à vista ou DI formado depois do debate.
3. O BCB não publica PTAX em 24/out (consulta à API retornou lista vazia, ver §B4).

Portanto: **nenhuma variação de mercado medida até hoje pode ser atribuída ao debate.** O que existe é o pregão da véspera do debate, com analistas dizendo que o mercado *esperava* o debate.

---

## A. Regras e formato do debate

Fonte primária usada: **transcrição integral publicada pelo Poder360** (PDF, 32 páginas no rodapé, 8 páginas no arquivo).
URL: https://static.poder360.com.br/uploads/2026/10/transcricao-debate-Lula-Flavio-Bolsonaro-Globo-23out2026.pdf
SHA-256 do arquivo baixado em 24/10 ~11h14: `39eaa874fa2a0e4126f86892eca5b303a4201965ed23b0b872daf13d361200a6`
Página de apresentação: https://www.poder360.com.br/poder-eleicoes-2026/leia-a-integra-do-ultimo-debate-entre-lula-e-flavio-na-globo/

Os sites do grupo Globo (g1, oglobo, valor.globo.com) estão bloqueados para a ferramenta de busca e de leitura desta coleta ("domains are not accessible to our user agent"). As regras foram conferidas na **fala do mediador lida na transcrição** e na imprensa que reproduziu o regulamento.

### A1. Ficha

| Item | Valor | Trecho conferido | Fonte |
|---|---|---|---|
| Data | sexta, 23/out/2026 | "nesta sexta-feira (23)" | Folhapress via Jornal de Brasília (22/10, 17h36) https://jornaldebrasilia.com.br/noticias/politica-e-poder/debate-da-globo-entre-lula-e-flavio-tera-quatro-blocos-e-restricao-a-movimentacao-veja-regras/ |
| Início programado | 21h20 | "o programa tem início marcado para as 21h20, assim que terminar o Jornal Nacional" | BPMoney (19/10) https://bpmoney.com.br/politica/debate-2-turno-lula-flavio-bolsonaro-tv-globo-sexta-23/ · Brasil de Fato (23/10, 21h29): "às 21h20" https://www.brasildefato.com.br/2026/10/23/debate-da-globo-lula-e-flavio-bolsonaro-se-enfrentam-pela-ultima-vez-antes-do-segundo-turno/ |
| Horário do 4º bloco | 23h25 | Tralli, na volta do 3º intervalo: "Onze horas mais 25 minutos, hora de Brasília. Estamos de volta ao vivo [...] com o 4º e último bloco" | transcrição Poder360, p. 25 |
| Término | **não informado diretamente** | indícios: Ibope mediu o programa "das 21h39 às 23h49" (Poder360); última entrada do ao vivo do Poder360 às 23h50 (metadado `datePublished` "2026-10-23T23:50:00-03:00") | https://www.poder360.com.br/poder-eleicoes-2026/debate-de-lula-e-flavio-na-globo-chega-a-30-pontos-de-audiencia/ · https://www.poder360.com.br/ao-vivo/acompanhe-em-tempo-real-o-debate-da-tv-globo/ |
| Duração | "quase duas horas" | "quase duas horas" | O Tempo (24/10, Wallace Graciano) https://www.otempo.com.br/eleicoes/2026/presidentes/2026/10/24/debate-da-globo-entre-flavio-e-lula-tem-68-ataques-diretos-e-um-pedido-de-desculpas-veja-os-dados |
| Local | Estúdios Globo, Rio de Janeiro | Tralli: "Bem-vindos aos Estúdios Globo"; imprensa: "nos Estúdios Globo, no Rio de Janeiro (RJ)" | transcrição p. 1 · Brasil de Fato (link acima) |
| Mediador | César Tralli | "mediação do jornalista César Tralli" | Brasil de Fato · BPMoney |
| Transmissão | Globo, GloboNews, g1, Globoplay | Tralli: "ao vivo aqui na Globo, na GloboNews, no G1 e no Globoplay" | transcrição p. 1 |
| Plateia | de convidados, com pedido de silêncio | "A plateia pode aproveitar esse momento para dar boas-vindas"; no fim: "à plateia de convidados" | transcrição p. 1 e p. 32 |
| Checagem ao vivo na TV | não; checagem no g1 (Fato ou Fake) e por Lupa/Folha, Aos Fatos, UOL Confere, Estadão Verifica, Comprova | Tralli cita os serviços; Brasil de Fato: "não terá verificação em tempo real" | transcrição p. 1 e 2 · Brasil de Fato |

### A2. Blocos, temas e tempos (fala de Tralli, transcrição p. 1)

| Trecho literal | O que estabelece |
|---|---|
| "O debate tem quatro blocos. Os três primeiros são de temas determinados, o quarto de tema livre e com as considerações finais." | 4 blocos; 3 temáticos, 1 livre + considerações finais |
| "No primeiro bloco, estarão em debate planos para cinco regiões do Brasil: Sul, Sudeste, Centro-Oeste, Norte e Nordeste. O sexto tema, neste primeiro bloco, é estratégico: Que projetos os candidatos têm no setor de infraestrutura para aumentar as exportações brasileiras?" | Bloco 1: 6 rodadas (5 regiões + infraestrutura e exportação), **sorteadas** ao vivo |
| "O segundo bloco e o terceiro têm dez questões fundamentais [...] os candidatos vão escolher seis desses temas, três no segundo bloco e três no terceiro bloco." | Blocos 2 e 3: 10 temas no telão, **escolhidos pelo candidato**, cada tema uma vez só |
| "endividamento dos brasileiros, ensino integral, dívida pública, inteligência artificial, meio ambiente, políticas sociais, reformas, relações com Estados Unidos e China, retomada de territórios e Sistema Único de Saúde" | a lista dos 10 temas |
| "vai haver um banco de tempo em cada rodada. Nos três primeiros blocos, o candidato tem um total de três minutos para a pergunta e a réplica, e o adversário terá a mesma quantidade de tempo, três minutos para a resposta e a tréplica." | **Banco de tempo por rodada**: 3 min (pergunta + réplica) e 3 min (resposta + tréplica) |
| "quem expõe sua proposta pode andar livremente pelo cenário, e nessa hora o outro candidato deve aguardar no púlpito" | regra de movimentação nos blocos 1 a 3 (pedida pela campanha de Lula, segundo a Folhapress) |
| "No quarto e último bloco de tema livre, cada candidato terá oito minutos para usar o banco de tempo como quiser e quantas vezes quiser, até o cronômetro zerar. [...] sem invadir o espaço do outro." | Bloco 4: banco de **8 min** por candidato, sem limite de intervenções |
| "o senhor tem 1 minuto e meio para a sua mensagem de despedida ao eleitor" (p. 30) e "o senhor tem 1 minuto e meio para se despedir do eleitor" (p. 31) | Considerações finais: **1min30s** cada; ordem "definida em sorteio prévio, feito na presença de assessores dos candidatos"; Lula primeiro |

Conta de controle: 12 rodadas temáticas × 3 min = 36 min por candidato, mais 8 min do bloco livre. O Tempo publicou o mesmo: "cada candidato tinha até 36 minutos distribuídos pelas 12 rodadas temáticas" (link acima).

### A3. O que foi sorteado e escolhido (transcrição)

| Bloco | Rodada | Quem pergunta | Tema | Como foi definido | Trecho |
|---|---|---|---|---|---|
| 1 | 1 | Flávio | infraestrutura e exportação | sorteio | "quem abre o debate é o candidato Flávio Bolsonaro, do PL" · "E o tema é infraestrutura e exportação" |
| 1 | 2 | Lula | Sudeste | sorteio | "Região Sudeste." |
| 1 | 3 | Flávio | Centro-Oeste | sorteio | "A região é Centro-Oeste." |
| 1 | 4 | Lula | Sul | sorteio | "região Sul, por favor." |
| 1 | 5 | Flávio | Norte | sorteio | "Região Norte, por favor." |
| 1 | 6 | Lula | Nordeste | último na urna | "Temos um único tema agora aqui na nossa urna: é a região do país Nordeste." |
| 2 | 1 | Lula (abre por sorteio) | políticas sociais | escolha | "O meu tema é políticas sociais." |
| 2 | 2 | Flávio | dívida pública | escolha | Tralli: "Dívida pública." |
| 2 | 3 | Lula | Sistema Único de Saúde | escolha | "Sistema Único de Saúde." |
| 3 | 1 | Flávio (abre por ter terminado o bloco 2 respondendo) | endividamento dos brasileiros | escolha | "Eu escolho 'endividamento dos brasileiros'." |
| 3 | 2 | Lula | ensino integral (Lula disse "Educação"; o mediador pediu o tema do telão) | escolha | "o tema que está no telão, candidato, é ensino integral" |
| 3 | 3 | Flávio | retomada de territórios | escolha | "Retomada de territórios." |
| 4 | livre | Lula abre por sorteio | tema livre | sorteio da ordem | "O candidato que abre o bloco é o candidato Luiz Inácio Lula da Silva" |

Temas do telão **não escolhidos**: meio ambiente, reformas, relações com Estados Unidos e China, inteligência artificial.

⚠️ **Divergência:** antes do debate, Observatório da TV/O Tempo e Brasil de Fato escreveram que "Por sorteio, Lula abre o debate" (https://www.otempo.com.br/entretenimento/2026/10/23/saiba-tudo-sobre-o-debate-da-globo-entre-lula-e-flavio-bolsonaro). Na transcrição, o sorteio ao vivo do 1º bloco deu **Flávio** ("quem abre o debate é o candidato Flávio Bolsonaro"), e a Agenda do Poder (23/10, 22h29) também registra que "Flávio começou questionando". A ordem que Lula de fato abriu foi a das **considerações finais** e a dos blocos 2 e 4. Vale a transcrição.

⚠️ **Divergência:** a página do Poder360 diz que os candidatos "tiveram 1 minuto cada para as considerações finais"; a fala do mediador na transcrição do próprio Poder360 diz "1 minuto e meio", e O Tempo diz 1min30s. Vale a transcrição.

### A4. Direito de resposta

Regra (Tralli, transcrição p. 1): "Se um candidato fizer ofensas pessoais a outro, o candidato ofendido poderá pedir direito de resposta. Para isso, deverá levantar a mão em silêncio. A nossa produção vai avaliar se o direito de resposta será ou não concedido." Tempo concedido: "O senhor tem um minuto" (p. 15), "1 minuto para se defender" (p. 25 e p. 31).

Pedidos e decisões, contados nas falas do mediador:

| Momento | Quem pediu | Decisão | Trecho |
|---|---|---|---|
| intervalo 1→2 e bloco 2 | Lula (1) e Flávio (1) | **2 concedidos** | "Durante o intervalo, o candidato Lula pediu um direito de resposta por se sentir ofendido" · "os dois candidatos pediram direito de resposta. Os direitos de resposta foram concedidos." |
| fim do bloco 2 | Flávio (1) | negado | "O senhor pediu um direito de resposta; o pedido foi negado." |
| bloco 3 | Flávio (3) | 2 negados, 1 concedido (exercido no início do bloco 4) | "o pedido foi negado" · "foi negado" · "pediu 3 direitos de resposta. Um deles foi concedido em relação ao 3º pedido" |
| bloco 4 (livre) | Flávio (5) | 5 negados | "o senhor pediu 5 direitos de resposta; os 5 foram negados" |
| depois das considerações de Lula | Flávio (1) | concedido | "o senhor pediu um direito de resposta. O senhor tem 1 minuto para se defender" |

**Total: 12 pedidos, 4 concedidos, 8 negados.** Flávio: 11 pedidos, 3 concedidos, 8 negados. Lula: 1 pedido, 1 concedido.
Conferência independente: O Tempo (24/10) publicou o mesmo total, "12 solicitações de direito de resposta: quatro concedidas e oito negadas", "Flávio acumulou 11 pedidos, dos quais três foram aceitos e oito rejeitados", "Lula apresentou um pedido, que foi concedido" (link em A1).

Outros dados do mesmo levantamento de O Tempo (metodologia editorial deles, não reconferida aqui): tempo de fala Flávio 48min02s, Lula 43min35s; "12 rodadas temáticas e 19 trocas de palavra no bloco livre".

### A5. Audiência (prévia Ibope, para contexto)

| Praça | Média | Pico | Trecho | Fonte |
|---|---|---|---|---|
| Grande São Paulo | 25 pontos | 28 | "média de 25 pontos de audiência, das 21h39 às 23h49, com pico de 28 pontos" | Poder360 (24/10, 1h49) link em A1 |
| PNT (15 metrópoles) | 28 pontos | 30 | "o encontro marcou média de 28 pontos, com pico de 30 pontos" | idem |

---

## B. Mercado

### B1. Fechamentos: quinta 22/out (base) e sexta 23/out (último pregão antes do 2º turno, **antes do debate**)

**Ibovespa**

| Dia | Pontos | Variação | Trecho | Fonte |
|---|---|---|---|---|
| qui 22/10 | 204.120,12 | −1,15% | "O Ibovespa fechou em queda de 1,15%, aos 204.120,12 pontos e com giro financeiro de R$ 25,8 bilhões" | GMC Online (22/10, 17h52) https://gmconline.com.br/economia/ibovespa-cai-com-aversao-a-risco-global-e-cautela-pre-segundo-turno/ |
| sex 23/10 | 205.082,56 | +0,47% | "o Ibovespa subiu 0,47%, aos 205.082,56 pontos, com giro financeiro de R$ 30,7 bilhões. Na semana [...] cedeu 0,17%, mas acumula avanço de 10,06% em outubro e de 27,28% em 2026" | Estadão/Broadcast via Jornal de Brasília (23/10, 18h30) https://jornaldebrasilia.com.br/noticias/economia/dolar-fura-r-500-com-aposta-em-vitoria-de-flavio-e-recua-158-na-semana/ |
| sex 23/10 | 205.082,56 | +0,47% | "avançou 0,47%, aos 205.082,56 pontos"; "oscilou entre a mínima de 203.428 pontos e a máxima de 205.757,04 pontos" | CNN Brasil, com Reuters https://www.cnnbrasil.com.br/economia/money/mercado/mercado-financeiro-ibovespa-dolar-23-outubro-2026/ |

Conta de controle: 204.120,12 × 1,0047 = 205.079, coerente com 205.082,56.
⚠️ Divergências entre fontes: semana **−0,17%** (Broadcast e Reuters/Forbes) contra "+0,12%" (CNN Brasil, provável erro); giro **R$ 30,7 bi** (Broadcast) contra R$ 45,52 bi e R$ 40,83 bi no mesmo texto da Reuters/Forbes https://forbes.com.br/forbes-money/2026/10/ibovespa-fecha-em-alta-e-dolar-cai-a-espera-de-desfecho-da-eleicao/

**Dólar à vista**

| Dia | R$ | Variação | Trecho | Fonte |
|---|---|---|---|---|
| qui 22/10 | 5,0394 | +0,23% | "o dólar à vista terminou o dia a R$ 5,0394, avanço de 0,23%" | GMC Online (22/10, 17h41) https://gmconline.com.br/economia/fechamento-cambio-dolar-tem-leve-alta-com-aversao-global-a-risco-e-tensao-eleitoral/ |
| sex 23/10 | **4,9931** | **−0,92%** | "o dólar à vista terminou o pregão em queda de 0,92%, a R$ 4,9931 [...] menor valor de fechamento desde o dia 9 (R$ 4,9851)"; semana "perdas de 1,58%" | Estadão/Broadcast via Jornal de Brasília (link acima) |
| sex 23/10 | 4,9896 | −0,97% | "A moeda norte-americana à vista fechou em baixa de 0,97%, cotado a R$ 4,9896"; semana "recuo de 1,64%"; ano "9,10%" | CNN Brasil com Reuters (link acima) |

Conta de controle: 5,0394 × (1 − 0,0092) = 4,9930, coerente com o Broadcast. A Reuters usa outra referência de fechamento; as duas séries não se misturam no relatório.

**Juros futuros (DI), fechamento de sexta 23/10**

| Vértice | 23/10 | Ajuste anterior | Variação | Trecho | Fonte |
|---|---|---|---|---|---|
| jan/27 | 13,475% | 13,496% | −2,1 bp | "o DI para janeiro de 2027 marcava 13,475% (de 13,496% no ajuste anterior)" | BDM Bom Dia Mercado (23/10, 18h23) https://www.bomdiamercado.com.br/mercado-financeiro/juros/juros-futuros-queimam-premios-na-reta-final-do-2o-turno-com-mercado-dobrando-a-aposta-em-flavio/ |
| jan/28 | 12,825% | 12,883% | −5,8 bp | "Jan/28 a 12,825% (12,883%)" | BDM |
| jan/29 | 12,595% | 12,664% | −6,9 bp | "Jan/29 a 12,595% (12,664%)" | BDM |
| jan/31 | 12,575% | 12,665% | −9,0 bp | "Jan/31 a 12,575% (12,665%)" | BDM |
| jan/33 | 12,650% | 12,749% | −9,9 bp | "Jan/33 a 12,650% (12,749%)" | BDM |
| jan/28 (Reuters) | 12,86% | 12,886% | −3 bp | "O vencimento para janeiro de 2028 caiu a 12,86%, três pontos-base abaixo do ajuste anterior, de 12,886%" | SpaceMoney, citando Reuters https://www.spacemoney.com.br/economia/macroeconomia/juros-futuros-recuam-antes-segundo-turno-eleicao |
| jan/35 (Reuters) | 12,735% | 12,762% | −2,7 bp | "o contrato para janeiro de 2035 recuou a 12,735%, contra 12,762% da véspera" | SpaceMoney/Reuters |

Intradia: "O DI para janeiro de 2035 marcou máxima de 12,865%, com avanço de dez pontos-base, às 10h31, pressionado pelo Datafolha e pelo movimento dos juros americanos" (SpaceMoney/Reuters).
⚠️ BDM e Reuters registram horários de fechamento diferentes para jan/28 (12,825% contra 12,86%). A CNN Brasil publicou jan/28 a 12,90% e jan/35 a 12,80% numa leitura **intradia** ("estava em"), não usar como fechamento.

Base de quinta 22/10 (fechamento): "a taxa do contrato de Depósito Interfinanceiro (DI) para janeiro de 2027 subiu de 13,479%, no ajuste da véspera, a 13,501%. O DI para janeiro de 2029 aumentou a 12,710%, vindo de 12,563% no ajuste, e o DI para janeiro de 2031 anotou alta de 12,602% a 12,720%." GMC Online, texto que cita o Broadcast (22/10, 18h11) https://gmconline.com.br/economia/taxas-de-juros-encerram-em-alta-com-cautela-antes-do-2o-turno-e-escalada-do-petroleo/

### B2. Dado mais recente depois do debate

| Ativo | Dado pós-debate | Por quê |
|---|---|---|
| Ibovespa | **não existe** | sem pregão no sábado 24/10; próximo pregão é 26/10, depois da eleição |
| Dólar à vista | **não existe** | idem |
| DI | **não existe** | idem |
| PTAX | **não existe** | API do BCB sem cotação em 24/10 (§B4) |

O debate começou às 21h20 de sexta, quando o pregão já havia fechado. O efeito do debate sobre preço **não pode ser medido separado do resultado do 2º turno**, porque o primeiro pregão posterior a ambos é o mesmo (26/10).

### B3. O que a imprensa de mercado atribuiu ao debate (pregão de 23/10, antes dele)

Nenhuma das matérias de fechamento atribui movimento ao debate; todas o tratam como **evento ainda por vir**.

| Quem | Casa | Trecho | Fonte |
|---|---|---|---|
| Vitor Kayo | Nomad (economista sênior) | "O pano de fundo continua prudente, com o mercado esperando o debate e as últimas pesquisas" | Reuters via Forbes (link em B1) |
| Redação Reuters | — | o debate "também deve ocupar as atenções" | Reuters via Forbes |
| André Galhardo | Análise Econômica (economista-chefe) | "aparentemente o mercado está dando maior peso a pesquisas internas que mostram uma vitória da oposição no domingo"; texto: "Investidores também aguardam o debate entre os candidatos, à noite, na TV Globo" | Estadão/Broadcast via Jornal de Brasília |
| Redação BDM | Bom Dia Mercado | "o debate da Globo esta noite ganha peso decisivo na reta final, podendo consolidar a recuperação de Lula ou devolver fôlego à vantagem de Flávio" | BDM (link em B1) |

O que essas mesmas matérias atribuem ao movimento de 23/10 (todas antes do debate):

| Fator citado | Trecho | Fonte |
|---|---|---|
| Posicionamento para vitória de Flávio | "o mercado financeiro seguiu majoritariamente posicionado para a vitória do senador Flávio Bolsonaro (PL) [...] conforme a Reuters" | SpaceMoney/Reuters |
| Fluxo e desmonte de proteção cambial | "Operadores relatam a possibilidade de entrada de fluxo estrangeiro para ativos locais e desmontagem parcial de 'hedge cambial' no último pregão antes da realização do segundo turno" | Broadcast via Jornal de Brasília |
| Marcos Weigt, Travelex Bank | "É natural que as pessoas se posicionem na reta final para um cenário mais provável" · "Pode cair um pouco com a vitória do Flávio e subir muito se o Lula ganhar." | Broadcast via Jornal de Brasília |
| Felipe Sant'Anna, grupo Axia | operadores estavam "montando posição final acreditando na vitória do Flávio, em um movimento coordenado pela ideia de que ninguém quer ficar de fora" | Broadcast via Jornal de Brasília |
| Rafael Stephano, Blue3 Investimentos | "Todos os setores em alta, mas os mais fortes são setor imobiliário e setor de consumo" | Broadcast via Jornal de Brasília |
| Álvaro Vivanco, Wells Fargo | cenário-base de vitória de Flávio, "apenas 33% de chance de reeleição de Lula"; alvo R$ 4,75 com Flávio e R$ 5,30 com Lula | Broadcast via Jornal de Brasília |
| Mário Lima, Medley Advisors | Flávio "segue como favorito por diferença apertada", mas Lula "reduziu a desvantagem a um empate estatístico" (relatório citado pela Reuters) | SpaceMoney/Reuters |
| Termômetro Broadcast Bolsa | "66,67% dos participantes esperam alta do índice na próxima semana, após o segundo turno, contra 50% na pesquisa anterior" | Broadcast via Jornal de Brasília |

**Outros fatos do dia citados pelas matérias** (o relatório precisa dizer que a variação de 23/10 não separa nenhum deles, e que o debate nem havia acontecido):

| Fator | Trecho | Fonte |
|---|---|---|
| Datafolha (quinta à noite) | "Lula e Flávio Bolsonaro empatados com 50% dos votos válidos [...] Na semana anterior, o senador aparecia com 51%"; totais "47% para o senador, 46% para o atual mandatário" | SpaceMoney/Reuters |
| Ipespe/Abrapel (sexta de manhã) | "o senador numericamente à frente tanto em votos totais (48% contra 47%) quanto em votos válidos (50,5% contra 49,5%)" | Broadcast via Jornal de Brasília |
| Vox Brasil | "aponta Lula com 50,6% das intenções de voto e o senador aparece com 49,4%" | Broadcast via Jornal de Brasília |
| IPCA-15 de outubro | "avançou 0,32% [...] após alta de 0,70% em setembro. O resultado ficou abaixo da projeção do mercado, que apontava 0,43%"; 12 meses "4,62%" (o BDM cita expectativa de "+0,44%") | SpaceMoney/Reuters · BDM |
| Selic | "A taxa básica está atualmente em 13,75% ao ano"; Flavio Serrano (Bmg) espera "corte de 25 pontos-base na Selic no início de novembro" | SpaceMoney/Reuters |
| Treasuries | "o papel de dez anos [...] avançava quatro pontos-base, a 4,995%" (por volta das 16h34) | SpaceMoney/Reuters |
| Dólar no exterior | "Por volta das 17h, o índice DXY avançava 0,19%, aos 101,799 pontos", após "dados acima das expectativas nos Estados Unidos" | Broadcast via Jornal de Brasília |
| Petróleo | "O contrato do Brent para dezembro encerrou em alta de 3,13%, a US$ 116,72 o barril, no maior nível desde abril" (a Reuters/Forbes escreve "US$3,55 ou 3,14%") | Broadcast via Jornal de Brasília · Reuters via Forbes |
| Oriente Médio | Andrew Lipow (Lipow Oil Associates): "O mercado está preocupado com esses ataques iranianos contínuos a petroleiros" | Reuters via Forbes |
| Bolsa americana | "O S&P 500 caiu 0,52%" (resumo do WebFetch, trecho literal não conferido) | Reuters via Forbes |
| Minério e blue chips | "Petrobras e Vale subiram, seguindo os ganhos de 3% do petróleo Brent e de 0,6% do minério de ferro em Dalian" | Broadcast via Jornal de Brasília |
| Balanço do Bradesco | "operadores absorveram a frustração com o balanço do terceiro trimestre de 2026" | Broadcast via Jornal de Brasília |
| Fed | **não citado** em nenhuma matéria de fechamento lida | — |

Precedente útil (debate da Band, 18/10): uma nota da corretora **EBC Financial Group** (não é a Empresa Brasil de Comunicação) registrou que, na segunda 19/10, "Quem mexeu com o mercado nesta segunda (19) foram as pesquisas divulgadas pela manhã, não o confronto na Band", e que as pesquisas daquela manhã "tiveram campo encerrado em 18 de outubro, o mesmo dia do debate". https://www.ebc.com/pt/forex/debate-lula-flavio-ibovespa-dolar-juros-pesquisas

Notas de XP, BTG, Valor, Bloomberg Línea e Exame sobre o debate da Globo: **não encontradas** nesta coleta (o Valor está no domínio globo.com, bloqueado para a ferramenta).

### B4. PTAX (Banco Central)

Consulta direta à API Olinda do BCB em 24/10, ~11h15:
`https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='MM-DD-AAAA'&$format=json`

| Data | Compra | Venda | Hora do boletim | Resposta bruta |
|---|---|---|---|---|
| qui 22/10 | 5,0377 | 5,0383 | 13h12 | `"cotacaoCompra":5.03770,"cotacaoVenda":5.03830,"dataHoraCotacao":"2026-10-22 13:12:09.300403"` |
| sex 23/10 | 5,0371 | 5,0377 | 13h07 | `"cotacaoCompra":5.03710,"cotacaoVenda":5.03770,"dataHoraCotacao":"2026-10-23 13:07:14.754567"` |
| sáb 24/10 | — | — | — | `"value":[]` |

Série SGS 1 (dólar venda PTAX) confere: 22/10 "5.0383", 23/10 "5.0377". https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=20/10/2026&dataFinal=24/10/2026
Observação: a PTAX de 23/10 fecha às 13h, antes da queda do dólar à vista na tarde ("se firmou em baixa nas duas últimas horas do pregão", Broadcast). Por isso PTAX (5,0377) e fechamento (4,9931) diferem.

---

## C. O que ficou faltando

1. **Regulamento oficial da Globo e a página do g1**: domínio globo.com bloqueado para a ferramenta; as regras vieram da fala do mediador (transcrição Poder360) e da Folhapress. Não conferido: se o regulamento tinha regra escrita sobre tempo de direito de resposta além do "um minuto" dito ao vivo.
2. **Horário exato de término**: não publicado por nenhuma fonte lida; só indícios (Ibope 21h39 a 23h49; último post do ao vivo do Poder360 às 23h50). O início **efetivo** também não está confirmado: programado para 21h20, mas a janela do Ibope começa às 21h39.
3. **Qualquer preço depois do debate**: não existe antes de 26/10 (sábado sem pregão, PTAX sem cotação). O pregão de 26/10 vai misturar debate e resultado da eleição.
4. **Notas de XP, BTG, Valor, Bloomberg Línea, Exame, Folha** sobre o debate: não encontradas.
5. **Fechamento oficial da B3 (ajustes do DI1)**: não consultado; os vértices são os da imprensa (BDM e Reuters), que divergem no jan/28.
6. "S&P 500 caiu 0,52%": veio do resumo do WebFetch da matéria Reuters/Forbes, trecho literal **não conferido**.
7. Dados de O Tempo (tempo de fala, contagem de ataques): metodologia editorial deles, não reconferida na transcrição.
