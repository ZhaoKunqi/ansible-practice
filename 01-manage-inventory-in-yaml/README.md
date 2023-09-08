# Practice 01: Converting Ansible Inventory from INI to YAML format

## Overview

In this practice, you will learn how to convert an Ansible inventory file from INI format to YAML format. The inventory file is a crucial component of Ansible that contains information about the hosts and groups that Ansible can manage. 

## Background Story

As a system engineer at the Norfolk Naval Base, you play a vital role in supporting the Navy's mission of testing new software. 

The Navy is constantly pushing the boundaries of technology, and it's your responsibility to ensure that their systems are running smoothly and efficiently.

Recently, the Navy acquired a state-of-the-art software solution that requires seamless deployment and management across a diverse range of systems. 
This is where Ansible comes into play. Ansible's automation capabilities will enable you to efficiently configure and manage the software on multiple hosts.

However, there's a small hurdle in your path. The Ansible inventory file you received is in the outdated INI format. 
While it served its purpose in the past, you know that YAML is now the preferred format for Ansible inventories due to its simplicity and readability.

To streamline your operations and make your life easier, you decide to convert the inventory file to YAML format. 
This will not only align with best practices but also provide you with a more intuitive and manageable inventory structure.

With your expertise and determination, you're ready to dive into the practice and convert the Ansible inventory file from INI to YAML format. Let's get started!

## Objectives

By the end of this practice, you will be able to:

- Understand the basic syntax of YAML format
- Convert an Ansible inventory file from INI to YAML format
- Gain a better understanding of the Ansible inventory format

## Prerequisites

Before you begin this practice, you should have a basic understanding of the Ansible inventory format and syntax. You should also have a text editor installed on your computer.

## Steps

1. Open the `inventory.ini` file in a text editor.
2. Create a new file named `inventory.yml`.
3. Copy the contents of `inventory.ini` into `inventory.yml`.
4. Modify the contents of `inventory.yml` to conform to the YAML syntax. For example, replace square brackets with hyphens and colons.
5. Save `inventory.yml` and close the file.

Here is an example of what the `inventory.yml` file should look like:

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

## Conclusion

In this practice, you learned how to convert an Ansible inventory file from INI format to YAML format. You also gained a better understanding of the YAML syntax and the Ansible inventory format. Converting inventory files to YAML format can help make them more readable and easier to manage.
