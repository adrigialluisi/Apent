# CLAUDE.md — Apent Holding LP

> Este arquivo é lido automaticamente pelo Claude Code a cada sessão.
> Contém todo o contexto necessário para trabalhar na landing page da Apent.

---

## O Projeto

Landing page institucional da **Apent Holding** — holding que integra tecnologia, dados, assessoria e gestão para o mercado de investimentos brasileiro.

**Tagline:** "Invista bem, viva melhor."

**Arquivos principais:**
- `wire/index.html` — wire funcional completo (referência de estrutura e copy)
- `hero/` — pasta com a versão mais recente do hero (hero_v6 = versão com vídeo)
- `Logos_PNG/` — logos oficiais da marca
- `font_Hanken_Grotesk/` — fonte local (usar em produção)
- `docs/` — documentos de referência

---

## Estrutura de Seções (ordem na página)

1. **NAV** — fixo, transparente → escurece no scroll
2. **HERO** — fullscreen com vídeo de fundo (ver `hero/`), overlay escuro, texto central
3. **ORIGEM** — história da empresa + timeline (2017 → 2025 → 2026)
4. **NORDIC STRIPE** — faixa decorativa multicolor (5 cores da paleta)
5. **ECOSSISTEMA** — duas colunas: Plataforma (carrossel) + Assessoria
6. **NORDIC STRIPE** — repete
7. **NÚMEROS** — 5 métricas animadas: R$3,2B · 46mil+ · +R$8B · 41% · R$10B
8. **SÓCIOS** — grid com cards do time
9. **CTA + FOOTER** — chamada final + footer

---

## Tarefa Principal: Integrar o Hero v6

O `wire/index.html` tem o hero atual com geometria SVG estática.
O `hero/` tem a versão v6 com **vídeo de fundo real**.

**O que fazer:**
1. Substituir o `<section id="hero">` do wire pelo hero do arquivo em `hero/`
2. Manter todos os CSS tokens do wire (`:root { --azul, --nyhavn... }`)
3. O hero usa vídeo local — garantir que o path do `<source src="...">` aponte para o arquivo de vídeo correto
4. Manter o `<div id="progress">` e `<nav id="nav">` acima do hero
5. Manter todos os scripts de scroll/reveal do wire intactos

**Atenção no hero:**
- Vídeo: `autoplay muted loop playsinline` (sem controles, sem som)
- Overlay: `rgba(24, 32, 40, 0.60)` sobre o vídeo
- Faixa accent-bar no bottom com as 5 cores: `#0044A2 → #00C8FF → #FBC200 → #FBC200 → #FF9E00`
- Scroll hint com linha animada abaixo do conteúdo

---

## Regras que NUNCA podem ser quebradas

1. **Cores:** usar SOMENTE as cores do brandbook (ver BRAND_COLORS.md). Nenhuma cor inventada.
2. **Dados:** usar SOMENTE informações presentes no wire ou neste arquivo. Não inventar métricas, nomes ou fatos.
3. **Fonte:** sempre `'Hanken Grotesk', sans-serif` — sem fallbacks para outras fontes serifadas.
4. **Copy:** manter o copy do wire exatamente como está. Não reescrever textos.
5. **Ícones:** usar somente Heroicons (outline style) — `npm install @heroicons/react` ou via CDN.

---

## Empresas do Grupo (não inventar outras)

### Apent Tech (cor: `#00C8FF` nyhavn)
- **Clube FII** — maior plataforma de FIIs do Brasil. +75 mil carteiras · +R$8B AUC virtual
- **White Label** — infraestrutura B2B2C para parceiros institucionais
- URL: `http://apenttech.com.br/`

### Apent Investimentos (cor: `#FF9E00` laranja)
- **Autem Investimentos** — assessoria. R$3,2B sob custódia · 46 mil+ clientes
- URL: `https://apentinvest.com.br/`

---

## Time (sócios confirmados no wire)

| Iniciais | Nome | Cargo | Área |
|----------|------|-------|------|
| FG | Felipe Guinle | Sócio & CEO | Holding |
| CP | Celson Plácido | CIO | Assessoria |
| PM | Prof. Mira | Sócio Investidor | Assessoria |

Demais slots: "A Confirmar" (placeholder com `?`)

---

## Métricas Confirmadas

| Valor | Contexto |
|-------|----------|
| R$3,2B | Sob custódia — Autem Investimentos |
| 46 mil+ | Clientes ativos |
| +R$8B | AUC virtual — Clube FII |
| 41% | Crescimento YoY 2025 |
| +75 mil | Carteiras de FII monitoradas |
| R$10B | Meta de patrimônio sob gestão |
| >50% | EBITDA margin |

---

## Fluxo de Trabalho

```bash
# Entrar na pasta do projeto
cd /Users/adrianagialluisi/Desktop/Apent

# Abrir Claude Code
claude

# Verificar arquivos disponíveis
ls -la
ls hero/
ls wire/
```

Ao receber uma tarefa, o Claude Code deve:
1. Ler este CLAUDE.md primeiro
2. Ler BRAND_COLORS.md para tokens de cor
3. Abrir `wire/index.html` para entender a estrutura existente
4. Verificar `hero/` para o código do hero_v6
5. Fazer as alterações mantendo consistência com os arquivos existentes
6. Não criar arquivos em locais diferentes sem confirmar com o usuário
