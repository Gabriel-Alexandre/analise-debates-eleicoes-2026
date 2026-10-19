# Como reproduzir o primeiro caso

Na raiz do repositório, com Python 3.11 ou superior:

```powershell
python ferramentas/selecionar_propostas.py casos/2026-10-18-band-lula-flavio/anotacoes/COMPROMISSOS.csv casos/2026-10-18-band-lula-flavio/resultados/SELECAO_C.json
python ferramentas/contar_oportunidades.py casos/2026-10-18-band-lula-flavio/anotacoes/OPORTUNIDADES.md casos/2026-10-18-band-lula-flavio/resultados/RESPOSTAS.json
python ferramentas/validar_caso.py casos/2026-10-18-band-lula-flavio
```

Os dois scripts recontam **anotações humanas/IA já feitas**. Eles não validam automaticamente se uma fala foi transcrita ou interpretada corretamente. A seleção C foi calculada e versionada antes da pesquisa de fontes; os arquivos atuais são os da primeira rodada.

O cálculo acústico de tempo exige `dados-locais/falantes-janelas.json`. Ele foi gerado de áudio/quadros do MP4 recebido por `ferramentas/planos.py` e `ferramentas/diarizar.py`; `resemblyzer`, `opencv-python`, `numpy`, `soundfile` e `ffmpeg` são dependências locais dessa etapa. A fonte, o WAV, os quadros e as janelas de falante permanecem fora do Git público, por direitos de terceiros e tamanho. Quem possuir licitamente o mesmo arquivo pode conferir o [SHA-256](ORIGEM.md), executar o pipeline e comparar totais. Sem o MP4 exato, o relatório e os dados públicos permitem conferir as contas de compromisso e oportunidade, **não** refazer a escuta ou a diarização.

O pré-registro explica o critério; `docs/EMENDAS.md` preserva o que foi ajustado após observar resultados. `docs/FONTES.md` relaciona documentos externos e suas datas. A revisão adversarial adicional solicitada por Gabriel foi reservada para outra interação.
