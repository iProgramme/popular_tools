# 量安科技脚手架

## 产生原因

由于公司每次新起一个项目的时候，都需要一些配置是固定的，如登录页面，账号密码登陆，UK登录，路由管理，权限管理，后台管理，请求管理，404页面，个人信息管理，常用的验证手机号，验证邮箱，验证密码等等。所以我们需要一个简单的脚手架来解决这些问题。

## 目前公司的Sonatype Nexus的问题

1. 包已经发布在 http://172.16.0.192:8081/repository/npm-host/ 上，但是不管用 http://172.16.0.192:8081/repository/npm-host/ 这个地址还是 http://172.16.0.192:8081/repository/npm-pub/ 地址都提示404找不到该包，而且又需要多记住一个账号密码，很不友好
2. 该包管理平台不会直接加载包的readme.md文档，无法直观看到用法，仅仅只是记录下了一个压缩包而已

## 量安科技脚手架的使用

量安科技脚手架的使用方法: 
1. 全局安装本包
2. 运行 `pqc my-project` 命令
3. sudo npm unlink web-yubowen -g 来移除本包

## 说明
该脚手架基于umi框架

## 存在的问题
2023年08月30日：
1. 目前在子进程上上下选择的时候还有点问题，虽然不影响实际生成的效果，但影响观感

## 已解决的问题

### 2023年08月30日：
1. 创建指定文件夹，并依次判断用户是否有 pnpm, yarn, cnpm, npm
2. 初始化项目，并将所有的ts改为js，所有的tsx改为jsx
3. 可以生成一个文件夹及一个带有内容的文件

## 待更新的内容
1. 将所需要的固定的配置，如登录页面，账号密码登陆，UK登录，路由管理，权限管理，后台管理，请求管理，404页面，个人信息管理，常用的验证手机号，验证邮箱，验证密码等等全部生成出来
2. 生成多个带有内容的文件并在每一步成功的时候打印出来，全部成功的时候打印出来
3. 生成的项目自动安装指定的包如antd等等