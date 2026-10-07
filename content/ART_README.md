# Supplied art library

The six posts use the supplied titles, blurbs, rubric tags, original JPEGs,
artwork titles, creators, museum links, and license credits. The publication
date is the import date, 7 October 2026; the pack has no post bylines or dates.
No article author is inferred from the art-direction brief.

Each slug detail page contains one featured artwork and four supporting works
in filename order. Responsive paper frames apply the supplied accent palette
using CSS; the archived JPEGs remain unchanged. The original pack instructions
and metadata live in `art-post-packs/`.

Run `python manage.py import_art_library` to validate all six posts and 30
assets. Add `--install` to import or update these records while preserving the
11 written articles. Cards appear in Art and search. Recently Added alternates
written articles and art, and Editor’s Top Picks selects from both types.
`?section=art` limits search to visual art.

The source pack credits are displayed on-page. Museum object-page verification
was attempted for every work; some Wellcome object pages were unavailable to
the browsing tool. Retain their supplied Public Domain Mark metadata and links.
