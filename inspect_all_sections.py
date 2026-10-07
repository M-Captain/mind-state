with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

body = content[content.find('</style>'):]

import re

def show_section(name, start_pat, end_pat):
    print(f"\n==================== {name} ====================")
    s = re.search(start_pat, body)
    if not s:
        print("Start pattern not found!")
        return
    start_pos = s.start()
    e = re.search(end_pat, body[start_pos:])
    end_pos = start_pos + e.start() if e else len(body)
    sec_html = body[start_pos:end_pos]
    print(f"Length: {len(sec_html)}")
    
    # Extract each card/item
    # find all card titles, images, authors, tags
    titles = re.findall(r'class="homepage__[^"]*title[^"]*"[^>]*>(.*?)</p>', sec_html)
    print("Titles:", titles)
    images = re.findall(r'<([a-zA-Z0-9]+)[^>]*class="homepage__[^"]*image[^"]*"[^>]*>', sec_html)
    print("Images:", images)

show_section("Articles", r'class="homepage__title-5"[^>]*>Articles', r'class="homepage__title-6"[^>]*>Events')
show_section("Events", r'class="homepage__title-6"[^>]*>Events', r'class="homepage__header-title-2"[^>]*>Editor')
show_section("Editor Picks", r'class="homepage__header-title-2"[^>]*>Editor', r'class="homepage__header-title-3"[^>]*>Art')
show_section("Art", r'class="homepage__header-title-3"[^>]*>Art', r'class="homepage__section-title"[^>]*>Our Community Members')
show_section("Community", r'class="homepage__section-title"[^>]*>Our Community Members', r'<footer\b')
