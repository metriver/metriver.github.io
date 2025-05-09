<!-- 以下是完整的自包含MD文件内容 -->

<div style="display: none">
<style>
/* Google Material Design 风格 */
:root {
  --primary-color: #4285f4;
  --secondary-color: #34a853;
  --accent-color: #fbbc05;
  --text-color: #202124;
  --bg-color: #f8f9fa;
}

* {
  box-sizing: border-box;
  font-family: 'Roboto', 'Noto Sans SC', sans-serif;
}

body {
  margin: 0;
  padding: 20px;
  background: var(--bg-color);
  color: var(--text-color);
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

/* 卡片式设计 */
.card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  margin: 1rem 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12);
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
}

/* 响应式布局 */
.grid {
  display: grid;
  gap: 2rem;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

/* 技能标签 */
.skill-tag {
  display: inline-block;
  background: var(--primary-color);
  color: white;
  padding: 0.3rem 1rem;
  border-radius: 20px;
  margin: 0.3rem;
  font-size: 0.9em;
}

/* 谷歌风格按钮 */
.g-button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 24px;
  cursor: pointer;
  font-weight: 500;
  transition: opacity 0.2s;
}

.g-button:hover {
  opacity: 0.9;
}

@media (max-width: 768px) {
  .container {
    padding: 10px;
  }
}
</style>

<!-- 引入Material Icons -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
</div>

<div class="container">
  
  # <i class="material-icons">person</i> 个人简介
  
  <div class="card">
    <div class="grid">
      <div>
        <h2>xxx</h2>
        <p>student</p>
        <p><i class="material-icons">location_on</i> 北京, 中国</p>
      </div>
      <div style="text-align: center">
        <img src="assets\avatar.jpg" 
             style="width:150px; height:150px; border-radius:50%" 
             alt="头像">
      </div>
    </div>
  </div>

  ## <i class="material-icons">code</i> 技术栈
  
  <div class="card grid">
    <div>
      <h3>核心技能</h3>
      <div>
        <span class="skill-tag">c</span>
        <span class="skill-tag">。。。</span>
        <span class="skill-tag">。。。</span>
      </div>
    </div>
    <div>
      <h3>其他技能</h3>
      <div>
        <span class="skill-tag">1</span>
        <span class="skill-tag">2</span>
        <span class="skill-tag">3</span>
      </div>
    </div>
  </div>

  ## <i class="material-icons">work</i> 项目展示
  
  <div class="card" id="projects">
    <!-- JS动态生成项目内容 -->
  </div>

  <div class="card" style="text-align: center">
    <button class="g-button" onclick="showContact()">
      <i class="material-icons">mail</i> 联系我
    </button>
  </div>

</div>

<script>
// 项目数据
const projects = [
  {
    title: '电商管理平台',
    tech: ['React', 'Redux', 'Ant Design'],
    desc: '基于微前端架构的企业级解决方案'
  },
  {
    title: '数据可视化系统',
    tech: ['ECharts', 'WebGL', 'Node.js'],
    desc: '实时数据监控与分析平台'
  }
]

// 动态生成项目
function renderProjects() {
  const container = document.getElementById('projects')
  let html = '<h2>代表项目</h2>'
  
  projects.forEach(proj => {
    html += `
      <div style="margin: 1rem 0; padding: 1rem; border-bottom: 1px solid #eee">
        <h3>${proj.title}</h3>
        <p>${proj.desc}</p>
        <div>${proj.tech.map(t => `<span class="skill-tag">${t}</span>`).join('')}</div>
      </div>
    `
  })
  
  container.innerHTML = html
}

// 联系弹窗
function showContact() {
  alert('📧 联系方式: 123@qq.com')
}

// 初始化
window.onload = () => {
  renderProjects()
  // 添加视差效果
  document.addEventListener('mousemove', (e) => {
    const cards = document.querySelectorAll('.card')
    cards.forEach(card => {
      const rect = card.getBoundingClientRect()
      const x = e.clientX - rect.left
      const y = e.clientY - rect.top
      card.style.transform = `
        perspective(1000px)
        rotateX(${(y - rect.height/2)/20}deg)
        rotateY(${-(x - rect.width/2)/20}deg)
      `
    })
  })
}
</script>