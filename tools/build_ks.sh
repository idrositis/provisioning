#!/bin/bash
# Script to build kickstart files out of a template using cheetah

# cheetah must be reachable
which cheetah >/dev/null || {
  echo "cheetah not found! Install cheetah (e.g. 'pip install cheetah') and retry..."
  exit 1
}

# Argument check
if [ -z "$1" ]; then
  echo "Script to build kickstart files out of a template using cheetah"
  echo "Usage: ${0##*/} <kickstart_file.tmpl>"
  echo " e.g.: ${0##*/} centos6.tmpl"
  exit 0
fi

filename="$1"
if [ ! -r "$filename" ]; then
  echo "[ERROR] Cannot access file '$filename'!" >&2
  exit 2
fi

# Main
cheetah fill --iext="tmpl" --flat "$filename" --oext=ks --nobackup

exit $?
