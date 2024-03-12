#!/usr/bin/env fish
rm (pwd)/.venv/lib/python3.10/site-packages/ansible_collections/laikar/jellyfin/plugins
mkdir --parents (pwd)/.venv/lib/python3.10/site-packages/ansible_collections/laikar/jellyfin/collection
ln --symbolic (pwd)/plugins (pwd)/.venv/lib/python3.10/site-packages/ansible_collections/laikar/jellyfin/