# MINDSTATE ARTICLES AI IMPLEMENTATION HANDOFF

## PURPOSE

You are implementing the MindState article library using the source documents and guides in this package.

This package is the source of truth for the article content.

Your job is to build the article experience from these materials without altering the written work.

## ABSOLUTE CONTENT RULE

DO NOT CHANGE EVEN A SINGLE WORD OF ANY SOURCE ARTICLE.

Do not:
• rewrite
• paraphrase
• summarize
• proofread
• correct grammar
• correct punctuation
• change capitalization
• translate
• merge sentences
• remove sentences
• add sentences
• silently fix typos
• change quotation marks
• change paragraph order
• change headings
• change bylines that are explicitly present in the source

Preserve the original article wording exactly.

If an article needs metadata that is not present in the article, store that metadata separately in the platform data model. Do NOT insert invented information into the article body.

## SOURCE FILES

The `source_articles` directory contains the original DOCX files.

Treat those files as immutable source material.

Some DOCX files contain more than one article. In particular, `Pieces by Ishita.docx` contains three separate articles. Use the article index and structure guide to distinguish them.

The complete article set is:

1. Just One More Scroll
2. A Little Comfort on a Bad Day
3. You Don’t Have to Love Your Body Every Day
4. What if they find out?
5. A Cozy Mental-Reset
6. YOU WERE MY MEANING
7. Echo der Gedanken
8. Shards
9. Der lange Weg zur Heilung
10. The Long Road to Healing
11. Die Weitergabe von Mutter zu Tochter: Das Körperbild

## ARTICLE METADATA

For every article, create a separate structured article record containing at minimum:

• title
• author
• publication date
• language
• content warning where applicable
• category
• slug
• featured image
• five image placements
• source document
• source paragraph references

### IMPORTANT DATE RULE

Use the date specified in the metadata guide.

Do not replace an explicit source date with today's date if the source already provides a publication date.

If the source does not provide a publication date, do not invent one. Mark it as requiring editorial confirmation or use the platform's separate publication-date field only if the product owner explicitly requests it.

### IMPORTANT AUTHOR RULE

Never invent an author.

If an article explicitly has a byline, preserve it.

If the document metadata suggests an author but the article itself does not contain a byline, keep that distinction clear.

## IMAGE SYSTEM

Every article must have exactly 5 image slots:

1. Featured image
2. Body image 1
3. Body image 2
4. Body image 3
5. Body image 4

The IMAGE_GUIDE contains the intended visual context, Unsplash search direction, URL, and exact placement instruction.

Do not replace these image concepts with unrelated stock photography.

Do not download random images just because they look aesthetically similar.

The image search URL is provided so the editor can choose an appropriate Unsplash image.

## IMAGE PLACEMENT

The layout is intentionally:

FEATURED IMAGE

ARTICLE TEXT

TWO IMAGE HORIZONTAL ROW

ARTICLE TEXT

TWO IMAGE HORIZONTAL ROW

ARTICLE TEXT

The guide specifies the exact source paragraph after which each body image or image row belongs.

Do not insert images arbitrarily.

Do not move the image rows to make the article "look better."

Do not insert images inside a sentence or paragraph.

When the guide says "after paragraph X", render the image block immediately after that source paragraph.

## ARTICLE STRUCTURE

The rendered article should support:

• content warning when applicable
• title
• author
• publication date
• article body
• featured image
• body image rows
• optional category
• reading experience
• attribution

The actual article body must remain faithful to the source.

## CONTENT WARNINGS

Content warnings are editorial metadata.

Do not rewrite the sensitive source material to make it less intense.

Show the supplied warning before the article body when the guide specifies one.

For example, `Shards` explicitly contains references to bipolar disorder, hearing voices, and suicidal thoughts. The source itself provides that content note.

`The Long Road to Healing` contains references to the death of a child, political persecution, detention, grief, trauma, and panic attacks.

## LANGUAGE

Preserve each article's original language.

Do not automatically translate German articles into English.

If the product supports multilingual metadata, mark the language separately.

## TECHNICAL IMPLEMENTATION

If you are implementing this in React/Next.js:

1. Create a structured article data model.
2. Keep article content separate from presentation.
3. Render paragraphs from the source without changing their text.
4. Render image slots from structured metadata.
5. Use the supplied image placement instructions.
6. Make the featured image a distinct slot.
7. Render body images in horizontal two-image rows.
8. Keep the article layout responsive.
9. Preserve typography and spacing from the existing MindState design system if a design system is already present.
10. Do not redesign the article content.

## DO NOT MAKE UP MISSING INFORMATION

If something is missing:

STOP and mark it as:

`EDITORIAL CONFIRMATION REQUIRED`

Do not fabricate it.

This applies to:

• author
• date
• category
• image
• source attribution
• external links
• quotations
• factual claims
• publication status

## VALIDATION BEFORE COMPLETION

Before declaring the implementation complete, verify:

[ ] All 11 articles are present.
[ ] Every source document is accounted for.
[ ] Every article's title is preserved.
[ ] Every explicit author is preserved.
[ ] No source article wording has been modified.
[ ] No paragraphs were silently omitted.
[ ] No paragraphs were reordered.
[ ] Each article has exactly 5 image slots.
[ ] Every image has a specified context/search direction.
[ ] Every image has a specified Unsplash search URL.
[ ] Every body image has an exact placement instruction.
[ ] Featured images are separate from body images.
[ ] Body images are rendered as two-image rows.
[ ] Content warnings are preserved as metadata where supplied.
[ ] German articles remain German.
[ ] No author/date/metadata was invented.
[ ] Source documents remain untouched.

## SOURCE OF TRUTH PRIORITY

When there is a conflict:

1. Original DOCX source text
2. ARTICLE_INDEX / metadata
3. IMAGE_GUIDE
4. CONTENT_STRUCTURE
5. This implementation guide
6. Your own assumptions

Never override the original source text with an assumption.

## FINAL RULE

The visual implementation can be changed and improved.

The article words cannot.

Build the platform around the writing, not the other way around.
