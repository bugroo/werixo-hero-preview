# Achse B · Copy-Befunde je Seite + Claims-Scan

Maßstab: Schreibkodex-Prinzipien (People-First, EEAT, keine Floskeln, keine Gedankenstriche
als Stilmittel), Voice-Guide-Prinzipien soweit aus dem Build ableitbar, Claims-Guardrails
(verboten: 24/7, Compliance-Garantie, Rechtsberatung, vollständige NIS2-Konformität,
all-inclusive, unbegrenzter Support). Volltexte von Schreibkodex/Voice Guide waren in dieser
Session nicht verfügbar — wo ich gegen sie prüfe, prüfe ich gegen die im Prompt genannten Regeln.

## B.1 Claims-Scan (Ersatz für `pnpm run check:claims`, SAFE_NEGATION-bewusst)

Ergebnis: **0 Verstöße auf allen 19 Seiten.**

- „rund um die Uhr" (14 Treffer): ausnahmslos als automatisierte Funktion qualifiziert, mit
  explizit daneben stehender Grenze („Automatisierte Funktion, kein durchgehend besetztes
  Lagezentrum", it-support.html:2774, endpoint-schutz.html:2787, endpoint-patch.html:2780,
  microsoft-365.html:2792). agb.html: „Es besteht keine 24/7-Bereitschaftsverpflichtung" =
  Safe Negation.
- „Garantie" positiv nur als SCC-Garantien in avv.html/datenschutz.html (juristischer
  Fachbegriff, korrekt).
- „NIS2-konform" nur als FAQ-Frage (index.html:3096ff), Antwort mit sauberer Grenze
  („Was wir nicht tun, ist vollständige Konformität garantieren oder Rechtsberatung leisten").
- „unbegrenzt / all-inclusive / lückenlos / vollumfänglich / Rundum-Sorglos": positiv 0 Treffer.
- Keine erfundenen Kunden, Fälle, Bewertungen oder Prozentzahlen. Die einzigen Zahlen mit
  Faktencharakter sind extern belegt (Bitkom 87 %, Quelle genannt; EU AI Act Art. 4 seit
  02.02.2025, korrekt).

Der echte `check:claims`-Lauf muss im Astro-Repo nachgeholt werden (Script dort).

## B.2 Befunde je Seite

Format: Urteil, dann nur echte Funde. Seiten ohne Befund sind bewusst kurz — die Copy ist
über alle Seiten hinweg ungewöhnlich diszipliniert: jede Sektion beantwortet eine echte
Kundenfrage, Grenzen werden konkret benannt, Köln/NRW wirkt natürlich platziert, nirgends
Keyword-Stuffing.

### index (Home) — stark
- **B-index-1 (prüfen, Bedeutungsfrage):** index.html:2850–2853 „Dez. 2025 … ist NIS2 in
  Kraft" (Quelle: IHK Köln). Die EU-Richtlinie ist seit Januar 2023 in Kraft, die deutsche
  Umsetzung ist der eigentliche Anker. Die Formulierung ist angreifbar, sobald ein
  informierter Leser (oder eine KI-Antwortmaschine) sie zitiert. Empfehlung: präzisieren auf
  das deutsche Umsetzungsgesetz und von José/juristischer Seite freigeben lassen. Kein
  mechanischer Fix, Faktenfrage.
- **B-index-2:** Dev-Kommentare mit Klarnamen und spanischen Notizen im Quelltext
  (2711, 2904) → Achse-A-Zusatzbefund, Fix S-03.
- Der 5-Fragen-Test (2814–2834) ist das stärkste Conversion-Asset der Site: konkret,
  überprüfbar, gegen den Wettbewerb gerichtet, ohne einen einzigen Claim über WERIXO selbst.

### leistungen — gut
- Kein Copy-Befund. A11y-Detail vorbildlich gelöst: Der Typewriter-Effekt hält den Volltext
  in `.visually-hidden` (leistungen.html:2835).

### it-support — stark
- Kein Befund. „Verlässlich heißt nicht, eine Zahl zu versprechen, die niemand hält"
  (2791) ist die beste Anti-SLA-Passage der Site; im Vertriebs-Doc wiederverwendet.

### endpoint-schutz — stark
- Kein Befund. Grenzen-Katalog (2794–2797) vorbildlich.

### endpoint-patch — stark
- Kein Befund. Pilot→Welle→Flotte (2745–2762) ist als Prozessnachweis genau die Sorte
  Substanz, die der Schreibkodex verlangt — und wörtlich das „Feature-Level-Control"-Prinzip
  der neuen Differenzierungsachse, nur auf Updates statt auf KI angewandt. Andockstelle für
  den Querschnitt (siehe C-Doc, C.5).

### backup — stark, ein Rest
- **B-backup-1 (Bedeutungsentscheidung, getroffen):** Der Restore-Test (2736) liest sich als
  Standardleistung, ist laut /preise aber Managed-Differenzierung (Essentials nur
  „Backup-Überwachung"). Beschlossene Formulierung, in „Wo die Grenze liegt" als vierter
  Punkt einzusetzen:
  > „Der geprüfte Restore-Test gehört zum Umfang von Business Managed. In Business
  > Essentials überwachen wir Ihre bestehende Sicherung und melden, wenn sie nicht läuft."
  Einbau → Sonnet-Backlog S-06. (Voraussetzung: entspricht D13 — von José bestätigen lassen,
  da ich die D13-Definition nicht einsehen kann.)

### microsoft-365 — stark
- Kein Befund. Die Entschärfung (noch keine M365-Datensicherung im Standard, 2798) ist
  ehrlich und präzise; Matrix als „Beispielhafte Darstellung" markiert (2745).

### sichere-ki-nutzung — gut, eine strategische Lücke
- **B-ki-1 (Chance, kein Fehler):** Die Seite behandelt ausschließlich die KI-Nutzung des
  Kunden. WERIXOs eigener kontrollierter KI-Einsatz (Protokollierung, human-in-the-loop,
  Rückfallebenen, Evidence) fehlt — dabei ist er das stärkste EEAT-Experience-Signal, das
  WERIXO ohne Kunden überhaupt hat: „Wir verlangen von KI im eigenen Betrieb dieselben
  Regeln, die wir Ihnen empfehlen." Entwurf einer Sektion im C-Doc (C.5). Bedeutungs- und
  Platzierungsentscheidung für José, kein Sonnet-Task.

### sicherheit — gut
- Kein Befund. „Mitwirkung bleibt nötig" (2766) ist eine seltene, gute Ehrlichkeit.

### standortbestimmung — gut, eine Konsistenzfrage
- **B-standort-1 (Entscheidung José):** 2820 „Köln, NRW und **remote in ganz Deutschland**"
  ist die einzige Stelle der Site, die über NRW hinausgeht (alle Fußzeilen: „B2B · Köln und
  NRW"). Gewollte Erweiterung oder Rest? Wenn gewollt: an 1–2 weiteren Stellen stützen
  (sonst wirkt es wie ein Versehen); wenn nicht: streichen.

### monatsbericht — stark
- **B-bericht-1 (GEO-relevant, mechanisch):** Die Count-up-Kennzahlen stehen im Roh-HTML als
  „0 /100", „0 Befunde", „0 Bereiche", „0 Tage-Plan", „0 Quellen" (2729–2753). Noscript-Leser
  und AI-Crawler lesen falsche Werte. Echte Endwerte ins Markup, Animation startet per JS bei
  0 → Sonnet-Backlog S-08.

### betriebsmodell — gut, ein Riss
- **B-modell-1 (Formulierung beschlossen):** 2693 „… wird im Erstgespräch gemeinsam
  festgelegt" widerspricht 2726 und preise.html:2839 („nach der Standortbestimmung,
  schriftlich"). Beschlossene neue Formulierung für 2693:
  > „Der Preis richtet sich nach Umfang und Teamgröße und steht nach der Standortbestimmung
  > schriftlich fest."
  → Sonnet-Backlog S-07.

### preise — Copy gut, Design siehe A-Doc
- Kein Copy-Befund. „Was Geschäftsführer an dieser Stelle wissen wollen" beantwortet die
  vier echten Einwände (Mindestzahl, Stufenwechsel, Ausschlüsse, Preiszeitpunkt).

### warum-werixo — gut, eine dünne Stelle
- **B-warum-1 (Vorschlag):** „Reaktion: Klar geregelt" (2694) ist die einzige leere Zusage
  der Seite — „klar geregelt" sagt nichts. Die Substanz existiert auf /it-support
  (Eingang bestätigt → nach Dringlichkeit geordnet → Verlauf einsehbar). Vorschlag:
  „Reaktion: Eingang bestätigt, nach Dringlichkeit geordnet" (wortgleich mit it-support,
  keine neue Zusage). → Sonnet-Backlog S-09.

### kontakt — stark
- Kein Befund. Privatsphäre-Regel (Anschrift nur im Impressum) sauber eingehalten.

### Legal (impressum, datenschutz, agb, avv) — Claims sauber
- **B-legal-1:** Telefonformat datenschutz.html:2710 (einziger Formatausreißer) → S-01.
- Inhaltlich-juristische Prüfung bleibt Anwaltssache; hier nur auf Claims und Konsistenz geprüft.

## B.3 Was fehlt (Substanz-Lücken, nicht erfinden)

- **Kein einziges externes Vertrauenssignal** (0 Kunden = korrekt nichts erfunden). Die Site
  kompensiert klug über den „Prüfen statt vertrauen"-Stack (offener Vertrag, offene Preise,
  Musterbericht, Datenwege). Das ist die richtige Strategie bis zu den ersten Referenzen —
  danach: echte Testimonials/Fälle nachrüsten (Slots dafür im Horizont-Doc F).
- **WERIXOs eigener KI-Einsatz** ist nirgends beschrieben (siehe B-ki-1) — die einzige
  Differenzierung, die heute schon ohne Kunden belegbar ist (Artefakte: Ledger, Flags,
  signierter Bericht, Evidence-Packs).
