with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

body = content[content.find('</style>'):]

import re

# Let's inspect the 7 articles in the articles section
articles_section = re.search(r'class="homepage__article-container"[^>]*>(.*?)<div class="homepage__events-header"', body)
if articles_section:
    html = articles_section.group(1)
    # find all article card containers
    # usually class="homepage__article-container-X" or similar
    print("Articles HTML length:", len(html))
    cards = re.findall(r'<div class="homepage__article-container-\d+"[^>]*>.*?</div></div></div>', html)
    print("Found cards with regex 1:", len(cards))
