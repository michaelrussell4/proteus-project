# Proteus Scriptorium · Digital Scripture & Literature Library

[![GitHub Pages Deployment](https://github.com/michaelrussell4/proteus-project/actions/workflows/deploy.yml/badge.svg)](https://github.com/michaelrussell4/proteus-project/actions/workflows/deploy.yml)
[![Live Site](https://img.shields.io/badge/Live%20Website-GitHub%20Pages-blue)](https://michaelrussell4.github.io/proteus-project/)
[![License: Public Domain](https://img.shields.io/badge/License-Public%20Domain-gold.svg)](https://creativecommons.org/publicdomain/mark/1.0/)

> **Live Website & Download Portal:** [https://michaelrussell4.github.io/proteus-project/](https://michaelrussell4.github.io/proteus-project/)

Welcome to **Proteus Scriptorium**, a curated digital library of computational scripture, critical textual collations, and public-domain Restoration classics. Every volume is compiled and packaged according to official IDPF/W3C **EPUB 3.3** standards and optimized specifically for **Amazon Kindle Paperwhite** and modern digital reading devices.

---

## 📚 Top Curated Selections (`data/`)

This repository hosts a curated collection of **11 top editions** from the Proteus publishing pipeline:

| Edition | Size | Highlights |
| :--- | :--- | :--- |
| [**Book of Mormon: Master Study Edition**](data/book-of-mormon-master-study.epub) | 5.69 MB | Unites red-letter divine speech (✦), BYU Onomasticon Hebrew/Egyptian etymologies (◈), and pre-1960 discourse citations ([★]) in instant modal pop-ups. |
| [**The Standard Works (Minimalist Edition)**](data/lds-standard-works-minimalist.epub) | 3.95 MB | All five scriptural volumes (OT, NT, BoM, D&C, PoGP) in a single distraction-free file preserving chapter and verse numbers. |
| [**Complete Apocrypha & Pseudepigrapha Compendium**](data/complete-apocrypha-pseudepigrapha-compendium.epub) | 3.56 MB | 99 ancient extra-canonical works (1,376 chapters, 1.27M words) with historical provenance and veracity dossiers for each book. |
| [**The Complete Restoration Literature Compendium**](data/complete-lds-literature-compendium.epub) | 15.2 MB | 71 historical Latter-day Saint books (5.91M words) organized into seven thematic divisions with 3,276 recovered pop-up notes. |
| [**Foundational Classics of the Restoration**](data/foundational-lds-classics-anthology.epub) | 2.99 MB | 9 landmark doctrinal classics (*Lectures on Faith*, *Jesus the Christ*, *Articles of Faith*, *House of the Lord*, etc.) with pop-up notes. |
| [**Book of Mormon: Historical Textual Variants**](data/book-of-mormon-historical-variants.epub) | 1.35 MB | Collation across eight major editions (1830 to 2013) based on Grant Hardy's BYU OpenScripture project with inline apparatus. |
| [**The Book of Mormon (1830 Narrative Edition)**](data/book-of-mormon-1830-narrative.epub) | 1.02 MB | The original 1830 Palmyra text formatted as continuous prose with tap-to-see verse ranges. |
| [**The Top 1,000 Cited Verses of the Restoration**](data/top-1000-cited-verses.epub) | 2.48 MB | The most-quoted scriptures in early Restoration sermons (1830–1886) ranked by frequency with speaker analytics and discourse excerpts. |
| [**The Scriptures (Minimal Canon)**](data/scriptures.epub) | 3.07 MB | Ultralight single-volume edition engineered for rapid page turns and high-contrast e-ink navigation on Kindle Paperwhite. |
| [**Book of Mormon Intertextual Parallels**](data/bom-intertextual-parallels.epub) | 358 KB | Word-level collation of Brass Plates Isaiah (2 Nephi 12–24) and Sermon at the Temple (3 Nephi 12–14) side-by-side with the KJV. |
| [**Reading Old English Scripture: A Quick Guide**](data/early-modern-english-quick-guide.epub) | 316 KB | Reader-friendly guide to Early Modern English pronouns (*thou/ye*), verbs (*-eth*), false friends, and a one-page cheat sheet. |

---

## ⚡ Key Engineering Features

1. **Native Kindle Pop-Up Footnotes:**
   Every cross-reference, textual variant, and etymological root note is encoded using bidirectional `<a epub:type="noteref">` and `<aside epub:type="footnote">` markup. On Kindle Paperwhite, tapping any footnote opens a clean modal pop-up card without jumping away from your reading location.

2. **Bespoke High-Resolution Covers:**
   Each edition features a high-DPI (`1200×1920`) cover from the Proteus Scriptorium suite, rendered with 2× supersampling and Lanczos filtering.

3. **W3C EPUBCheck 5.3.0 Verified:**
   Every compiled `.epub` passes official W3C validation with zero errors and zero warnings.

4. **Zero-Build Static Website:**
   The front-facing website is completely static, fast, and accessible. It features client-side real-time search, collection filtering, sorting, theme toggling (warm parchment / midnight dark mode), and native `<dialog>` preview modals.

---

## 📱 How to Read on Your Device

### Amazon Kindle (Paperwhite, Oasis, Scribe, Colorsoft, Kindle App)
1. Download the desired `.epub` file from the [download portal](https://michaelrussell4.github.io/proteus-project/) or the `data/` folder.
2. Visit [amazon.com/sendtokindle](https://www.amazon.com/sendtokindle) and sign in to your Amazon account.
3. Drag and drop the `.epub` file. Amazon will process and deliver the book to your device within minutes with cover art and pop-up footnotes intact.
4. *Alternative:* Email the `.epub` directly as an attachment to your personal `@kindle.com` email address.

### Apple Books (iPhone, iPad, Mac)
- Click **Download EPUB** in Safari or Chrome on your Apple device. Tap **Open in Books**. The book will automatically sync across all your devices via iCloud.

### Kobo, Android & E-Ink Devices
- **Kobo:** Connect your device via USB and transfer the `.epub` into the root directory, or download directly via the Kobo experimental browser.
- **Android:** Open the file using Google Play Books, ReadEra, Moon+ Reader, or PocketBook.

### Desktop Computers (PC / Mac / Linux)
- We recommend **Thorium Reader** (open-source, built by the European Digital Reading Lab) or **Calibre**.

---

## 🛠️ Local Development & Site Generation

To view or rebuild the site locally:

```bash
# Preview locally using any static web server
python -m http.server 8000

# Re-generate index.html from catalog.json
uv run python build_site.py
```

---

## 🏛️ Sources & Academic Attribution

- **BYU Book of Mormon Onomasticon Project** (ed. Paul Y. Hoskisson) — Hebrew and Egyptian lexical roots.
- **BYU Scripture Citation Index** (Stephen W. Liddle & Richard C. Galbraith) — Pre-1960 citation statistics and discourse links.
- **Grant Hardy's OpenScripture Project** — 1830–2013 Book of Mormon textual variant collation.
- **Internet Sacred Text Archive & Project Gutenberg** — Public-domain historical and extra-canonical source texts.

*Disclaimer: Proteus is an independent, non-commercial educational project and is not affiliated with or endorsed by The Church of Jesus Christ of Latter-day Saints or Brigham Young University.*
