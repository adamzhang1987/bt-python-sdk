
# 宝塔 Linux 面板 API 接口文档（Markdown 格式）

> 所有接口均为 `POST` 请求，返回格式为 `JSON`。

---

## 🖥 系统状态相关接口

| 接口名称 | URL 地址 |
|----------|----------|
| 获取系统基础统计 | `/system?action=GetSystemTotal` |
| 获取磁盘分区信息 | `/system?action=GetDiskInfo` |
| 获取实时状态信息（CPU、内存、网络、负载） | `/system?action=GetNetWork` |
| 检查是否有安装任务 | `/ajax?action=GetTaskCount` |
| 检查面板更新 | `/ajax?action=UpdatePanel` |

---

## 🌐 网站管理接口

### 网站基本操作

| 接口名称 | URL 地址 |
|----------|----------|
| 获取网站列表 | `/data?action=getData&table=sites` |
| 获取网站分类 | `/site?action=get_site_types` |
| 获取已安装 PHP 版本列表 | `/site?action=GetPHPVersion` |
| 创建网站 | `/site?action=AddSite` |
| 删除网站 | `/site?action=DeleteSite` |
| 停用网站 | `/site?action=SiteStop` |
| 启用网站 | `/site?action=SiteStart` |
| 设置网站到期时间 | `/site?action=SetEdate` |
| 修改网站备注 | `/data?action=setPs&table=sites` |

---

### 网站备份管理

| 接口名称 | URL 地址 |
|----------|----------|
| 获取网站备份列表 | `/data?action=getData&table=backup` |
| 创建网站备份 | `/site?action=ToBackup` |
| 删除网站备份 | `/site?action=DelBackup` |

---

### 域名管理

| 接口名称 | URL 地址 |
|----------|----------|
| 获取域名列表 | `/data?action=getData&table=domain` |
| 添加域名 | `/site?action=AddDomain` |
| 删除域名 | `/site?action=DelDomain` |

---

### 伪静态与配置管理

| 接口名称 | URL 地址 |
|----------|----------|
| 获取可选的预定义伪静态列表 | `/site?action=GetRewriteList` |
| 获取指定伪静态规则内容 | `/files?action=GetFileBody` |
| 保存伪静态规则内容 | `/files?action=SaveFileBody` |
| 获取网站配置文件内容 | `/files?action=GetFileBody` |
| 保存网站配置文件内容 | `/files?action=SaveFileBody` |

---

### 网站目录与运行配置

| 接口名称 | URL 地址 |
|----------|----------|
| 获取网站根目录 | `/data?action=getKey&table=sites&key=path` |
| 获取防跨站配置、运行目录、日志开关等 | `/site?action=GetDirUserINI` |
| 设置防跨站状态（自动取反） | `/site?action=SetDirUserINI` |
| 设置是否写访问日志 | `/site?action=logsOpen` |
| 修改网站根目录 | `/site?action=SetPath` |
| 设置网站运行目录 | `/site?action=SetSiteRunPath` |

---

### 密码访问控制

| 接口名称 | URL 地址 |
|----------|----------|
| 设置密码访问 | `/site?action=SetHasPwd` |
| 关闭密码访问 | `/site?action=CloseHasPwd` |

---

### 流量限制（仅支持 nginx）

| 接口名称 | URL 地址 |
|----------|----------|
| 获取流量限制配置 | `/site?action=GetLimitNet` |
| 设置或保存流量限制配置 | `/site?action=SetLimitNet` |
| 关闭流量限制 | `/site?action=CloseLimitNet` |

---

### 默认文档管理

| 接口名称 | URL 地址 |
|----------|----------|
| 获取默认文档信息 | `/site?action=GetIndex` |
| 设置默认文档 | `/site?action=SetIndex` |
