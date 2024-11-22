# 在 Azure 中通过命令行创建 Python 函数
[快速入门](https://learn.microsoft.com/zh-cn/azure/azure-functions/create-first-function-cli-python?pivots=python-mode-decorators&tabs=windows%2Cbash%2Cazure-cli%2Cbrowser)

## 配置本地环境
- [在 Windows 上安装 Azure CLI](https://learn.microsoft.com/zh-cn/cli/azure/install-azure-cli-windows?tabs=azure-cli)
- [Azure Az PowerShell 模块 5.9.0 或更高版本](https://learn.microsoft.com/zh-cn/powershell/azure/install-azure-powershell)
    - [安装受支持的 PowerShell 版本 7 或更高版本](https://mirrors.sdu.edu.cn/github-release/1729821064/github-release/PowerShell_PowerShell/v7.4.6/)
    - 将 PowerShell 执行策略设置为“远程签名”或“更低限制”
        ```
        Get-ExecutionPolicy -List
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        ```
    - 使用 Install-Module cmdlet 安装 Az PowerShell 模块：
        ```
        Install-Module -Name Az -Repository PSGallery -Force
        ```
