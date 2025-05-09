<div style="display: none">
<style>
:root {
  --primary: #1a73e8;
  --surface: #ffffff;
  --border: #dadce0;
  --text-primary: #202124;
  --text-secondary: #5f6368;
}

* {
  margin: 0;
  box-sizing: border-box;
  <!-- font-family: 'Google Sans', 'Noto Sans SC', sans-serif; -->
}

body {
  background: #f8f9fa;
  line-height: 1.5;
  color: var(--text-primary);
  padding: 2rem 1rem;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

.section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 2rem;
  margin: 1.5rem 0;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 3px solid var(--border);
}

.grid {
  display: grid;
  gap: 2rem;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border: 1px solid var(--border);
  border-radius: 20px;
  margin: 0.25rem;
  font-size: 0.9em;
  color: var(--text-secondary);
}

.contact-bar {
  display: flex;
  gap: 1rem;
  justify-content: center;
  padding: 1rem;
}

@media (max-width: 600px) {
  body {
    padding: 1rem;
  }
  
  .section {
    padding: 1.5rem;
  }
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">
</div>

<div class="container">

<div class="section" style="text-align: center">
  <img src="https://via.placeholder.com/120" class="avatar" alt="头像">
  <h1 style="margin: 1rem 0 0.5rem">xxxx</h1>
  <p style="color: var(--text-secondary)">学生 | 哈哈</p>
  <div class="contact-bar">
    <a href="mailto:contact@qq.com">📧 contact@qq.com</a>
    <span>|</span>
    <a href="https://github.com/metriver">🐙 GitHub</a>
  </div>
</div>

<div class="section">
  <h2>技术能力</h2>
  <div class="grid" style="margin-top: 1rem">
    <div>
      <h3>1</h3>
      <div>
        <span class="badge">c</span>
        <span class="badge">...</span>
        <span class="badge">.....</span>
      </div>
    </div>
    <div>
      <h3>2</h3>
      <div>
        <span class="badge">.</span>
        <span class="badge">...</span>
        <span class="badge">.</span>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <h2>项目经历</h2>
  <div id="projects" style="margin-top: 1rem"></div>
</div>

</div>

<script>
const projects = [
  {
    title: '123',
    stack: ['React 18', 'Ant Design 5', 'NestJS'],
    desc: '123+'
  },
  {
    title: '456',
    stack: ['ECharts', 'WebGL', 'WebSocket'],
    desc: '456'
  }
]

function renderProjects() {
  const container = document.getElementById('projects')
  container.innerHTML = projects.map(proj => `
    <div style="margin: 1.5rem 0; padding-bottom: 1rem; border-bottom: 1px solid var(--border)">
      <h3 style="margin-bottom: 0.5rem">${proj.title}</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.75rem">${proj.desc}</p>
      <div>${proj.stack.map(t => `<span class="badge">${t}</span>`).join('')}</div>
    </div>
  `).join('')
}

document.addEventListener('DOMContentLoaded', renderProjects)
</script>