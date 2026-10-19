# Emendas ao pré-registro

## 19/out/2026 · qualificação jurídica de L03

- **Antes da pesquisa externa:** `COMPROMISSOS.csv` e a seleção congelada resumiam L03 como "manter saída temporária sob critérios". A regra de inclusão de compromissos futuros não mudou.
- **Depois da pesquisa externa:** a fala em 62:10–63:21 menciona saída para contato familiar. O art. 122 da Lei de Execução Penal, na redação vigente consultada em 19/out, autoriza saída temporária no semiaberto para estudo, com requisitos, mas os incisos de visita familiar e atividades de reintegração foram revogados. Portanto, manter a modalidade educacional e restaurar visitas familiares são ações juridicamente diferentes; a segunda exige mudança legislativa. Ver S06 e S07 em `FONTES.md`.
- **Efeito:** L03 continua selecionada por 71 segundos. O resumo original fica preservado no CSV para manter o registro da primeira codificação; o relatório usa a leitura qualificada. A ordem da seleção já era conhecida quando esta emenda foi escrita.

## 19/out/2026 · cobertura das falas e medidas auxiliares

- O pré-registro previa classificação temática de toda fala atribuível e métricas de confronto com extração de turnos. A primeira execução conseguiu anotar compromissos e componentes explícitos de pergunta, mas **não fechou** uma taxonomia exaustiva de todos os turnos ou uma cronometragem de temas. Por isso o relatório não publica percentuais de tempo por tema nem uma taxa geral de desempenho. O tempo de fala disponível é estimativa por janelas acústicas de 2 segundos e inclui 1.178 segundos incertos; não equivale à soma precisa de cada fala.
- Esta limitação foi identificada **depois** das primeiras codificações e da seleção C. Não altera os critérios A/B/C nem a seleção; restringe o alcance dos resultados publicados. Uma classificação exaustiva exigirá completar e conferir o ledger de turnos, preservando esta versão para comparação.

## 19/out/2026 · tema adicional de segurança

- **Antes:** `SELECAO_C_CONGELADA.md` tratou segurança/justiça como questão comum adicional por presumir que havia ocupado mais tempo combinado de confronto.
- **Correção:** a primeira execução não produziu uma cronometragem exaustiva e conferida por tema. Logo, a condição de **maior tempo** do §2 do pré-registro não foi demonstrada. A seção de segurança do relatório passa a ser **exploratória**, fora da seleção formal C. As quatro ações F04/F05/L09/L03, cuja duração está em intervalos públicos, permanecem selecionadas. A correção foi feita depois de conhecidos os resultados e de consultadas as fontes externas; por isso não se substitui por outro tema escolhido retrospectivamente.


## 19/out/2026 · segunda passada (depois dos resultados da primeira rodada)

Tudo abaixo foi feito **depois** de conhecidos os resultados e as fontes da primeira rodada. Nenhuma regra do pré-registro mudou; o que mudou foi a aplicação. Detalhe, com o antes e o depois: [`AUDITORIA_SEGUNDA_PASSADA.md`](../casos/2026-10-18-band-lula-flavio/AUDITORIA_SEGUNDA_PASSADA.md).

- **C11 de N para D e C12 de N para P**, pela regra já escrita (contestar a premissa é resposta direta; tratar parte do pedido é parcial).
- **Confronto livre ampliado de 8 para 24 núcleos (C13–C28)**, pela mesma regra de unidade. A primeira lista não tinha percorrido o bloco inteiro. Cada núcleo ganhou o campo `Tipo do núcleo` (política, posição ou conduta), marcado pela pergunta, não pela resposta. `contar_oportunidades.py` passou a contar esse tipo por quem perguntou.
- **Detalhes verificáveis de cada compromisso** (§2, A do pré-registro), que a primeira rodada não tinha preenchido: `anotacoes/DETALHES_COMPROMISSOS.csv` e `ferramentas/contar_detalhes.py`.
- **Seleção C mantida como amostra fixada antes das fontes.** As durações anotadas incluíam outros assuntos; sem eles, F04 continua a maior de Flávio, mas a segunda dele e as duas de Lula ficam a poucos segundos de outras ações. O relatório deixa de dizer que são necessariamente as mais longas. As quatro não foram trocadas.
- **Fontes da investigação C atualizadas** com S19–S29: limite de R$ 10 mil e de atraso da MP 1.393, volume anunciado de R$ 150 bilhões, status da PEC 18/2025 em 14 e 15/out e a ADI 7663.

## 19/out/2026 · critérios de conclusão por tema (depois dos resultados)

- **Pedido do autor:** cada achado fecha com uma escolha e o vídeo termina com uma conclusão. O pré-registro (§4) dizia que não haveria soma das dimensões nem vencedor nominal; isso **continua valendo**.
- **O que entrou:** [`CRITERIOS_DE_CONCLUSAO.md`](CRITERIOS_DE_CONCLUSAO.md), com a escala de exequibilidade (já vigente, decisão do Executivo, lei nova, emenda, não demonstrado) e a escolha por tema e por critério, nunca por candidato. Os critérios foram escritos **depois** de conhecidos os resultados; por isso cada escolha traz a fonte e a escala, para ser refeita por quem discordar.
- **Fontes novas:** S30 (LC 97/1999, art. 16-A) e S31 (aprovação da PEC 18/2025 na Câmara).
