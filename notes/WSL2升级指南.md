# WSL 1 → WSL 2 升级指南（阶段 0 遗留任务）

> 原因：node v24.19.0 已装好，但 WSL1（无 Linux 内核）无法运行，npm 官方不支持 WSL1。
> 升级 WSL2 是阶段 0 必做项，也是阶段 7（Docker）的前提。
> 检查当前状态：`wsl -l -v`（VERSION 应为 2）

## 步骤（共 3 步，约 5-10 分钟 + 1 次重启）

### 第 1 步：启用"虚拟机平台"功能（需要管理员权限）
1. 开始菜单搜索"PowerShell" → 右键 → **以管理员身份运行**
2. 执行：
   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All
   ```
3. 出现提示时**重启电脑**

### 第 2 步：把 Ubuntu26 转换为 WSL2（重启后做）
1. 再次用**管理员 PowerShell** 执行：
   ```powershell
   wsl --set-version Ubuntu26 2
   ```
2. 等待转换完成（约 1-3 分钟，显示 "Conversion complete"）

### 第 3 步：验证
```powershell
wsl -l -v        # Ubuntu26 的 VERSION 应为 2
wsl -e bash -c "node --version"   # 应输出 v24.19.0，不再报错
```

## 如果第 1 步报错（虚拟化未开启）
- 重启进 BIOS（开机按 Del/F2），开启 **Intel VT-x / AMD SVM** 选项
- 然后重复第 1 步

## 完成后通知导师
在下次会话说"WSL2 已升级"，我会帮你验证 node/npm 运行 + 继续阶段 1。
