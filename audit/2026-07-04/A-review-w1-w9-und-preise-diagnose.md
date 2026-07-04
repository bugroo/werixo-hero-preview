# Achse A · Review der jüngsten Arbeit (W1–W9) + /preise-Diagnose

Stand: 2026-07-04 · Geprüft am gebauten Preview-HTML (Auto-Deploy aus `werixo-web-astro@0996dfe`,
Preview-Commit `951656e`). Die `_preview-pages/*.html` sind laut Architektur die einzige
Copy-Quelle für Route UND Preview, daher ist der Copy-Stand hier 1:1 verifizierbar.

**Einschränkung dieser Session:** Kein Zugriff auf das Astro-Quell-Repo (weder als
`clouitreee/werixo-web-astro` noch `clouitreee/AstroFlow` für die Session-Credential freigegeben).
Daher: kein `git diff` gegen den Branch, kein `pnpm run check:claims` als Script, keine Einsicht in
CLAUDE.md / Voice Guide / Funnel-Doc / die Memory `project-web-scope-copy-audit-2026-07-04`.
Ersatz: inhaltliche Verifikation am Build + eigener SAFE-NEGATION-bewusster Claims-Scan.
Zeilenangaben beziehen sich auf das Preview-HTML; der zitierte Suchstring macht jede Stelle
im Quell-Repo per grep auffindbar.

## A.1 Review-Tabelle (Audit-Punkte, adversarial geprüft)

| # | Audit-Punkt | Urteil | Beleg (file:line im Preview-Build) |
|---|---|---|---|
| 1 | Anonymisiert → fiktive Daten | **umgesetzt** | index.html:2928 „Mai 2026 · Beispiel fiktive Daten"; monatsbericht.html:2687/2689 „Muster Maschinenbau GmbH, fiktiv" / „Musterbericht, fiktive Daten"; standortbestimmung.html:2698/2780 „Beispiel-Befund, fiktive Daten … keine Zertifizierung"; microsoft-365.html:2745 „Beispielhafte Darstellung"; warum-werixo.html:2708 „Musterbericht · fiktive Daten". Das Wort „anonymisiert" existiert nur noch in HTML-Kommentaren (index.html:2905, monatsbericht.html:2668) — nicht sichtbar, aber Teil des Kommentar-Leaks (siehe A.3). |
| 2 | /betriebsmodell vs. /preise entkoppelt | **umgesetzt** | betriebsmodell.html trägt keine Zahlen mehr (Kommentar 2664 „KEINE Preise"), Fußzeile 2800 „Preis nach Umfang", Verweis auf die Preise-Seite in 2769. /preise trägt die D13-Tarife exklusiv. Rest-Riss: betriebsmodell.html:2693 sagt „wird **im Erstgespräch** gemeinsam festgelegt", während betriebsmodell.html:2726 und preise.html:2839 sagen „**nach der Standortbestimmung**". Eine Stelle angleichen → Sonnet-Backlog S-07. |
| 3 | „M365 vollständig" entschärft | **umgesetzt** | microsoft-365.html:2798 „Datensicherung von Microsoft 365 **noch nicht im Standard**. Kommt als eigener Baustein dazu, sobald das Werkzeug dafür steht."; 2799 Lizenzkosten ausgenommen; 2800 keine Rechtsberatung. Grep über alle Seiten: kein „vollständig"-Claim im M365-Kontext mehr; alle „vollständig"-Treffer sind Safe-Negations oder juristische Standardformeln (AGB/AVV). |
| 4 | 20-vs-30-Minuten vereinheitlicht | **umgesetzt** | Einheitlich 30 Minuten: agb.html:2715 „30-minütiges Erstgespräch", datenschutz.html:2745 „30-Minuten-Erstgespräch". Kein „20 Minuten"/„20 Min" im gesamten Build (grep negativ). |
| 5 | „Kein Tag Ausfall" ersetzt | **umgesetzt** | Wendung existiert im Build nicht mehr. Ersatz: index.html:2999 „Kein Stillstand" (+ 3000 realistische Beschreibung). Alle verbleibenden „Ausfall"-Treffer sind risikobeschreibend, nicht versprechend (index.html:2984, betriebsmodell.html:2765, sicherheit.html:2706, standortbestimmung.html:2698). |
| 6 | Telefon-Format vereinheitlicht | **teilweise** | Standardformat „+49 1556 5029989" an 60 Stellen inkl. Shell-Footer und Impressum. **Eine Abweichung:** datenschutz.html:2710 zeigt „+49 155 650 29989" (tel:-href ist korrekt). Fix → Sonnet-Backlog S-01. Wichtig auch für NAP-Konsistenz (LocalBusiness/GEO). |
| 7 | Backup-Grenze nach Tarif | **teilweise** | backup.html:2743–2745 benennt Grenzen ehrlich (kein Null-Datenverlust; Umfang vorher festgelegt; Backup ersetzt keinen Schutz). ABER: Die Tarif-Differenz aus /preise — Essentials = „Backup-Überwachung" (preise.html:2727) vs. Managed = „Backup und Wiederherstellung, geprüft zurückgespielt" (preise.html:2744) — wird auf der Backup-Seite nicht gespiegelt. backup.html:2736 „Wir stellen probeweise wieder her …" liest sich als Standard für alle Tarife. Formulierungsentscheidung getroffen (siehe B-Doc, Befund B-backup-1), Einbau → Sonnet-Backlog S-06. |
| 8–9 | Restliche Audit-Punkte | **nicht prüfbar** | Der Prompt nennt 7 der 9 Punkte namentlich. Für die übrigen brauche ich den Volltext des Copy-/Scope-Audits W1–W10 (Memory `project-web-scope-copy-audit-2026-07-04`) von José. W10 war laut Vorgabe bewusst nicht umzusetzen — im Build ist nichts erkennbar, das wie eine eigenmächtige W10-Umsetzung aussieht, aber ohne Volltext ist das kein belastbares Urteil. |

**Gesamturteil Achse A:** Die Sonnet-Umsetzung ist inhaltlich sauber und vollständiger als erwartet.
5 von 7 prüfbaren Punkten vollständig, 2 mit kleinen, präzise lokalisierten Resten. Keine
Regression, keine neuen Claim-Verstöße durch die Umsetzung.

## A.2 /preise-Diagnose: Warum v1–v8 durchfielen

Nicht neu improvisiert — Diagnose am gerenderten Stand (v5 „Stil Ramp" laut Build-Kommentar
preise.html:2663–2671) plus der dort dokumentierten Ablehnungshistorie („v1..v4 zu weiß/insipido",
José-Feedback „basura/feo/sin gusto" bis v8). Desktop- und Mobile-Screenshots liegen unter
`audit/2026-07-04/shots/`.

**Kerndiagnose — vier Ursachen, die alle Iterationen teilen:**

1. **Alle Versionen waren Reskins über dasselbe Skelett.** Hero-Text → 3 Karten → Banner →
   Rechner → FAQ → CTA ist das generische SaaS-Pricing-Muster. Die Iterationen drehten an
   Farbe, Badges, Borders — nie an der Dramaturgie. José reagiert auf Seiten mit eigenem
   Konzept (jede andere Unterseite hat ein „Signaturmoment": Rückweg-Bogen, Zugriffs-Matrix,
   Fenster-Kontraktion). /preise hat keins — bzw. es hat eins und versteckt es (Punkt 2).
2. **Die Signatur-Komponente ist marginalisiert.** Der Live-Rechner ist die einzige
   interaktive, differenzierende Idee der Seite — und sitzt klein in Sektion 3 rechts,
   nachdem drei statische Karten das Zentrum besetzt haben. Die eigentliche Frage des
   Zielgeschäftsführers ist nicht „welche drei Tarife gibt es?", sondern „**was kostet das
   für UNS?**" — und genau die beantwortet nur der Rechner.
3. **Monotonie ohne Fokusobjekt.** Drei gleich große weiße Karten mit gleich langen Listen,
   die Differenzierung hängt an einer Coral-Border und einem Badge. Es gibt kein Element mit
   eigener visueller Masse (vgl. das 3-2-1-Zahlenpanel auf /backup oder die dunkle
   Cobalt-Lektüre auf /monatsbericht). „Zu viel Coral" in frühen Versionen und „zu weiß" in
   späteren sind zwei Symptome desselben Problems: Farbe ersetzte Hierarchie, statt dass
   Struktur sie erzeugt.
4. **CTA-Rauschen.** Zwei Buttons pro Karte × 3 Karten + Sprint-CTA = 7–8 Buttons im ersten
   Screen der Tarifsektion, alle im selben Mono-Uppercase-Stil. Der Coral-Haupt-CTA verliert
   seine Einzigartigkeit (Governance: Coral = einziger Lead-Akzent — das gilt sinngemäß auch
   für Handlungsaufforderungen).

**Referenzbasierter Richtungsvorschlag (zur Freigabe, kein Blind-Versuch):**

> **„Ihre Zahl zuerst":** Der Rechner wird das Eingangsobjekt der Seite (direkt unter dem
> Hero, groß, als Fokusobjekt), die Tarifkarten reagieren auf ihn. Teamgröße einstellen →
> bis 10 Nutzer hebt sich Small Office als Empfehlung hervor, darüber der Essentials/Managed-
> Vergleich; die aktive Karte bekommt die visuelle Masse, die passiven treten zurück.
> Ein Coral-CTA pro Zustand („Erstgespräch vereinbaren"), Rückruf als stiller Textlink.
> NIS2-Sprint bleibt als klar getrennter „Projekt, kein Abo"-Block. Preisbeträge,
> Stufen-Namen, Leistungslisten wortgleich (D13 unangetastet).

- Wirkung: Die Seite beantwortet die GF-Frage in unter 5 Sekunden, das Signaturmoment ist
  endlich die Signatur, und die Karten-Monotonie löst sich durch Zustands-Hierarchie statt
  durch mehr Farbe.
- Referenzen zum Konsultieren vor der Umsetzung (Regel José 07-04 — ui-ux-pro-max-Datenbank
  und frontend-design-Skill liegen im Astro-Repo, in dieser Session nicht verfügbar,
  Konsultation dort nachholen): Ramp Pricing (bereits v5-Referenz: solide Badges, ein
  dominanter CTA), Stripe Pricing (ein CTA pro Karte, Zustands-Klarheit), Linear Pricing
  (ruhige Differenzierung ohne Farbflut), Basecamp (eine ehrliche Zahl als Haltung — passt
  zur WERIXO-Stimme „Orientierung, keine Rechnung").
- **Nächster Schritt:** Diese Richtung José als 1-Absatz-Entscheidung vorlegen. Erst nach
  konkretem Feedback bauen; danach Referenz-Screens sammeln und als Bild vorlegen, bevor
  Code entsteht.

## A.3 Zusatzbefund aus dem Review (kritisch, vorher nicht im Audit)

1. **Preview-Transform leakt unevaluierten Template-Code ins ausgelieferte HTML.**
   index.html:8–9 `{noindex && <meta name="robots" …/>}` / `{!noindex && <link rel="canonical" …/>}`
   und index.html:27–28 `{localBusiness &&}` / `{offerCatalog && <JsonLDOfferCatalog />}` stehen
   wörtlich im Build (alle 19 Seiten). Folgen:
   - Text-Knoten im `<head>` beenden den Head vorzeitig → das robots-Meta landet im Body.
     **Der noindex-Schutz der öffentlichen Preview (mit echten D13-Preisen) ist damit
     unzuverlässig** — Google verarbeitet meta-robots im Body nicht garantiert.
   - Die Ausdrücke rendern als **sichtbarer Textmüll** vor dem Hero (Mobile-Screenshot
     `index-mobile.png`, oberste Zeile: „{noindex && } {!noindex && } {localBusiness…").
   - Die JSON-LD-Architektur (existiert im Shell!) wird nie ausgeführt → 0 strukturierte
     Daten im gesamten Build.
   - Canonical und og:url zeigen zusätzlich auf allen Seiten hart auf `https://werixo.de/` (Root).
   Ob die echte Worker-Route (ShellLayout.astro) korrekt rendert, kann ich ohne Quell-Repo
   nicht prüfen — **im Astro-Repo verifizieren**. Der Preview-Transform-Bug ist unabhängig
   davon real. → Sonnet-Backlog S-02 (Transform-Fix), S-03 (Kommentar-Strip).
2. **Interne Governance-Kommentare werden ausgeliefert:** José-Klarname, Entscheidungsdaten,
   Gate-6-Status, Ablehnungshistorie („v1..v4 zu weiß/insipido"), spanische Arbeitsnotizen —
   z. B. index.html:2711, index.html:2904, preise.html:2663–2671, kontakt.html:2666. Für eine
   öffentliche Preview (und erst recht für den Launch) gehören Build-Artefakte kommentarfrei.
   → Sonnet-Backlog S-03.
