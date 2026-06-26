---
title: 首页
hide:
  - toc
---

<style>
.md-grid { max-width: 100%; }
.md-content__inner { padding: 0 !important; }
.md-typeset > h1:first-of-type { display: none; }
.md-sidebar { display: none !important; }
.md-main__inner { max-width: 100%; padding: 0; }

.home-page {
  min-height: 80vh;
  max-width: 860px;
  margin: 0 auto;
  padding: 3rem 2rem 2rem;
  animation: fadeIn 0.5s ease both;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Hero */
.home-hero { text-align: center; margin-bottom: 3rem; }
.home-hero-name {
  font-size: 2.2rem; font-weight: 800;
  letter-spacing: -0.02em; line-height: 1.2;
  margin-bottom: 0.3rem;
}
.home-hero-name em {
  font-style: normal;
  background: linear-gradient(135deg, #4f6cf7, #7c5bf5);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.home-hero-motto {
  font-size: 0.9rem;
  color: #64748b;
  letter-spacing: 0.2em;
  margin: 0 0 0.6rem;
}
.home-hero-bio {
  font-size: 0.85rem;
  color: #94a3b8;
  max-width: 400px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Section */
.sec-head {
  font-size: 0.72rem; font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(100,116,139,0.15);
}

/* Post list */
.post-list { margin-bottom: 2.5rem; }
.post-item {
  display: flex; align-items: baseline; gap: 1rem;
  padding: 0.65rem 0 0.65rem 1rem;
  text-decoration: none !important;
  border-left: 2px solid transparent;
  transition: all 0.2s;
}
.post-item:hover {
  border-left-color: #4f6cf7;
  padding-left: 1.3rem;
}
.post-item-title {
  flex: 1; font-size: 0.92rem; font-weight: 600;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.post-item-date {
  font-size: 0.72rem; color: #64748b;
  white-space: nowrap;
}
.post-empty { color: #64748b; font-size: 0.85rem; padding: 1rem 0; }

/* Stats */
.stats-row {
  display: flex; gap: 2rem; justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}
.stats-item { text-align: center; }
.stats-val {
  font-size: 1.2rem; font-weight: 800;
  font-variant-numeric: tabular-nums;
}
.stats-lbl {
  font-size: 0.62rem; color: #64748b;
  text-transform: uppercase; letter-spacing: 0.06em;
}

/* Footer */
.home-footer {
  text-align: center;
  padding-top: 2rem;
  font-size: 0.72rem; color: #64748b;
  border-top: 1px solid rgba(100,116,139,0.1);
}

@media (max-width: 600px) {
  .home-page { padding: 2rem 1.2rem 1.5rem; }
  .home-hero-name { font-size: 1.6rem; }
  .stats-row { gap: 1.2rem; }
}
</style>

<div class="home-page">

  <div class="home-hero">
    <div class="home-hero-name">Hi, I'm <em>Metriver</em></div>
    <p class="home-hero-motto">好好学习 天天向上</p>
    <p class="home-hero-bio">A space for continuous learning, creation, and sharing. Exploring tech and life.</p>
  </div>

  <div class="sec-head">Recent Posts</div>
  <div class="post-list" id="recent-list">
    <div class="post-empty">Loading...</div>
  </div>

  <div class="sec-head">Stats</div>
  <div class="stats-row">
    <div class="stats-item"><div class="stats-val" id="stat-pages">--</div><div class="stats-lbl">Pages</div></div>
    <div class="stats-item"><div class="stats-val" id="stat-words">--</div><div class="stats-lbl">Words</div></div>
    <div class="stats-item"><div class="stats-val" id="stat-codes">--</div><div class="stats-lbl">Code</div></div>
    <div class="stats-item"><div class="stats-val" id="stat-time">--</div><div class="stats-lbl">Uptime</div></div>
  </div>

  <div class="home-footer">© 2024-2025 Metriver · Learning River</div>
</div>

<script>
fetch('sitemap.xml').then(function(r) {
  if (!r.ok) throw 0; return r.text();
}).then(function(xml) {
  var doc = new DOMParser().parseFromString(xml, 'text/xml');
  var pages = [];
  doc.querySelectorAll('url').forEach(function(u) {
    var loc = u.querySelector('loc'), mod = u.querySelector('lastmod');
    if (!loc) return;
    try { var path = new URL(loc.textContent).pathname; } catch(e) { return; }
    if (path.indexOf('/tags/') !== -1 || path.indexOf('/blog/page/') !== -1) return;
    pages.push({ path: path, date: mod ? mod.textContent : '' });
  });

  /* Blog posts only */
  var posts = [];
  for (var i = 0; i < pages.length; i++) {
    var p = pages[i];
    if (!p.date) continue;
    var segs = p.path.replace(/\/+$/, '').split('/');
    if (segs[1] === 'blog' && segs.length >= 6 &&
        /^\d{4}$/.test(segs[2]) && /^\d{2}$/.test(segs[3]) && /^\d{2}$/.test(segs[4])) {
      posts.push(p);
    }
  }
  posts.sort(function(a, b) { return b.date.localeCompare(a.date); });

  var html = '';
  posts.slice(0, 5).forEach(function(p) {
    var slug = p.path.replace(/^\/blog\/\d{4}\/\d{2}\/\d{2}\//, '').replace(/\/+$/, '');
    try { slug = decodeURIComponent(slug); } catch(e) {}
    slug = slug.replace(/-/g, ' ');
    html += '<a class="post-item" href="' + p.path + '">'
      + '<span class="post-item-title">' + slug + '</span>'
      + '<span class="post-item-date">' + p.date.substring(0, 10) + '</span></a>';
  });
  document.getElementById('recent-list').innerHTML = html || '<div class="post-empty">No posts yet</div>';

  /* Stats */
  document.getElementById('stat-pages').textContent = pages.length;
  var t0 = new Date('2024-06-27T10:21:33').getTime();
  function tick() { document.getElementById('stat-time').textContent = Math.floor((Date.now() - t0) / 864e5) + 'd'; }
  tick(); setInterval(tick, 60000);
  var wc = 0, cc = 0, n = 0, lim = Math.min(pages.length, 20);
  if (lim) for (var k = 0; k < lim; k++) (function(u) {
    fetch(u).then(function(r) { return r.text(); }).then(function(h) {
      var t = document.createElement('div'); t.innerHTML = h;
      var a = t.querySelector('.md-content__inner') || t;
      wc += (a.textContent || '').replace(/\s/g, '').length;
      cc += a.querySelectorAll('pre code').length;
      if (++n === lim) {
        document.getElementById('stat-words').textContent = wc.toLocaleString();
        document.getElementById('stat-codes').textContent = cc;
      }
    }).catch(function() { n++; });
  })(pages[k].path);
}).catch(function() {});
</script>
