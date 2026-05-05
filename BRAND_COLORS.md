# BRAND_COLORS.md — Paleta Oficial Apent

> Cores extraídas pixel a pixel da página 12 do brandbook oficial (arquivo brandbook.pdf).
> Estes são os únicos valores de cor autorizados para uso na LP.

---

## Primárias

| Nome (dinamarquês) | Token CSS | HEX | RGB | Uso |
|--------------------|-----------|-----|-----|-----|
| **åpent** | `--azul` | `#0044A2` | `rgb(0, 68, 162)` | Cor institucional principal · CTAs · fundos escuros azuis |
| **fartøj** | `--cinza` | `#F3F3F3` | `rgb(243, 243, 243)` | Fundo neutro · áreas de respiro |
| **tag** | `--preto` | `#182028` | `rgb(24, 32, 40)` | Textos escuros · fundos noturnos · hero background |

## Secundárias

| Nome (dinamarquês) | Token CSS | HEX | RGB | Uso |
|--------------------|-----------|-----|-----|-----|
| **nyhavn** | `--nyhavn` | `#00C8FF` | `rgb(0, 200, 255)` | Destaques · Clube FII · Apent Tech · progress bar |
| **gult hus** | `--amarelo` | `#FBC200` | `rgb(251, 194, 0)` | Gráficos · ícones · energia · eyebrow hero |
| **lyserød hus** | `--salmo` | `#FFB188` | `rgb(255, 177, 136)` | Tons de constância · decorativos |
| **orange hus** | `--laranja` | `#FF9E00` | `rgb(255, 158, 0)` | Apent Investimentos · Autem · sol · dinamismo |

---

## CSS Variables (copiar no `:root`)

```css
:root {
  /* Primárias */
  --azul:   #0044A2;   /* åpent */
  --cinza:  #F3F3F3;   /* fartøj */
  --preto:  #182028;   /* tag */

  /* Secundárias */
  --nyhavn:  #00C8FF;  /* nyhavn */
  --amarelo: #FBC200;  /* gult hus */
  --salmo:   #FFB188;  /* lyserød hus */
  --laranja: #FF9E00;  /* orange hus */

  /* Aliases usados no wire */
  --branco: #FFFFFF;
  --font: 'Hanken Grotesk', sans-serif;
}
```

---

## Tailwind Config (se usar Tailwind)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        apent: {
          blue:   '#0044A2',  // åpent
          grey:   '#F3F3F3',  // fartøj
          dark:   '#182028',  // tag
          sky:    '#00C8FF',  // nyhavn
          yellow: '#FBC200',  // gult hus
          salmon: '#FFB188',  // lyserød hus
          orange: '#FF9E00',  // orange hus
        }
      }
    }
  }
}
```

---

## Gradiente Nordic Stripe (accent-bar)

A faixa multicolor que aparece no hero e entre seções usa as 5 cores em sequência:

```css
background: linear-gradient(
  90deg,
  #0044A2 0%,    /* åpent */
  #00C8FF 25%,   /* nyhavn */
  #FBC200 50%,   /* gult hus */
  #FFB188 75%,   /* lyserød hus */
  #FF9E00 100%   /* orange hus */
);
```

Ou como blocos sólidos (versão do wire):

```css
/* Stripe com 5 divs ou usando background multicolor */
.nordic-stripe {
  height: 4px;
  background: linear-gradient(
    to right,
    #0044A2 20%, #00C8FF 20% 40%,
    #FBC200 40% 60%, #FFB188 60% 80%,
    #FF9E00 80%
  );
}
```

---

## Tipografia

- **Família:** Hanken Grotesk
- **Fonte:** Google Fonts (gratuita, licença comercial OK)
- **Import CDN:**
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  ```
- **Arquivos locais:** `font_Hanken_Grotesk/` (usar em produção para performance)
- **Pesos autorizados pelo brandbook:** Thin → Black (100 a 900)
- **Pesos mais usados na LP:** 300 (light), 400 (regular), 500 (medium), 700 (bold)

---

## Ícones

- **Biblioteca:** Heroicons — https://heroicons.com/
- **Estilo:** sempre **outline** (alinhado com identidade visual do brandbook)
- **NPM:** `npm install @heroicons/react`
- **CDN:** usar inline SVG exportado do heroicons.com

---

## O que NÃO usar

❌ Nenhuma cor fora desta paleta (sem "aproximações" ou variações não listadas)
❌ Nenhuma fonte diferente de Hanken Grotesk
❌ Ícones filled (só outline)
❌ Gradientes que misturem cores além das listadas acima
