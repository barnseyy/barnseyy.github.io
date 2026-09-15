import re

with open('style.css', 'r') as f:
    css = f.read()

replacement = """/* ---------- carousel ---------- */
.carousel-container {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
}

.carousel-track {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  gap: 24px;
  padding-bottom: 12px;
  scrollbar-width: none;
}
.carousel-track::-webkit-scrollbar {
  display: none;
}

.carousel-track .card {
  flex: 0 0 100%;
  scroll-snap-align: center;
}

@media (min-width: 768px) {
  .carousel-track .card {
    flex: 0 0 calc(50% - 12px);
  }
}

/* ---------- carousel navigation ---------- */
.carousel-nav {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
  flex-wrap: wrap;
}

.nav-dot {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: var(--bg-elev);
  border: 2px solid transparent;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  transition: all 0.3s ease;
  opacity: 0.5;
}

.nav-dot img {
  width: 100%;
  height: auto;
  border-radius: 6px;
}

.nav-dot svg {
  width: 100%;
  height: 100%;
  color: var(--text-dim);
}

.nav-dot:hover {
  opacity: 0.8;
  transform: translateY(-2px);
}

.nav-dot.active {
  opacity: 1;
  border-color: var(--accent);
  box-shadow: var(--shadow-soft);
  transform: scale(1.1);
}
"""

css = re.sub(r'\.card-grid \{[^}]+\}', replacement, css)

css = css.replace('.card-grid .card.reveal', '.carousel-track .card.reveal')

with open('style.css', 'w') as f:
    f.write(css)

