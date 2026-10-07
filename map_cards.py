with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
body = content[content.find('</style>'):]

print("=== Scanning cards in body ===")
# Articles: 7 items
# Events: event cards, sidebar cards, bottom cards
# Top Picks: 3 items
# Art: 3 items
# Community: 3 items

# Let's find every image container / img element and its neighboring title
for img_m in re.finditer(r'(<(?:div|img)[^>]*class="(homepage__[^"]*image[^"]*)"[^>]*>)', body):
    img_tag = img_m.group(1)
    img_cls = img_m.group(2)
    pos = img_m.start()
    snippet = body[pos:pos+1200]
    title_m = re.search(r'class="homepage__[^"]*title[^"]*"[^>]*>(.*?)</p>', snippet)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else "NO TITLE"
    print(f"IMG CLASS: {img_cls}\n  TAG: {img_tag[:80]}\n  NEARBY TITLE: {title[:70]}\n")
