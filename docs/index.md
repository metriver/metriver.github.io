---
title: 首页
---

<style>
.md-grid { max-width: 900px; }
.md-content__inner { padding-bottom: 2rem; }

/* 隐藏默认标题 */
.md-typeset > h1:first-of-type { display: none; }

/* Hero */
.home-hero {
  padding: 4rem 0 2.5rem;
  text-align: center;
}
.home-emoji { font-size: 3.5rem; margin-bottom: 1rem; display: block; }
.home-title {
  font-size: 2.2rem; font-weight: 800; color: #1a2a3a;
  margin-bottom: 0.3rem; line-height: 1.3;
}
.home-title em {
  font-style: normal;
  background: linear-gradient(135deg, #3a7bd5, #6366f1);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.home-motto {
  font-size: 1rem; color: #8a9ab0; letter-spacing: 0.15em;
  margin-bottom: 0;
}

/* 分隔线 */
.home-divider {
  width: 60px; height: 3px; border-radius: 2px;
  background: linear-gradient(90deg, #3a7bd5, #6366f1);
  margin: 2rem auto;
}

/* 导航列表 */
.home-nav {
  max-width: 400px;
  margin: 0 auto 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 0;
}
.home-nav a {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.9rem 0;
  text-decoration: none !important;
  color: #3a5a8a;
  font-size: 1rem;
  font-weight: 500;
  border-bottom: 1px solid rgba(58,123,213,0.08);
  transition: color 0.2s, padding-left 0.2s;
}
.home-nav a:last-child { border-bottom: none; }
.home-nav a:hover {
  color: #2563a8;
  padding-left: 0.5rem;
}
.home-nav-icon { font-size: 1.1rem; width: 1.5rem; text-align: center; }
.home-nav-label { flex: 1; }
.home-nav-arrow { color: #b0c4d8; font-size: 0.85rem; transition: transform 0.2s; }
.home-nav a:hover .home-nav-arrow { transform: translateX(3px); color: #2563a8; }

/* 站点统计 */
.home-stats-toggle {
  display: inline-flex; align-items: center; gap: 0.4rem;
  padding: 0.4rem 1rem; border-radius: 999px;
  font-size: 0.82rem; color: #6a8aaa;
  background: rgba(58,123,213,0.05);
  border: 1px solid rgba(58,123,213,0.1);
  cursor: pointer; transition: all 0.2s;
}
.home-stats-toggle:hover { background: rgba(58,123,213,0.1); color: #3a6b9f; }

.stats-panel {
  display: none; max-width: 500px; margin: 1rem auto 0;
  padding: 1.5rem; border-radius: 16px;
  background: rgba(58,123,213,0.04);
  border: 1px solid rgba(58,123,213,0.08);
  animation: fadeUp 0.3s ease;
}
.stats-panel.show { display: block; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }

.stats-row {
  display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;
  text-align: center;
}
.stat-item { min-width: 80px; }
.stat-icon { font-size: 1.3rem; margin-bottom: 0.2rem; }
.stat-value { font-size: 1.1rem; font-weight: 800; color: #2563a8; }
.stat-label { font-size: 0.7rem; color: #8a9ab0; text-transform: uppercase; letter-spacing: 0.05em; }

/* 底部 */
.home-footer-note {
  text-align: center;
  font-size: 0.78rem;
  color: #b0c4d8;
  margin-top: 2rem;
}

/* 暗色 */
[data-md-color-scheme="slate"] .home-title { color: #e0e8f4; }
[data-md-color-scheme="slate"] .home-motto { color: #5a7a9a; }
[data-md-color-scheme="slate"] .home-nav a { color: #8ab4e0; border-color: rgba(255,255,255,0.06); }
[data-md-color-scheme="slate"] .home-nav a:hover { color: #5b9bd5; }
[data-md-color-scheme="slate"] .home-nav-arrow { color: #3a5068; }
[data-md-color-scheme="slate"] .home-nav a:hover .home-nav-arrow { color: #5b9bd5; }
[data-md-color-scheme="slate"] .home-stats-toggle { background: rgba(91,155,213,0.08); color: #5a7a9a; border-color: rgba(91,155,213,0.1); }
[data-md-color-scheme="slate"] .stats-panel { background: rgba(30,48,80,0.4); border-color: rgba(255,255,255,0.05); }
[data-md-color-scheme="slate"] .stat-value { color: #5b9bd5; }
[data-md-color-scheme="slate"] .stat-label { color: #5a7a9a; }
[data-md-color-scheme="slate"] .home-footer-note { color: #3a5068; }
</style>

<div class="home-hero">
  <span class="home-emoji">😎</span>
  <div class="home-title">Hi, I'm <em>Metriver</em></div>
  <p class="home-motto">好好学习 天天向上</p>
</div>

<div class="home-divider"></div>

<div class="home-nav">
  <a href="blog/">
    <span class="home-nav-icon">📝</span>
    <span class="home-nav-label">博客</span>
    <span class="home-nav-arrow">→</span>
  </a>
  <a href="aboutMe/">
    <span class="home-nav-icon">👤</span>
    <span class="home-nav-label">关于我</span>
    <span class="home-nav-arrow">→</span>
  </a>
  <a href="Tech/Git_Learn/">
    <span class="home-nav-icon">🔧</span>
    <span class="home-nav-label">Git 学习</span>
    <span class="home-nav-arrow">→</span>
  </a>
  <a href="Learn/DataStruct/">
    <span class="home-nav-icon">🏗️</span>
    <span class="home-nav-label">数据结构</span>
    <span class="home-nav-arrow">→</span>
  </a>
  <a href="link/">
    <span class="home-nav-icon">🔗</span>
    <span class="home-nav-label">朋友们</span>
    <span class="home-nav-arrow">→</span>
  </a>
</div>

<div style="text-align:center">
  <span class="home-stats-toggle" onclick="toggleStats()">📊 站点统计</span>
</div>

<div class="stats-panel" id="stats-panel">
  <div class="stats-row">
    <div class="stat-item">
      <div class="stat-icon">📄</div>
      <div class="stat-value" id="stat-pages">--</div>
      <div class="stat-label">页面</div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">✏️</div>
      <div class="stat-value" id="stat-words">--</div>
      <div class="stat-label">字数</div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">💻</div>
      <div class="stat-value" id="stat-codes">--</div>
      <div class="stat-label">代码块</div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">⏱️</div>
      <div class="stat-value" id="stat-time">--</div>
      <div class="stat-label">已运行</div>
    </div>
  </div>
</div>

<div class="home-footer-note">© 2024-2025 Metriver · Learning River</div>

<script>
function toggleStats() {
  var p = document.getElementById('stats-panel');
  p.classList.toggle('show');
  if (p.classList.contains('show') && !p.dataset.loaded) {
    p.dataset.loaded = '1';
    loadStats();
  }
}
function loadStats() {
  var s = new Date('2024-06-27T10:21:33').getTime();
  function t() {
    var d = Date.now() - s;
    document.getElementById('stat-time').textContent =
      Math.floor(d/864e5) + '天' + Math.floor(d/36e5%24) + '时' + Math.floor(d/6e4%60) + '分';
  }
  t(); setInterval(t, 60000);
  fetch('sitemap.xml').then(function(r){return r.text()}).then(function(x){
    var d = new DOMParser().parseFromString(x,'text/xml');
    var pages = [];
    d.querySelectorAll('loc').forEach(function(l){
      var u = new URL(l.textContent);
      if (u.pathname.endsWith('/') && !u.pathname.includes('/tags/') && !u.pathname.includes('/blog/page/'))
        pages.push(u.pathname);
    });
    document.getElementById('stat-pages').textContent = pages.length;
    var w=0,c=0,n=0,lim=Math.min(pages.length,25);
    if(!lim) return;
    for(var i=0;i<lim;i++){
      (function(u){
        fetch(u).then(function(r){return r.text()}).then(function(h){
          var t=document.createElement('div'); t.innerHTML=h;
          var a=t.querySelector('.md-content__inner')||t;
          w+=(a.textContent||'').replace(/\s/g,'').length;
          c+=a.querySelectorAll('pre code').length;
          n++;
          if(n==lim){document.getElementById('stat-words').textContent=w.toLocaleString();document.getElementById('stat-codes').textContent=c;}
        }).catch(function(){n++;});
      })(pages[i]);
    }
  }).catch(function(){});
}
</script>
