# score_print_helper
## 项目介绍： 
### 相必各位打印谱子总存在打印要求过于繁琐，比如各声部谱各需要打n份（有可能会招打印店厌烦/(ㄒoㄒ)/~~）
### 本项目旨在解决这个问题，通过简单的配置文件，即可实现一键打印谱子，支持多声部，支持打印多份

## v0.1.0 版本更新内容
### 支持基本的多声部打印

## v0.2.0 版本更新内容
### 在v0.0.1版本的基础上，增加了一个GUI界面，用户可以在界面上输入源文件名、新文件名和乐器名及数量，然后点击“生成PDF”按钮，程序会根据用户输入的信息生成新的PDF文件。

## v0.3.0 版本更新内容
### 该版本的代码是在v0.2.0的基础上进行修改的，给乐器选择框添加了默认选项和自定义乐器输入框，用户可以选择常见乐器类型或输入自定义乐器名称。
### 另外可以选择源文件名，省去输入。新文件名默认为源文件名加上“_改”。

## v0.4.0 版本更新内容
### 该版本在v0.3.0的基础上将默认乐器列表保存到了JSON文件中，用户可以在JSON文件中添加或删除乐器类型。程序会在启动时加载JSON文件中的乐器列表，用户可以在乐器选择框中选择常见乐器类型或输入自定义乐器名称。
### 同时，json会在用户添加新乐器时自动更新，用户下次启动程序时会看到新添加的乐器类型。

## v1.0.0正式版 版本更新内容
### 该版本在v0.4.0的基础上实现了跨文件夹选择源文件及目标地址的功能，用户可以选择源文件夹和目标文件夹。

## 项目使用说明（截至v1.0.0）：
### 1. 下载项目文件夹
### 2. 使用IDE打开项目文件夹
### 3. 安装依赖库：
```
pip install requirements.txt
```
### 4. 运行score_print_helper.py文件


