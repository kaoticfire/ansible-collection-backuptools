# Docker Backup Role

Backs up all running containers to compressed archives. Includes systemd service + timer.

## Variables

| Name                    | Default               |
|-------------------------|------------------------|
| `docker_backup_target` | `/var/backups/docker` |
| `docker_backup_oncalendar` | `"daily"`           |

## Setup

- Exports container images
- Saves to: `/var/backups/docker/docker-backup-<host>-<timestamp>.tar.gz`
- Uses systemd timer to automate

