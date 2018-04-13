#!/bin/bash
# Script to build kickstart files out of a template using cheetah
#
FILE_VARIABLES="variables"
FILE_FUNCTIONS="functions.tmpl"

# cheetah must be reachable
which cheetah >/dev/null || {
  echo "[ERROR] cheetah not found!" >&2
  echo "[ERROR] Install cheetah (eg. 'pip install cheetah') and retry..." >&2
  exit 1
}

function list_possible_tmpl_files()
{
  ls -1 cen*.tmpl 1>/dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo
    echo "Available templates:"
    ls -1 cen*.tmpl | sed 's/^/ - /g'
  fi
}

# Argument check
if [ -z "$1" ]; then
  echo "Script to build kickstart files for RHEL/CentOS unattended installations"
  echo "Machine configuration is taken from the '$FILE_VARIABLES' file"
  echo
  echo "Usage: ${0##*/} <kickstart_template_file.tmpl>"
  echo "  eg.: ${0##*/} centos6[.tmpl]"
  list_possible_tmpl_files
  echo
  exit 0
fi

# File with variables should be present
if [ ! -r "$FILE_VARIABLES" ]; then
  echo "[ERROR] File '$FILE_VARIABLES' is missing!"
  echo "[ERROR] Either create a new one, or copy and modify one of the existing ones"
  exit 1
fi

filename="$1"
if [ ! -r "$filename" ]; then
  filenameTmpl="${filename}.tmpl"
  if [ ! -r "$filenameTmpl" ]; then
    echo "[ERROR] Cannot access file '$filename[.tmpl]!" >&2
    exit 2
  else
    filename="$filenameTmpl"
  fi
fi

# Main
cat "$FILE_VARIABLES" "$FILE_FUNCTIONS" "$filename" | \
  cheetah fill --iext="tmpl" --flat --oext=ks --nobackup -

exit $?
