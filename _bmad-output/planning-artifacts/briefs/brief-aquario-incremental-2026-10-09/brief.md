---
title: 'Game Brief: Aquário Incremental'
status: draft
created: '2026-10-09'
updated: '2026-10-09'
---

# Game Brief: Aquário Incremental

> Rascunho em modo rápido. Trechos marcados com `[ASSUMPTION]` são inferências do facilitador a partir da sessão de brainstorming (`_bmad-output/brainstorming-session-2026-10-09.md`) e precisam da sua confirmação. O nome é provisório.

## Executive Summary

Aquário Incremental é um jogo incremental (idle) para PC, feito na Unity, em que o jogador monta uma sala de aquários e a vai enchendo de peixes cada vez mais raros e bonitos. A renda vem dos peixes, nunca do aquário: cada espécie comprada gera dinheiro, o dinheiro compra mais peixes e, depois, aquários novos, cada um com um tipo de água e um salto visual próprios.

A experiência é contemplativa. Não há sorteio, eventos nem game over; alimentar os peixes é só um gesto visual. O prazer vem de ver o aquário crescer, de completar a coleção e de decidir o que comprar. Cada run passa por vários aquários e termina no aquário gigante. O penúltimo aquário libera o prestígio, que dá Pérolas para a loja da maré e acelera a run seguinte.

O jogo é pensado para uma única pessoa desenvolver (Murilo, solo), com economia em planilha e prototipagem em etapas pequenas.

## Vision

**Frase central:** um incremental contemplativo em que você se torna o colecionador de uma sala de aquários, vendo cada tanque ficar mais bonito e mais raro que o anterior.

**Fantasia do jogador:** colecionador e maravilha do oceano.

**Sensação ao sair:** a de ter construído algo bonito aos poucos, sem pressa e sem culpa por ter deixado o jogo aberto.

**Assinatura:** o aquário bonito é o produto. Cada tanque tem um salto visual claro.

## Target Players & Market

**Público principal `[ASSUMPTION]`:** adultos e jovens adultos que já jogam incrementais e gostam de jogos tranquilos para deixar numa segunda tela ou numa janela pequena; sessões curtas e frequentes, com o jogo aberto por horas.

**Público secundário `[ASSUMPTION]`:** quem gosta de colecionar e de jogos "aconchegantes" (cozy), mesmo sem experiência com incrementais.

**Mercado `[ASSUMPTION]`:** o gênero é lotado de clones de Cookie Clicker. O espaço aberto é um incremental que seja visualmente bonito e contemplativo, com economia limpa e sem monetização agressiva. Não há pesquisa de mercado feita ainda.

## Core Fundamentals

**Gênero:** incremental / idle com prestígio.

**Loop principal:** comprar peixes → peixes geram dinheiro → comprar mais peixes e, depois, um aquário novo → ao chegar ao penúltimo aquário, o prestígio fica disponível → reiniciar com Pérolas e a loja da maré → chegar de novo ao aquário gigante, que é o último.

**Pilares:**
1. **O aquário bonito é o produto.** Salto visual a cada tanque; arte e animação calmas importam mais que qualquer mecânica extra.
2. **Colecionar é o motor.** Bestiário, descoberta de espécies e álbuns completos dão sentido ao crescimento.
3. **Loop simples e equilibrado por baixo.** Sem sorteio, sem eventos, sem game over; a economia é testada em simulador antes de virar conteúdo.

**Mecânicas principais:**
- O custo de cada peixe cresce exponencialmente por cópia comprada, inclusive o peixe barato.
- Limite por aquário e cota por espécie.
- Exibição: até N peixes animados; o resto vira contador ("x1.2K").
- Vários aquários coexistem; os antigos continuam rendendo, mas perdem peso relativo.
- Prestígio liberado no penúltimo aquário; a loja da maré vende aceleradores, bônus de renda e desconto em aquários, com teto suave por prateleira.
- Progresso offline com limite pequeno.
- Ritmo longo: várias horas a dias por run, 8 ou mais aquários.

## References & Differentiation

Os comparáveis abaixo são `[ASSUMPTION]`; o que se pega e o que não se pega vem do brainstorming.

- **Cookie Clicker:** pegamos custo exponencial por cópia e marcos de quantidade; não pegamos o clique ativo nem os eventos aleatórios.
- **AdVenture Capitalist:** pegamos a escada de negócios (aqui, espécies e aquários) e o prestígio; não pegamos a estética de interface de planilha.
- **Neko Atsume:** pegamos o prazer de colecionar e a contemplação; não pegamos a falta de progressão econômica.
- **Egg, Inc.:** pegamos o crescimento visual da granja e a longa duração; não pegamos a pressão por sessões ativas.

**Diferenciais:** a renda vem apenas dos peixes (o aquário é palco e capacidade); a fantasia é de colecionador, com um salto visual por aquário; e o gigante é o fim de cada run. Se o jogo vai se destacar, será pela execução visual e pela clareza da economia, não por tecnologia.

## Scope & MVP

**Plataforma:** PC (Unity). **Equipe:** solo. **Prazo e orçamento:** não definidos.

**Estratégia:** protótipo primeiro, em dois passos.

**Passo 1 do protótipo (MVP que valida a hipótese central):** um único tanque com cerca de 5 espécies, custo exponencial por cópia, renda, cota, progresso offline e save. A hipótese é: comprar peixes e vê-los se acumular já é divertido por si só.

**Passo 2 (só depois de aprovar o passo 1):** segundo tanque, compra de aquário e prestígio com um item de loja.

**Dados:** espécies e tanques em planilha (`species.csv` e `tanks.csv`), com um simulador (`sim_economia.py`) para calibrar o ritmo antes de produzir arte.

**Fora do MVP:** modo foto, trilha sonora em camadas, prestígio por tanque, jarra de Pérolas, gigante permanente.

## Content & Direction

**Mundo e narrativa:** sem enredo. A narrativa é a coleção que cresce.

**Conteúdo `[ASSUMPTION]`:** 8 ou mais aquários na versão completa, com cerca de 5 espécies cada. Na versão completa os peixes são visualmente diferentes; palette swap só em variantes baratas dentro de uma família. A arte entra em ondas, um tanque por vez, depois que a economia daquele tanque estiver fechada.

**Arte `[ASSUMPTION]`:** pixel art 2D, com visual calmo e bonito; no protótipo, formas simples provisórias.

**Áudio `[ASSUMPTION]`:** ambiente sonoro por tipo de água, com camadas que crescem com a coleção (pós-MVP).

## Risks & Open Questions

- **Ritmo longo vs. escopo solo:** 8 ou mais aquários exigem muita arte. Mitigação: protótipo menor, arte em ondas e dados em planilha.
- **Economia desequilibrada:** o primeiro resultado do simulador já mostrou que o segundo tanque estava barato demais; os preços atuais são chutes. Mitigação: calibrar com o bot antes de produzir conteúdo.
- **Combinar as três prateleiras da loja sem quebrar a economia:** tetos suaves por prateleira, validados em simulação.
- **Muitos peixes na tela:** contador e limite de animados; só o tanque em foco anima.
- **Mercado saturado:** sem pesquisa feita. Definir o posicionamento com cuidado antes de produzir arte final.
- **Em aberto:** nome definitivo; limite exato do progresso offline; sufixos temáticos de número; prazo.
