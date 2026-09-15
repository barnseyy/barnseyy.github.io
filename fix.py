with open('index.html', 'r') as f:
    c = f.read()
c = c.replace('  </div>\nction>\n', '  </section>\n')
with open('index.html', 'w') as f:
    f.write(c)
