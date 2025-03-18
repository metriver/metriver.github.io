---
title: obsidian + git 实现自动部署
date: 2024-10-12 10:01:07
tags:
  - tech
---

# 基本配置

## 创建知识库

首先用obsidian打开你的本地博资源，打开成功后，将会在根目录会生成一个`.obsidian`文件夹，作用是记录你的设置以及在这个知识库里装的一些插件，在别的设备打开这个知识库就不用重新配置了。

## 忽略多余文件

打开 设置>文件与链接>Exclude Files
因为文章都在source下，所以只保留source，其它的忽略掉
这有利于提高检索效率

## 文章管理

### 自定义文章生成路径

`ctrl+，`打开设置 > Files & Links > 存放新建笔记文件夹 > `source/_posts`

### 快速插入Front-Matter模板

设置 > 核心插件 >  模板 > 打开模板设置 
在根目录创建一个`template`文件夹，让模板保存在此
设置日期格式 `YYYY-MM-DD HH:mm:ss`
编写模板:
比如这样：

```markdown
---
title: {{title}}
date: {{date}}
tags:
thumbnail: 
categories:
sticky: 
excerpt: 
---
```

# git插件的使用

## 安装git

在obsidian中，关闭安全模式。
在社区插件中搜索Git，下载Git插件。

## 配置仓库

在GitHub上创建一个**空**仓库，readme文件也不要有。私人仓库即可~
在根目录bash一下，输入

```bash
git init                 #初始化文件夹  
git add .                #添加文件到缓存区域  
git commit -m "文件描述"  #提交更改并添加更改信息  
git remote add origin https://github.com/xxx/note.git （SSH或着HTTP的仓库链接）  
git push -u origin main （branch是什么就是什么，一般默认是main） #推送到仓库存储
```

完成上述，obsidian中的Git插件就可以正常使用啦，同时在`git init`后，目录下出现了`.git`文件(看不见就是被隐藏了)~
tips 可以设置每X分钟自动备份文件到github仓库上哦

## 配置Git Hook

打开`.git/hook`，新建`pre_commit`文件（无后缀）写入一下代码：

```sh
#!/bin/sh

#进入博客所在的根目录进行hexo操作 这里基础目录与`.git`同目录
  
hexo cl  
  
hexo g  
  
hexo d  
  
if [ $? -ne 0 ]; then  
  echo "Hexo generate or deploy failed. Commit aborted."  
  exit 1  
fi  
  
exit 0
```

恭喜你 现在就可以自动部署啦！
只需要写完文章 等待obisidian自动部署就好啦~（当然这需要设置自动上传，否则需要你动动鼠标点一点）

# Last

实现的逻辑 obsidian仓库上传到GitHub时会触发配置的Hook，这时会运行`pre_commit`文件，实现hexo的--cl，--g，--d
配置图片的事情 下次吧~