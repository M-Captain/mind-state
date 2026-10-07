from bs4 import BeautifulSoup

input_file= "templates/search-358-6820-images-removed.html"
output_file = "templates/seach.html"
with open(input_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(soup.prettify(formatter="html"))

print(f"Formatted HTML saved to: {output_file}")