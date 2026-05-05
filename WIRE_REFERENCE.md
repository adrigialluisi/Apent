# WIRE_REFERENCE.md — Mapa do Wire

> Referência detalhada da estrutura atual do `wire/index.html`.
> Use este arquivo para entender o que existe antes de fazer qualquer alteração.

---

## Estrutura HTML (ordem das seções)

```
<div id="progress">          ← barra de progresso de scroll (nyhavn, 2px, fixed top)
<nav id="nav">               ← nav fixo, transparente → scrolled com blur
<section id="hero">          ← hero atual (SVG geométrico — será substituído por hero_v6)
<section id="origem">        ← história + timeline
<div class="nordic-stripe">  ← faixa decorativa 4px com 5 cores
<section id="ecossistema">   ← duas colunas: plataforma + assessoria
<div class="nordic-stripe">  ← repete
<section id="numeros">       ← 5 métricas animadas
<section id="socios">        ← grid de sócios
<section id="cta-footer">    ← CTA + footer
```

---

## Copy Confirmado (não alterar)

### NAV
- Wordmark: `āpent` (o "ā" com mácron, "pent" em nyhavn)
- Links: "Nossa história" → `#origem` · "O ecossistema" → `#ecossistema`
- CTA nav: "Fale conosco" → `#cta-footer`

### HERO
- Eyebrow: `APENT HOLDING`
- H1: `Invista bem,` / `viva melhor.` (em itálico/nyhavn)
- Sub: `O ecossistema financeiro que conecta tecnologia, dados e assessoria para transformar como você investe.`
- CTA: `Conheça o ecossistema` → `#ecossistema`
- Scroll hint: label `SCROLL` + linha animada

### ORIGEM
- Eyebrow: `A NOVA FASE`
- H2: `Do maior canal de FIIs do Brasil ao ecossistema completo.`
- Body: `O Clube FII construiu a maior plataforma de cobertura de Fundos Imobiliários do país. A Apent é o próximo passo — uma holding que integra tecnologia, dados, distribuição e assessoria em uma estrutura única, preparada para capturar valor em toda a cadeia do investidor.`
- Timeline:
  - 2017: "Clube FII nasce" — A principal plataforma de cobertura de Fundos Imobiliários do Brasil — construída sobre dados, análise e comunidade.
  - 2025: "Virada estratégica" — +41% de crescimento YoY. EBITDA acima de 50%. Início da vertical transacional e da solução White Label B2B2C.
  - 2026: "Nasce a Apent Holding" — A holding que integra tecnologia, assessoria e gestão. R$ 3,2B sob custódia. 46 mil clientes. Uma nova fase começa.

### ECOSSISTEMA
- Eyebrow: `O GRUPO APENT`
- H2: `Um ecossistema construído para crescer.`
- Body: `Cada frente conectada. Cada especialista no lugar certo. Da tecnologia à alocação — tudo integrado.`

#### Coluna Plataforma (cor: nyhavn `#00C8FF`)
- Tag: `PLATAFORMA`
- H3: `Tecnologia e dados em escala.`
- Sub: `Infraestrutura proprietária que conecta conteúdo, comunidade e distribuição de produtos financeiros.`
- Slide 1 — Clube FII:
  - Desc: `A principal plataforma de cobertura de FIIs do Brasil. Dados em tempo real, carteiras integradas B3 e a maior comunidade de investidores em fundos imobiliários do país.`
  - Stat: `+75 mil carteiras monitoradas · +R$ 8B em AUC virtual`
  - CTA: `Conheça mais`
- Slide 2 — Apent Tech:
  - Desc: `Infraestrutura White Label B2B2C para criação, distribuição e monetização de produtos financeiros em escala. A camada tecnológica que opera além das marcas do grupo.`
  - Stat: `White Label disponível para parceiros institucionais`
  - CTA: `Conheça mais`

#### Coluna Assessoria (cor: laranja `#FF9E00`)
- Tag: `ASSESSORIA, CONSULTORIA & GESTÃO`
- H3: `O que os grandes bancos não oferecem.`
- Sub: `Curadoria humana de ativos alternativos — para quem quer mais do que uma prateleira genérica.`
- Brand: `Autem Investimentos`
- Desc: `Assessoria que democratiza o acesso a ativos de alta qualidade. Curadoria isenta, relatórios exclusivos e atendimento contínuo — sem precisar ser do mercado financeiro.`
- Stat: `R$ 3,2B sob custódia · 46 mil+ clientes`
- CTA: `Conheça mais`

### NÚMEROS
| Valor | Label |
|-------|-------|
| +R$ 3,2B | Sob custódia · Autem |
| 46 mil+ | Clientes ativos |
| +R$ 8B | AUC virtual · Clube FII |
| 41% | Crescimento YoY 2025 |
| R$ 10B | Meta de patrimônio |

### SÓCIOS
- Eyebrow: `O TIME`
- H2: `Quem está por trás da Apent.`
- Sub: `Experiência que constrói convicção.`

| Iniciais | Nome | Cargo | Área | Avatar bg |
|----------|------|-------|------|-----------|
| FG | Felipe Guinle | Sócio & CEO | Holding | `#0044A2` |
| CP | Celson Plácido | CIO | Assessoria | `#0D3A6B` |
| PM | Prof. Mira | Sócio Investidor | Assessoria | `#B85C00` |
| ? | A Confirmar (×5) | Cargo | — | `#ccc` |

Bio CP: `Ex-Partner XP e CIO Warren Brasil. 25+ anos em gestão e asset management.`
Bio PM: `Fundador da Autem. Educador financeiro e referência em fundos imobiliários.`
Bio FG: `Liderança e visão estratégica do grupo.`

### CTA FINAL
- Eyebrow: `FALE CONOSCO`
- H2: `Invista para viver melhor. Saiba como.`
- Sub: `Conectamos você à inteligência certa para cada etapa da sua jornada. Dados, plataforma e assessoria — tudo em um ecossistema.`
- CTA: `Fale conosco` → `mailto:contato@apent.com.br`
- Provas sociais:
  - `Acesse dados reais de +75 mil carteiras de FIIs integradas à B3 via Clube FII.`
  - `Invista com assessores que já cuidam de R$ 3,2 bilhões para 46 mil clientes na Autem.`
  - `Faça parte de um grupo com a meta de chegar a R$ 10 bilhões sob gestão.`

### FOOTER
- `© 2026 Apent Holding®. Todos os direitos reservados.`
- Links: Política de Privacidade · Termos de Uso

---

## JavaScript no Wire

### Scroll Progress Bar
```js
window.addEventListener('scroll', () => {
  const el = document.documentElement;
  document.getElementById('progress').style.width =
    (el.scrollTop / (el.scrollHeight - el.clientHeight) * 100) + '%';
});
```

### Nav Scroll Effect
```js
window.addEventListener('scroll', () => {
  document.getElementById('nav').classList.toggle('scrolled', window.scrollY > 80);
});
```

### IntersectionObserver (reveal / num-item / socio-card)
- Threshold: 0.12
- Adds class `visible` (opacity + translateY)
- Delay escalonado: `i * 0.06s`

### Timeline Observer
- Threshold: 0.3
- Delay: `i * 0.15s`

### Carrossel Ecossistema
- `total = 2` slides
- Auto-avança a cada `4000ms`
- `goToSlide(n)` · `moveCarousel(dir)`

### Counter Animado (seção Números)
- Threshold: 0.4
- Duração: `1300ms`
- Ease: `1 - (1 - p)³`
- Data attributes: `data-target`, `data-prefix`, `data-suffix`

### Equalize Eco Columns
- Iguala altura das `.eco-col` em viewport > 960px
- Roda no `load`, `resize` e com `setTimeout(200)`

---

## Breakpoints Responsivos

| Breakpoint | Ajuste |
|------------|--------|
| `≤960px` | Grid origem → 1 col · eco-cols → 1 col · socios → 2 col · cta → 1 col |
| `≤600px` | socios → 2 col (gap 10px) · nav-center oculto · num-inner → coluna |
