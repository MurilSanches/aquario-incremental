# Conteúdo: tanques e espécies — Aquário Incremental

Lista oficial de conteúdo do jogo completo (8 tanques × 5 espécies = 40 espécies). Detalha a seção 7 de `backlog-v1.md`.

Status: **tanque 1 = DEFINIDO** (dados reais em `_bmad-output/dados/species.csv` e `tanks.csv`). **Tanques 2 a 8 = PROPOSTA** do facilitador (nomes, temas e espécies), a confirmar pelo dev antes da onda de cada tanque (decisão T-00 do backlog). Custos/rendas/preços de 2 a 8 **não estão aqui de propósito**: saem do simulador (E-xx), nunca de chute.

## Regras de composição (valem para todos os tanques)
- 5 espécies em degraus: **comum, comum, incomum, raro, lendário** (#012). O lendário é a meta de várias horas do tanque, comprado, nunca sorteado (#021).
- Degrau de referência (tanque 1): custo base ×~12 e renda base ×~7,5 a cada espécie; razão de custo 1,15; cota 200/200/150/100/50; marcos x2 em 25/50/100 cópias.
- Desbloqueio em cadeia: `libera_apos_ter = especie_anterior:10`.
- Cada espécie tem **desenho próprio** no jogo real; palette swap só para variante barata dentro da mesma família (#053). Aqui nenhuma variante foi planejada; se virar, entra como espécie nova na mesma família.
- Cada tanque tem tipo de água, paleta e ambiente próprios, e uma resposta a "o que só este aquário tem?" (salto visual).
- Raridade distinguida por forma/brilho, não só cor (#060).
- IDs: `snake_case` sem acento (ex.: `peixe_leao`); `tanque_id` no padrão `agua_doce_01`, `agua_salgada_01`... (novo sufixo numérico por tipo de água).

## Classes de tamanho (sprite)
Valores em px dependem da decisão A-01 (bíblia de arte). Classes: **PP** (muito pequeno), **P**, **M**, **G**, **GG** (ocupa boa parte do tanque), **XL** (quase a tela, só tanque 8).

## Tanques e espécies

### Tanque 1 — Aquário Inicial · água doce · ordem 1 · DEFINIDO
`agua_doce_01`, preço 0, capacidade 400, 25 animados. Salto visual: o tanque simples e acolhedor — cascalho, plantas, água clara, luz de sala.
| # | id | Espécie | Família | Raridade | Tamanho | Custo base | Renda/s | Cota | Libera após |
|---|---|---|---|---|---|---|---|---|---|
| 1 | lebiste | Lebiste | lebiste | comum | PP | 10 | 0,1 | 200 | — |
| 2 | neon | Tetra Neon | tetra | comum | PP | 120 | 1 | 200 | lebiste:10 |
| 3 | betta | Betta | betta | incomum | P | 1.400 | 8 | 150 | neon:10 |
| 4 | acara | Acará-bandeira | acará | raro | M | 16.000 | 60 | 100 | betta:10 |
| 5 | disco_dourado | Disco Dourado | disco | lendário | M/G | 190.000 | 450 | 50 | acara:10 |

### Tanque 2 — Recife Pequeno · água salgada · ordem 2 · PROPOSTA
Nome já existe em `tanks.csv` (`agua_salgada_01`). Salto visual: primeira água salgada — azul saturado, corais pequenos, anêmona.
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | donzela_azul | Donzela-azul | donzela | comum | PP | azul elétrico, cardume denso |
| 2 | peixe_palhaco | Peixe-palhaço | palhaço | comum | P | laranja/branco, vive junto da anêmona |
| 3 | tang_azul | Tang-azul | tang | incomum | M | corpo oval, cauda amarela |
| 4 | peixe_anjo_imperador | Peixe-anjo-imperador | anjo | raro | M | listras e máscara azul, padrão rico |
| 5 | cavalo_marinho_dourado | Cavalo-marinho-dourado | cavalo-marinho | lendário | M | nada na vertical, brilho dourado, animação própria |

### Tanque 3 — Rio Amazônico · água doce plantada · ordem 3 · PROPOSTA
Salto visual: vegetação densa, troncos submersos, luz filtrada em raios, água amarronzada-esverdeada.
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | cardinal | Cardinal | tetra | comum | PP | faixa azul e vermelha, cardume |
| 2 | corydora | Corydora | corydora | comum | P | no fundo, bigodes, anda no leito |
| 3 | piranha_vermelha | Piranha-vermelha | piranha | incomum | M | dentes à mostra, ventre vermelho |
| 4 | aruana_prateada | Aruanã-prateada | aruanã | raro | G | longo, escamas grandes prateadas, nada na superfície |
| 5 | pirarucu | Pirarucu | pirarucu | lendário | GG | gigante vermelho nas escamas traseiras, animação própria |

### Tanque 4 — Recife de Coral · água salgada · ordem 4 · PROPOSTA
Salto visual: recife grande, camadas de coral colorido, cardumes cruzando.
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | peixe_borboleta | Peixe-borboleta | borboleta | comum | P | achatado, amarelo/branco, mancha-olho |
| 2 | peixe_papagaio | Peixe-papagaio | papagaio | comum | M | bico, escamas verde-azul |
| 3 | baiacu_balao | Baiacu-balão | baiacu | incomum | M | infla (animação de susto) |
| 4 | peixe_leao | Peixe-leão | leão | raro | M | barbatanas em leque, listras |
| 5 | tubarao_ponta_branca | Tubarão-de-ponta-branca | tubarão | lendário | GG | patrulha o tanque, animação própria |

### Tanque 5 — Floresta de Kelp · água fria · ordem 5 · PROPOSTA
Salto visual: algas altas que balançam, luz verde-azulada vinda de cima, fundo rochoso.
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | garibaldi | Garibaldi | donzela | comum | P | laranja vivo, único da paleta fria |
| 2 | sardinha | Sardinha-prateada | sardinha | comum | P | cardume que gira em bola |
| 3 | linguado | Linguado | linguado | incomum | M | achatado, se camufla no fundo |
| 4 | lula_vidro | Lula-de-vidro | lula | raro | M | translúcida, órgãos visíveis |
| 5 | polvo_gigante | Polvo-gigante-do-Pacífico | polvo | lendário | GG | tentáculos animados, troca de cor |

### Tanque 6 — Abismo · água abissal · ordem 6 · PROPOSTA
Salto visual: quase escuro, bioluminescência é a única luz; neve marinha caindo.
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | peixe_lanterna | Peixe-lanterna | lanterna | comum | PP | pontos de luz ao longo do corpo |
| 2 | peixe_machado | Peixe-machado | machado | comum | P | corpo prateado achatado |
| 3 | peixe_viper | Peixe-víbora | víbora | incomum | M | presas enormes, fotóforos |
| 4 | peixe_pescador | Peixe-pescador | pescador | raro | M | isca luminosa balançando |
| 5 | lula_colossal | Lula-colossal | lula | lendário | GG | olho gigante, animação própria |

### Tanque 7 — Laguna Luminosa · água fantasiosa · ordem 7 · PROPOSTA · libera o prestígio
Penúltimo tanque da sala. Salto visual: contraste noite/dia forte, águas que brilham, espécies de fantasia (maravilha do oceano).
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | agua_viva_lunar | Água-viva-lunar | água-viva | comum | P | translúcida, pulsa em azul-lua |
| 2 | peixe_cometa | Peixe-cometa | cometa | comum | P | deixa rastro de partículas |
| 3 | carpa_aurora | Carpa-aurora | carpa | incomum | M | escamas em gradiente de aurora |
| 4 | raia_estelar | Raia-estelar | raia | raro | G | constelações no dorso |
| 5 | dragao_das_mares | Dragão-das-marés | dragão-marinho | lendário | GG | serpentiforme de luz, animação própria |

### Tanque 8 — Aquário Gigante · água salgada de oceano aberto · ordem 8 · PROPOSTA · último da run
`gigante_01`, capacidade e preço a redefinir (hoje 800 / 5 bi no CSV de 3 tanques). Salto visual: escala monumental — túnel de vidro, parallax em muitas camadas, e uma baleia de pixel ocupando a tela (#033).
| # | id | Espécie | Família | Raridade | Tamanho | Nota de arte |
|---|---|---|---|---|---|---|
| 1 | atum_azul | Atum-azul | atum | comum | M | nada rápido, brilho metálico |
| 2 | tartaruga_verde | Tartaruga-verde | tartaruga | comum | G | nada lenta, casco detalhado |
| 3 | tubarao_martelo | Tubarão-martelo | tubarão | incomum | G | cabeça em T, cardume ao fundo |
| 4 | raia_manta | Raia-manta-gigante | raia | raro | GG | envergadura enorme, planeia |
| 5 | baleia_azul | Baleia-azul | baleia | lendário | XL | ocupa a tela, canto de baleia no áudio (PÓS) |

## Entregáveis por espécie (checklist de cada uma das 40)
1. Linha em `species.csv` (família, raridade, custo base, razão, renda base, cota, `sprite_base`, `paleta`, `libera_apos_ter`) — **gerada a partir do simulador**.
2. Sprite base na classe de tamanho, voltado para a direita (espelha por código), contorno e sombreamento da bíblia de arte.
3. Animações: nado (mín. 4 quadros), parado, virada, comer.
4. Formações de cardume para 25, 50 e 100 cópias (#014).
5. Raridade legível por forma/brilho/tamanho (#060).
6. Silhueta "???" e miniatura do bestiário (#031).
7. Textos: nome, bioma, curiosidade (chaves `Loc` em todos os idiomas ativos).
8. Lendário: animação de entrada (feixe de luz, bolhas, música) e animação própria extra.
9. Teste de silhueta preta: espécie reconhecível só pelo contorno; registrado em `estado/`.

## Entregáveis por tanque (checklist de cada um dos 8)
1. Fundo em 3 camadas (fundo, meio, frente) com parallax (#033).
2. Cor/textura da água, raios de luz, partículas próprias (#032).
3. Decoração fixa que sustenta o salto visual; versão "acesa" quando o tanque é completo (#028).
4. Moldura/vidro do tanque e miniatura de baixa taxa para a sala (#030).
5. Variação dia/noite (relógio real) e brilho noturno das espécies bioluminescentes.
6. Página do álbum e selo de tanque completo (#037, #028).
7. Linha em `tanks.csv` (tipo de água, ordem, preço, capacidade, `max_animados`, `libera_prestigio`) e simulação do tanque no `sim_economia.py`.
8. Textos do tanque em `Loc` (nome, descrição, página do álbum).
9. Áudio ambiente do tipo de água (PÓS).

## Volume de arte (jogo completo)
- 40 espécies com 4+ animações cada, 8 lendários com animação própria extra, 40 silhuetas e 40 miniaturas.
- 8 tanques com 3 camadas de fundo, decoração, miniatura e variação noturna.
- Ordem de produção: onda por tanque, nunca o tanque N+1 antes de fechar economia e arte do N.
