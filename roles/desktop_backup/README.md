# Desktop Backup Role

Configurable user backup script with systemd timer support.

## Variables

| Name | Description | Default |
|------|-------------|---------|
| `desktop_backup_include` | List of folders to back up | `["$HOME/Documents", "$HOME/Pictures"]` |
| `desktop_backup_exclude` | Glob rules to skip | `["**/node_modules", "**/.cache"]` |
| `desktop_backup_target` | Output folder path | `"$HOME/backups"` |
| `desktop_backup_time` | Time for daily backup | `"03:00"` |

## Behavior

- Compresses selected folders nightly
- Skips excluded patterns
- Stores `tar.gz` archive in user directory
