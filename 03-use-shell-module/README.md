# 实践 03：使用Ansible的shell模块

## 概述

在本实践中，您将学习如何在 Ansible的Playbook文件中使用shell模块和jinja2模板来实现简单的shell操作。

## 背景故事

您是一位初级运维工程师，为了抗击疫情，您加入了北京健康码项目团队。在疫情恶化的情况下，北京实施了全面封城措施，限制了人员流动，以遏制疫情的蔓延。

不幸的是，您的上级领导和一群资深工程师，感染了病毒，并被送往传染病医院接受治疗。然而，幸运的是，您保持了健康，并被困在了北京健康码项目的服务器机房里。

由于封城措施的实施，您被困在机房中，每天只能依靠穿着白色防护服的工作人员送来勉强维持生命体征的食物。

尽管面临着营养不良的困扰，但您仍然坚守岗位，独自一人维护着北京健康码项目的服务器集群，为北京市民提供健康码和核酸检测服务器管理的服务。

在这个艰难的时期，您的上级领导，正在医院床上躺着咳嗽输液，仍然牢记项目的重要性，通过手机给您发了一条微信消息。

命令您创建并编写一个Ansible playbook `add-random-covid-positive.yml`，

因为动态清零封城期间需要不停制造恐惧来使民众服从，但是真正做核酸检测又太昂贵，所以需要每天随机找一些普通民众并赋予他们"核酸阳性"和红码警告。

而您的同事，那些经验丰富的高级工程师编写了一个Python脚本，这个脚本会根据指定的参数随机从北京市健康宝活跃用户中选出一定数量的幸运用户，并且赋予他们核酸阳性。

例: 使用这个Python脚本选出一百名北京健康宝活跃用户并赋予他们核酸阳性和红码警告。

```python
python3 add-random-dao-mei-dan.py --count 100
```

但是由于疫情来袭，这个Python脚本还没有成功部署您的这群同事就都被抓到方舱医院隔离治疗了，而您要接替这群感染病毒的倒霉同事完成这个崇高的任务，

add-random-covid-positive-case.yml这个playbook所做的事情就是调用这个Python脚本并且随机生成一个1000-2000之间的数字，来完成阳性任务指标。

尽管您营养不良，并且饿的眼睛冒光，但您毫不犹豫地接受了这个任务，并决心编写这个Ansible剧本，来实现核酸阳性任务的自动化。

您深入研究了Ansible的`shell`模块，并将其应用于`add-random-covid-positive.yml` playbook中。

通过使用这些功能，您成功地实现了这个playbook的需求，实现了每天随机选择1000-2000名幸运用户关押到方舱医院。

## 目标

在本实践结束时，您将能够：

* 简单理解Ansible Playbook中内置模块shell的简单使用
* 初步理解Ansible Playbook中使用{{jinja2}}作为模板来实现一定的动态操作
* 更好地理解 Ansible

## 先决条件

在开始本实践之前，您应该对 Ansible 有基本的了解。

## 步骤

您编写了Ansible-Playbook

add-random-covid-positive-case.yml

```yaml
- name: randomly find 1000-2000 dao mei dan to fangcang
  hosts: mariadb
  become: True
  tasks:
  - name: generate random number to python script
    shell: 'python3 add-random-dao-mei-dan.py --count {{ range(1000, 2001)|random }}'
```

并且将这个playbook提交到了Ansible Tower中，使用Ansible Tower的计划任务功能实现了定期执行。

## 结论

在本实践中，您学习了如何在Ansible Playbook使用shell模块和jinja2来实现简单任务。
希望这对您有帮助！ 
