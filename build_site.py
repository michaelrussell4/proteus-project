"""
Static site generator for Proteus Digital Library.
Generates an accessible, responsive, pre-rendered static HTML download portal.
"""

import json
import html

def generate_html():
    with open('catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Categories
    categories = [
        {"id": "all", "label": "All Editions", "count": len(catalog)},
        {"id": "study-editions", "label": "Study Editions", "count": sum(1 for b in catalog if b['collection'] == 'study-editions')},
        {"id": "standard-works", "label": "Standard Works", "count": sum(1 for b in catalog if b['collection'] == 'standard-works')},
        {"id": "apocrypha", "label": "Apocrypha & Ancient Texts", "count": sum(1 for b in catalog if b['collection'] == 'apocrypha')},
        {"id": "literature", "label": "Restoration Literature", "count": sum(1 for b in catalog if b['collection'] == 'literature')},
        {"id": "reading-guides", "label": "Reading Guides", "count": sum(1 for b in catalog if b['collection'] == 'reading-guides')},
    ]

    total_mb = sum(b['size_bytes'] for b in catalog) / (1024 * 1024)

    cards_html = []
    for book in catalog:
        search_terms = f"{book['title']} {book['subtitle']} {book['short_desc']} {book['collection_label']} {book['badge']} {' '.join(book.get('highlights', []))}".lower()
        search_terms_escaped = html.escape(search_terms, quote=True)
        title_esc = html.escape(book['title'])
        subtitle_esc = html.escape(book['subtitle'])
        short_desc_esc = html.escape(book['short_desc'])
        badge_esc = html.escape(book['badge'])
        col_esc = html.escape(book['collection'])
        col_label_esc = html.escape(book['collection_label'])
        size_human = html.escape(book['size_human'])
        cover_path = html.escape(book['cover'])
        file_path = html.escape(book['file'])
        book_id = html.escape(book['id'])

        cards_html.append(f"""
        <article class="book-card" data-id="{book_id}" data-collection="{col_esc}" data-search="{search_terms_escaped}">
          <div class="book-cover-wrap">
            <img class="book-cover" src="{cover_path}" alt="Cover art for {title_esc}" width="240" height="360" loading="lazy">
            <span class="book-badge">{badge_esc}</span>
          </div>
          <div class="book-content">
            <div class="book-meta-top">
              <span class="book-collection-tag">{col_label_esc}</span>
              <span class="book-size-tag"><svg class="icon-inline" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 2a.75.75 0 01.75.75v8.69l2.72-2.72a.75.75 0 111.06 1.06l-4 4a.75.75 0 01-1.06 0l-4-4a.75.75 0 011.06-1.06l2.72 2.72V2.75A.75.75 0 0110 2zM3 13.75A.75.75 0 013.75 13h12.5a.75.75 0 010 1.5H3.75A.75.75 0 013 13.75z" clip-rule="evenodd"/></svg>{size_human}</span>
            </div>
            <h3 class="book-title"><a href="{file_path}" download>{title_esc}</a></h3>
            <p class="book-subtitle">{subtitle_esc}</p>
            <p class="book-description">{short_desc_esc}</p>
            <div class="book-actions">
              <a class="btn btn-primary" href="{file_path}" download title="Download {title_esc}">
                <svg class="icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 2a.75.75 0 01.75.75v8.69l2.72-2.72a.75.75 0 111.06 1.06l-4 4a.75.75 0 01-1.06 0l-4-4a.75.75 0 011.06-1.06l2.72 2.72V2.75A.75.75 0 0110 2zM3 13.75A.75.75 0 013.75 13h12.5a.75.75 0 010 1.5H3.75A.75.75 0 013 13.75z" clip-rule="evenodd"/></svg>
                <span>Download EPUB</span>
              </a>
              <button type="button" class="btn btn-secondary btn-details" data-open-modal="{book_id}" aria-label="View details for {title_esc}">
                <span>Details</span>
              </button>
            </div>
          </div>
        </article>
        """)

    filter_chips_html = []
    for c in categories:
        pressed = 'true' if c['id'] == 'all' else 'false'
        filter_chips_html.append(f"""<button class="chip" data-filter="{c['id']}" aria-pressed="{pressed}">{c['label']} <span class="chip-count">({c['count']})</span></button>""")

    html_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Proteus Scriptorium · Curated Scripture &amp; Study EPUB Editions</title>
  <meta name="description" content="Download handcrafted, Kindle Paperwhite-optimized EPUB3 editions of Latter-day Saint scripture, critical study collations, biblical apocrypha, and Restoration classics.">
  <meta name="theme-color" content="#1c1917">
  
  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Proteus Scriptorium · Curated Scripture &amp; Study EPUBs">
  <meta property="og:description" content="Free, non-commercial digital library of computational scripture, textual collations, and public-domain Restoration classics. Optimized for Kindle Paperwhite &amp; modern e-readers.">
  <meta property="og:image" content="covers/book-of-mormon-master-study.png">

  <link rel="stylesheet" href="style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
</head>
<body>
  <!-- Header / Nav -->
  <nav class="top-nav">
    <div class="wrap top-nav-inner">
      <a class="nav-brand" href="#top">
        <span class="brand-crest">✦</span>
        <span class="brand-name">Proteus <span>Scriptorium</span></span>
      </a>
      <div class="nav-links">
        <a href="#editions">Editions</a>
        <a href="#how-to-read">E-Reader Guide</a>
        <a href="#about">About</a>
        <a href="#attribution">Attribution</a>
        <button id="theme-toggle" class="btn-theme-toggle" type="button" aria-label="Toggle light or dark theme" title="Toggle theme">
          <span class="theme-icon-light" aria-hidden="true">☀️</span>
          <span class="theme-icon-dark" aria-hidden="true">🌙</span>
        </button>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header id="top" class="hero">
    <div class="wrap hero-inner">
      <div class="hero-content">
        <div class="hero-pill">
          <span class="pill-dot"></span>
          <span>Free &amp; Non-Commercial Digital Library</span>
        </div>
        <h1 class="hero-title">Scripture &amp; Classics,<br>Engineered for Your E-Reader</h1>
        <p class="hero-lede">
          Curated, commercial-grade EPUB3 editions of the Latter-day Saint scriptural canon, intertextual collations, extra-canonical apocrypha, and 19th-century classics.
          Every volume is hand-crafted and validated with zero errors for <strong>Amazon Kindle Paperwhite</strong> and modern reading devices.
        </p>

        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-number">11</span>
            <span class="stat-label">Curated Volumes</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-number">{total_mb:.1f} MB</span>
            <span class="stat-label">Total Library Size</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-number">100%</span>
            <span class="stat-label">Public Domain &amp; Free</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-number">EPUB3</span>
            <span class="stat-label">Kindle Pop-Up Notes</span>
          </div>
        </div>

        <div class="hero-cta-row">
          <a class="btn btn-primary btn-hero" href="#editions">Browse Editions ↓</a>
          <a class="btn btn-outline btn-hero" href="#how-to-read">Send-to-Kindle Guide</a>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Catalog Controls -->
  <section id="editions" class="catalog-section">
    <div class="controls-bar">
      <div class="wrap controls-inner">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clip-rule="evenodd"/>
          </svg>
          <input type="search" id="catalog-search" class="search-input" placeholder="Search by title, topic, author, or keyword…" aria-label="Search editions" autocomplete="off">
          <button type="button" id="search-clear" class="search-clear" aria-label="Clear search" hidden>×</button>
        </div>

        <div class="filter-chips" role="group" aria-label="Filter by collection">
          {"".join(filter_chips_html)}
        </div>

        <div class="catalog-summary-bar">
          <span id="results-count">Showing <strong>11</strong> editions</span>
          <div class="sort-wrapper">
            <label for="catalog-sort">Sort by:</label>
            <select id="catalog-sort" class="sort-select">
              <option value="featured">Featured Selections</option>
              <option value="title">Title (A–Z)</option>
              <option value="size-desc">File Size (Largest first)</option>
              <option value="size-asc">File Size (Smallest first)</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <!-- Editions Grid -->
    <div class="wrap">
      <div id="books-grid" class="books-grid">
        {"".join(cards_html)}
      </div>

      <div id="empty-state" class="empty-state" hidden>
        <div class="empty-icon">🔍</div>
        <h3>No matching editions found</h3>
        <p>Try searching with another keyword or resetting the category filter.</p>
        <button type="button" id="reset-filters" class="btn btn-secondary">Reset Filters</button>
      </div>
    </div>
  </section>

  <!-- How to Read / Send to Kindle Guide -->
  <section id="how-to-read" class="guide-section">
    <div class="wrap">
      <div class="section-header">
        <span class="section-eyebrow">Device Compatibility</span>
        <h2 class="section-title">How to Read on Your Device</h2>
        <p class="section-lede">All editions are packaged according to official IDPF EPUB 3.3 standards with bidirectional pop-up footnote markup and high-resolution covers.</p>
      </div>

      <div class="guide-grid">
        <div class="guide-card">
          <div class="guide-icon">📱</div>
          <h3>Amazon Kindle (Paperwhite, Oasis, Scribe, App)</h3>
          <p>The fastest way to load onto your Kindle is via Amazon's official web tool:</p>
          <ol>
            <li>Download the desired <code>.epub</code> from this page.</li>
            <li>Go to <a href="https://www.amazon.com/sendtokindle" target="_blank" rel="noopener">amazon.com/sendtokindle</a> and sign in.</li>
            <li>Drag &amp; drop the <code>.epub</code> file. In 1–2 minutes, it will automatically sync to your Kindle library with covers and native pop-up notes!</li>
          </ol>
          <div class="guide-tip">
            <strong>Pro-tip:</strong> You can also send the file as an email attachment directly to your <code>@kindle.com</code> email address.
          </div>
        </div>

        <div class="guide-card">
          <div class="guide-icon">🍎</div>
          <h3>Apple Books (iPhone, iPad, Mac)</h3>
          <p>Seamless one-tap integration with iOS and macOS devices:</p>
          <ol>
            <li>Click <strong>Download EPUB</strong> on your iPhone, iPad, or Mac.</li>
            <li>When prompted, tap <em>Open in Books</em>.</li>
            <li>The book is automatically added to your library and syncs across all your Apple devices via iCloud with progress and bookmark saving.</li>
          </ol>
        </div>

        <div class="guide-card">
          <div class="guide-icon">📖</div>
          <h3>Kobo, Android &amp; Third-Party Readers</h3>
          <p>Compatible with all modern e-ink readers and mobile apps:</p>
          <ol>
            <li><strong>Kobo:</strong> Connect via USB and drag into the Kobo drive, or download directly via the experimental browser.</li>
            <li><strong>Android:</strong> Open directly in apps like <em>Google Play Books</em>, <em>ReadEra</em>, <em>Moon+ Reader</em>, or <em>PocketBook</em>.</li>
          </ol>
        </div>

        <div class="guide-card">
          <div class="guide-icon">💻</div>
          <h3>PC &amp; Mac Desktop Reading</h3>
          <p>For research and reference on desktop computers:</p>
          <ol>
            <li><strong>Thorium Reader</strong> (Recommended, free &amp; open-source): Built specifically for accessibility and pure EPUB3 conformance.</li>
            <li><strong>Calibre</strong>: Great for managing large digital libraries and converting formats.</li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- Technical Standards / About Proteus -->
  <section id="about" class="about-section">
    <div class="wrap">
      <div class="section-header">
        <span class="section-eyebrow">Publishing Technology</span>
        <h2 class="section-title">The Proteus Publishing Standard</h2>
        <p class="section-lede">What makes these editions fundamentally different from raw scans or automated web exports?</p>
      </div>

      <div class="features-grid">
        <div class="feature-item">
          <div class="feature-icon">✨</div>
          <h4>Kindle Paperwhite Pop-Up Footnotes</h4>
          <p>Every scripture cross-reference, textual variant, and Hebrew/Greek etymology uses reciprocal <code>&lt;a epub:type="noteref"&gt;</code> and <code>&lt;aside epub:type="footnote"&gt;</code> pairs. Tap any note to see an instant modal card on your Kindle without losing your reading location.</p>
        </div>

        <div class="feature-item">
          <div class="feature-icon">🎨</div>
          <h4>Proteus Scriptorium Cover Suite</h4>
          <p>Each volume carries a bespoke high-DPI (1200×1920) cover rendered with 2× supersampled Lanczos filtering, classical scriptorium medallion artwork, and thematic series color palettes.</p>
        </div>

        <div class="feature-item">
          <div class="feature-icon">🛡️</div>
          <h4>W3C epubcheck 5.3.0 Verified</h4>
          <p>Every compiled volume passes the official W3C / IDPF Java EPUBCheck validation suite with zero errors and zero warnings. Valid XHTML5, verified internal links, and strict XML well-formedness.</p>
        </div>

        <div class="feature-item">
          <div class="feature-icon">🔤</div>
          <h4>Smart Typography Engine</h4>
          <p>Clean typographic normalizations: curly quotation marks, proper em-dashes, non-breaking spaces before verse locators, and dark-mode resilient typography.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Attribution & Public Domain -->
  <section id="attribution" class="attribution-section">
    <div class="wrap">
      <div class="section-header">
        <span class="section-eyebrow">Academic Heritage &amp; Notice</span>
        <h2 class="section-title">Sources, Attribution &amp; Non-Commercial Notice</h2>
      </div>

      <div class="attribution-card">
        <ul class="attribution-list">
          <li>
            <strong>Non-Profit &amp; Educational Mission:</strong> All Proteus editions hosted here are distributed strictly free of charge for personal, non-commercial, and educational study.
          </li>
          <li>
            <strong>Public-Domain Textual Foundations:</strong> Canonical texts (1769 King James Bible, 1830–1920 Book of Mormon, pre-1929 Doctrine &amp; Covenants and Pearl of Great Price), historical Restoration volumes (1833–1927, via Project Gutenberg and the Mormon Documentation Project), and the Apocrypha &amp; Pseudepigrapha corpora (R. H. Charles, M. R. James, Richard Laurence, Ante-Nicene Fathers) are derived from public-domain sources.
          </li>
          <li>
            <strong>Academic Project Attribution:</strong> We express deep gratitude to the <a href="https://onoma.lib.byu.edu/" target="_blank" rel="noopener">BYU Book of Mormon Onomasticon Project</a> (ed. Paul Y. Hoskisson), the <a href="https://scriptures.byu.edu/" target="_blank" rel="noopener">BYU Scripture Citation Index</a> (Stephen W. Liddle &amp; Richard C. Galbraith), Grant Hardy's OpenScripture 1830–2013 collation, and the Internet Sacred Text Archive.
          </li>
          <li>
            <strong>Independent Status:</strong> Proteus is an independent, non-commercial educational project. It is not affiliated with, endorsed by, or sponsored by The Church of Jesus Christ of Latter-day Saints or Brigham Young University.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="wrap footer-inner">
      <div class="footer-left">
        <p class="footer-brand">✦ Proteus Scriptorium</p>
        <p class="footer-tagline">Crafted for serious scripture study and distraction-free digital reading.</p>
      </div>
      <div class="footer-right">
        <p>100% Free &amp; Open Source · Hosted on GitHub Pages</p>
        <p><a href="https://github.com/michaelrussell4/proteus-project" target="_blank" rel="noopener">View GitHub Repository</a> · <a href="#top">Back to Top ↑</a></p>
      </div>
    </div>
  </footer>

  <!-- Book Details Modal (Native HTML <dialog>) -->
  <dialog id="book-modal" class="book-modal" aria-labelledby="modal-book-title" closedby="any">
    <div class="modal-card">
      <header class="modal-header">
        <span id="modal-book-badge" class="book-badge"></span>
        <button type="button" class="modal-close-btn" id="modal-close" aria-label="Close dialog">×</button>
      </header>
      
      <div class="modal-body">
        <div class="modal-cover-column">
          <img id="modal-book-cover" class="modal-cover" src="" alt="Book cover">
          <a id="modal-download-btn" class="btn btn-primary btn-full-width" href="" download>
            <svg class="icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 2a.75.75 0 01.75.75v8.69l2.72-2.72a.75.75 0 111.06 1.06l-4 4a.75.75 0 01-1.06 0l-4-4a.75.75 0 011.06-1.06l2.72 2.72V2.75A.75.75 0 0110 2zM3 13.75A.75.75 0 013.75 13h12.5a.75.75 0 010 1.5H3.75A.75.75 0 013 13.75z" clip-rule="evenodd"/></svg>
            <span id="modal-download-text">Download EPUB</span>
          </a>
          <span id="modal-book-size" class="modal-file-size"></span>
        </div>

        <div class="modal-info-column">
          <div class="modal-meta-row">
            <span id="modal-book-collection" class="book-collection-tag"></span>
            <span id="modal-book-creator" class="modal-creator-tag"></span>
          </div>

          <h2 id="modal-book-title" class="modal-title"></h2>
          <p id="modal-book-subtitle" class="modal-subtitle"></p>

          <div class="modal-section">
            <h4 class="modal-section-title">Overview</h4>
            <p id="modal-book-desc" class="modal-desc"></p>
          </div>

          <div class="modal-section">
            <h4 class="modal-section-title">Key Highlights</h4>
            <ul id="modal-book-highlights" class="modal-highlights-list"></ul>
          </div>

          <div class="modal-section">
            <h4 class="modal-section-title">Contents &amp; Scope</h4>
            <p id="modal-book-contents" class="modal-contents-desc"></p>
          </div>
        </div>
      </div>
    </div>
  </dialog>

  <!-- Embed catalog JSON for instantaneous client-side access -->
  <script type="application/json" id="catalog-data">
{json.dumps(catalog, indent=2)}
  </script>

  <script src="app.js" type="module"></script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as out:
        out.write(html_content)
    print("Generated index.html successfully!")

if __name__ == '__main__':
    generate_html()
