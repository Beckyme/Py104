### Git安装及仓库创建  
在廖雪峰老师提供的[网址](https://pan.baidu.com/s/1kU5OCOB#list/path=%2Fpub%2Fgit)下载exe文件后，双击打开并按默认选项安装。  
开始菜单找到"Git"->"Git Bash"在跳出的命令行窗口中添加姓名和E-mail地址。命令如下：
```
$ git config --global user.name "Name"
$ git config --global user.email "E-mail Address"
```
`git config`命令中`--global`参数的使用表示当前计算机上所有的Git仓库都会使用这个配置。  

`mkdir`会在当前路径中创建一个空目录，所以如果不想在当前路径创建仓库，需先使用`cd`命令进入想创建仓库的路径，再使用`mkdir`命令。`pwd`命令可显示当前路径。  
也可以手动新建文件夹，然后使用`cd`命令切换到该路径中（不推荐）。  
__注意：__ 路径中各级都推荐使用英文。  

`git init`命令可以将当前目录变成Git可管理的仓库，使用后当前目录会生成`.git`的隐藏文件，使用`ls -ah`命令可以显示隐藏文件夹。若仍不能显示，可以在文件夹选项中更改显示隐藏文件夹的复选框。  

### 文件操作
#### 新建及提交文件
【补充新建文件】`vi`文件名.txt，`i`进入编辑模式输入完内容后按ESC键，键盘输入`:wq`即可保存退出。  

在当前目录下新建.txt文档，输入内容保存。

使用`git add <file>`命令将文件添加到仓库：
```
$ git add readme.txt
```
使用`git commit -m "XXX"`命令告诉Git，将文件提交到仓库，该命令`-m`后输入的是本次提交的说明，方便从历史记录中找到改动记录。`comit`命令可一次性上传多次`add`的文件。  

Git有工作区和缓存区，其中`git add`将修改放至缓存区。如果不`add`到缓存区，使用`git commit`无法将该修改提交到`master`或`branch`。
#### 修改文件状态查询
`git status`命令用于查看仓库当前状态，如文件是否修改，修改是否被提交。  
修改过的文档提交与提交新文档相同（`git add` + `git commit`)。

`git diff`命令可以查看文档修改内容。

`git log`命令可以查看历史记录。使用`--pretty=oneline`参数可以简化历史记录，只显示`commit id`以及该版本的提交说明。
#### 版本切换
在Git中，`HEAD`表示当前版本，上一个版本为`HEAD^`，上上个版本为`head^^`，往上的第n个版本为`head~n`。
`git reset --hard`命令可以返回之前的版本。返回原来的版本，其后的版本就在`git log`中看不到了。  
该命令行窗口没被关掉，查找到最新版本的`commit id`就可以继续使用`git reset --hard`命令回到未来的那个最新版本。`commit id`可以不用写全，但要能与其他版本号区别开。  
当命令行窗口被关掉，仍要恢复到之前的最新版，可以使用`git reflog`命令找到最新版的`commit id`，同上使用`git reset --hard commit_id`返回。  
#### 撤销修改
撤销工作区的修改使用`git checkout --<file>`命令。  
撤销暂存区的修改首先用`git reset HEAD <file>`命令，之后与撤销工作区修改相同。  
没有推送至远程仓库但commit的情况参考 __版本切换__ 。  
__注意：__ `git checkout --<file>`命令中如果没有`--`就变成了“切换到另一个分支”的命令。
#### 删除文件
使用`rm`命令删除该设备文件。  
使用`git rm`命令删除版本库中的文件，并且需要继续`git commit`。  
__注意 ：__ `git checkout`其实是用版本库中的版本替换工作区的版本，无论工作区是修改还是删除都可还原。提交至版本库中的文件如果恢复只能恢复到最新版本，最后一次提交后作出的修改会丢失。  

### GitHub仓库
#### 本地Git仓库与GitHub仓库连接
1. 创建SSH Key。  
`$ ssh-keygen -t rsa -C "E-mail Address"`  
之后使用默认值即可。  
在用户主目录中找到`.ssh`目录，其中的`id_rsa`是私钥，不能泄露出去；`id_rsa.pub`是公钥。   
2. 登陆GitHub，打开“Settings”->“SSH and GPG keys”->“New SSH Key”页面。Title任意填，Key中国粘贴`id_rsa.pub`文件的内容，然后“Add Key”。  
#### 远程仓库克隆
使用`git clone`命令可以将远程仓库克隆至一个本地仓库。
1. ```$ git clone git@github.com:YourGitHubName/YourGitHubRepository.git```  
2.```$ git clone https://github.com/YourGitHubName/YourGitHubRepository.git```   
Git支持多种协议，默认的`git://`使用ssh，也可以使用`https`等其他协议。  
`https`协议传输速度慢，每次推送都必须输入口令，但推荐只开放`http`端口的公司使用。

### 分支管理
#### 分支的创建与合并
`git checkout -b "BranchName"`命令创建并切换到该分支。相当于命令`git branch ""`和`git checkout ""`的合并。  
`git branch`命令会列出所有分支，其中当前分支以`*`区分。  
`git merge "BranchName"`命令可以将指定分支合并到当前分支。  
`git checkout -d "BranchName"`命令用于删除指定分支。  
使用分支完成某个任务，合并后再删掉分支，这和直接在`master`分支上工作效果相同，但过程更安全。