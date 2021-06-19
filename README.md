[![](https://github.com/ansible-roles-mamono210/prometheus/workflows/build/badge.svg)](https://github.com/ansible-roles-mamono210/prometheus/actions?query=workflow%3Abuild)

Role Description
=========

Installs [Prometheus](https://prometheus.io) for CentOS7/8.

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

```YAML
---
- hosts: all
  become: true
  roles:
    - prometheus
```

License
-------

BSD
