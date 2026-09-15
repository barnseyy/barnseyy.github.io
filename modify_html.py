import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace <div class="card-grid"> with the container and track
content = content.replace('<div class="card-grid">', '<div class="carousel-container">\n    <div class="carousel-track" id="projectCarousel">')

# Find where the track ends and insert the nav
# The track ends just before </section> (the projects section)
track_end = content.find('  </section>\n\n  <section id="contact"')
if track_end != -1:
    # Insert closing div for track, and the nav HTML, and closing div for container
    nav_html = """    </div>
    
    <div class="carousel-nav" id="carouselNav">
      <button class="nav-dot active" aria-label="Project 1">
        <img src="assets/onetapdrift-icon.png" alt="One Tap Drift">
      </button>
      <button class="nav-dot" aria-label="Project 2">
        <img src="assets/rizen-icon.png" alt="Rizen">
      </button>
      <button class="nav-dot" aria-label="Project 3">
        <img src="assets/wordhive-icon.png" alt="WordHive">
      </button>
      <button class="nav-dot" aria-label="Project 4">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
      </button>
      <button class="nav-dot" aria-label="Project 5">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
      </button>
      <button class="nav-dot" aria-label="Project 6">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <line x1="12" y1="5" x2="12" y2="19"></line>
          <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
      </button>
    </div>
  </div>
"""
    content = content[:track_end] + nav_html + content[track_end+6:] # track_end+6 is to remove the `    </div>` that originally closed the card-grid

with open('index.html', 'w') as f:
    f.write(content)

