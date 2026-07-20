# VISUAL-POLISH.md — Registro de trabajo UI/UX + accesibilidad

> Documento de continuidad. Qué se hizo, cómo se hizo, qué falta.
> Última actualización: 2026-07-20 · Rama: `visual-polish` (7 commits sobre `main`).

---

## 1. Qué es este repo

- Snapshot estático (build de Astro, repo fuente `werixo-web-astro` — **no está en esta máquina**).
- Preview privado: `clouitreee.github.io/werixo-hero-preview/` (noindex, nofollow).
- 19 páginas HTML, cada una ~370–400 KB con CSS/JS inline.
- Remoto `origin` configurado pero **NADA pusheado** desde esta máquina. Todo el trabajo es local.
- Copia portable: `/home/ubuntu/werixo-visual-polish.bundle` (ramas `main` + `visual-polish`).

## 2. Estado de ramas

```
main            22a7d44  preview: Auto-Deploy aus werixo-web-astro (97b2795)
visual-polish   7 commits encima (ver §3) — working tree limpio
```

## 3. Commits realizados (orden cronológico)

| Commit | Qué | Detalle |
|---|---|---|
| `85981c6` | Botones hover | `scale(1.02)` eliminado (demasiado "startup"); lift sutil 1px; sombras más cortas; transición color añadida. |
| `63bef3f` | Header + anclas | Sticky header 93 %→97 % opaco (las cards se veían cortadas detrás); `scroll-margin-top: 96px/84px` para que `#cal`, `#nachweis` y secciones no queden tapadas. |
| `0cffcd7` | Hero | Trust-chips a una línea por item (mono .95→.86rem + `nowrap`); eyebrow móvil cabe en una línea (.78rem/.08em). |
| `e9e5075` | Showcase `lbr` | Runway del pin GSAP 2400→2050px (−15 %): había ~290px de scroll muerto tras el sello "GEPRÜFT". ÚNICO toque a JS; coreografía intacta. |
| `343fb63` | Widget Termin | "LÄDT …" texto plano → skeleton shimmer de 35 celdas (respeta `prefers-reduced-motion`); hover de `.cal-cta-btn` refinado. |
| `007a446` | **Contraste WCAG AA** | 43 reemplazos. Ver §4. |
| `0043984` | Target táctil | `.brand` con `padding:3px 0` → 29px (mínimo WCAG 2.2: 24px). |

## 4. Decisión de diseño clave: contraste AA (commit `007a446`)

Problema: blanco sobre coral `#FF5A3C` = **3.09:1** (WCAG exige 4.5:1). Estaba en TODOS los CTAs.

**Decisión**: texto **ink oscuro `#1A1612` sobre el coral de marca** (5.3:1) en lugar de oscurecer el naranja. Mantiene la identidad, es más "terminal" y menos genérico. Aplicado a: `.btn.primary`, `.head-cta`, `.mn-cta`, `.cal-cta-btn`, `.cal-day:hover`, `.cal-slot.sel`, `.pos-tag`, `.pf-img-tag`, `.wy-btn`, `.pr-cfg-badge`, hovers de iconos `.lst-ic`/`.sec-ic`. Hovers de fondo → coral claro `#FF6A50` (5.8:1).

Otras variables tocadas:
- `--ink-3`: .40→**.62** (era 2.55:1, lo peor del sitio)
- `--ink-2`: .60→**.64** (fallaba sobre #FAFAFA por 0.01)
- `--ww-tx2`: .50→**.62**
- 13 reglas con `color:rgba(19,21,26,…)`/`rgba(26,22,18,…)` sub-AA → suelo **.62**
- Texto pequeño coral (nav hover, TOC legal, etiquetas mono) → `--accent-ink` (#C2410C, 5.2:1), que el propio sistema ya reservaba para esto.
- **NO se tocó**: acentos en titulares grandes (3.09 pasa como texto grande ✓), iconos (3.0 ✓), texto claro sobre secciones oscuras (pasa ✓).

## 5. CONOCIMIENTO CRÍTICO — estructura del CSS/JS inline

Antes de editar cualquier página, lee esto:

1. **Hay UN solo stylesheet de diseño por página**: el bloque `<style is:global>` (~240 KB), **byte-idéntico en las 19 páginas**. Contiene TODO: fuentes, variables, header, footer, botones, todos los componentes de todas las páginas.
2. **Los demás `<style>` que aparecen son FALSOS POSITIVOS**: la cadena `<style>` existe dentro de comentarios CSS y comentarios JS. Bloques reales adicionales: solo uno pequeño page-specific tras el global (p.ej. "Der Test" en index).
3. El JS del showcase `lbr` y del widget Cal **también está embebido idéntico en las 19 páginas** (aunque solo se active en index).
4. Por tanto: **un cambio global = reemplazar la cadena en las 19 páginas**, verificando antes que el hash del bloque es idéntico en todas (abortar si alguna diverge).

### Patrón de propagación segura (usado en todos los commits)

```python
import re, glob, hashlib
def gblock(s): return re.search(r'<style is:global>(.*?)</style>', s, re.S).group(1)
files = sorted(glob.glob('*.html'))
ref = gblock(open(files[0], encoding='utf8').read())
rh = hashlib.md5(ref.encode()).hexdigest()
for f in files:
    assert hashlib.md5(gblock(open(f, encoding='utf8').read()).encode()).hexdigest() == rh
assert ref.count(OLD) == N           # conteo exacto obligatorio
new = ref.replace(OLD, NEW)
for f in files:
    s = open(f, encoding='utf8').read()
    open(f, 'w', encoding='utf8').write(s.replace(ref, new))
```

## 6. Herramientas QA

- **Playwright + Chromium**: `/home/ubuntu/tools/qa` (ya instalado, `node_modules/playwright`). Chromium en `~/.cache/ms-playwright/`.
- **Servidor local**: `cd ~/werixo && python3 -m http.server 8901` → `http://127.0.0.1:8901/index.html`
- **axe-core**: descargado a `/tmp/wxshots/axe.min.js` (¡/tmp es efímero! redescargar: `curl -sLO https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js`).
- Los scripts de QA (screenshots, axe, teclado) vivían en `/tmp/wxshots/` — se pierden al reiniciar. Recrearlos según necesidad; el patrón es: lanzar chromium desde `/home/ubuntu/tools/qa/node_modules/playwright/index.mjs`, `page.evaluate(axeSrc)` + `axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}})`.

## 7. Verificación actual (2026-07-20)

- axe-core WCAG 2.0/2.1 A+AA: **0 violaciones en 19/19 páginas**.
- Consola: **0 errores** en 19/19 páginas.
- Teclado desktop: skip-link primero, outline 2px visible, mega-menú abre con Enter, cierra con Escape ✓
- `prefers-reduced-motion`: showcase renderiza estado final estático, contenido accesible ✓
- Móvil 390px / tablet 768px: layouts correctos ✓

## 8. PENDIENTE — qué falta por hacer

1. **Push a GitHub**: el usuario decide destino (rama en `clouitreee/werixo-hero-preview` o repo nuevo). Requiere credenciales GitHub en esta máquina (no disponibles aún). Ver comandos en la conversación o al final de este archivo.
2. **Label "RESILIENZ" del globo cobe**: se solapa/recorta con otro label (elemento JS con CSS anchor-positioning). No se tocó por riesgo. Requiere depurar con la animación corriendo.
3. **Port al repo fuente `werixo-web-astro`**: estos cambios viven en el BUILD. El source Astro debe recibirlos o se perderán en el próximo deploy. Idealmente reimplementar allí (los selectores/reglas son los mismos).
4. **Auditoría BFSG formal**: axe-core cubre la base técnica; la conformidad legal (BFSG/EAA, EN 301 549) requiere auditoría con lector de pantalla real (NVDA/JAWS) y revisión de la "Declaración de accesibilidad" (Erklärung zur Barrierefreiheit), que los sitios B2B alemanes pueden necesitar publicar.
5. **Radios de borde** (9/11/12/16/100px): escala algo arbitraria. No se tocó (churn de riesgo bajo beneficio). Unificar solo si hay decisión de diseño.
6. **Regenerar el bundle** tras nuevos commits: `git bundle create ~/werixo-visual-polish.bundle main visual-polish`

## 9. Reglas para futuras sesiones en este repo

- Solo cambios visuales: NO lógica de negocio, rutas, formularios, analytics (Plausible), JSON-LD, textos/copy.
- Commits pequeños por sección, mensajes en inglés `visual:`/`a11y:`.
- Nunca `git push` sin confirmación explícita del usuario.
- Si el bloque global diverge del hash esperado → alguien redesplegó desde Astro: reconciliar ANTES de editar (posiblemente portar cambios de vuelta al source).
- Verificar siempre con screenshots Playwright antes/después + axe-core.
- Identidad git local del repo: `kimi-code <kimi@localhost>` (solo repo-local, nada global).
