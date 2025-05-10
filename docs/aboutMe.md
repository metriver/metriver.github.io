# 关于我 

<div class="about-container" style="
    display: flex;
    gap: 2rem;
    align-items: center;
    margin: 2rem 0;
    flex-wrap: wrap;
">

![我的头像](assets\avatar.jpg){ .avatar style="
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    flex-shrink: 0;
" }

<div class="bio" style="flex: 1; min-width: 300px;">
<h2 style="margin: 0 0 1rem 0; color: var(--md-primary-fg-color)">王小明</h2>

<div class="social-links" style="
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
">
[<span class="twemoji">{% include ".icons/fontawesome/brands/github.svg" %}</span> GitHub](https://github.com){: target="_blank" .md-button .md-button--primary }
[<span class="twemoji">{% include ".icons/fontawesome/brands/twitter.svg" %}</span> Twitter](https://twitter.com){: target="_blank" .md-button }
</div>

<p style="margin: 0; line-height: 1.6;">学生。</p>
</div>
</div>

## 技术栈 {#skills .skill-header}

<div class="skill-grid" style="
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
">

<div class="skill-card" style="
    background: var(--md-code-bg-color);
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
">
<h3 style="margin: 0 0 1rem 0;">前台</h3>
<div class="skill-item" style="margin: 0.5rem 0;">
    <div style="display: flex; justify-content: space-between;">
        <span>Vue/React</span>
        <span>90%</span>
    </div>
    <div class="progress-bar" style="
        height: 8px;
        background: #eee;
        border-radius: 4px;
        overflow: hidden;
    ">
        <div style="width: 90%; height: 100%; background: #007bff; transition: width 0.3s;"></div>
    </div>
</div>
<!-- 更多技能项 -->
</div>

<div class="skill-card" style="...">
<h3 style="...">后厨</h3>
<!-- 类似结构 -->
</div>

</div>

## 精选项目 {#projects}

<div class="project-grid" style="
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
">

<div class="project-card" style="
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 8px;
    overflow: hidden;
">
<div style="padding: 1.5rem;">
<h3 style="margin: 0 0 1rem 0;">123</h3>
<p style="margin: 0 0 1rem 0;">4567</p>
<div class="tech-tags" style="
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
">
    <span style="
        background: var(--md-primary-fg-color);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8em;
    ">Vue3</span>
    <!-- 更多标签 -->
</div>
</div>
<div class="project-footer" style="
    background: var(--md-code-bg-color);
    padding: 1rem;
    text-align: right;
">
<a href="#" class="md-button md-button--primary">查看详情 →</a>
</div>
</div>

<!-- 更多项目卡片 -->

</div>