# Addendum — Game Brief: Aquário Incremental

Material de apoio que não cabe no brief (1 a 2 páginas).

## Alternativas descartadas ou adiadas
- Aquário como fonte de renda (ideia inicial): substituída por "a renda vem dos peixes" (decidido).
- Gigante permanente que cresce entre runs (#042): adiado ([talvez], pós-MVP).
- Prestígio por tanque (#050) e jarra de Pérolas (#049): adiados.
- Alimentar com efeito na renda: descartado; alimentar é só visual.

## Economia (valores provisórios do protótipo, tanque 1)
- Espécies: Lebiste (custo base 10, renda 0,1/s), Tetra Neon (120, 1), Betta (1.400, 8), Acará-bandeira (16.000, 60), Disco Dourado (190.000, 450); razão de custo 1,15; marcos de cardume x2 em 25/50/100 cópias.
- Primeiro resultado do bot: lendário em ~50 min de jogo; parede de cópias depois de ~1,5 h; segundo tanque a 2 milhões saía barato demais (rascunho subiu para 50 milhões; gigante, 5 bilhões).
- Arquivos: `_bmad-output/dados/species.csv`, `tanks.csv`, `sim_economia.py`.

## Prestígio (rascunho)
- Moeda: Pérolas, ganho suavizado (algo como raiz da renda total da run) mais bônus por álbum completo.
- Loja da maré: aceleradores, bônus de renda e desconto em aquários; níveis com retorno decrescente e teto por prateleira.
- Persiste: bestiário, estatísticas e loja. Reinicia: peixes, dinheiro e aquários.
