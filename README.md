# Kaotic Fire: Backuptools Ansible Collection

Automated backup tools for containers and desktops — semantically versioned, CI-tested, and Galaxy-published.

## Collection Overview

This collection bundles roles for reliable data backup:

- `kaoticfire.backuptools.docker_backup`  
  System-level container backup with OverlayFS, logs, timers, JSON summaries.

- `kaoticfire.backuptools.desktop_backup`  
  Desktop backup of user folders with exclusions, compression, and timer scheduling.

## Quick Install

```bash
ansible-galaxy collection install kaoticfire.backuptools
```

## Usage Example
    - name: Run Docker Backup
    hosts: docker_hosts
    roles:
        - role: kaoticfire.backuptools.docker_backup

    - name: Schedule Desktop Backup
    hosts: localhost
    become: true
    roles:
        - role: kaoticfire.backuptools.desktop_backup
        vars:
            desktop_backup_include:
            - "$HOME/Documents"
            - "$HOME/Pictures"
            desktop_backup_exclude:
            - "**/node_modules"
            desktop_backup_time: "03:00"

## CI & Versioning
- Continuous Integration with Molecule and ansible-lint
- Semantic versioning with bump2version
- Tagged releases for traceable changelogs

## Galaxy Publishing
    make package
    ansible-galaxy collection publish kaoticfire-backuptools-1.0.0.tar.gz

## Documentation Site
Hosted via GitHub Pages: [docs]("https://kaoticfire.github.ioansible-collection-backuptools")  
Includes branded logo, favicon, and syntax highlighting powered by [Prism.js] (https://Prism.js)

## Built with by Kaotic Fire — unleash your backups

---
