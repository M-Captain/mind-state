import re

with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('</style>')
body = content[body_start:]

print("--- Elements with image classes ---")
for m in re.finditer(r'<([a-zA-Z0-9]+)[^>]*class="([^"]*image[^"]*)"[^>]*>', body):
    print(m.group(0))

print("\n--- Ellipse elements (avatars?) ---")
for m in re.finditer(r'<([a-zA-Z0-9]+)[^>]*class="([^"]*ellipse[^"]*)"[^>]*>', body):
    print(m.group(0))
