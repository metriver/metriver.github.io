---
title: 首页
hide:
  - toc
  - navigation
  - tabs
---

<style>
/* ===== 全局重置 ===== */
.md-grid { max-width: 100%; }
.md-content__inner { padding: 0 !important; }
.md-typeset > h1:first-of-type { display: none; }
.md-sidebar, .md-tabs { display: none !important; }
.md-main__inner { max-width: 100%; padding: 0; }

/* ===== Hero — 全宽背景 ===== */
.home-hero {
  width: 100vw;
  position: relative; left: 50%; right: 50%;
  margin-left: -50vw; margin-right: -50vw;
  text-align: center;
  padding: 4.5rem 2rem 3rem;
  background: linear-gradient(180deg, rgba(58,123,213,0.06) 0%, transparent 100%);
}
.home-emoji { font-size: 3.2rem; display: block; margin-bottom: 0.8rem; }
.home-title { font-size: 2.2rem; font-weight: 800; color: #1a2a3a; margin-bottom: 0.3rem; }
.home-title em {
  font-style: normal;
  background: linear-gradient(135deg, #3a7bd5, #6366f1);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.home-motto { font-size: 1rem; color: #8a9ab0; letter-spacing: 0.2em; margin: 0; }

/* ===== 主体容器 ===== */
.home-body {
  max-width: 920px; width: 100%;
  margin: 0 auto;
  padding: 2.5rem 2rem 3rem;
  display: flex; gap: 2.5rem;
  align-items: flex-start;
}

/* ===== 左栏 — 文章列表 ===== */
.home-left { flex: 1; min-width: 0; }

/* ===== 右栏 — 热力图 + 导航 + 统计 ===== */
.home-right { width: 280px; flex-shrink: 0; }

/* ===== 区块标题 ===== */
.section-title {
  font-size: 0.78rem; font-weight: 700; color: #6a8aaa;
  text-transform: uppercase; letter-spacing: 0.1em;
  margin-bottom: 1rem;
  display: flex; align-items: center; gap: 0.5rem;
}
.section-title::after {
  content: ''; flex: 1; height: 1px;
  background: linear-gradient(90deg, rgba(58,123,213,0.12), transparent);
}

/* ===== 文章列表 ===== */
.post-list { display: flex; flex-direction: column; }
.post-item {
  display: flex; align-items: baseline; gap: 1rem;
  padding: 0.7rem 0;
  border-bottom: 1px solid rgba(58,123,213,0.06);
  text-decoration: none !important;
  transition: all 0.2s;
}
.post-item:last-child { border-bottom: none; }
.post-item:hover { padding-left: 0.4rem; }
.post-item-title {
  flex: 1; font-size: 0.95rem; font-weight: 600; color: #2a4a6a;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.post-item:hover .post-item-title { color: #2563a8; }
.post-item-date { font-size: 0.75rem; color: #a0b8d0; white-space: nowrap; }
.post-empty { color: #a0b8d0; font-size: 0.85rem; padding: 1rem 0; }

/* ===== 热力图 — 右栏自适应 ===== */
.heatmap-box {
  background: rgba(58,123,213,0.03);
  border: 1px solid rgba(58,123,213,0.08);
  border-radius: 14px;
  padding: 1rem;
  margin-bottom: 2rem;
}
.heatmap-grid {
  display: flex; gap: 2px;
  width: 100%;
}
.heatmap-week {
  flex: 1;
  display: flex; flex-direction: column; gap: 2px;
}
.heatmap-cell {
  width: 100%; aspect-ratio: 1; border-radius: 2px;
  background: #e8eff8; transition: transform 0.15s;
}
.heatmap-cell:hover { transform: scale(1.4); z-index: 1; }
.heatmap-cell.l1 { background: #b8d4f0; }
.heatmap-cell.l2 { background: #7bade0; }
.heatmap-cell.l3 { background: #3a7bd5; }
.heatmap-cell.l4 { background: #1a4a90; }
.heatmap-foot {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 0.6rem; font-size: 0.65rem; color: #a0b8d0;
}
.heatmap-legend { display: flex; align-items: center; gap: 0.25rem; }
.heatmap-legend-cell { width: 10px; height: 10px; border-radius: 2px; }

/* ===== 导航 — 右栏竖排 ===== */
.nav-list { display: flex; flex-direction: column; gap: 0; margin-bottom: 2rem; }
.nav-list a {
  display: flex; align-items: center; gap: 0.6rem;
  padding: 0.55rem 0;
  border-bottom: 1px solid rgba(58,123,213,0.06);
  text-decoration: none !important;
  color: #3a5a8a; font-size: 0.88rem; font-weight: 500;
  transition: all 0.2s;
}
.nav-list a:last-child { border-bottom: none; }
.nav-list a:hover { color: #2563a8; padding-left: 0.3rem; }
.nav-icon { font-size: 1rem; width: 1.4rem; text-align: center; }
.nav-arrow { margin-left: auto; color: #b0c4d8; font-size: 0.75rem; transition: transform 0.2s; }
.nav-list a:hover .nav-arrow { transform: translateX(3px); color: #2563a8; }

/* ===== 统计 — 右栏 ===== */
.stats-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;
}
.stats-card {
  background: rgba(58,123,213,0.03);
  border: 1px solid rgba(58,123,213,0.06);
  border-radius: 10px;
  padding: 0.7rem 0.8rem; text-align: center;
}
.stats-card-icon { font-size: 1.1rem; margin-bottom: 0.15rem; }
.stats-card-value { font-size: 1rem; font-weight: 800; color: #2563a8; }
.stats-card-label { font-size: 0.6rem; color: #8a9ab0; text-transform: uppercase; letter-spacing: 0.05em; }

/* ===== 页脚 ===== */
.home-footer {
  text-align: center; padding: 2rem;
  font-size: 0.75rem; color: #b0c4d8;
}

/* ===== 暗色 ===== */
[data-md-color-scheme="slate"] .home-hero { background: linear-gradient(180deg, rgba(20,30,50,0.6) 0%, transparent 100%); }
[data-md-color-scheme="slate"] .home-title { color: #e0e8f4; }
[data-md-color-scheme="slate"] .home-motto { color: #5a7a9a; }
[data-md-color-scheme="slate"] .section-title { color: #5a7a9a; }
[data-md-color-scheme="slate"] .section-title::after { background: linear-gradient(90deg, rgba(91,155,213,0.1), transparent); }
[data-md-color-scheme="slate"] .post-item { border-color: rgba(255,255,255,0.04); }
[data-md-color-scheme="slate"] .post-item-title { color: #8ab4e0; }
[data-md-color-scheme="slate"] .post-item:hover .post-item-title { color: #5b9bd5; }
[data-md-color-scheme="slate"] .post-item-date { color: #5a7a9a; }
[data-md-color-scheme="slate"] .heatmap-box { background: rgba(20,30,50,0.3); border-color: rgba(255,255,255,0.05); }
[data-md-color-scheme="slate"] .heatmap-cell { background: #1a2840; }
[data-md-color-scheme="slate"] .heatmap-cell.l1 { background: #1e3a5a; }
[data-md-color-scheme="slate"] .heatmap-cell.l2 { background: #2a5a8a; }
[data-md-color-scheme="slate"] .heatmap-cell.l3 { background: #3a7bd5; }
[data-md-color-scheme="slate"] .heatmap-cell.l4 { background: #5b9bd5; }
[data-md-color-scheme="slate"] .heatmap-foot { color: #5a7a9a; }
[data-md-color-scheme="slate"] .nav-list a { color: #8ab4e0; border-color: rgba(255,255,255,0.04); }
[data-md-color-scheme="slate"] .nav-list a:hover { color: #5b9bd5; }
[data-md-color-scheme="slate"] .nav-arrow { color: #3a5068; }
[data-md-color-scheme="slate"] .nav-list a:hover .nav-arrow { color: #5b9bd5; }
[data-md-color-scheme="slate"] .stats-card { background: rgba(20,30,50,0.3); border-color: rgba(255,255,255,0.04); }
[data-md-color-scheme="slate"] .stats-card-value { color: #5b9bd5; }
[data-md-color-scheme="slate"] .stats-card-label { color: #5a7a9a; }
[data-md-color-scheme="slate"] .home-footer { color: #3a5068; }

/* ===== 响应式 ===== */
@media (max-width: 700px) {
  .home-hero { padding: 3rem 1.2rem 2rem; }
  .home-title { font-size: 1.6rem; }
  .home-body { flex-direction: column; padding: 1.5rem 1.2rem 2rem; gap: 2rem; }
  .home-right { width: 100%; }
}
</style>

<!-- ===== Hero ===== -->
<div class="home-hero">
  <span class="home-emoji">😎</span>
  <div class="home-title">Hi, I'm <em>Metriver</em></div>
  <p class="home-motto">好好学习 天天向上</p>
</div>

<!-- ===== 左右分栏 ===== -->
<div class="home-body">

  <!-- 左栏：文章 -->
  <div class="home-left">
    <div class="section-title">📰 Recent Posts</div>
    <div class="post-list" id="recent-list">
      <div class="post-empty">Loading...</div>
    </div>
  </div>

  <!-- 右栏：热力图 + 导航 + 统计 -->
  <div class="home-right">

    <!-- 热力图 -->
    <div class="section-title">📊 Activity</div>
    <div class="heatmap-box">
      <div class="heatmap-grid" id="heatmap"></div>
      <div class="heatmap-foot">
        <div class="heatmap-legend">
          <span>Less</span>
          <div class="heatmap-legend-cell" style="background:#e8eff8"></div>
          <div class="heatmap-legend-cell" style="background:#b8d4f0"></div>
          <div class="heatmap-legend-cell" style="background:#7bade0"></div>
          <div class="heatmap-legend-cell" style="background:#3a7bd5"></div>
          <div class="heatmap-legend-cell" style="background:#1a4a90"></div>
          <span>More</span>
        </div>
        <span id="heatmap-count"></span>
      </div>
    </div>

    <!-- 导航 -->
    <div class="section-title">🔗 Navigate</div>
    <div class="nav-list">
      <a href="blog/"><span class="nav-icon">📝</span>Blog<span class="nav-arrow">→</span></a>
      <a href="aboutMe/"><span class="nav-icon">👤</span>About Me<span class="nav-arrow">→</span></a>
      <a href="Learn/"><span class="nav-icon">📚</span>Learn<span class="nav-arrow">→</span></a>
      <a href="Tech/"><span class="nav-icon">🔧</span>Tech<span class="nav-arrow">→</span></a>
      <a href="link/"><span class="nav-icon">🔗</span>Friends<span class="nav-arrow">→</span></a>
    </div>

    <!-- 统计 -->
    <div class="section-title">📈 Stats</div>
    <div class="stats-grid">
      <div class="stats-card"><div class="stats-card-icon">📄</div><div class="stats-card-value" id="stat-pages">--</div><div class="stats-card-label">Pages</div></div>
      <div class="stats-card"><div class="stats-card-icon">✏️</div><div class="stats-card-value" id="stat-words">--</div><div class="stats-card-label">Words</div></div>
      <div class="stats-card"><div class="stats-card-icon">💻</div><div class="stats-card-value" id="stat-codes">--</div><div class="stats-card-label">Code</div></div>
      <div class="stats-card"><div class="stats-card-icon">⏱️</div><div class="stats-card-value" id="stat-time">--</div><div class="stats-card-label">Uptime</div></div>
    </div>

  </div>
</div>

<div class="home-footer">© 2024-2025 Metriver · Learning River</div>

<script>
// ===== 热力图 =====
function renderHeatmap(dateMap, days) {
  var today = new Date(); today.setHours(0,0,0,0);
  var el = document.getElementById('heatmap');
  var startDate = new Date(today);
  startDate.setDate(startDate.getDate() - days + 1);
  startDate.setDate(startDate.getDate() - startDate.getDay());
  var weeks = Math.ceil((days + startDate.getDay()) / 7);
  var total = 0, html = '';
  for (var w = 0; w < weeks; w++) {
    html += '<div class="heatmap-week">';
    for (var dd = 0; dd < 7; dd++) {
      var dt = new Date(startDate);
      dt.setDate(dt.getDate() + w * 7 + dd);
      var y = dt.getFullYear();
      var m = String(dt.getMonth()+1).padStart(2,'0');
      var d = String(dt.getDate()).padStart(2,'0');
      var key = y+'-'+m+'-'+d;
      var count = dateMap[key] || 0;
      total += count;
      var cls = count === 0 ? '' : count <= 2 ? 'l1' : count <= 5 ? 'l2' : count <= 10 ? 'l3' : 'l4';
      var opacity = dt > today ? ' style="opacity:0.2"' : '';
      html += '<div class="heatmap-cell '+cls+'" title="'+key+': '+count+' commits"'+opacity+'></div>';
    }
    html += '</div>';
  }
  el.innerHTML = html;
  var countEl = document.getElementById('heatmap-count');
  if (countEl) countEl.textContent = total + ' commits / ' + days + 'd';
}

// 优先: commits.json (构建时 hook 生成，纯静态文件，零性能开销)
// fallback: sitemap lastmod
fetch('commits.json').then(function(r){
  if (!r.ok) throw 0; return r.json();
}).then(function(data){
  if (Object.keys(data).length > 0) { renderHeatmap(data, 30); return; }
  throw 0;
}).catch(function(){
  fetch('sitemap.xml').then(function(r){return r.text()}).then(function(x){
    var dm = {};
    new DOMParser().parseFromString(x,'text/xml').querySelectorAll('lastmod').forEach(function(m){
      var d = m.textContent.substring(0,10); dm[d] = (dm[d]||0) + 1;
    });
    renderHeatmap(dm, 30);
  }).catch(function(){ renderHeatmap({}, 30); });
});

// ===== 文章 & 统计 =====
fetch('sitemap.xml').then(function(r){return r.text()}).then(function(x){
  var d = new DOMParser().parseFromString(x,'text/xml');
  var pages = [];
  d.querySelectorAll('url').forEach(function(u){
    var loc = u.querySelector('loc'), mod = u.querySelector('lastmod');
    if (!loc) return;
    var path = new URL(loc.textContent).pathname;
    if (path.includes('/tags/') || path.includes('/blog/page/')) return;
    pages.push({ path: path, date: mod ? mod.textContent : '' });
  });

  // 最近文章
  var posts = pages.filter(function(p){
    return /^\/blog\/\d{4}\/\d{2}\/\d{2}\//.test(p.path) && p.date;
  }).sort(function(a,b){ return b.date.localeCompare(a.date); });

  var html = '';
  posts.slice(0, 5).forEach(function(p){
    var slug = p.path.replace(/^\/blog\/\d{4}\/\d{2}\/\d{2}\//, '').replace(/\/$/, '');
    try { slug = decodeURIComponent(slug); } catch(e) {}
    slug = slug.replace(/-/g, ' ');
    html += '<a class="post-item" href="'+p.path+'">'
      + '<span class="post-item-title">'+slug+'</span>'
      + '<span class="post-item-date">'+p.date.substring(0,10)+'</span></a>';
  });
  document.getElementById('recent-list').innerHTML = html || '<div class="post-empty">No posts yet</div>';

  // 统计
  document.getElementById('stat-pages').textContent = pages.length;
  var t0 = new Date('2024-06-27T10:21:33').getTime();
  function tick(){ document.getElementById('stat-time').textContent = Math.floor((Date.now()-t0)/864e5)+'d'; }
  tick(); setInterval(tick, 60000);

  var wc=0, cc=0, n=0, lim=Math.min(pages.length, 20);
  if(lim) for(var i=0;i<lim;i++) (function(u){
    fetch(u).then(function(r){return r.text()}).then(function(h){
      var t=document.createElement('div'); t.innerHTML=h;
      var a=t.querySelector('.md-content__inner')||t;
      wc+=(a.textContent||'').replace(/\s/g,'').length;
      cc+=a.querySelectorAll('pre code').length;
      if(++n===lim){document.getElementById('stat-words').textContent=wc.toLocaleString();document.getElementById('stat-codes').textContent=cc;}
    }).catch(function(){n++;});
  })(pages[i].path);
}).catch(function(){});
</script>
