# Achse C · Seitenstrategie, SEO/GEO, Schema, A11y, Core Web Vitals

Verifiziert mit Playwright (Chromium, iPhone-15-Viewport 393×852 + Desktop 1440×900) am lokal
servierten Build. Screenshots: `audit/2026-07-04/shots/`.

## C.1 Funnel und Seitenzwecke

Beobachtete Home-Reihenfolge: Hero → „Der Test" (5 Fragen + Lage/Pflicht-Statistiken) →
„WERIXO in drei Sätzen" → „Der Nachweis" (lebender Bericht) → „Wie wir arbeiten" (Wechsel)
→ „Prüfen statt vertrauen" → FAQ → Kalender im Footer. Das ist ein kohärenter
Problem→Beweis→Einwandbehandlung→Handlung-Funnel für einen GF, der in Sekunden scannt:
jede Sektion hat genau eine Aussage, die Zwischenüberschriften tragen die Argumentation
allein. Direktabgleich gegen WERIXO_WEB_HOME_FUNNEL_v1 steht aus (Doc nicht in dieser
Session) — als Annahme markiert.

Seitenzwecke, gegeneinander geprüft — **keine Seite ist die umbenannte Kopie einer anderen**:

| Seite | Zweck | Suchintention |
|---|---|---|
| index | Positionierung + Test + Beweis | „externe IT-Abteilung Köln", brand |
| leistungen | Hub Betrieb/Schutz/Nachweis | „IT-Dienstleister Leistungen KMU" |
| it-support | Betrieb: der persönliche Kanal | „IT-Support Köln Mittelstand" |
| microsoft-365 | Betrieb: Zugriffe/Identität | „Microsoft 365 Verwaltung KMU" |
| endpoint-patch | Betrieb: Updates/Fenster | „Patch-Management KMU" |
| endpoint-schutz | Schutz: erkennen/eindämmen | „Endpoint Security Mittelstand" |
| backup | Schutz: der getestete Rückweg | „Backup Wiederherstellung KMU" |
| sichere-ki-nutzung | Schutz: Schatten-KI + AI-Act Art. 4 | „KI Richtlinie Unternehmen / AI Act Schulung" |
| sicherheit | Schichten-Übersicht (Schutz-Hub) | „IT-Sicherheit KMU NRW" |
| monatsbericht | Nachweis: das Produkt-Artefakt | brand + „IT-Bericht Nachweis" |
| standortbestimmung | Einstiegsprodukt ohne Bindung | „IT-Sicherheitscheck / Audit KMU" |
| preise | Kaufentscheidung | „IT-Betreuung Kosten pro Nutzer" |
| betriebsmodell | Arbeitsweise/Vertrauen | „Managed Service Festpreis wie funktioniert" |
| warum-werixo | Differenzierung | Vergleichs-/Vertrauensintention |
| kontakt | Konversion | navigational |

Einzige Doppelungs-Wachsamkeit: /sicherheit und /leistungen sind beide Hubs. Sie trennen sich
sauber (Sicherheit = Schichten-Argument, Leistungen = Katalog in drei Feldern), aber bei
künftigen Erweiterungen zuerst prüfen, wohin neuer Inhalt gehört, statt beide wachsen zu lassen.

## C.2 Technisches SEO — Befund und Launch-Struktur (nichts davon jetzt deployen)

**Blocker (im Astro-Repo zu fixen, Preview belegt sie):**
1. Preview-Transform leakt `{noindex && …}` / `{!noindex && …}` / `{localBusiness &&}` /
   `{offerCatalog && …}` als Text → robots-Meta rutscht aus dem Head, sichtbarer Textmüll
   vor dem Hero (Mobile), JSON-LD rendert nie. Details in A-Doc A.3. **Bis zum Fix ist die
   noindex-Absicherung der öffentlichen Preview mit echten Preisen unsicher.** → S-02/S-03.
2. Canonical und og:url hart auf `https://werixo.de/` auf allen 19 Seiten → pro Seite
   parametrisieren. → S-04.
3. Meta-Description auf allen Seiten = „WERIXO Vorschau (privat, noindex)." → Launch-Set
   (19 fertige Texte) liegt im Sonnet-Backlog S-05.
4. Kein robots.txt, keine sitemap.xml, keine llms.txt im Build. Launch-Fassungen fertig in
   S-10/S-11 — scharf geschaltet wird erst mit Gate 6 (Holding-503 + noindex bleiben bis dahin).
5. Head referenziert `/favicon.svg`, `/manifest.webmanifest`, `og.png` — im Preview-Artefakt
   nicht vorhanden; im Astro-`public/` verifizieren. → S-12.

**Bereits gut:** ein H1 pro Seite (verifiziert, alle 15), saubere H2/H3-Hierarchie, sprechende
Zwischenüberschriften, `lang="de"`, semantisches `<main>`, Alt-Texte durchgängig beschreibend
(z. B. monatsbericht.html:2687), Fonts self-hosted mit `font-display:swap`, Plausible defer,
interne Verlinkung der Bausteine untereinander konsequent („Jeder Baustein hat seine eigene
Seite und seine eigene Grenze").

## C.3 Strukturierte Daten (Schema-Design, ausführbar bei Gate 6)

Prinzipien: José-Privatsphäre-Regel (kein legalName, keine Inhaber-Person, volle Anschrift nur
im Impressum), keine Bewertungs-/AggregateRating-Blöcke (0 Kunden — nichts erfinden).

- **Alle Seiten:** `Organization` (name WERIXO, url, logo, email, telephone `+4915565029989`,
  areaServed Köln/NRW, sameAs erst wenn Profile existieren) als `@id`-Referenzknoten.
- **kontakt + impressum:** `ProfessionalService` (LocalBusiness-Subtyp); auf /kontakt nur
  `addressLocality: Köln, addressRegion: NRW` + `openingHoursSpecification` (Mo–Fr 08–17);
  volle `PostalAddress` ausschließlich auf /impressum (dort steht sie ohnehin).
- **Je Leistungsseite:** `Service` (name, description = Meta-Description, provider → @id,
  areaServed) — 9 Stück.
- **index:** `FAQPage` mit den 8 vorhandenen FAQ (Fragen/Antworten wortgleich aus dem DOM,
  kein Sondertext — Google-Richtlinie: Markup = sichtbarer Inhalt).
- **preise:** `FAQPage` (4 Fragen) + `OfferCatalog` (Small Office 990/Monat, Essentials 129,
  Managed 159 je Nutzer/Monat, NIS2-Sprint 1490 einmalig; priceCurrency EUR, netto kennzeichnen).
- **monatsbericht:** `Service` + ggf. `DigitalDocument` fürs Muster-PDF.
- Fertige JSON-LD-Vorlagen: Sonnet-Backlog S-13 (Einbau in die bestehenden, bereits
  vorgesehenen Shell-Slots `JsonLD*` — Architektur existiert, sie rendert nur nicht, s. o.).

## C.4 GEO / AI-Search (Zitierbarkeit für ChatGPT/Perplexity/Gemini/AI Overviews)

Was schon jetzt stark ist: kurze, behauptungsarme Antwortabsätze unter echten Fragen
(FAQ-Sektionen), extern belegte Statistik mit Quellnennung (Bitkom 87 %), konsistente
Entitäts-Signale (WERIXO · externe IT-Abteilung · Köln/NRW in Fußzeilen), ehrliche
Grenz-Aussagen — genau die Sätze, die Answer-Engines gern wörtlich übernehmen.

Lücken, alle vor Gate 6 günstig zu schließen:
1. **JS-abhängige Zahlen:** Count-up-Werte stehen als „0" im HTML (monatsbericht) — Crawler
   ohne JS zitieren falsch. Echte Werte ins Markup. → S-08.
2. **llms.txt:** fehlt. Fertiger Entwurf in S-11 (Kurzprofil, Seitenliste mit
   Ein-Satz-Zwecken, explizite Grenz-/Claims-Hinweise, damit KI-Antworten WERIXO korrekt
   und ohne Überversprechen wiedergeben).
3. **NAP-Konsistenz:** Telefonformat vereinheitlichen (S-01) — LocalBusiness-Konsistenz ist
   ein GEO-Ranking-Signal.
4. **Zitierfähige Definitionssätze:** Jede Leistungsseite beginnt bereits mit einem
   definierenden Absatz; bei künftiger Copy-Arbeit dieses Muster halten (1 Satz Definition,
   1 Satz Abgrenzung — ideal für AI-Snippets).
5. **NIS2-Datumsangabe präzisieren** (B-index-1) — falsch zitierte Fakten in AI-Antworten
   sind kaum rückholbar.

## C.5 Querschnitt „KI unter Kontrolle" in der Seitenstrategie

Platzierungs-Empfehlung (Copy-Entwürfe zur Freigabe, Claims-Grenzen eingehalten — nie
„zertifiziert/konform", immer „orientiert an den Prinzipien von …"):

1. **/sichere-ki-nutzung, neue Sektion „Wie wir selbst mit KI arbeiten"** (stärkstes
   EEAT-Experience-Signal, Belegprinzip erfüllt — jedes Statement hat ein Artefakt):
   > **Wir verlangen von KI bei uns dieselben Regeln, die wir Ihnen empfehlen.**
   > WERIXO setzt KI im eigenen Betrieb ein, aber nie als Blackbox: Jede Aktion wird
   > protokolliert und ist einem Auslöser zuordenbar. Änderungen an Systemen gibt ein
   > Mensch frei, nicht die KI allein. Neue Automatisierungen starten klein, mit Messung
   > und einer Rückfallebene auf das bewährte Verhalten. Und was die KI für Ihren Bericht
   > zusammenträgt, wird als Beleg abgelegt, prüfbar bis zur Quelle. Wir orientieren uns
   > dabei an den Prinzipien etablierter Rahmenwerke wie ISO 27001 und SOC 2 — eine
   > Zertifizierung ist das nicht, und das sagen wir genauso offen.
2. **/warum-werixo, sechster Punkt „06 / KI unter Kontrolle"** (Kurzform desselben Inhalts,
   3–4 Zeilen + Verweis auf /sichere-ki-nutzung).
3. **/monatsbericht:** ein Satz beim Threat-Intelligence/Quellen-Teil, dass KI-gestützte
   Auswertung protokolliert und menschlich freigegeben wird („Geprüft und freigegeben" ist
   als Baustein schon da — nur die KI-Herkunft benennen).
4. **Vertrieb:** siehe D-Doc (dort trägt die Differenzierung am meisten).
5. **Home-Hero:** gesperrt — Vorschlag separat in `E-hero-vorschlag-ki-unter-kontrolle.md`,
   Umsetzung nur nach José-OK und nur, wenn José den Hero öffnet.

Anti-Beispiel, das NICHT passieren darf: „SOC-2-zertifizierte KI-Prozesse", „ISO-27001-konforme
Automatisierung", erfundene Prozentwerte („60 % weniger Aufwand"). Jede Formulierung braucht
das reale Artefakt (Ledger, Flag, Review-Schritt, Evidence-Pack, signierter Bericht).

## C.6 A11y (WCAG AA, GF 55+) und Core Web Vitals — Messergebnisse

Playwright-Lauf über alle 15 Inhaltsseiten @393×852 (`shots/*.png`, `audit-results.json`):

- **Querscroll: 0 px auf allen 15 Seiten.** ✓
- **H1-Zählung: exakt 1 pro Seite.** ✓
- **JS-Fehler: keine** (ERR_TUNNEL = Plausible/Cal.com im Offline-Sandbox erwartbar; der
  Cal.com-Hinweis auf der Preview ist bekannt und kein Bug).
- **Touch-Targets < 44 px (echter Befund, Shell-weit):** Footer-Telefonlink 126×15 px und
  Footer-Wortmarke „WERIXO" 93×23 px auf jeder Seite; dazu Inline-Links wie
  „Ladungsfähige Anschrift im Impressum" (349×28, kontakt). Inline-Fließtextlinks sind nach
  WCAG 2.5.8 ausgenommen, die alleinstehenden Footer-Links nicht → Padding auf ≥44 px
  Zielhöhe. → S-14.
- **Kontraste:** Stichproben unauffällig (Ink auf Weiß, Weiß auf Coral #FF5A3C für große
  Mono-Labels). Vollständige programmatische Kontrastmessung steht aus — im Astro-Repo mit
  axe-core im bestehenden Audit-Muster nachziehen (Backlog-Notiz S-15).
- **CLS:** Reveals sind opacity-basiert, Bilder mit width/height-Attributen → kein
  beobachteter Shift. ✓
- **LCP:** Hero ist Canvas/typografisch, Fonts preloaded-fähig (self-hosted, swap). Auf der
  Preview solide; echte Messung gehört auf die Worker-Route vor Gate 6.
- **INP-Risiko:** ~35 Shell-Scripts inkl. GSAP + COBE auf jeder Seite. Auf Desktop kein
  beobachtetes Problem; für Launch ein Lighthouse/INP-Budget aufsetzen und Script-Laden
  seitenspezifisch beschneiden (Horizont-Doc F, Punkt 3).
- **Reveal-Robustheit (Hinweis):** Sektionen stehen bis zum IntersectionObserver auf
  opacity:0 (sichtbar an den leeren Full-Page-Screenshots). Die CSP-Kommentar-Historie
  (index.html:2788) zeigt, dass GSAP-Blockade schon mal alles unsichtbar gemacht hat.
  Empfehlung: `noscript`-/Timeout-Fallback, der Inhalte nach ~2 s zeigt, falls das
  Animations-Bundle nicht lädt. → S-16.
