with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('<body>')
body_end = content.find('</body>')
body = content[body_start + 6:body_end]

import re

# Let's find all occurrences of articles, events, top picks, art, community members
# Print major landmarks with their surrounding HTML tags
patterns = [
    r'Articles',
    r'Events',
    r'Editor',
    r'Art',
    r'Community'
]

for p in patterns:
    print(f"=== Matches for {p} ===")
    for m in re.finditer(re.escape(p), body, re.IGNORECASE):
        start = max(0, m.start() - 200)
        end = min(len(body), m.end() + 300)
        print(f"...{body[start:end]}...\n")
