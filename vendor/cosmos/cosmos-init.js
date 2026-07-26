// Preview-Init (GitHub-Pages-Snapshot, CSP 'self'): Gate + Start des Auroral-Flow-Felds.
// In der echten Astro-Route macht das leistungen.astro via Vite-Dynamic-Import; hier self-hosted.
import { initCosmosFlow } from './cosmos-flow.min.js';
const canvas = document.querySelector('.lst-cosmos');
const hero = document.querySelector('.lst-hero--cosmos');
const mq = (s) => window.matchMedia(s).matches;
if (canvas && hero && !mq('(prefers-reduced-motion: reduce)') && !mq('(hover: none) and (pointer: coarse)') && !mq('(max-width: 860px)')) {
  hero.classList.add('lst-cosmos-on');
  try { initCosmosFlow({ canvas, container: hero }); } catch (e) { /* Fallback-Bild bleibt */ }
}
