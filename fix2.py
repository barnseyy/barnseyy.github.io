with open('index.html', 'r') as f:
    c = f.read()
c = c.replace('    </div>\n    </div>\n    \n    <div class="carousel-nav"', '    </div>\n    \n    <div class="carousel-nav"')
with open('index.html', 'w') as f:
    f.write(c)
