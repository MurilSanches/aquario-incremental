# Backlog v1: Aquário Incremental (da brief ao lançamento)

Origem: game brief (`_bmad-output/planning-artifacts/briefs/brief-aquario-incremental-2026-10-09/brief.md` + `addendum.md`) e brainstorming (`_bmad-output/brainstorming-session-2026-10-09.md`; `#NNN` = número da ideia de lá). Este arquivo é a **fila ativa**. Conteúdo (tanques e espécies com nomes): `game/docs/conteudo-tanques.md`. Dados da economia: `_bmad-output/dados/` (`species.csv`, `tanks.csv`, `sim_economia.py`).

Regras do projeto (valem para tudo):
- Sem derrota, sem sorteio, sem eventos aleatórios; renda só vem dos peixes; alimentar é só visual.
- Lógica nova em Core (sem dependência de Unity) com `*Tests.cs`.
- Texto novo = chave `Loc` em **todos os idiomas ativos** (seção 10); nenhum literal de texto em código/UI.
- Conteúdo é dado: espécies e tanques vêm do CSV → ScriptableObject; criar tanque/espécie não exige código.
- CSV só ganha coluna no fim; asset existente não é sobrescrito sem aviso.
- Economia: a mesma fórmula roda online, offline e no simulador (#006).
- **Calibração só no fim** (item E-05). Antes, número só muda se for bug. Toda mudança de número de balanceamento = 1 run do bot + comparação de tempo por tanque com a anterior.
- Itens **DECIDIR** esperam resposta do dev (seção 11); não construir antes.

Legenda: `[x]` feito, `[~]` parcial, `[ ]` a fazer. Tamanho S/M/L = hipótese. Fase: **P1** protótipo passo 1 (um tanque), **P2** protótipo passo 2 (sala + prestígio), **JOGO** versão completa, **LANÇ** lançamento Steam, **PÓS** adiado.

---

## 1. Configuração do projeto (passo a passo; fazer primeiro) [P1]

- [x] **C-01 Instalar Unity Hub e a versão do Editor** (verificado 2026-10-09: Editor 6000.6.2f1 com Windows Mono + IL2CPP; falta só conferir se 6000.6 é LTS, ver D-01) [S, dev]: instalar a versão LTS escolhida em D-01, com módulos *Windows Build Support (IL2CPP)* e *Documentation*. Registrar a versão em `game/docs/estado/01-fundacao.md`. Critério: o Editor abre.
- [x] **C-02 Criar o projeto 2D** (2026-10-09: Universal 2D, URP 17.6.0, em `game/`; aberto pelo Hub pelo dev) [S]: template *Universal 2D* (URP 2D) em `game/` (ou Built-in 2D conforme D-02). Critério: cena vazia roda no Play sem erro.
- [~] **C-03 Repositório e backup** (2026-10-09: repo local na raiz `D:\aquario-incremental` com `main`, `.gitignore`, `.gitattributes` e LFS ativo; **sem commit e sem remoto ainda**, fica com o dev) [S]: `git init`, `.gitignore` de Unity (Library, Temp, Logs, Builds, `*.csproj`), `.gitattributes` com Git LFS para `*.png`, `*.psd`, `*.aseprite`, `*.wav`, `*.ogg`; remoto privado (GitHub/GitLab). Push final fica com o dev; preparo os comandos.
- [ ] **C-04 Pacotes** [S]: instalar *Input System*, *TextMeshPro*, *2D Pixel Perfect*, *2D Sprite*, *Test Framework*, *Localization* (ou tabelas `Loc` próprias, ver D-06) e *Addressables* só se necessário. Critério: `manifest.json` versionado, console sem warning.
- [ ] **C-05 Estrutura de pastas e assemblies** [S]: `Assets/Game/{Core,Gameplay,Hud,Data,Art,Audio,Loc,Editor,Tests}`; `.asmdef` para `Core` (sem referência a UnityEngine), `Gameplay`, `Hud`, `Editor`, `Tests`. Critério: `Core` compila sem Unity; testes rodam no Test Runner.
- [ ] **C-06 Player Settings (PC/Windows)** [S]: nome do produto e da empresa, ícone provisório, resolução padrão em janela redimensionável (mín. 800×500, janelinha para segunda tela), *Run In Background* ligado (#007), color space Linear, backend IL2CPP para release, Mono para desenvolvimento, API compatibility .NET Standard 2.1, desligar logo "Made with Unity" se a licença permitir. Critério: build de teste abre e roda em janela pequena.
- [ ] **C-07 Pixel perfect e câmera** [S]: *Pixel Perfect Camera* com *Assets PPU* e resolução de referência da bíblia de arte (A-01); filtro Point em todos os sprites; compressão None; *Sprite Atlas* por tanque. Critério: sprite de teste sem borrão em 1080p e 720p.
- [ ] **C-08 Importadores de dados** [M]: menu `Aquário > Create Default Data` lê `species.csv` e `tanks.csv` e gera `SpeciesData`/`TankData` (ScriptableObjects). Não sobrescreve asset existente; relatório do que criou/ignorou. Teste Core do parser (colunas faltando, vírgula decimal, linha vazia). Critério: tanque 1 carregado com 5 espécies.
- [ ] **C-09 Build de teste e pasta de logs** [S]: script `Aquário > Build Windows` (Development), pasta `Builds/` fora do git, `RunLogs/` para telemetria (#056).
- [ ] **C-11 Backup dos fontes de arte** [S]: pasta `ArteFontes/` (Aseprite, PSD, referências) versionada com LFS ou espelhada em nuvem/HD externo, fora de `Assets/`; convenção de nome (`tanque01_lebiste_v03.aseprite`); rotina semanal de cópia. Critério: perder o disco não perde nenhum sprite editável.
- [ ] **C-10 Fluxo de cenas** [S]: `Boot` (carrega save e idioma) → `Title` → `Room` (sala com o tanque em foco); regra: uma única cena/prefab de tanque dirigida por dados (#051).

## 2. Núcleo técnico [P1]

- [ ] **F-01 Números grandes** [M]: tipo `BigNumber` (mantissa/expoente, saneado contra NaN e mantissa fora de [1,10)), soma, multiplicação, potência, comparação, `MaxAffordable(custo_base, razão, n, dinheiro)` com guardas para razão ≤ 1. Testes de borda.
- [ ] **F-02 Formatação** [S]: abreviação (K, M, B…) e notação clássica/científica com alternância (#001); sufixos temáticos do mar **(DECIDIR D-09)**. Respeita o idioma (separador decimal).
- [ ] **F-03 Economia em Core** [M]: `EconomyState` + `EconomyModel`: renda por espécie `renda_base × n × 2^marcos` (marcos 25/50/100), custo da n-ésima cópia `custo_base × razão^n`, cota por espécie e capacidade total (#020). Passo fixo online; forma fechada para offline/simulador (#006). Teste: online e fechada dão o mesmo resultado em janelas de 1 s, 1 h e 24 h.
- [ ] **F-04 Save versionado** [M]: `SaveData` separa **estado da run** de **estado permanente** (#004); autosave periódico, 3 backups rotativos, escrita atômica (arquivo temporário → rename), exportar/importar código copiável (#003). `TryLoad` lê para estado temporário e só aplica no fim; clamp de valores; migração por `saveVersion`. Testes: save corrompido, save de versão antiga, ida e volta.
- [ ] **F-05 Offline** [M]: tela "enquanto você estava fora", fração da renda e teto de horas **(DECIDIR D-03)**, trava contra relógio do sistema voltando (#002, #023). Testes: sem tempo, relógio negativo, teto.
- [ ] **F-06 Janela de segunda tela** [S]: sem foco, limita para poucos fps e continua simulando (#007).
- [ ] **F-07 Telemetria local** [S]: grava em `RunLogs/` o tempo para cada tanque/peixe/marco (CSV), base do `ring_pace`-equivalente (E-03) (#056).
- [ ] **F-08 Segurança de ciclo de vida** [S]: pools/arrays liberados em `OnDisable`; nenhum `NativeArray` vaza ao recompilar no Play.
- [ ] **F-13 Migração de save e patches de balanço** [M]: contrato de compatibilidade: todo patch pós-lançamento abre saves antigos; `saveVersion` + migrações encadeadas (v1→v2→v3) em Core, cada uma com teste usando um save-fixture da versão antiga; mudança de custo/renda/cota em CSV nunca invalida cópias já compradas (recalcula custo e renda a partir de `n`); espécie removida ou renomeada ganha alias; se a capacidade/cota diminuir, as cópias excedentes são mantidas e só bloqueiam novas compras. Fixtures de save guardados em `Tests/Fixtures/` a cada versão publicada.
- [ ] **F-09 Metas e profiling de performance** [M]: metas escritas em `game/docs/performance.md`: 60 fps em foco com tanque cheio (25–40 animados), ≤ 5 fps e ≤ 3% de CPU em segunda tela sem foco, RAM ≤ 1 GB, tempo de carregamento ≤ 5 s, build ≤ 500 MB. Profiling com Unity Profiler no tanque mais pesado (T-08) e em máquina fraca (sem placa dedicada). Critério: números medidos registrados em `estado/`; regressão > 20% vira bug.
- [ ] **F-10 Estratégia de testes e CI** [M]: Test Runner EditMode para Core (obrigatório por item) e PlayMode para fluxos (compra, save, prestígio); script de linha de comando que roda tudo (`Unity -runTests -batchmode`); CI (GitHub Actions ou local) que roda testes e gera o build de Windows a cada push; teste de fumaça do build (abre, carrega save, fecha). Critério: um comando verde = pode integrar.
- [ ] **F-11 Log, crash e diagnóstico** [S]: log do jogo em arquivo (`Player.log` + log próprio rotativo), captura de exceção não tratada com tela "algo deu errado" que oferece copiar o log e restaurar o último backup do save; botão "copiar informações de suporte" em Opções (versão, idioma, resolução). Sem envio automático **(DECIDIR D-19)**.
- [ ] **F-12 Janela, resolução e DPI** [S]: testar 1280×720, 1920×1080, 2560×1440, 3440×1440 (ultrawide), 4K com DPI 150–200%, janelinha 800×500 e múltiplos monitores; UI com âncoras e escala por DPI; lembrar posição/tamanho da janela entre sessões; tela cheia sem borda e exclusiva. Critério: sem UI cortada em nenhuma combinação, registrado com prints.

## 3. Protótipo passo 1: um tanque [P1]
Hipótese a validar: comprar peixes e vê-los se acumular já é divertido por si só.

- [ ] **P1-01 Compra** [M]: comprar espécie com custo exponencial, cota e capacidade; botões x1/x10/x100/máx com custo total (#013). Compra nunca cobra e entrega zero (limitar `qty` pelas vagas livres antes de cobrar). Teste Core `min(limite econômico, vagas livres)`.
- [ ] **P1-02 Desbloqueio** [S]: `libera_apos_ter` (ex.: `lebiste:10`); silhueta da próxima espécie e "faltam X para o próximo peixe" (#047).
- [ ] **P1-03 UI da loja** [M]: por espécie: nome, custo, renda, cópias/cota, vagas livres, "paga-se em X min" (#016). Tooltip com marco de cardume seguinte.
- [ ] **P1-04 HUD de dinheiro** [S]: dinheiro e renda/s com easing suave (#034), formatação de F-02.
- [ ] **P1-05 Tanque em cena** [L]: até `max_animados` peixes animados (placeholder: formas simples, uma por família), o resto vira contador "x1.2K" (#009); movimento de nado calmo; pool de objetos; benchmark com 25 animados e 400 total.
- [ ] **P1-06 Renda visível** [S]: cada peixe solta moeda/bolha dourada que sobe e some; limite de partículas (#008, #034).
- [ ] **P1-07 Ritual da comida** [M]: soltar comida, cardume corre e come, bolhas; **sem efeito na economia** (#011).
- [ ] **P1-08 Progresso offline integrado** [S]: usa F-05 ao abrir o jogo; mostra a tela de retorno.
- [ ] **P1-09 Tutorial mínimo** [S]: dica de primeira vez (J-style): "compre seu primeiro lebiste", "faltam X para o próximo". Textos em `Loc`.
- [ ] **P1-11 Primeira sessão (FTUE)** [M]: fluxo dos primeiros 10 minutos: título → "Novo jogo" → tanque vazio com cena de abertura curta → dinheiro inicial 10 → primeira compra guiada → primeira moeda sobe → "faltam X" para a próxima espécie → primeiro marco de espécie desbloqueada. Metas: primeira compra em ≤ 30 s, jogador entende "peixes geram dinheiro" em ≤ 2 min, nenhuma tela de texto longa. Dicas de primeira vez, cada uma aparece uma única vez (`SaveData`: dicas vistas). Textos em `Loc`.
- [ ] **P1-12 Título, novo jogo e continuar** [S]: tela de título (Continuar, Novo jogo com confirmação se houver save, Opções, Créditos, Sair); mostrar resumo do save (tempo, tanques, Pérolas); "Novo jogo" nunca apaga save sem confirmação dupla e cria backup antes.
- [ ] **P1-10 Playtest do passo 1 (portão)** [S, dev]: 3 a 5 pessoas, 30 a 60 min, ficha em `game/docs/playtest-checklist.md` (criar em G-03). Registrar em `resultados/playtest-01.md`: onde largaram, o que não entenderam, nota de "comprar e acumular é divertido?". **Nada de P2 antes disto.**

## 4. Protótipo passo 2: sala e prestígio [P2] `[dep: P1-10]`

- [ ] **P2-01 Múltiplos tanques** [L]: vários tanques coexistem; antigos continuam rendendo; só o tanque em foco anima, os outros rodam na fórmula e aparecem como miniaturas de poucos quadros (#025, #030).
- [ ] **P2-02 Compra de tanque** [M]: `preco` e `capacidade_total` do `tanks.csv`; botão "faltam X"; silhueta do peixe do próximo tanque aparece no atual (#047).
- [ ] **P2-03 Navegação** [S]: vista da sala (todos os tanques lado a lado), clique dá zoom no tanque (#025); atalhos de teclado.
- [ ] **P2-04 Prestígio** [L]: botão liberado ao comprar o **penúltimo** tanque (#038); ganho de Pérolas suavizado (~raiz da renda total da run) mostrado antes de confirmar (#039). Reset em Core (`RunReset`): zera peixes, dinheiro e tanques; mantém Pérolas, loja, bestiário e estatísticas. Testes do contrato do que fica e do que zera.
- [ ] **P2-05 Loja da maré (1 item)** [M]: 1 item barato e perceptível para o primeiro prestígio já fazer diferença (#040).
- [ ] **P2-06 Tanque gigante como fim da run** [M]: último tanque, comprado de novo a cada run, jogável até o fim; recompensa extra de Pérolas por completá-lo (#038).
- [ ] **P2-07 Bônus dos tanques antigos** [S] **(DECIDIR D-10)**: cada tanque novo dá bônus pequeno aos anteriores (#027)?
- [ ] **P2-09 Tutorial do prestígio** [S]: ao liberar o botão pela primeira vez, painel curto: o que zera (peixes, dinheiro, tanques), o que fica (Pérolas, loja, bestiário, estatísticas), quantas Pérolas ganha agora; confirmação dupla; na segunda vez só o resumo. Depois do primeiro prestígio, a loja da maré abre com seta no item barato (P2-05). Textos em `Loc`.
- [ ] **P2-08 Playtest do passo 2 (portão)** [S, dev]: registrar em `resultados/playtest-02.md`; decidir se segue para o jogo completo.

## 5. Sistemas do jogo completo [JOGO] `[dep: P2-08]`

- [ ] **S-01 Bestiário** [M]: silhuetas "???"; ao comprar a primeira cópia vira o peixe colorido com ficha (nome, bioma, curiosidade) (#031); persiste no prestígio. Lendários: entrada especial (feixe de luz, bolhas, música).
- [ ] **S-02 Álbum por tanque** [M]: página completa dá bônus pequeno e permanente + bônus de Pérolas (#037); plaquinha de museu por espécie (#057).
- [ ] **S-03 Estatísticas** [S]: tempo de jogo, dinheiro total, peixes comprados, Pérolas, runs, tempo por tanque; persistem.
- [ ] **S-04 Marcos de cardume** [M]: 25/50/100 cópias: multiplicador x2 + formação visual nova do cardume (#014).
- [ ] **S-05 Tanque completo** [S]: cotas cheias + cardumes completos = selo e bônus fixo; o tanque deixa de pedir decisões (#028).
- [ ] **S-17 Catálogo da loja da maré e fórmula de Pérolas** [M, design] `[dep: E-04 em paralelo]`: documento `game/docs/mare-pearls.md` com: fórmula exata de Pérolas (base ~raiz da renda total da run, bônus por álbum, bônus por completar o gigante); lista nominal de itens por prateleira, cada um com nome, descrição, efeito, número de níveis, custo por nível e teto (ex.: *Aceleradores*: Correnteza (+velocidade de renda), Biólogo atento (offline +horas); *Renda*: Ração premium (+% renda por espécie), Cardume veterano (marcos de cardume antecipados); *Descontos*: Corretor de aquários (-% preço de tanques), Atacado de peixes (-% custo de compra)). Nomes são proposta; o dev aprova (D-20). Texto de cada item em `Loc`.
- [ ] **S-18 Lista de conquistas do jogo** [M, design]: `game/docs/conquistas.md` com ~30 conquistas sem sorteio e sem pressão, cada uma com id, nome, descrição, condição em Core e ícone; categorias: Coleção (descobrir a 1ª/10ª/40ª espécie, cada lendário, bestiário completo), Tanques (comprar cada tanque, completar cada um), Cardume (1º marco 25/50/100), Prestígio (1º, 5º, 10º; gigante completo), Tempo (1 h, 24 h abertos), Segredos (alimentar 100 vezes, ver o dia virar noite). Espelhadas na Steam em ST-04.
- [ ] **S-19 Feedback de compra por raridade** [S]: som, partícula e animação por raridade (comum discreto, incomum com brilho, raro com onda de luz, lendário com entrada especial #031); distinção por forma/brilho e não só cor (#060); tudo ajustável nas Opções.
- [ ] **S-20 Controles e Steam Deck** [M] **(DECIDIR D-18)**: jogo inteiro jogável só com mouse e também só com teclado (Tab/setas/Enter, atalhos para tanque anterior/próximo, compra x1/x10/máx); gamepad (navegação de UI por *Input System*); layout legível em 1280×800 (Steam Deck) com fonte ≥ 14 px equivalentes; ícones de botão por dispositivo. Critério: ficar "Jogável" na Steam Deck; conseguir comprar tudo sem mouse.
- [ ] **S-06 Loja da maré completa** [L] `[dep: S-17]`: 3 prateleiras (aceleradores, renda, descontos em aquários), níveis com retorno decrescente e teto suave por prateleira (#040, #046); item para subir teto/percentual do offline (#002, #023). Fórmulas em Core com teste.
- [ ] **S-07 Biólogo automático** [M] **(DECIDIR D-11)**: compra por regras simples escolhidas pelo jogador, item da loja (#015).
- [ ] **S-08 Painel de melhores compras** [M]: lista global por tempo de retorno, com atalho de compra (#029).
- [ ] **S-09 Parede amiga e termômetro** [M]: sugestão contextual quando a progressão desacelera (comprar em lote, trocar de tanque, prestigiar) (#048); termômetro "boa hora para reiniciar" (#044).
- [ ] **S-10 Sala que lembra** [S]: após o prestígio, silhuetas translúcidas das espécies já descobertas; recomprar "acende" (#041).
- [ ] **S-11 Cerimônia de prestígio** [M]: câmera afasta, maré leva os peixes, Pérolas contadas, sala vazia (#043).
- [ ] **S-12 Ciclos que encurtam** [S]: runs seguintes mais rápidas por Pérolas, até um piso; medido no simulador (#045).
- [ ] **S-13 Acessibilidade** [M]: raridade por forma/brilho (#060), modo daltônico, notação alternativa, tamanho de fonte, redução de movimento; todos os sons com controle de volume por categoria; alto contraste na UI; indicador visual para cada som importante (compra, descoberta, retorno do offline) para quem joga sem som; sem informação só por cor ou só por som; declarar os recursos na página da Steam.
- [ ] **S-21 Qualidade de vida** [S]: lembrar última escolha de x1/x10/x100/máx por sessão; atalhos de teclado documentados na tela de Opções; botão "comprar o melhor" (menor tempo de retorno) com confirmação opcional; ordenar/filtrar a lista de espécies; "ocultar tanques completos"; atalho para o tanque com a próxima compra. Sem automatizar o jogo (isso é o S-07).
- [ ] **S-14 Opções** [S]: volume (música/efeitos/ambiente), idioma, notação, FPS sem foco, tela cheia/janela, exportar/importar save, apagar save.
- [ ] **S-15 Janela sempre no topo** [S] **(DECIDIR D-12)**: modo "papel de parede vivo" (#058).
- [ ] **S-16 Final da run/jogo** [M] **(DECIDIR D-13)**: o que acontece ao completar tudo (cena final, créditos, modo livre?). Hoje a run termina no gigante e reinicia.

## 6. Arte: bíblia e pipeline [JOGO]

- [ ] **A-01 Bíblia de arte** [M, dev + eu] **(DECIDIR D-04)**: resolução/PPU, tamanho em px de cada classe (PP, P, M, G, GG, XL), resolução da cena de cada tanque, paleta global e por tipo de água (máx. N cores por peixe), regras de contorno, sombra e luz, direção da luz, estilo de animação. Saída: `game/docs/guia-de-arte.md` com exemplos. **Bloqueia todos os itens de arte.**
- [ ] **A-02 Peixe de referência** [M]: um peixe (Lebiste) feito até o fim (sprite, nado, comer, silhueta, miniatura) para validar o padrão e o tempo de produção por peixe.
- [ ] **A-03 Tanque de referência** [L]: o Tanque 1 completo (3 camadas, água, decoração, moldura, miniatura, noite) para validar o padrão e o tempo por tanque.
- [ ] **A-04 Importação e animação genérica** [M]: configuração pixel perfect, atlas por tanque, controlador de nado por família (parâmetros: velocidade, amplitude, profundidade), virada, comer.
- [ ] **A-05 Ambiente vivo** [M]: dia/noite pelo relógio real, correntes, plâncton, peixes de fundo fora da economia, brilho noturno (#032).
- [ ] **A-06 Escala de maravilha** [M]: parallax em camadas e peixes de tamanhos muito diferentes (#033).
- [ ] **A-07 Juice calmo** [S]: bolhas douradas, easing de números, "plim" discreto, sem tremor de tela (#034).
- [ ] **A-08 Interface** [L]: tema visual da UI (fontes, moldura de madeira/vidro?, ícones de moeda, Pérola, raridades), estados hover/pressed/disabled, telas do bestiário, álbum, loja da maré, opções.
- [ ] **A-10 Lista de ambiente por tanque** [M, design] `[dep: A-01, T-00]`: acrescentar a `conteudo-tanques.md`, para cada tanque, a lista nominal de: peixes de fundo (fora da economia, ex.: lambaris no tanque 1; garoupas no 4), decoração fixa (plantas, troncos, corais, ruínas, túnel), partículas (bolhas, plâncton, neve marinha), tipo de iluminação dia/noite e o objeto que "acende" quando o tanque é completo. Cada item com tamanho em classe e quantidade de quadros. Base para estimar o tempo de arte.
- [ ] **A-09 Logo, ícone e título** [M]: nome definitivo **(DECIDIR D-08)**, logotipo, ícone do app, cena da tela de título.

## 7. Conteúdo por tanque: uma onda por tanque [JOGO]
Detalhe de nomes e espécies: `game/docs/conteudo-tanques.md`. Cada onda segue as mesmas etapas; **só entra o tanque N+1 depois de fechar o N**.

Etapas de cada onda (cada uma vira um item `T-NN-x`):
- **a)** Dados: preencher/revisar `species.csv` e `tanks.csv`; rodar `sim_economia.py` até o ritmo do tanque fechar (E-01/E-02).
- **b)** Arte do tanque (checklist por tanque).
- **c)** Arte das 5 espécies (checklist por espécie), cardumes 25/50/100 e entrada do lendário.
- **d)** Textos (`Loc`, todos os idiomas ativos): nome do tanque, nomes, fichas e curiosidades das 5 espécies, página do álbum.
- **e)** Integração: criar os ScriptableObjects, testar o tanque no jogo, benchmark de performance.
- **f)** Revisão visual (prints 1080p e 720p, teste de silhueta preta, daltonismo).
- **g)** Áudio ambiente do tipo de água [PÓS].

- [ ] **T-00 Confirmar o roster** [S, dev]: aprovar ou trocar os nomes de tanques e espécies de 2 a 8 em `conteudo-tanques.md` **(DECIDIR D-05)**.
- [ ] **T-01 Tanque 1: Aquário Inicial** (água doce; Lebiste, Tetra Neon, Betta, Acará-bandeira, Disco Dourado) [L]: dados já existem; falta etapas b–f.
- [ ] **T-02 Tanque 2: Recife Pequeno** (salgada; Donzela-azul, Peixe-palhaço, Tang-azul, Peixe-anjo-imperador, Cavalo-marinho-dourado) [L]
- [ ] **T-03 Tanque 3: Rio Amazônico** (doce plantada; Cardinal, Corydora, Piranha-vermelha, Aruanã-prateada, Pirarucu) [L]
- [ ] **T-04 Tanque 4: Recife de Coral** (salgada; Peixe-borboleta, Peixe-papagaio, Baiacu-balão, Peixe-leão, Tubarão-de-ponta-branca) [L]
- [ ] **T-05 Tanque 5: Floresta de Kelp** (fria; Garibaldi, Sardinha-prateada, Linguado, Lula-de-vidro, Polvo-gigante-do-Pacífico) [L]
- [ ] **T-06 Tanque 6: Abismo** (abissal; Peixe-lanterna, Peixe-machado, Peixe-víbora, Peixe-pescador, Lula-colossal) [L]
- [ ] **T-07 Tanque 7: Laguna Luminosa** (fantasiosa, penúltimo, libera o prestígio; Água-viva-lunar, Peixe-cometa, Carpa-aurora, Raia-estelar, Dragão-das-marés) [L]
- [ ] **T-08 Tanque 8: Aquário Gigante** (oceano aberto, último da run; Atum-azul, Tartaruga-verde, Tubarão-martelo, Raia-manta-gigante, Baleia-azul) [L]
- [ ] **T-09 Fichas do bestiário** [M]: curiosidade real de cada uma das 40 espécies, 2 a 3 linhas, revisada (fatos checados).

## 8. Áudio [JOGO / PÓS]

- [ ] **U-01 Efeitos** [M]: compra, moeda, clique, descoberta, lendário, prestígio, comida; sintetizados primeiro, depois arquivos (`Resources/Sfx/`) com fallback; samples só CC0/CC-BY registrados em `creditos-audio.md`.
- [ ] **U-02 Música e ambiente** [M] **(DECIDIR D-07)**: música livre ou compositor; ambiente sonoro por tipo de água, com camadas que crescem com a coleção (#036) [PÓS]; loops sem emenda audível.
- [ ] **U-03 Teste de escuta** [S]: perguntas de som na ficha do playtest.

## 9. Economia e simulador (corre em paralelo; calibração só no fim)

- [ ] **E-01 Simulador para N tanques** [M]: `sim_economia.py` sem filtro fixo `agua_doce_01`: compra de tanque, bônus de tanques antigos, capacidade, cotas, cardumes.
- [ ] **E-02 Preço dos tanques** [M]: derivar o preço de cada tanque da renda do anterior (#019 como régua) em vez de chutar; metas: várias horas a dias por run, 8 tanques; hoje o tanque 2 a 2 mi saía barato (rascunho 50 mi). Gerar `custo_base`/`renda_base` das espécies de 2 a 8 seguindo o degrau do tanque 1.
- [ ] **E-03 Curva-alvo e ferramenta de ritmo** [M]: `game/docs/curva-alvo.md` (tempo por tanque, prestígio, runs seguintes em 1/3 a 1/2 da primeira) e `tools/pace.py` que lê `RunLogs/*.csv` e imprime o tempo de cada tanque, paredes e diferença para a run anterior.
- [ ] **E-04 Simular prestígio e loja** [M]: Pérolas, 3 prateleiras com teto suave, duração das runs seguintes (#045).
- [ ] **E-05 Calibração final** [L] `[dep: playtests, T-08, S-06]`: todos os tanques com dados de telemetria real; cada ajuste com run do bot e `pace.py`.

## 10. Idiomas (localização) [JOGO / LANÇ]
Regra: nenhum texto fixo em código; tudo por chave (`Loc`). Idioma base = **Português (Brasil)**; inglês é obrigatório no lançamento.

- [ ] **I-01 Sistema de localização** [M] **(DECIDIR D-06)**: pacote *Unity Localization* vs. tabelas `Loc` próprias em CSV/JSON; chaves por domínio (`ui.`, `species.<id>.name`, `species.<id>.fact`, `tank.<id>.name`...). Fallback para EN quando faltar chave. Troca de idioma sem reiniciar. Teste Core: toda chave existe em todos os idiomas ativos.
- [ ] **I-02 Fontes** [M]: fonte pixel/estilizada com acentos (PT, ES, FR, DE), cirílico (RU) e, se D-14 incluir, glifos CJK (fonte separada em atlas dinâmico do TMP). Critério: nenhum "□" em nenhum idioma ativo.
- [ ] **I-03 Formatação por idioma** [S]: separador decimal/milhar, abreviações de números (K/M/B), plurais (PT/EN/RU têm regras diferentes), ordem de palavras sem concatenar frases.
- [ ] **I-04 Extração e auditoria** [S]: `tools/audit_loc.py`: nenhum literal de texto no código/UI, nenhuma chave órfã, nenhuma chave sem tradução, texto > largura do botão em cada idioma (alemão e russo são os mais longos).
- [ ] **I-05 PT-BR e EN completos** [M]: escritos pelo dev/revisados; são os idiomas "completos" na loja.
- [ ] **I-06 Idiomas adicionais** [L] **(DECIDIR D-14)**: proposta de ordem: ES, FR, DE, RU (mercado forte na Steam) e depois ZH-Hans, JA, KO, TR. Cada idioma novo = tabela completa + fonte + prints. Tradução automática entra marcada como "(beta)" no seletor de idioma até haver revisão nativa; a loja lista como completos só os revisados.
- [ ] **I-07 Seletor de idioma** [S]: no primeiro boot detecta o idioma do sistema (fallback EN); opção em Opções; nome do idioma sempre no próprio idioma ("Deutsch", "Português").
- [ ] **I-08 Textos da loja Steam por idioma** [S]: descrição curta/longa, tags, legendas de capturas, traduzidas junto (ver ST-06).
- [ ] **I-09 Teste por idioma** [S]: uma passada de cada idioma ativo no jogo (menu, loja, bestiário, prestígio, offline) com prints para conferir estouro de texto.

## 11. Steam e lançamento [LANÇ]

- [ ] **ST-01 Conta e legal** [S, dev]: conta Steamworks (taxa por app de US$ 100), dados bancários e fiscais (W-8BEN/ impostos), empresa/pessoa física. Critério: acesso ao painel Steamworks.
- [ ] **ST-02 Criar o app e o AppID** [S]: criar o app, definir nome (D-08), copiar o AppID; `steam_appid.txt` só em desenvolvimento (fora do build final); criar também o app da **demo** [dep: D-15].
- [ ] **ST-03 SDK no Unity** [M]: Steamworks.NET (ou Facepunch) isolado em `Platform/` atrás de interface (`IPlatform`), jogo roda sem Steam (fallback no-op). Inicialização, overlay, `RestartAppIfNecessary`.
- [ ] **ST-04 Conquistas** [M] `[dep: S-18]`: espelhar na Steam a lista de `conquistas.md`, ícones 256×256 (desbloqueada e bloqueada), nome e descrição localizados; conquistas locais primeiro, espelhadas na Steam.
- [ ] **ST-05 Steam Cloud** [M]: configurar no painel os arquivos de save a sincronizar (Auto-Cloud) e resolver conflito (mais recente vs. maior progresso); manter exportar/importar como plano B. Testes obrigatórios: (1) trocar de PC com o mesmo save; (2) dois PCs com saves divergentes (jogo mostra os dois resumos e o jogador escolhe, sempre fazendo backup do descartado); (3) save corrompido na nuvem (cai no backup local); (4) offline sem internet (jogo não trava, sincroniza depois); (5) apagar a nuvem. Nunca sobrescrever um save mais avançado em silêncio.
- [ ] **ST-06 Página da loja** [L]: textos curtos/longos em todos os idiomas ativos, tags (Idle, Incremental, Relaxing, Cozy, Pixel Graphics, Fish…), capturas 1920×1080 (mín. 5), trailer (30 a 60 s, mostrando o salto visual dos tanques), GIFs, classificação indicativa (questionário), requisitos mínimos, preço **(DECIDIR D-16)**, idiomas suportados.
- [ ] **ST-07 Artes de cápsula** [L]: header 460×215, small 231×87, main 616×353, vertical 374×448, library capsule 600×900, hero 3840×1240, logo 1280×720, ícone; todas com o logo legível em tamanho pequeno.
- [ ] **ST-08 Build e depots** [M]: build Windows 64 bits (IL2CPP, Release), SteamPipe (`app_build.vdf`, depot), branches (`default`, `beta`, `demo`), script de upload; teste de instalação limpa em outra máquina.
- [ ] **ST-09 Demo** [M] **(DECIDIR D-15)**: limitar a demo (ex.: até o fim do tanque 2); build separado; botão "lista de desejos" no jogo.
- [ ] **ST-10 "Em breve" e wishlist** [S]: publicar a página pelo menos algumas semanas antes do lançamento para acumular lista de desejos; Next Fest se quiser.
- [ ] **ST-11 Revisão da Valve e checklist** [M]: página aprovada, build aprovado; checklist: save/carregar, janela redimensionável, sem crash ao fechar, sem texto cortado, Steam sem rodar, offline sem internet, sem permissão de admin.
- [ ] **ST-12 Lançamento e pós** [S]: data e horário, anúncio, plano de patch (v1.0.1), coleta de bugs; plano de preços/promoção (detalhe em M-05).
- [ ] **ST-13 Steam Deck e controle** [S] `[dep: S-20]`: preencher o questionário de compatibilidade, testar no aparelho (ou no modo Big Picture/Deck do Steam no PC): texto legível, entrada de texto, suspender/retomar sem perder o relógio do offline, sem launcher. Meta: selo *Verificado* ou *Jogável*.
- [ ] **ST-14 Classificação e conformidade da loja** [S, dev]: questionário de conteúdo da Steam, classificação etária (sem violência/aposta; atenção ao termo "loot box" não se aplica: nada é sorteado), declaração de IA generativa (se alguma arte/texto usar), países com restrição, preço regional, impostos; registrar as respostas em `game/docs/steam-checklist.md`.

## 12. Adiado [PÓS]
Modo foto (#035) · trilha em camadas completa (#036) · gigante permanente com obras (#042) · prestígio por tanque (#050) · jarra de Pérolas (#049) · eventos aleatórios · cruzamento de peixes · cena final · modo livre · multiplayer/nuvem própria.

## 13. Decisões pendentes do dev (responder antes dos itens marcados)

| ID | Pergunta | Recomendação |
|---|---|---|
| D-01 | Qual versão LTS do Unity? | A LTS mais recente instalada na sua máquina |
| D-02 | URP 2D ou Built-in 2D? | **RESOLVIDO 2026-10-09: Universal 2D (URP)** |
| D-03 | Limite e % do offline? | Teto 2 a 4 h, 50% da renda, sobe na loja da maré |
| D-04 | Resolução/PPU dos sprites e dos tanques? | Decidir com o peixe de referência A-02 |
| D-05 | Aprova o roster de tanques e espécies 2 a 8? | Revisar `conteudo-tanques.md` |
| D-06 | Unity Localization ou tabelas `Loc` próprias? | Tabelas próprias em CSV (casa com o fluxo CSV → asset) |
| D-07 | Música livre ou compositor? | Livre no lançamento, compositor se o playtest pedir |
| D-08 | Nome definitivo do jogo? | Antes de criar o app na Steam (ST-02) |
| D-09 | Sufixos temáticos de número agradam? | Testar no playtest, alternância sempre disponível |
| D-10 | Tanques novos dão bônus aos antigos (#027)? | Sim, pequeno |
| D-11 | Biólogo automático entra? | Sim, como item da loja da maré |
| D-12 | Modo janela sempre no topo? | Sim, pós-lançamento |
| D-13 | O que acontece depois do tanque gigante/fim? | Cena curta + créditos, depois prestígio |
| D-14 | Quais idiomas além de PT/EN? | ES, FR, DE, RU como beta; ZH-Hans e JA depois do lançamento |
| D-15 | Haverá demo? | Sim, até o tanque 2 |
| D-16 | Preço? | Definir perto do lançamento, comparando incrementais cozy |
| D-17 | Prazo, orçamento e horas semanais disponíveis? | Definir para calcular marcos reais (G-01) |
| D-18 | Gamepad e Steam Deck entram no lançamento? | Teclado/mouse no lançamento, gamepad/Deck logo depois |
| D-19 | Envio de crash/telemetria? | Não enviar nada automático; só log local e botão de copiar |
| D-20 | Aprova nomes e efeitos dos itens da loja da maré e das conquistas? | Revisar `mare-pearls.md` e `conquistas.md` |
| D-21 | Orçamento e plano de marketing? | Sem pago no lançamento; orgânico + Next Fest |

---

## 14. Ordem da fila (um item por chat)

1. **Configuração:** C-01 → C-02 → C-03 → C-04 → C-05 → C-06 → C-07 → C-08 → C-09 → C-10
2. **Núcleo:** F-01 → F-02 → F-03 → F-04 → F-05 → F-06 → F-07 → F-08
3. **Protótipo 1:** P1-01 → P1-02 → P1-03 → P1-04 → P1-05 → P1-06 → P1-07 → P1-08 → P1-09 → **P1-10 (portão)**
4. **Economia mínima:** E-01
5. **Protótipo 2:** P2-01 → … → P2-08 (portão)
6. **Economia:** E-02 → E-03 → E-04
7. **Sistemas:** S-01 → S-14 (S-07, S-15, S-16 após decisão)
8. **Idiomas base:** I-01 → I-04 (cedo, para nenhum texto nascer fora do sistema); I-05 junto de cada onda
9. **Arte:** A-01 → A-02 → A-03 → A-04 → A-05 → A-06 → A-07 → A-08 → A-09
10. **Conteúdo:** T-00 → T-01 → T-02 → … → T-08 (uma onda por vez); T-09; U-01; U-02; U-03
11. **Idiomas extras:** I-06 → I-09
12. **Calibração:** E-05
13. **Steam:** ST-01 e ST-02 cedo (nome e AppID); ST-03 → ST-05 durante o JOGO; ST-06 → ST-14 perto do lançamento
14. **Gestão e documentação (seção 15):** G-01 e G-03 antes do P1-10; G-02 (GDD), G-04 (glossário) e G-05 (licenças) cedo e atualizados a cada onda; G-06 antes do lançamento
15. **Marketing e pós (seção 16):** M-01 e M-04 desde o P2; M-02 a M-03 durante as ondas de arte; M-05 depois do lançamento
16. **Controle de escopo (seção 17):** G-08, G-09 e G-10 junto de G-01; G-11 ao fim de cada onda de tanque; C-11 logo após C-03; F-13 antes do primeiro playtest externo; P2-09 com P2-04; S-21 depois de S-14
17. **Qualidade contínua:** F-09 (performance) e F-10 (testes/CI) logo após a configuração; F-11 e F-12 antes do primeiro playtest externo; S-17, S-18, S-19 antes de S-06; S-20 antes de ST-13

Fluxo por chat (CLAUDE.md): pegar o próximo `[ ]` desta ordem, construir só o item, anotar aqui e em `game/docs/estado/`, terminar a resposta com "Como testar". Item com **DECIDIR** sem resposta: pular e avisar.

---

## 15. Gestão, documentação e legal

- [ ] **G-01 Orçamento, prazo e marcos** [S, dev] **(DECIDIR D-17)**: horas por semana, data-alvo de lançamento, custos previstos (conta Steamworks US$ 100, ferramentas, fontes/licenças, música, tradução, marketing); marcos: protótipo 1, protótipo 2, vertical slice (tanque 1 com arte final), 4 tanques, 8 tanques, demo, lançamento. Cada marco com data e critério. Revisar a cada onda de tanque.
- [ ] **G-02 GDD formal** [M]: gerar o GDD (`gds-gdd`) a partir do brief e do brainstorming, com loop, economia, prestígio, tanques, interface, arte, áudio e escopo; vira a fonte de verdade acima do backlog. Atualizar quando uma decisão D-xx for tomada.
- [ ] **G-03 Checklist de playtest** [S]: criar `game/docs/playtest-checklist.md` (roteiro, perguntas, ficha por pessoa: minuto de abandono, primeiro momento de confusão, sistema que ninguém entendeu, nota de "comprar e acumular é divertido?", nota de visual e de som, pergunta de idioma) e `resultados/` para as sessões.
- [ ] **G-04 Glossário** [S]: `game/docs/glossario.md` com termos do jogo e tradução oficial por idioma (Pérolas, Loja da Maré, Cardume, Marco, Tanque/Aquário, Bestiário, Álbum, Prestígio, Lendário…); fonte para I-01 e para a loja Steam.
- [ ] **G-05 Licenças e créditos** [S]: `game/docs/licencas.md` com todo material de terceiros (pacotes Unity, Steamworks.NET, fontes, samples, música, ícones): autor, licença, URL, obrigação (atribuição?); tela de Créditos no jogo gerada a partir disso; conferir compatibilidade comercial antes de qualquer asset entrar no projeto.
- [ ] **G-06 Política de privacidade e termos** [S]: política de privacidade curta (o jogo não coleta nem envia dados pessoais; saves ficam locais e na Steam Cloud; telemetria só local), EULA mínima se necessária, URL pública para a página da Steam (D-19).
- [ ] **G-07 Versão e changelog** [S]: esquema de versão (`0.x` protótipo, `1.0` lançamento), número visível em Opções, `CHANGELOG.md`, nome de build no SteamPipe.

## 16. Marketing e pós-lançamento

- [ ] **M-01 Comunidade** [S]: servidor Discord (regras, canais de feedback e bugs), conta social do jogo (Bluesky/X/Instagram) com ao menos um post por tanque concluído (print/gif); link na página da Steam.
- [ ] **M-02 Press kit** [S]: página simples (itch.io ou site) com descrição, logo, capturas, trailer, fatos (preço, plataforma, idiomas, contato) para imprensa e curadores.
- [ ] **M-03 Divulgação** [M] **(DECIDIR D-21)**: lista de criadores/curadores de jogos cozy e incrementais, chaves de review, participação no Steam Next Fest com a demo, posts em comunidades relevantes; orçamento definido antes.
- [ ] **M-04 Devlog** [S]: um texto curto por marco (tanque novo, economia, arte); alimenta a página da Steam e as redes.
- [ ] **M-05 Pós-lançamento** [M]: monitorar avaliações e o Discord, triagem semanal de bugs, patches (v1.0.1…), métricas da Steam (lista de desejos, conversão, reembolso, tempo jogado) para decidir o conteúdo seguinte (itens de PÓS da seção 12), plano de preços/promoções.

## 17. Controle de escopo e decisões

- [ ] **G-08 Congelador de escopo e critério de corte** [S]: `game/docs/escopo.md` com a lista "fora desta versão" (seção 12) revisada ao fim de cada onda de tanque (#054); critério de corte se o prazo estourar, na ordem: (1) tanques 6 a 8 viram pós-lançamento, (2) idiomas extras, (3) loja da maré reduzida a 1 prateleira, (4) conquistas Steam reduzidas; o mínimo vendável é **5 tanques + prestígio + PT/EN**. Marcos da G-01 reavaliados por esse critério.
- [ ] **G-09 Log de decisões** [S]: `game/docs/decisoes.md` com cada D-xx respondida (data, escolha, motivo); a tabela da seção 13 aponta para ele em vez de crescer; decisões reabertas ficam registradas.
- [ ] **G-10 Plataformas fora do escopo** [S]: registrar em `escopo.md`: Windows 64 bits é a única plataforma de lançamento; macOS/Linux nativos e mobile fora (Steam Deck via Proton só quando ST-13 for feito); sem modding nem editor de dados para jogadores; sem multiplayer; sem sistema de contas; sem anúncios nem compras dentro do jogo.
- [ ] **G-11 Revisão de backlog por onda** [S]: ao fim de cada tanque (T-0N), reabrir estimativas, tempo real gasto de arte por peixe/tanque (medido), e corrigir `T-0N+1`; registrar em `estado/`.
