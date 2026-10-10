# 01 — Fundação

Cada entrada: o que mudou, quais cenas regenerar, se precisa `Create Default Data`, o que bot/CSV fazem com isso, e o que foi/não foi verificado (compilado com csc vs Test Runner vs visto no Editor).

## C-01 Unity instalado (2026-10-09), feito
- Atualização: módulo IL2CPP confirmado (variações `win64_player_*_il2cpp` presentes). Resta só conferir se 6000.6 é LTS (D-01). Templates locais no Editor: `2d-cross-platform-2d 7.0.0` e `urp-blank 17.2.1`.

### Verificação inicial (parcial)
- O que mudou: nada no projeto; só verificação da máquina.
- Encontrado: Unity Hub e Editor `6000.6.2f1` (em `C:/Program Files/Unity/Hub/Editor/`), módulos Windows (Mono) e WebGL. Git 2.52 e git-lfs 3.7.1 instalados.
- Falta: módulo Windows Build Support (IL2CPP) pelo Unity Hub (Installs, engrenagem, Add modules); confirmar se a versão é LTS (D-01).
- Cenas / `Create Default Data` / bot-CSV: não se aplica.
- Verificado: só listagem de pastas; Editor não aberto.

## C-02 Projeto Universal 2D criado (2026-10-09), parcial
- O que mudou: projeto criado pelo dev (template Universal 2D, Editor 6000.6.2f1, URP 17.6.0, Input System 1.20.0, Test Framework 1.8.0, 2D Animation/Aseprite/PSD importer). O Hub criou em `aquario-incremental/aquario-incremental`; movi `Assets`, `Packages`, `ProjectSettings`, `UserSettings`, `Library`, `Logs`, `.vscode`, `.slnx` e `.csproj` para `game/` e apaguei a pasta repetida.
- Cenas / `Create Default Data` / bot-CSV: não se aplica.
- Verificado: `ProjectVersion.txt` em `game/ProjectSettings` confere (6000.6.2f1). **Não verificado:** abrir no Hub e dar Play sem erro (feito pelo dev).

## C-03 Repositório local (2026-10-09), parcial
- O que mudou: `git init -b main` na raiz `D:/aquario-incremental` (projeto Unity em `game/`, mais `_bmad`, `_bmad-output`, `.claude`, `CLAUDE.md`). Criados `.gitignore` (Unity em `game/`, Steam `steam_appid.txt`, logs) e `.gitattributes` (LFS para png/jpg/psd/aseprite/xlsx/wav/ogg/mp3/ttf/otf/mp4/fbx; YAML do Unity com `unityyamlmerge`). `git lfs install --local` feito.
- Conferido: serialização do Unity em texto (`m_SerializationMode: 2`); `git status` não lista `Library`, `Logs`, `UserSettings`.
- Cenas / `Create Default Data` / bot-CSV: não se aplica.
- Pendente (dev): primeiro commit, criar repositório privado e `git remote add origin` + push. Decidir se `.claude/` (skills BMAD) entra no repositório.
- Não verificado: `git lfs ls-files` ainda vazio porque nada foi adicionado.
