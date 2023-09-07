# Practice 01: Converting Ansible Inventory from INI to YAML format

## Overview

In this practice, you will learn how to convert an Ansible inventory file from INI format to YAML format. The inventory file is a crucial component of Ansible that contains information about the hosts and groups that Ansible can manage. 

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
active_web_servers:
  hosts:
    serverb.lab.example.com:
    serverc.lab.example.com:

inactive_web_servers:
  hosts:
    serverd.lab.example.com:
    servere.lab.example.com:
    serverf.lab.example.com:

region_eu:
  hosts:
    serverc.lab.example.com:
    serverf.lab.example.com:

web_servers:
  children:
    active_web_servers:
    inactive_web_servers:

all_servers:
  hosts:
    servera.lab.example.com:
  children:
    web_servers:
```

## Conclusion

In this practice, you learned how to convert an Ansible inventory file from INI format to YAML format. You also gained a better understanding of the YAML syntax and the Ansible inventory format. Converting inventory files to YAML format can help make them more readable and easier to manage.
