#!/bin/bash

BACKUP_DIR="{{ docker_backup_target }}"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
HOSTNAME=$(hostname)
ARCHIVE="$BACKUP_DIR/docker-backup-${HOSTNAME}-${TIMESTAMP}.tar.gz"

echo "[*] Creating backup directory: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

echo "[*] Saving running container list"
docker ps -a > "$BACKUP_DIR/containers-$TIMESTAMP.txt"

echo "[*] Exporting container images"
for ID in $(docker ps -q); do
  NAME=$(docker inspect --format='{{.Name}}' "$ID" | cut -c2-)
  docker export "$ID" | gzip > "$BACKUP_DIR/${NAME}-${TIMESTAMP}.tar.gz"
done

echo "[*] Creating archive..."
tar -czf "$ARCHIVE" -C "$BACKUP_DIR" .

echo "[*] Backup complete: $ARCHIVE"
