# MindState article library

This library contains the eleven articles supplied in `mindstate-article-packs.zip`.
Original Word documents are preserved byte-for-byte in `source_articles/`; the
supplied instructions and source manifest are retained in `article-guides/`.

`article-library.json` stores the article metadata, original paragraph text and
formatting, source paragraph references, image credits, and placement decisions.
Each article has one featured image and two pairs of body images. All 55 original
JPEGs are stored in `static/articles/` without alteration.

Where paragraph numbers disagreed with the quoted passages, the owner explicitly
selected the quoted passages. The catalog retains both the printed paragraph
number and the resolved source paragraph. Two quoted passages span adjacent source
paragraphs; their image pair follows the final paragraph of the passage.

All publication dates are 7 October 2026, as instructed by the package. The two
Long Road to Healing articles have no inline article byline. At the owner's
request, their displayed author credit is Sophia Kanesarasa, taken from the
document author metadata `Kanesarasa, Sophia`. The catalog records this source;
the original article paragraphs remain unchanged.

The existing LandingContent model stores listing and search data. Reading pages
include the corresponding lossless templates in `templates/article-content/`.
No schema migration or changes to newsletter, account, or signup behavior are
needed.

To validate the package without changing the database:

```powershell
.\.venv\Scripts\python.exe manage.py import_article_library
```

To replace demo content with the supplied library:

```powershell
.\.venv\Scripts\python.exe manage.py import_article_library --replace-demos
```

The replacement is transactional and backs up the previous LandingContent records
to `work/demo-articles-before-import.json`. Other database records are preserved.

To compare all rendered paragraphs directly with the original Word XML and verify
image anchors, authors, dates, search, and the removal of demo articles:

```powershell
.\.venv\Scripts\python.exe content/verify_article_library.py
```
