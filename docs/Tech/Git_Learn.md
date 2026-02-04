## 初始化仓库

### 本地仓库初始化

`git init`：创建.git子目录，初始化仓库

`git add`

`git commit`

### 克隆仓库

`git clone <url> (NewName)`：克隆远程仓库，()为可选项

## Git 基础

### 文件的状态周期

![文件的状态周期](https://git-scm.com/book/zh/v2/images/lifecycle.png)

`git status`：查看文件状态、branch、Untracked files、Changes to be committed......

`git add <filename>`：对于 Untracked file，添加跟踪；对于Modified file 放入 Staged

`.gitignore`：配置忽略文件

`git diff`：Unstaged

`git diff --staged`

`git commit -a -m "message"`：提交，-a 选项把所有 Tracked files staged一并提交

`git rm`

`git mv`

### 提交历史

`git log`：--patch/-p 选项 以补丁格式输出每次提交引入的差异；--stat 选项 粗略统计；--graph 图形显示

### 撤销

`git commit --amend`：代替上一次提交

### 远程仓库

`git remote`：列出远程服务器简写，默认origin

`git remote add <shortname> <url>`：添加远程仓库，shortname为简写，可代替url

`git fetch <remote>`：拉取内容

`git push <remote> <branch>`：推送

`git remote rename oldname newname`：重命名

### 打标签

`git tag`

## Git 分支











