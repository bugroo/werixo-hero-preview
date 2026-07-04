# Horizont 24 Monate · worauf die WERIXO-Web sich einstellen sollte

Prinzip: nur Vorarbeit benennen, die HEUTE billig ist und in 24 Monaten teuer nachzuholen wäre.

1. **GEO/AI-Search wird der Hauptkanal, nicht die Beilage.** Kaufrecherche der Zielgruppe
   wandert in ChatGPT/Perplexity/Gemini/AI Overviews; für „externe IT-Abteilung Köln" wird
   die Antwortmaschine häufiger konsultiert als Seite 1 von Google. Billige Vorarbeit heute:
   S-11 (llms.txt), S-13 (Schema), S-08 (Zahlen ins Markup), das Definitionssatz-Muster je
   Seite beibehalten, jede Faktenaussage mit Quelle (Bitkom-Muster). Teuer in 24 Monaten:
   eine Site, deren Substanz nur in JS-Animationen lebt und deren Fakten KIs falsch zitieren.

2. **Scroll-driven Animations nativ (CSS) statt GSAP-Abhängigkeit.** `animation-timeline: view()`
   ist auf /leistungen bereits im Einsatz — richtige Richtung. In 24 Monaten ist die
   Browser-Abdeckung durchgehend; jedes neue Signaturmoment ab jetzt zuerst nativ denken,
   GSAP nur wo nötig. Gewinn: CSP-Robustheit (die GSAP/CSP-Vorfälle sind dokumentiert),
   weniger Script-Gewicht, besseres INP.

3. **INP als das CWV-Feld, auf dem man verliert.** ~35 Shell-Scripts auf jeder Seite sind
   heute unauffällig und in 24 Monaten das Problem. Billig jetzt: Script-Manifest pro Seite
   (was braucht diese Route wirklich?), Lighthouse-CI-Budget in die Preview-Pipeline, COBE/
   three.js strikt auf die Seiten begrenzen, die sie nutzen.

4. **Programmatische Service×Regions-Seiten — vorbereiten, nicht bauen.** Wenn echte
   Einsatzorte existieren (Kunden in Bonn, Leverkusen, Bergisch Gladbach …), tragen Seiten
   wie „IT-Betreuung Bonn" echte Substanz: Anfahrt/Vor-Ort-Radius, reale Einsatzformen,
   lokale Ansprechbarkeit. Ohne Kunden sind sie Thin-Content/Stuffing — genau das Gegenteil
   des Schreibkodex. Billig heute: die Seiten-Architektur (Route-Muster, Service-Schema mit
   areaServed) so bauen, dass Regionen später Daten sind, kein neues Template.

5. **EEAT-Blog erst, wenn es etwas zu belegen gibt.** Kein Content-Marketing auf Vorrat.
   Der erste echte Fall (anonymisiert, mit Kundenerlaubnis), der erste Prüfer-Dialog, das
   erste Restore-Ereignis — das sind die ersten drei Artikel. Vorher höchstens die
   bestehenden Grenz-Philosophie-Texte als zitierbare Einzelseiten ausbauen. Billig heute:
   Autoren-/E-E-A-T-Struktur (Person, Qualifikation, Datum, Quellen) als Template definieren.

6. **Funnel-Evolution nach den ersten Kunden.** Heute kompensiert „Prüfen statt vertrauen"
   das Fehlen von Referenzen — richtig so. Ab Kunde 3–5: Testimonial-/Case-Slots an den
   Stellen, wo heute der Musterbericht allein trägt (Home „Der Nachweis", /warum-werixo,
   /preise-FAQ). Billig heute: die Slots als Komponenten-Spezifikation festhalten (Zitat,
   Name mit Erlaubnis, Branche, eine Zahl mit Beleg), damit später kein Redesign nötig ist —
   nicht rendern, solange sie leer sind.

7. **DSGVO- und EU-AI-Act-Transparenz als Vertrauensmerkmal, nicht als Pflichttext.** Die
   Transparenzpflichten (AI Act gestaffelt bis 2026/2027) machen „Wie wir selbst mit KI
   arbeiten" (C.5) vom Marketing-Text zum Nachweis-Dokument: eingesetzte Systeme, Zweck,
   menschliche Aufsicht, Protokollierung, Rückfallebenen. WERIXO kann das als einer der
   ersten kleinen Anbieter öffentlich vorleben — dieselbe Bewegung wie der offene AVV.
   Billig heute: die C.5-Sektion so schreiben, dass sie später nur ergänzt, nie umgebaut wird.

8. **Der signierte Bericht als API-fähiges Artefakt.** In 24 Monaten fragen Versicherer,
   Banken und Auditoren zunehmend maschinenlesbare Nachweise an (Cyber-Police-Fragebögen,
   Lieferketten-Audits). Evidence-Packs mit Hashes und ein signiertes Berichtsformat sind
   die Rohform davon. Billig heute: Berichtsdaten strukturiert halten (JSON neben PDF),
   nichts wegwerfen, was später Nachweiskette ist.
