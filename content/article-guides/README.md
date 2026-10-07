# MindState Article Import Package

Prepared: **7 October 2026**

This package contains the original article documents plus implementation instructions for adding them to the MindState platform.

## NON-NEGOTIABLE SOURCE INTEGRITY RULE

**DO NOT CHANGE EVEN A SINGLE WORD OF THE SOURCE ARTICLES.**

Do not rewrite, paraphrase, proofread, translate, shorten, expand, reorder, merge, split sentences, change punctuation, change capitalization, remove content, or silently correct grammar.

The DOCX files in `source_articles/` are the source of truth.

Do not edit the source DOCX files to add:
* author metadata
* publication dates
* category labels
* content warnings
* image URLs
* featured images
* inline images
* captions
* tags
* slugs
* reading time

Instead, keep the article text intact and enter those items as separate CMS/platform fields.

The only exception is visual presentation performed by the platform itself. Typography, spacing, cards, image placement, and responsive layout may be controlled by the MindState frontend without changing the article wording.

## Preserve document structure

Keep each source DOCX intact in the repository/archive.

Do not flatten the documents into one text file.

Do not alter paragraph order.

Do not remove blank paragraphs.

Do not merge paragraphs.

Do not split paragraphs unless the platform's rich-text importer requires a technical representation of the same paragraph content. If that happens, preserve every character and preserve the original paragraph order.

`guides/SOURCE_MANIFEST.json` contains SHA-256 hashes and structural counts for the supplied source files so that accidental changes can be detected.

## Publication metadata

For the platform, use:

**Publication date:** 7 October 2026

For each article, use the author explicitly identified in the article or the attribution information documented in `ARTICLE_METADATA_AND_PLACEMENT.md`.

Do not invent an author when the source does not provide an article byline.

## Image policy

Each article has exactly five planned image slots:

1. One featured image before the article body.
2. Two images inserted together after the first specified source paragraph.
3. Two images inserted together after the second specified source paragraph.

The exact anchors, image concepts, and Unsplash search URLs are in `IMAGE_GUIDE.md`.

Do not insert an image in the middle of the source paragraph named as an anchor. Insert it immediately after that paragraph.

For sensitive pieces, the image guide intentionally avoids graphic depictions of self-harm, death, medication misuse, detention, or trauma.

## Recommended CMS fields

For every article:

* Title
* Author
* Publication date
* Language
* Content type
* Content warning, when applicable
* Article body
* Featured image
* Inline image group 1
* Inline image group 2
* Image alt text
* Image credit/source
* Slug
* Category
* Tags

Only the article body must remain word-for-word identical to the source.

## Source files

All nine uploaded DOCX files are included under `source_articles/`.

This package does not replace those files with edited versions.
