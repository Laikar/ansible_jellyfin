#!/bin/bash

# usage:
#
# run all tests:
# ./run_tests.sh
#
# run all tests against specific uptime kuma version:
# ./run_tests.sh 1.19.4
#
# run all tests against specific uptime kuma version and specific modules:
# ./run_tests.sh 1.19.4 maintenance maintenance_info

venv_path="$(pwd)/.venv/bin/python"
collection_path="$HOME/.ansible/collections/ansible_collections/laikar/jellyfin"
version="$latest"
modules="${@:2}"

# if [ ! -d "$collection_path" ]
# then
#   ansible-galaxy collection install git+https://github.com/laikar/ansible_jellyfin.git
# fi
# cp -r ./{plugins,tests} "$collection_path"
# cd "$collection_path"

if [ $version ] && [ "$version" != "all" ]
then
  versions=("$version")
else
  versions=(10.8.13)
fi

unit_targets=""
integration_targets=""
for module in ${modules[*]}
do
  unit_filepath="tests/unit/plugins/module_utils/test_${module}.py"
  unit_targets+="${unit_filepath} "

  integration_targets+="${module} "
done

for version in ${versions[*]}
do
  docker rm -f uptimekuma > /dev/null 2>&1

  echo "Starting jellyfin $version..."
  docker run -d -it --rm -p 8096:8096 --name jellyfin "lscr.io/linuxserver/jellyfin:$version" > /dev/null || exit 1

  while [[ "$(curl -s -L -o /dev/null -w ''%{http_code}'' localhost:8096)" != "200" ]]
  do
    sleep 0.5
  done

  echo "Running unit tests..."
  ansible-test units -v --requirements --python-interpreter "$venv_path" --num-workers 1 $unit_targets

  echo ""
  echo "Running integration tests..."
  ansible-test integration -v --requirements --python-interpreter "$venv_path" $integration_targets

  echo "Stopping jellyfin..."
  docker stop jellyfin > /dev/null
  sleep 1

  echo ""
done