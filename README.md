# WERIXO Hero Preview (pública, noindex)

Aplicación web pública actual de WERIXO en GitHub Pages. Snapshot estático de la fuente AstroFlow; `werixo.de` permanece como holder hasta un cutover separado. `noindex,nofollow`.

## Verificación

```bash
python3 scripts/verify_static.py
```

El gate valida las 19 páginas HTML, referencias locales, CSP y hashes inline,
`noindex,nofollow`, ausencia de Zeeg, acciones fijadas por SHA y el manifiesto
SHA-256 de todos los archivos publicados. Para actualizar intencionadamente el
snapshot: `python3 scripts/verify_static.py --write-manifest` y después repetir
el comando sin opciones.
