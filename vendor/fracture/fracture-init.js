// Preview-Init (GitHub-Pages-Snapshot, CSP 'self'): Gate + Start des Schutzrings.
import { initFractureRing } from './fracture-ring.min.js';
const canvas = document.querySelector('.sec-ring');
const hero = document.querySelector('.sec-hero');
const mq = (s) => window.matchMedia(s).matches;
if (canvas && hero && !mq('(prefers-reduced-motion: reduce)') && !mq('(hover: none) and (pointer: coarse)') && !mq('(max-width: 860px)')) {
  hero.classList.add('sec-ring-on');
  try { initFractureRing({ canvas, container: hero }); } catch (e) { /* Fallback-Bild bleibt */ }
}
