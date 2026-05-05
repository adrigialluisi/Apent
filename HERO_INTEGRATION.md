# HERO_INTEGRATION.md — Integração do Hero v6

> Guia passo a passo para substituir o hero atual do wire pelo hero_v6 com vídeo.
> Execute exatamente nesta ordem para não quebrar o resto da página.

---

## O que é o Hero v6

O hero_v6 é a versão com **vídeo de fundo real** (arquivo `Casal.mp4` ou similar em `hero/`).

Diferenças em relação ao hero atual do wire:
- **Wire atual:** fundo `#182028` com geometria SVG estática
- **Hero v6:** vídeo `autoplay muted loop playsinline` com overlay + logo + accent-bar colorida

---

## Passo 1 — Verificar arquivos disponíveis

```bash
# Confirmar o que existe na pasta hero/
ls -la hero/

# Confirmar o nome do arquivo de vídeo
ls hero/*.mp4 hero/*.webm 2>/dev/null
```

Anotar o caminho exato do vídeo — será usado no `<source src="...">`.

---

## Passo 2 — Identificar o bloco a substituir no wire

No `wire/index.html`, localizar e marcar este bloco para substituição:

```html
<!-- HERO -->
<section id="hero">
  <svg class="hero-bg-geo" ...>
    <!-- geometria SVG estática -->
  </svg>

  <div class="hero-content">
    ...
  </div>

  <div class="hero-scroll">
    ...
  </div>
</section>
```

**NÃO remover** o que está antes (`<div id="progress">` e `<nav id="nav">`).

---

## Passo 3 — CSS do Hero v6

Adicionar estes estilos ao `<style>` do wire (ou criar `hero.css` separado).
**Remover** os estilos antigos do hero SVG (`#hero`, `.hero-bg-geo`) para evitar conflito.

```css
/* ── HERO V6 ── */
#hero {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: #182028; /* fallback enquanto vídeo carrega */
}

/* Vídeo full bleed — sem barras pretas */
.hero-video {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100vw;
  height: 56.25vw;    /* 16:9: 100vw ÷ 1.778 */
  min-height: 100vh;
  min-width: 177.78vh; /* 100vh × 1.778 */
  transform: translate(-50%, -50%);
  object-fit: cover;
  display: block;
}

/* Overlay escuro sobre o vídeo */
.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(24, 32, 40, 0.60); /* tag / 60% */
}

/* Conteúdo central */
.hero-content {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 10;
  text-align: center;
  padding: 0 32px;
  gap: 24px;
}

/* Eyebrow */
.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.30em;
  color: var(--nyhavn);
  margin-bottom: 8px;
}
.hero-eyebrow::before,
.hero-eyebrow::after {
  content: '';
  display: block;
  height: 1px;
  width: 28px;
  background: var(--nyhavn);
  opacity: 0.4;
}

/* H1 */
.hero-h1 {
  font-size: clamp(52px, 7.5vw, 96px);
  font-weight: 300;
  line-height: 1.0;
  letter-spacing: -0.04em;
  color: #fff;
  margin-bottom: 0;
}
.hero-h1 em {
  font-style: normal;
  color: var(--nyhavn);
  font-weight: 300;
}

/* Subtítulo */
.hero-sub {
  font-size: clamp(15px, 1.8vw, 19px);
  font-weight: 300;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.55);
  max-width: 520px;
}

/* CTA button */
.hero-cta {
  display: inline-block;
  background: var(--azul);
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.04em;
  padding: 17px 44px;
  border-radius: 3px;
  transition: background 0.2s;
  text-decoration: none;
  margin-top: 8px;
}
.hero-cta:hover { background: #0055cc; }

/* Scroll hint */
.hero-scroll {
  position: absolute;
  bottom: 52px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 11;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.hero-scroll-label {
  font-size: 9px;
  letter-spacing: 0.25em;
  color: rgba(255, 255, 255, 0.25);
  font-weight: 500;
}
.hero-scroll-line {
  width: 1px;
  height: 36px;
  background: linear-gradient(to bottom, rgba(57, 198, 254, 0.5), transparent);
}

/* Accent bar — faixa de 5 cores no bottom */
.accent-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  z-index: 10;
  background: linear-gradient(
    90deg,
    #0044A2 0%,
    #00C8FF 33%,
    #FBC200 55%,
    #FFB188 75%,
    #FF9E00 100%
  );
}
```

---

## Passo 4 — HTML do Hero v6

Substituir o bloco `<section id="hero">` do wire por:

```html
<!-- HERO V6 — com vídeo de fundo -->
<section id="hero">

  <video class="hero-video" autoplay muted loop playsinline preload="auto">
    <source src="hero/[NOME_DO_VIDEO].mp4" type="video/mp4">
    <!-- fallback: sem vídeo → fundo #182028 pelo CSS -->
  </video>

  <div class="hero-overlay"></div>

  <div class="hero-content">
    <div class="hero-eyebrow">APENT HOLDING</div>
    <h1 class="hero-h1">Invista bem,<br><em>viva melhor.</em></h1>
    <p class="hero-sub">O ecossistema financeiro que conecta tecnologia, dados e assessoria para transformar como você investe.</p>
    <a href="#ecossistema" class="hero-cta">Conheça o ecossistema</a>
  </div>

  <div class="hero-scroll">
    <span class="hero-scroll-label">SCROLL</span>
    <div class="hero-scroll-line"></div>
  </div>

  <div class="accent-bar"></div>

</section>
```

> ⚠️ Substituir `[NOME_DO_VIDEO]` pelo nome real do arquivo encontrado no Passo 1.

---

## Passo 5 — Verificação

Abrir `index.html` no browser e confirmar:

- [ ] Vídeo cobre 100% da tela sem barras pretas
- [ ] Overlay está visível (não muito claro, não muito escuro — ~60% opacidade)
- [ ] Texto legível sobre o vídeo
- [ ] Logo/wordmark "āpent" aparece no nav acima
- [ ] Faixa de 5 cores aparece no bottom do hero
- [ ] Scroll hint visível no bottom (antes da faixa)
- [ ] Ao scroll, nav escurece com `nav.scrolled`
- [ ] CTA "Conheça o ecossistema" rola para `#ecossistema`
- [ ] Seções abaixo (origem, ecossistema etc.) continuam funcionando

---

## Troubleshooting

**Vídeo não aparece:**
- Verificar se o path em `<source src="...">` está correto
- Abrir via servidor local (não file://) — usar `python3 -m http.server 8080`
- Checar console do browser por erros de CORS

**Barras pretas nas laterais/topo:**
- O vídeo original pode ter letterbox embutido — ver se precisa re-crop com ffmpeg
- Comando: `ffmpeg -i input.mp4 -vf "crop=in_w:in_h-102:0:51" output.mp4`

**Nav transparente demais:**
- Confirmar que `.scrolled` está sendo aplicado via JS no scroll
- Checar se o observer de scroll está ativo

**Seções abaixo quebradas:**
- Verificar se `#progress`, `<nav>` e scripts JS do final do body foram preservados
- Não remover o `<script>` no final do wire
