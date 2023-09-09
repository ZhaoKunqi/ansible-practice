# 实践 01：将 Ansible 清单从 INI 格式转换为 YAML 格式

## 概述

在本实践中，您将学习如何将 Ansible 清单文件从 INI 格式转换为 YAML 格式。清单文件是 Ansible 的关键组成部分，其中包含 Ansible 可以管理的 hosts 和 groups 的信息。

## 背景故事

您是诺福克海军基地的系统工程师，在支持海军测试新软件的使命中发挥着重要作用。

海军一直在不断推动技术的边界，您有责任确保他们的系统运行顺畅高效。

最近，海军收购了一种先进的软件解决方案，需要在各种系统上进行无缝部署和管理。这就是 Ansible 的用武之地。 Ansible 的自动化功能将使您能够有效地配置和管理软件在多个主机上。

但是，您面临一个小障碍。您收到的 Ansible 清单文件是过时的 INI 格式。虽然它在过去曾发挥过作用，但您知道 YAML 现在是 Ansible 清单的首选格式，因为它简单易读。

为了简化您的操作并让您的生活更轻松，您决定将清单文件转换为 YAML 格式。这不仅符合最佳实践，还将为您提供更直观和可管理的清单结构。

有了您的专业知识和决心，您准备好开始实践并将 Ansible 清单文件从 INI 格式转换为 YAML 格式。让我们开始吧！

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
ansible_tower:
  hosts:
    server[2:4].lab.gilbert.navy.private:

k8s_ndk:
  hosts:
    server[6:172].lab.gilbert.navy.private:

satellite_uplink_bak:
  hosts:
    server[210-212].lab.gilbert.navy.private:

jumpserver:
  hosts:
    - server179.lab.gilbert.navy.private
    - server180.lab.gilbert.navy.private
    - server181.lab.gilbert.navy.private

testing_env:
  children:
    - k8s_ndk
    - satellite_uplink_bak
```

## 结论

在本实践中，您学习了如何将 Ansible 清单文件从 INI 格式转换为 YAML 格式。您还对 YAML 语法和 Ansible 清单格式有了更好的理解。将清单文件转换为 YAML 格式可以使它们更易读和更易管理。


希望这对您有帮助！ 
