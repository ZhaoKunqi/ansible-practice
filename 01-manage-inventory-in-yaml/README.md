# 实践 01：将 Ansible 清单从 INI 格式转换为 YAML 格式

## 概述

在本实践中，您将学习如何将 Ansible 清单文件从 INI 格式转换为 YAML 格式。清单文件是 Ansible 的关键组成部分，其中包含 Ansible 可以管理的 hosts 和 groups 的信息。

## 背景故事

您是一位初级运维工程师，为了抗击疫情，您加入了北京健康码项目团队。在疫情恶化的情况下，北京实施了全面封城措施，限制了人员流动，以遏制疫情的蔓延。

不幸的是，您的上级领导和一群资深工程师，感染了病毒，并被送往传染病医院接受治疗。然而，幸运的是，您保持了健康，并被困在了北京健康码项目的服务器机房里。

由于封城措施的实施，您被困在机房中，每天只能依靠穿着白色防护服的工作人员送来勉强维持生命体征的食物。

尽管面临着营养不良的困扰，但您仍然坚守岗位，独自一人维护着北京健康码项目的服务器集群，为北京市民提供健康码和核酸检测服务器管理的服务。

在这个艰难的时期，您的上级领导通过手机给您发了一条微信消息，要求您将Ansible的主机清单文件`inventory.ini`转换为YAML格式的`inventory.yml`。

尽管任务艰巨，但作为一名坚定的工程师，您接受了这个挑战，并决心完成任务，以确保系统的正常运行。

现在，让我们开始转换Ansible清单文件的任务，将其从INI格式转换为YAML格式，以提高清单文件的可读性和可维护性。

通过这个实践，您将更好地理解YAML格式的基本语法，并加深对Ansible清单格式的理解，为您的工作提供更好的基础。

## 目标

在本实践结束时，您将能够：

* 理解 YAML 格式的基本语法
* 将 Ansible 清单文件从 INI 格式转换为 YAML 格式
* 更好地理解 Ansible 清单格式

## 先决条件

在开始本实践之前，您应该对 Ansible 清单格式和语法有基本的了解。您还应该在您的计算机上安装文本编辑器。

## 步骤

1. 在文本编辑器中打开 `inventory.ini` 文件。
2. 创建一个名为 `inventory.yml` 的新文件。
3. 将 `inventory.ini` 文件的内容复制到 `inventory.yml` 文件中。
4. 修改 `inventory.yml` 文件的内容以符合 YAML 语法。例如，用连字符和冒号替换方括号。
5. 保存 `inventory.yml` 文件并关闭该文件。

以下是 `inventory.yml` 文件的示例：

```yaml
---
ansible_tower_hosts:
  hosts:
    server[2:4].healthcode.covid-apps.beijing.gov.cn:

backend_servers:
  hosts:
    server[6:172].healthcode.covid-apps.beijing.gov.cn:

loadbalancer:
  hosts:
    server[210-212].healthcode.covid-apps.beijing.gov.cn:

jumpserver:
  hosts:
    server[179-181].healthcode.covid-apps.beijing.gov.cn:

health_code_testing:
  children:
    - loadbalancer
    - backend_servers
```

## 结论

在本实践中，您学习了如何将 Ansible 清单文件从 INI 格式转换为 YAML 格式。您还对 YAML 语法和 Ansible 清单格式有了更好的理解。将清单文件转换为 YAML 格式可以使它们更易读和更易管理。


希望这对您有帮助！ 
