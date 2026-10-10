---
title: 'Game Brainstorming Session'
date: '2026-10-09'
author: 'Murilo'
version: '1.0'
stepsCompleted: [1, 2, 3, 4]
status: 'complete'
---

# Game Brainstorming Session

## Session Info

- **Date:** 2026-10-09
- **Facilitator:** Game Designer Agent
- **Participant:** Murilo

---

_Ideas will be captured as we progress through the session._

## Brainstorming Approach

**Selected Mode:** YOLO (facilitador conduz a sessão com todas as técnicas; revisão do Murilo ao final)

**Plataforma-alvo:** PC (Unity)
**Equipe:** solo (só o Murilo)
**Estratégia:** protótipo primeiro; as rodadas de brainstorming alimentam o protótipo

**Decisões do Murilo (travadas antes da ideação):**
- Prestígio é obrigatório: o jogo é um ciclo, não tem fim fixo
- A renda vem dos peixes: quanto mais peixes e mais raros, mais dinheiro. O aquário não gera renda
- Vários aquários coexistem (uma sala de aquários). Cada um é comprado, mais caro que o anterior,
  e tem tipo de água próprio (doce, salgada etc.), capacidade, conjunto de espécies e salto visual
- Aquários antigos continuam gerando renda, mas ela perde peso relativo conforme os peixes novos
  ficam mais caros (aceito pelo Murilo como parte da curva)
- Fantasia do jogador: colecionador + maravilha do oceano
- O custo de cada peixe cresce exponencialmente a cada cópia comprada, inclusive o peixe barato
- Exibição: até N peixes animados na tela; o restante vira contador (ex.: "x1.2K")
- Ritmo longo: várias horas a dias por run, 8 ou mais aquários. Motivo do Murilo: incrementais
  raramente passam de ~20 horas, e deixar o jogo aberto um dia inteiro não deve zerá-lo
- Limite de peixes: total por aquário E cota por espécie (os dois)
- Alimentar é só um gesto visual, sem efeito na renda; pilar candidato: contemplativo e visualmente bonito
- Todos os peixes, inclusive os raros, são comprados: nada é sorteado
- Protótipo menor: começa com UM tanque (loop de compra, offline, save); prestígio e segundo tanque entram num segundo passo
- Jogo real: muitos peixes visualmente diferentes (palette swap só para variantes baratas)
- Loop convencional, simples, bem feito e equilibrado, sem eventos especiais:
  comprar peixes → gerar dinheiro → comprar aquário novo → ... → prestígio (reinicia a run)
- A loja de prestígio vende: aceleradores, bônus de renda e desconto em aquários
- Gatilho do prestígio: libera ao comprar o PENÚLTIMO aquário da sala (não só no fim)
- O aquário gigante é apenas o ÚLTIMO tanque da sala, comprado de novo a cada run e jogável até o fim (não é obra permanente)

**Pilares candidatos (fecho da rodada 1):**
1. O aquário bonito é o produto (contemplativo, salto visual a cada tanque)
2. Colecionar é o motor (bestiário, álbuns, espécies por tipo de água)
3. Loop simples e equilibrado por baixo (sem sorteio, sem eventos; economia testada em simulador)
- Nota de escopo: arte provisória (placeholder) no protótipo da semana 1; arte final só depois que a economia fechar

**Techniques Available:**
- Conceituais: MDA Framework, Player Fantasy Mining, Core Loop Brainstorming, Genre Mashup, Verbs Before Nouns
- Sistemas: Economy Balancing Thought Experiments, Meta-Game Layer Design,
  Progression Curve Sculpting, Reward Schedule Architecture, Failure State Design,
  Emergence Engineering
- Experiência/Criatividade: Emotion Targeting, Game Feel Playground, Toy Before Game,
  Constraint-Based Creativity, Remix an Existing Game
- Narrativa/Inclusão: Ludonarrative Harmony, Environmental Storytelling, Accessibility Layers

**Ordem das rodadas (protótipo primeiro): 0 → 2 → 1 → 3 → 4**
0. Fundamentos técnicos: números grandes, progresso offline, save versionado,
   o que persiste no prestígio, conteúdo orientado a dados (ScriptableObject por espécie)
2. Loop e economia (núcleo do jogo): Core Loop + Verbs Before Nouns + Economy Balancing
   + Reward Schedule (custo por cópia e renda por espécie, capacidade do aquário,
   desbloqueio de espécies, simulador de economia)
1. Fantasia e brinquedo, com game feel: Player Fantasy + Toy Before Game
   + Emotion Targeting + Game Feel Playground
   (inclui o salto visual de cada aquário; fecha com "o que só este aquário tem?")
3. Progressão e prestígio: Progression Curve + Meta-Game Layer
   (moeda de prestígio, o que reseta e o que persiste, catálogo da loja de prestígio,
   quando vale reiniciar) + Failure State Design
4. Mutações e escopo: Genre Mashup + Remix + Constraint (palette swap,
   teto de escopo do MVP para um dev solo)

**Fios transversais (perguntas recorrentes em todas as rodadas):**
- Tempo: segunda tela/janela pequena, progresso offline, sessões curtas vs. longas
- Coleção: bestiário com silhuetas "???" e espécies por aquário
- Tema: o que o aquário "diz" (cuidar vs. explorar) e como aparece em economia e visual
- Legibilidade: números enormes e variantes de peixe claros em qualquer estágio (inclui daltonismo)

**Fora do núcleo por ora ([talvez] para depois do MVP):**
- Eventos aleatórios, verbos novos por estágio, cruzamento de peixes com genes,
  cena final, modo livre pós-final

**Convenções de captura:**
- Toda ideia recebe número (#001...) e marca [manter] / [cortar] / [talvez] na revisão
- Cada rodada fecha com 2 a 3 decisões candidatas (pilares) para o game brief

**Focus Areas:**
- Loop principal: comprar peixes, gerar dinheiro, comprar aquário novo, prestigiar
- Fantasia do jogador: cuidar do aquário e vê-lo crescer até um aquário gigante
- Economia: custo exponencial por cópia, renda por espécie, capacidade por aquário, simulador para equilíbrio
- Prestígio: o que reseta, o que persiste, loja de prestígio (aceleradores, bônus de renda,
  desconto em aquários) e quando compensa reiniciar
- Coleção: bestiário e peixes raros fantasiosos desbloqueados por aquário
- Estética e game feel: salto visual a cada aquário, peixes, bolhas, sons
- Direção de arte pixel art na Unity, palette swap para variantes baratas
- Ideias de protótipo: vertical slice da semana 1 (1 tanque, 5 espécies, 1 raro,
  progresso offline e save), tanque com 3 peixes, glossário de uma página

**Questões em aberto:**
- Offline: Murilo prefere um limite não muito grande (valor exato a definir no simulador; a loja de prestígio pode aumentá-lo). Falta saber se os sufixos temáticos de número agradam (rodada 0)
- Como combinar os três tipos de item da loja sem quebrar a economia? (rodada 3, com simulador)
- Quantos aquários e espécies cabem no MVP de um dev solo? (rodada 4)

---

## Ideas Generated

_Marcar [manter] / [cortar] / [talvez] na revisão. [decidido] = adotada pelo Murilo durante a sessão._

### Rodada 0: Fundamentos técnicos

**[Fundamentos #001]**: Números com sotaque do mar
_Core Loop_: Notação abreviada (K, M...) com sufixos temáticos do mar; botão alterna para notação clássica ou científica.
_Novelty_: O contador vira parte do tema sem perder legibilidade (daltonismo e leitura).

**[Fundamentos #002]**: Maré de volta
_Core Loop_: Ao reabrir, o aquário entrega a renda acumulada fora, com teto de horas, numa tela "enquanto você estava fora". Relógio do sistema confiável, com trava para tempo negativo.
_Novelty_: O retorno vira recompensa, e o teto offline pode ser estendido na loja de prestígio.

**[Fundamentos #003]**: Save com cofre
_Core Loop_: Autosave periódico, backups rotativos e código copiável de exportar e importar.
_Novelty_: Protege de save corrompido e resolve backup e troca de PC sem servidor.

**[Fundamentos #004]**: Memória do aquário
_Core Loop_: No prestígio a run reseta, mas bestiário, estatísticas e loja de prestígio permanecem.
_Novelty_: A coleção vira memória permanente; o save separa "estado da run" de "estado permanente".

**[Fundamentos #005]**: Planilha vira aquário
_Core Loop_: Custos, rendas, espécies e itens da loja em CSV; uma ferramenta do Editor da Unity gera os ScriptableObjects.
_Novelty_: Ajustar o equilíbrio sem mexer em código, ligado ao simulador de economia.

**[Fundamentos #006]**: Mesma fórmula, dentro e fora
_Core Loop_: Economia em passos fixos online; o offline usa a mesma fórmula em forma fechada (renda x tempo).
_Novelty_: Online, offline e simulador dão o mesmo resultado.

**[Fundamentos #007]**: Janela de segunda tela
_Core Loop_: Sem foco, o jogo cai para poucos quadros por segundo e continua rodando; funciona em janela pequena.
_Novelty_: Respeita a CPU do jogador e reforça o aquário como companhia de segundo monitor.

### Rodada 2: Loop e economia

**[Economia #008]**: Quem paga é o peixe [decidido]
_Core Loop_: Cada peixe gera renda e o jogador vê a moeda ou bolha saindo dele; mais peixes e espécies melhores, mais dinheiro. O aquário não gera renda.
_Novelty_: A renda tem rosto: o jogador sabe de onde vem cada centavo.

**[Economia #009]**: Cardume com contador [decidido]
_Core Loop_: A tela mostra até N peixes animados; o resto vira contador ("x1.2K").
_Novelty_: Resolve a performance e vira marca visual do jogo.

**[Economia #010]**: Todo peixe encarece [decidido]
_Core Loop_: O custo da n-ésima cópia é a base multiplicada por uma razão crescente (costuma ficar entre 1,07 e 1,15; valor final sai do simulador), inclusive para o peixe barato.
_Novelty_: O peixe barato é útil no começo, mas subir de espécie sempre compensa.

**[Loop #011]**: Ritual da comida [decidido]
_Core Loop_: O jogador solta comida, o cardume corre e come, bolhas sobem. Sem efeito na renda: é só gesto visual.
_Novelty_: Único toque direto no jogo, puro game feel e sem pressão de clicar.

**[Loop #012]**: Degraus de espécie
_Core Loop_: Cada aquário libera cerca de cinco espécies em degraus, com custo e renda base bem maiores a cada degrau.
_Novelty_: A progressão tem forma visível: o jogador sempre sabe qual é o próximo peixe desejado.

**[Loop #013]**: Comprar em lote
_Core Loop_: Botões x1, x10, x100 e "máx" por espécie, com o custo total à vista.
_Novelty_: Qualidade de vida obrigatória com custo exponencial por cópia.

**[Loop #014]**: Cardume completo
_Core Loop_: Em 25, 50 e 100 cópias de uma espécie, ela ganha multiplicador fixo de renda e uma formação visual nova do cardume.
_Novelty_: Recompensa previsível, sem sorteio, ligando quantidade a visual.

**[Loop #015]**: Biólogo automático
_Core Loop_: Item da loja de prestígio que compra peixes sozinho dentro de regras simples.
_Novelty_: Alivia o clique repetitivo nas runs seguintes e dá motivo concreto para prestigiar.

**[Loop #016]**: Tempo de retorno visível
_Core Loop_: Cada compra mostra "paga-se em X minutos".
_Novelty_: A economia vira decisão legível, alinhada ao simulador.

**[Economia #017]**: A parede da capacidade
_Core Loop_: Com o aquário cheio a renda para de crescer; a saída é juntar dinheiro para o próximo aquário. Antes, o jogador decide entre encher e poupar.
_Novelty_: Cria um ponto de decisão natural, sem "falha" no jogo.

**[Economia #018]**: Cota por espécie ou por tanque
_Core Loop_: O limite pode ser total de peixes ou cota por espécie.
_Novelty_: Cota por espécie força variedade (resolvida em #020).

**[Economia #019]**: O aquário que se paga
_Core Loop_: Cada aquário novo custa uma fração fixa do que o anterior rendia numa janela de tempo.
_Novelty_: O preço nasce da renda, e o balanceamento vira uma única régua.

**[Economia #020]**: Cota dupla [decidido]
_Core Loop_: Cada aquário tem total de vagas e cada espécie tem cota própria; a UI mostra vagas ocupadas e livres.
_Novelty_: A cota máxima coincide com o último marco do cardume completo (#014).

**[Progressão #021]**: Peixe lendário no fim de cada aquário
_Core Loop_: A última espécie de cada aquário é a "fantasiosa": a mais cara, meta de várias horas, comprada (não sorteada).
_Novelty_: Cada aquário tem um grande objetivo próprio, que dá forma ao ritmo longo sem eventos.

**[Progressão #022]**: Ritmo em camadas
_Core Loop_: Recompensas em escalas de tempo: minutos (comprar peixe), horas (cardume ou espécie nova), muitas horas (aquário novo e lendário).
_Novelty_: Evita o tédio da run longa.

**[Economia #023]**: Offline que rende menos
_Core Loop_: O offline paga uma fração da renda online; a loja de prestígio sobe o percentual e o teto de horas.
_Novelty_: Quem joga e quem deixa rodando recebem de forma diferente; o prestígio melhora o offline aos poucos.

**[Escopo #024]**: Famílias de espécies com palette swap
_Core Loop_: Espécies do mesmo degrau compartilham o sprite base com paletas diferentes; só o lendário tem desenho e animação próprios.
_Novelty_: Jogo bonito e variado sem dezenas de sprites feitos do zero.

**[Progressão #025]**: Sala de aquários [decidido]
_Core Loop_: Vários aquários coexistem numa sala vista lado a lado; clicar dá zoom num tanque. O aquário gigante pode ser o auge da sala.
_Novelty_: O progresso de longo prazo é espacial e visível.

**[Estética #026]**: Águas diferentes [decidido]
_Core Loop_: Cada aquário tem tipo de água (doce, salgada, recife, abissal...) com espécies, paleta e ambiente próprios.
_Novelty_: Variedade visual sem sistema novo.

**[Progressão #027]**: O antigo vira coadjuvante, não lixo
_Core Loop_: Cada aquário novo dá bônus pequeno e permanente (na run) a todos os anteriores.
_Novelty_: A obsolescência vem com graça e o jogador não abandona os tanques antigos.

**[Progressão #028]**: Tanque completo
_Core Loop_: Ao encher todas as cotas e completar o cardume, o tanque ganha selo e bônus fixo e deixa de pedir decisões.
_Novelty_: Fecha cada tanque com uma conquista e reduz a carga de decisão.

**[Interface #029]**: Painel de melhores compras
_Core Loop_: Lista global das melhores compras em todos os tanques, ordenada por tempo de retorno, com atalho de compra.
_Novelty_: Mantém a decisão legível com muitos tanques.

**[Técnica #030]**: Só o tanque em foco anima
_Core Loop_: Só o tanque na tela é animado; os outros rodam na fórmula e aparecem como miniaturas de poucos quadros por segundo.
_Novelty_: Viabiliza 8 ou mais tanques num jogo Unity feito por uma pessoa só.

### Rodada 1: Fantasia e game feel (colecionador + maravilha do oceano)

**[Fantasia #031]**: Descoberta da espécie
_Core Loop_: Ao comprar uma espécie pela primeira vez, a silhueta "???" vira o peixe colorido com ficha (nome, bioma, curiosidade). Lendários ganham entrada especial com feixe de luz, bolhas e música.
_Novelty_: A compra vira descoberta mesmo sem sorteio.

**[Estética #032]**: Oceano que respira
_Core Loop_: Luz que muda com dia e noite do relógio real, correntes, plâncton e peixes de fundo fora da economia; algumas espécies brilham à noite.
_Novelty_: O tanque é agradável mesmo antes do primeiro peixe.

**[Estética #033]**: Escala de maravilha
_Core Loop_: Peixes de tamanhos muito diferentes, com parallax em camadas; no aquário final uma baleia de pixel ocupa a tela.
_Novelty_: Sensação de escala numa tela 2D, mais custo de arte que de sistema.

**[Game feel #034]**: Juice calmo
_Core Loop_: Renda vira bolhas douradas que sobem e somem, números sobem com easing suave, compras com "plim" discreto, sem tremor de tela.
_Novelty_: Feedback contemplativo em vez do juice de caça-níquel do gênero.

**[Colecionador #035]**: Modo foto
_Core Loop_: Botão esconde a interface e libera zoom e câmera livre, gerando foto em alta resolução com moldura de colecionador.
_Novelty_: Dá ao colecionador algo para mostrar, a custo baixo.

**[Estética #036]**: Trilha que cresce com a coleção
_Core Loop_: Cada tipo de água tem ambiente sonoro, e novas camadas de som entram com a quantidade de peixes e espécies.
_Novelty_: O áudio também comunica o progresso.

**[Colecionador #037]**: Álbum completo
_Core Loop_: Bestiário em páginas por tanque; completar uma página dá bônus pequeno e permanente que persiste no prestígio.
_Novelty_: A coleção vira meta de longo prazo e motivo para reiniciar sem perder o que foi descoberto.

### Rodada 3 — Progressão e prestígio

**[Prestígio #038]**: O gigante como carta de despedida
_Core Loop_: Comprar o penúltimo aquário libera o botão de prestígio. O aquário gigante (último) continua à venda: quem prestigia cedo reinicia rápido; quem insiste e compra o gigante ganha uma recompensa de Pérolas bem maior. [decidido: gatilho no penúltimo; gigante = último tanque da run, jogável até o fim]
_Novelty_: A tensão "reiniciar agora ou perseguir o sonho" nasce da própria sala, sem evento nem sorteio.

**[Prestígio #039]**: Pérolas
_Core Loop_: Moeda de prestígio ganha ao reiniciar, suavizada (algo como raiz da renda total da run), mais um bônus por álbuns completos. Ganho mostrado antes de confirmar, para o jogador decidir quando vale.
_Novelty_: Tema marinho consistente (pérola nasce da pressão do tempo) e a fórmula é uma só linha, fácil de simular.

**[Prestígio #040]**: Loja da maré
_Core Loop_: Três prateleiras: aceleradores (mais rápido), renda (mais dinheiro por peixe) e descontos (aquários mais baratos). O primeiro item é barato e perceptível, para o primeiro prestígio já fazer diferença.
_Novelty_: Separar por prateleira deixa a loja legível e dá ao simulador três alavancas independentes para equilibrar.

**[Colecionador #041]**: Sala que lembra
_Core Loop_: Após o prestígio, a sala volta vazia, mas com silhuetas translúcidas das espécies já descobertas nos tanques; recomprar uma "acende" a silhueta.
_Novelty_: O reinício vira reconstrução de uma coleção que você já conhece, em vez de começar do zero.

**[Prestígio #042]**: Gigante que cresce entre runs [talvez, pós-MVP; Murilo escolheu o gigante como último tanque da run]
_Core Loop_: Pérolas também financiam obras no aquário gigante, que persiste entre runs: vidro, rochas, recife, túnel. Cada obra é visível e dá um bônus pequeno.
_Novelty_: A fantasia original (construir um aquário gigante) vira a meta de longo prazo do ciclo, e o prestígio tem rosto.

**[Estética #043]**: Cerimônia de prestígio
_Core Loop_: Ao confirmar, a câmera se afasta e mostra a sala inteira, uma maré leva os peixes, as Pérolas são contadas uma a uma e a sala fica vazia.
_Novelty_: O reinício deixa de ser um botão frio e vira o momento mais bonito do jogo.

**[Prestígio #044]**: Termômetro de reinício
_Core Loop_: Um indicador compara o ganho de Pérolas por hora agora com o histórico da run; quando a curva achata, acende "boa hora para reiniciar".
_Novelty_: Responde a pergunta clássica do incremental ("quando prestigiar?") sem tutorial.

**[Progressão #045]**: Ciclos que encurtam
_Core Loop_: Com a loja, cada run seguinte passa pelos mesmos aquários mais rápido, até um piso. A primeira run é a longa; as seguintes viram "reconstrução".
_Novelty_: Duração da run vira parâmetro de design validado no simulador, não acaso.

**[Economia #046]**: Níveis com teto suave
_Core Loop_: Cada item da loja tem níveis com custo crescente e efeito com retorno decrescente; cada prateleira (aceleradores, renda, descontos) tem teto próprio.
_Novelty_: Resolve de saída o risco de combinar os três tipos sem quebrar a economia.

**[Falha #047]**: Estagnação é a única falha
_Core Loop_: Não há game over. A "falha" é a parede de renda; o antídoto é o próximo degrau sempre visível: "faltam X para o próximo peixe", e a silhueta do peixe do próximo aquário aparece no atual.
_Novelty_: Falha sem punição, só desejo adiado.

**[Falha #048]**: Parede amiga
_Core Loop_: Quando a progressão desacelera, o jogo sugere uma saída (comprar em lote, trocar de tanque, prestigiar) em vez de bloquear.
_Novelty_: A dica surge do estado do jogo, nunca de tutorial ou de monetização.

**[Colecionador #049]**: Jarra de Pérolas
_Core Loop_: As Pérolas acumuladas ficam numa jarra visível na sala, que enche entre runs. [talvez]
_Novelty_: Moeda abstrata vira objeto de colecionador.

**[Prestígio #050]**: Prestígio por tanque
_Core Loop_: Dá para esvaziar só um aquário antigo em troca de Pérolas parciais. [talvez, fora do núcleo]
_Novelty_: Reinício em escala menor, mas dobra a complexidade da economia.

### Rodada 4 — Mutações e escopo

**[Escopo #051]**: Um tanque, vários dados
_Core Loop_: Existe uma única cena/prefab de tanque; cada aquário é um ScriptableObject (fundo, tipo de água, paleta, capacidade, espécies, preço). Criar o aquário 8 é preencher dados, não programar.
_Novelty_: O custo de adicionar aquários cai a quase só arte e balanceamento.

**[Escopo #052]**: Protótipo em um tanque, depois em dois passos
_Core Loop_: Passo 1: um único tanque com cerca de 5 espécies, custo exponencial por cópia, renda, progresso offline e save; serve só para sentir o loop. Passo 2 (depois de aprovado): segundo tanque, compra de aquário e prestígio com um item de loja.
_Novelty_: O loop de comprar peixe é validado antes de gastar tempo com prestígio e vários tanques. [decidido: Murilo prefere protótipo menor]

**[Escopo #053]**: Arte provisória no protótipo, arte própria no jogo real
_Core Loop_: No protótipo, as espécies podem ser formas simples e a mesma silhueta com outra paleta (palette swap), só para testar a economia. No jogo real, cada espécie tem aparência própria e diferente; o palette swap fica restrito a variantes baratas dentro da mesma família.
_Novelty_: O orçamento de arte cresce por ondas, um tanque por vez, depois que a economia daquele tanque estiver fechada. [corrigido por Murilo: o jogo real quer vários peixes realmente diferentes]

**[Escopo #054]**: Congelador de escopo
_Core Loop_: Lista escrita do que está fora do MVP (modo foto, trilha em camadas, prestígio por tanque, gigante permanente, jarra de Pérolas), revisada ao fim de cada sprint.
_Novelty_: Um dev solo só mantém o ritmo se o "não agora" estiver registrado.

**[Qualidade #055]**: Bot jogador no editor
_Core Loop_: Um script simula um jogador que sempre compra a melhor opção e registra quanto tempo leva cada aquário e cada run.
_Novelty_: A curva de ritmo longo (várias horas por run) é medida em minutos de simulação, antes de qualquer arte.

**[Qualidade #056]**: Telemetria local
_Core Loop_: O jogo grava em arquivo o tempo gasto por tanque e por run, para comparar com o simulador durante os playtests.
_Novelty_: Dá dados reais ao ajuste de balanceamento sem backend.

**[Mashup #057]**: Incremental + museu de curadoria
_Core Loop_: Cada espécie descoberta ganha uma plaquinha de museu com nome e curiosidade; completar uma sala de aquários gera uma "exposição".
_Novelty_: Reforça a fantasia de colecionador sem nenhuma mecânica nova.

**[Mashup #058]**: Incremental + papel de parede vivo
_Core Loop_: Uma janela pequena, sempre no topo e sem borda, mostra só o tanque em foco enquanto o jogador trabalha em outra coisa.
_Novelty_: Resolve o ritmo longo (jogo aberto o dia todo) tornando o jogo uma companhia, não uma tarefa.

**[Remix #059]**: Cookie Clicker sem clique
_Core Loop_: Pega-se o Cookie Clicker e remove-se o clique ativo: o único gesto é alimentar, e ele é só visual. Toda a graça está em escolher o que comprar.
_Novelty_: Testa se a escolha de compra e a beleza do tanque seguram o jogo sozinhas.

**[Acessibilidade #060]**: Raridade por forma
_Core Loop_: Raridade e variante se distinguem por forma e brilho, não só por cor (moldura, partícula, tamanho).
_Novelty_: Mantém a leitura clara para daltonismo, em qualquer estágio.

**[Escopo #061]**: Espécies e tanques em CSV
_Core Loop_: Duas planilhas (`dados/species.csv` e `dados/tanks.csv`) guardam nome, família, raridade, custo base, razão de custo, renda base, cota, sprite-base, paleta e condição de liberação. Um importador na Unity transforma cada linha em ScriptableObject. Ajustar a economia é editar a planilha.
_Novelty_: Balanceamento e conteúdo viram dados, sem recompilar. Os arquivos estão em `_bmad-output/dados/`.

**[Qualidade #062]**: Primeiro resultado do bot (tanque 1, valores provisórios)
_Core Loop_: Com 5 espécies, razão de custo 1,15 e marcos de cardume x2 em 25/50/100 cópias, o bot compra o lendário (Disco Dourado) em cerca de 50 minutos de jogo e entra numa parede de cópias depois de ~1,5 hora. Ao fim de 1 hora a renda já seria suficiente para comprar um tanque de 2 milhões em ~10 minutos, o que é barato demais para o ritmo longo.
_Novelty_: O primeiro achado do simulador: o preço do segundo aquário precisa ser muito maior (rascunho passou para 50 milhões). Números provisórios, a calibrar.

---

## Themes and Patterns

1. **O peixe é o motor, o aquário é o palco.** Renda só vem de peixes (#008, #010); o aquário é visual, capacidade e vitrine (#025, #026, #030). A progressão é "comprar mais e melhores peixes".
2. **Colecionar dá sentido ao crescimento.** Bestiário, descoberta, álbuns, silhuetas que sobrevivem ao prestígio e plaquinhas de museu (#031, #037, #041, #057) respondem à fantasia "colecionador + maravilha do oceano".
3. **Contemplativo, sem pressão.** Alimentar é só visual, nada é sorteado, não há game over; a única "falha" é a parede de renda, e o jogo oferece saídas (#011, #034, #047, #048).
4. **Um ciclo claro e simples.** Peixes → dinheiro → aquário novo → penúltimo libera o prestígio → Pérolas e loja da maré → nova run; o gigante é o último tanque da run (#038–#040, #046).
5. **Tempo longo sem punir quem sai.** Progresso offline com limite pequeno, mesma fórmula dentro e fora do jogo, janela pequena sempre no topo (#002, #006, #007, #058).
6. **Dados em vez de código.** Espécies e tanques em CSV, ScriptableObject por linha, simulador e bot para balancear (#005, #051, #055, #061, #062).
7. **Escopo de dev solo protegido.** Protótipo de um tanque, arte provisória, congelador de escopo e ondas de arte por tanque (#024, #052–#054).

## Promising Combinations

- **#010 + #009 + #014 (custo exponencial, cardume com contador e marcos de cardume):** é o coração da economia; os marcos dão metas curtas e o contador resolve a performance de milhares de peixes.
- **#038 + #039 + #040 + #046 (penúltimo libera prestígio, Pérolas, loja da maré e tetos suaves):** o ciclo inteiro de prestígio, com as três prateleiras equilibradas por teto.
- **#021 + #031 + #037 (lendário no fim do tanque, descoberta e álbum):** cada aquário termina com um momento de conquista que alimenta a coleção permanente.
- **#051 + #061 + #055 (um tanque, vários dados; CSV; bot):** o fluxo de desenvolvimento: editar a planilha, rodar o bot, ajustar, importar na Unity.
- **#007 + #058 + #002 (segunda tela, janela sempre no topo, maré de volta):** sustenta o ritmo longo sem exigir sessões longas.

---

## Session Summary

### Most Promising Concepts

**Top Pick: Sala de aquários de colecionador (peixe como motor da renda)**
Reúne a fantasia (colecionador + maravilha do oceano), a economia (custo exponencial por cópia, cota dupla, cardume com contador) e o visual (um salto a cada tanque). É o que torna o jogo reconhecível e é o que o protótipo precisa provar.

**Runner-up: Prestígio com Pérolas e loja da maré**
Com o gatilho no penúltimo aquário e o gigante como último tanque da run, o ciclo tem começo, meio e fim. Tetos suaves por prateleira reduzem o risco de quebrar a economia.

**Honorable Mention: Fluxo guiado por dados (CSV, bot, telemetria)**
Não é uma mecânica, mas é o que deixa um dev solo calibrar um jogo de várias horas por run. Já existem `species.csv`, `tanks.csv` e `sim_economia.py` em `_bmad-output/dados/`.

### Key Insights

- O jogo é contemplativo por escolha: sem sorteio, sem eventos, sem game over. Isso simplifica o design e aumenta a importância do visual.
- O ritmo longo não se resolve com "mais tempo", e sim com preços de tanque muito maiores que a renda do tanque anterior; o primeiro resultado do bot já mostrou isso (#062).
- O gigante como último tanque (e não obra permanente) mantém o escopo menor; a versão permanente ficou como [talvez].
- No jogo real os peixes são visualmente diferentes; palette swap só em variantes baratas (#053).

### Recommended Next Steps

1. Criar o game brief a partir desta sessão (`gds-create-game-brief`), com os três pilares: o aquário bonito é o produto, colecionar é o motor, loop simples e equilibrado por baixo.
2. Construir o passo 1 do protótipo na Unity: um tanque, 5 espécies importadas do CSV, custo exponencial, renda, progresso offline e save.
3. Voltar ao simulador com mais espécies e os tanques 2 e 3 para calibrar o ritmo longo e a loja de prestígio.

## Revisão do Murilo (sugestão do facilitador, a confirmar)

Marcação sugerida para cada ideia. Mude à vontade para [manter] / [cortar] / [talvez].

- **[manter]:** #001–#003, #005, #006, #008–#011, #013, #014, #016, #017, #020, #021, #024–#026, #029–#031, #034, #037–#041, #043, #044, #046–#048, #051–#055, #060, #061
- **[talvez]:** #004, #007, #012, #015, #018, #019, #022, #023, #027, #028, #032, #033, #035, #036, #042, #045, #049, #050, #056–#059, #062
- **[cortar]:** nenhuma por enquanto. #018 e #019 foram superadas por #020 e pelo modelo de renda dos peixes, então podem ser cortadas.

---

## Session Complete

**Date:** 2026-10-09
**Participant:** Murilo

### Output

This brainstorming session generated:

- 62 raw ideas
- 14 developed concepts (decisões travadas e combinações promissoras)
- 7 emerging themes

### Document Status

Status: Complete
Steps Completed: [1, 2, 3, 4]
