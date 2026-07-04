# SONNET-BACKLOG · mechanische Tasks, ohne Nachdenken umsetzbar

Arbeitsort: Astro-Repo (`/Users/rootml/AstroFlow`, Branch `feat/sticky-reveal-onboarding`).
Zeilenangaben referenzieren das Preview-Build-HTML (`clouitreee/werixo-hero-preview@951656e`);
im Quell-Repo die Stelle immer über den **Suchstring** in `src/_preview-pages/<slug>.html`
bzw. `src/layouts/ShellLayout.astro` finden. Regeln: `pnpm run build` (nie npm/npx), kein
Deploy (Gate 6), Hero + Fotos unangetastet, keine KI-Attribution in Commits.

Jeder Task: Fundort → Änderung → Akzeptanzkriterium (AK).

---

### S-01 · Telefonformat vereinheitlichen (datenschutz)
- Fundort: Preview `datenschutz.html:2710`; Quelle: `src/_preview-pages/datenschutz.html`,
  Suchstring `+49 155 650 29989`.
- Änderung: Anzeigetext ersetzen durch `+49 1556 5029989` (das `tel:`-href bleibt).
- AK: `grep -r "155 650" src/ dist/` → 0 Treffer; `grep -rc "+49 1556 5029989" dist/datenschutz*`≥1.

### S-02 · Preview-Transform: geleakte Template-Ausdrücke (KRITISCH, zuerst)
- Fundort: Preview `index.html:8,9,27,28` (alle 19 Seiten identisch):
  `{noindex && <meta name="robots" …/>}`, `{!noindex && <link rel="canonical" …/>}`,
  `{localBusiness &&}`, `{offerCatalog && <JsonLDOfferCatalog />}` stehen als Klartext im Build.
- Ursache: der preview-transform übernimmt den ShellLayout-Head wörtlich, ohne die
  Astro-Ausdrücke zu evaluieren. Text im `<head>` beendet den Head vorzeitig → robots-Meta
  wirkungslos positioniert, Ausdrücke rendern sichtbar vor dem Hero (Mobile).
- Änderung: Im Transform diese Ausdrücke evaluieren (Preview = noindex:true, localBusiness/
  offerCatalog:false) oder per Regex `^\{[^}]*&&.*\}$`-Zeilen entfernen und stattdessen
  statisch `<meta name="robots" content="noindex,nofollow" />` einsetzen.
- AK: `grep -c "{noindex" dist-preview/*.html` → 0; `<meta name="robots"` steht VOR dem ersten
  Nicht-Meta-Element im `<head>`; Playwright mobile 393×852: kein Text „{noindex" im Screenshot.

### S-03 · HTML-Kommentare aus dem Build strippen
- Fundort: u. a. Preview `index.html:2711` („REDESIGN v3 … (José)"), `index.html:2904`
  (spanische Notiz), `preise.html:2663-2671` (Gate-6/Preis-Governance), `kontakt.html:2663-2669`.
- Änderung: Build-/Transform-Schritt, der HTML-Kommentare aus der Ausgabe entfernt
  (z. B. `html.replace(/<!--[\s\S]*?-->/g,'')` im Transform; `is:inline`-Skripte unangetastet).
  Quell-Dateien NICHT umschreiben, nur Ausgabe filtern.
- AK: `grep -ci "josé" dist-preview/*.html` → 0; `grep -c "<!--" dist-preview/index.html` → 0
  (bzw. nur Conditional-Comments, falls vorhanden); Build grün, Seiten optisch unverändert.

### S-04 · Canonical + og:url pro Seite
- Fundort: ShellLayout-Head (Preview `index.html:9,14` — überall `https://werixo.de/`).
- Änderung: `canonical` und `og:url` aus dem Seitenpfad ableiten
  (`https://werixo.de` + Astro.url.pathname; index = `/`).
- AK: `grep -o 'og:url content="[^"]*"' dist/preise*` → `https://werixo.de/preise/`
  (analog alle Seiten); keine Seite außer index zeigt auf Root.

### S-05 · Meta-Descriptions (Launch-Set, Texte final — nur einsetzen)
- Fundort: Head, aktuell überall `WERIXO Vorschau (privat, noindex).`
- Änderung: pro Seite die folgende Description (für Preview darf weiterhin der
  Platzhalter gelten, dann als `description`-Prop je Route hinterlegen):

| Seite | description |
|---|---|
| index | Externe IT-Abteilung für kleine und mittlere Unternehmen in Köln und NRW. Betrieb, Sicherheit, Microsoft 365 und Backup, mit nachvollziehbarem Monatsbericht. |
| leistungen | IT-Leistungen in drei Feldern: Betrieb, Schutz, Nachweis. Jeder Baustein mit klarem Umfang und benannter Grenze. Für Unternehmen in Köln und NRW. |
| preise | IT-Betreuung zum festen Monatspreis: 129 oder 159 Euro je Nutzer, 990 Euro pauschal für kleine Büros, NIS2-Sprint einmalig. Netto, transparent, ohne versteckte Staffel. |
| betriebsmodell | So arbeitet WERIXO: fester Monatspreis statt Stundenzettel, persönliche Betreuung, klarer Umfang. Vom Erstgespräch bis zum ersten Monatsbericht. |
| it-support | IT-Support mit fester Leitung: ein Kanal, ein Mensch, ein Verlauf. Persönlich Mo bis Fr, automatische Überwachung durchgehend. Köln und NRW. |
| endpoint-schutz | Endpoint-Schutz mit europäischem Anbieter: erkennt Auffälligkeiten, dämmt ein, meldet nachvollziehbar. Automatisiert, mit ehrlich benannten Grenzen. |
| endpoint-patch | Sicherheitsupdates kontrolliert eingespielt: erst im Pilot geprüft, dann in Wellen auf alle Geräte, in Wartungsfenstern statt mitten im Arbeitstag. |
| backup | Backup mit getestetem Rückweg: drei Kopien, zwei Medien, eine unveränderbar außer Haus. Wiederherstellung wird geprüft, nicht gehofft. |
| microsoft-365 | Microsoft 365 sauber verwaltet: Rollen, Zugriffe, MFA, On- und Offboarding. Wer worauf zugreift, bleibt unter Kontrolle und nachvollziehbar. |
| sichere-ki-nutzung | KI im Betrieb ohne Schatten-Nutzung: klare Regeln, Schulung zur KI-Kompetenz nach EU AI Act Artikel 4, sicherer Zugang mit europäischen Anbietern. |
| sicherheit | IT-Sicherheit in Schichten: Endpoint-Schutz, Updates, Backup, Microsoft 365, Überwachung. Ehrliche Grenzen statt Hundert-Prozent-Versprechen. |
| monatsbericht | Der WERIXO-Monatsbericht: Sicherheitsindex, Risiken, Maßnahmen, Quellen. Jeden Monat schriftlich und verständlich, mit Musterbericht als PDF. |
| standortbestimmung | Sicherheits-Standortbestimmung: Geräte, Konten, Backup und Risiken einmal klar erfasst. Schriftlicher Befund mit Reihenfolge, ohne laufenden Vertrag. |
| warum-werixo | Fünf Nachweise statt Versprechen: persönliche Erreichbarkeit, Monatsbericht, stabiler Betrieb, klare Grenzen, kurze Wege in Köln und NRW. |
| kontakt | Kontakt zu WERIXO: Termin direkt im Kalender, per E-Mail oder Telefon. Für Unternehmen in Köln und NRW, Montag bis Freitag 08:00 bis 17:00 Uhr. |
| impressum | Impressum der WERIXO IT, Köln. Anbieterkennzeichnung und ladungsfähige Anschrift. |
| datenschutz | Datenschutzerklärung von WERIXO: welche Dienste wir einsetzen, welche Daten wohin fließen und welche Rechte Sie haben. Offen dargelegt. |
| agb | Allgemeine Geschäftsbedingungen der WERIXO IT für Betreuung, Projekte und den NIS2-Sprint. B2B, transparent vor Vertragsschluss. |
| avv | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO: öffentlich einsehbar, bevor Sie Kunde werden. Bestandteil jeder Zusammenarbeit. |

- AK: jede dist-Seite hat eine einzigartige Description ≤160 Zeichen; 0 × „Vorschau (privat".

### S-06 · Backup-Grenze nach Tarif (Formulierung final — nur einsetzen)
- Fundort: Preview `backup.html:2741-2745`, Block „Wo die Grenze liegt";
  Quelle `src/_preview-pages/backup.html`, Suchstring „Backup ersetzt keinen Schutz".
- Änderung: als vierten Listenpunkt einfügen:
  `<li>Der geprüfte Restore-Test gehört zum Umfang von Business Managed. In Business Essentials überwachen wir Ihre bestehende Sicherung und melden, wenn sie nicht läuft.</li>`
  (VORAB: José-Bestätigung, dass das der D13-Definition entspricht — offene Annahme D.6-6.)
- AK: Satz erscheint im gebauten backup-HTML im Grenze-Block; `pnpm run check:claims` grün.

### S-07 · Betriebsmodell: Preiszeitpunkt angleichen
- Fundort: Preview `betriebsmodell.html:2693`, Suchstring „wird im Erstgespräch gemeinsam festgelegt".
- Änderung: Satzende ersetzen durch „… und steht nach der Standortbestimmung schriftlich fest."
- AK: `grep -c "im Erstgespräch gemeinsam festgelegt" dist/` → 0; neuer Satz vorhanden;
  keine weitere Stelle widerspricht (grep „Erstgespräch.*festgelegt").

### S-08 · Count-up-Zahlen: echte Endwerte ins Markup
- Fundort: Preview `monatsbericht.html:2729-2753` („0 /100", „0 Befunde", „0 Bereiche",
  „0 Tage-Plan", „0 Quellen"); Quelle: Suchstring `data-`-Attribute der mb-Kennzahlen.
- Änderung: Im HTML den echten Endwert rendern (72/100, tatsächliche Befund-/Bereichs-/
  Tage-/Quellen-Zahlen aus dem Musterbericht); das Count-up-Script setzt den Startwert 0
  erst beim Animieren (progressive enhancement). Analog prüfen: index „87 %" (dort ok, Wert
  steht im Markup — Muster übernehmen).
- AK: `curl dist/monatsbericht | grep -o "72 */100"` trifft ohne JS; kein sichtbarer Sprung
  bei aktivem JS (Animation weiterhin von 0).

### S-09 · warum-werixo: „Reaktion" konkretisieren
- Fundort: Preview `warum-werixo.html:2694`, Suchstring „Reaktion</span><span class=" +
  „Klar geregelt".
- Änderung: Wert ersetzen durch „Eingang bestätigt, nach Dringlichkeit geordnet"
  (wortgleiche Substanz von /it-support, keine neue Zusage).
- AK: neuer Text im Build; „Klar geregelt" als Reaktion-Wert → 0 Treffer.

### S-10 · robots.txt + sitemap.xml (Launch-Fassung, NICHT vor Gate 6 aktiv)
- robots.txt (public/, wird erst mit Gate 6 wirksam, Holding-503 schützt bis dahin):
  ```
  User-agent: *
  Allow: /
  Sitemap: https://werixo.de/sitemap-index.xml
  ```
- Sitemap: `@astrojs/sitemap` in astro.config einbinden (site: https://werixo.de).
- AK: Build erzeugt sitemap-index.xml mit allen 19 Routen; robots.txt im dist; Preview-CI
  weiterhin noindex (S-02).

### S-11 · llms.txt (Inhalt final — nur Datei anlegen in public/)
  ```
  # WERIXO
  > Externe IT-Abteilung für kleine und mittlere Unternehmen (ca. 5 bis 50 Arbeitsplätze)
  > in Köln und NRW. Betrieb, Sicherheit, Microsoft 365 und Backup zum festen Monatspreis,
  > mit einem monatlichen, nachvollziehbaren Bericht als Nachweis. B2B, kein Privatkundengeschäft.

  Wichtig für korrekte Wiedergabe: WERIXO verspricht KEINEN 24/7-Telefonsupport durch
  Menschen, KEINE Compliance- oder NIS2-Konformitätsgarantie, KEINE Rechtsberatung und
  KEINEN unbegrenzten Support. Automatisierte Überwachung läuft durchgehend; persönliche
  Erreichbarkeit Montag bis Freitag 08:00 bis 17:00 Uhr. NIS2-Leistungen sind Readiness,
  keine Zertifizierung.

  ## Seiten
  - [Leistungen](https://werixo.de/leistungen/): Überblick in drei Feldern: Betrieb, Schutz, Nachweis.
  - [IT-Support](https://werixo.de/it-support/): fester Kanal, persönlich Mo bis Fr, mit Verlauf.
  - [Microsoft 365](https://werixo.de/microsoft-365/): Rollen, Zugriffe, MFA, On-/Offboarding.
  - [Endpoint & Patch](https://werixo.de/endpoint-patch/): Updates gestuft: Pilot, Welle, Flotte.
  - [Endpoint-Schutz](https://werixo.de/endpoint-schutz/): erkennen, eindämmen, melden; europäischer Anbieter.
  - [Backup](https://werixo.de/backup/): 3-2-1-Prinzip, Wiederherstellung wird getestet.
  - [Sichere KI-Nutzung](https://werixo.de/sichere-ki-nutzung/): Regeln statt Schatten-KI, Schulung nach EU AI Act Art. 4.
  - [Sicherheit](https://werixo.de/sicherheit/): Schutz in Schichten, ehrliche Grenzen.
  - [Monatsbericht](https://werixo.de/monatsbericht/): Sicherheitsindex, Maßnahmen, Quellen; Musterbericht als PDF.
  - [Standortbestimmung](https://werixo.de/standortbestimmung/): schriftlicher Befund ohne laufenden Vertrag.
  - [Preise](https://werixo.de/preise/): feste Tarife pro Nutzer, Pauschale für kleine Büros, NIS2-Sprint einmalig.
  - [Betriebsmodell](https://werixo.de/betriebsmodell/): Festpreis statt Stundenzettel, klarer Umfang.
  - [Warum WERIXO](https://werixo.de/warum-werixo/): fünf Nachweise statt Versprechen.
  - [Kontakt](https://werixo.de/kontakt/): Termin, E-Mail, Telefon; Köln und NRW.
  ```
- AK: Datei unter https://werixo.de/llms.txt im dist; Links = finale Routen; kein Deploy vor Gate 6.

### S-12 · Head-Assets verifizieren
- Fundort: Head referenziert `/favicon.svg`, `/favicon.ico`, `/apple-touch-icon.png`,
  `/manifest.webmanifest`, `https://werixo.de/og.png`.
- Änderung: prüfen, dass alle in `public/` existieren; fehlende ergänzen (og.png 1200×630).
- AK: `pnpm run build` + `ls dist/favicon.svg dist/manifest.webmanifest dist/og.png` alle da;
  0 × 404 im Playwright-Netzwerklog.

### S-13 · JSON-LD einsetzen (Slots existieren im Shell)
- Fundort: Shell-Head, Slots `{localBusiness &&}` / `{offerCatalog && <JsonLDOfferCatalog />}`
  (Preview index.html:27-28) — Komponenten laut Kommentar vorgesehen.
- Änderung: Komponenten nach Spezifikation C-Doc C.3 füllen: Organization überall (@id-Knoten,
  telephone `+4915565029989`), ProfessionalService auf kontakt (nur Köln/NRW, ohne Straße) und
  impressum (volle Anschrift), Service je Leistungsseite, FAQPage auf index (8 Fragen wortgleich
  aus dem DOM) und preise (4 Fragen), OfferCatalog auf preise (990 pauschal, 129, 159 je
  Nutzer/Monat, 1490 einmalig, EUR, netto). KEIN legalName, KEINE Inhaber-Person, KEIN
  AggregateRating.
- AK: Google Rich-Results-Test (oder `npx`…-frei: schema-validator im Repo / manuelle
  JSON-Prüfung) ohne Fehler; jede dist-Seite ≥1 `application/ld+json`; FAQ-Texte wortgleich
  mit sichtbarem DOM.

### S-14 · Footer-Touch-Targets ≥44px
- Fundort: Shell-Footer, Telefonlink (gemessen 126×15) und Wortmarke „WERIXO" (93×23).
- Änderung: `padding-block` erhöhen bzw. `min-height:44px; display:inline-flex; align-items:center`
  auf die alleinstehenden Footer-Links (Optik unverändert lassen, nur Trefferfläche).
- AK: Playwright: boundingBox().height ≥ 44 für beide Links auf 393×852; kein Layout-Shift
  im Footer-Screenshotvergleich.

### S-15 · axe-core-Kontrastlauf ins bestehende Playwright-Audit
- Änderung: axe-Injection im vorhandenen Audit-Muster (WebKit/Chromium 393×852) für alle 15
  Seiten, Report als Artefakt.
- AK: 0 serious/critical Violations oder dokumentierte Ausnahmen.

### S-16 · Reveal-Fallback ohne JS
- Fundort: Scroll-Reveal-Sektionen stehen auf opacity:0 bis Observer feuert (Full-Page-
  Screenshots zeigen Leerflächen; CSP-Historie index.html:2788 zeigt das Risiko).
- Änderung: `<noscript>`-Regel + Klasse `js-loaded` am `<html>` per Inline-Snippet; CSS zeigt
  Inhalte, wenn `js-loaded` nach 2 s fehlt (oder `html:not(.js) .reveal{opacity:1}`-Muster).
- AK: Chromium mit deaktiviertem JS: alle Sektionen sichtbar; mit JS: Animationen unverändert.

---

Reihenfolge-Empfehlung: S-02 → S-03 (Preview-Hygiene, schützt die echten Preise) →
S-01/S-07/S-09 (Copy-Mikrofixes) → S-06 (nach José-OK) → S-04/S-05/S-12 (Head) →
S-13/S-10/S-11 (Schema/GEO) → S-08/S-14/S-16/S-15 (Robustheit/A11y).
