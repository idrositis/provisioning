#!/usr/bin/env python
# Script to render kickstart template files, using Cheetah
#
from __future__ import print_function  # msg_to_stderr, warning, error, debug, info
import sys                             # msg_to_stderr

import argparse
from argparse import RawTextHelpFormatter

# Functions to print warning & debug MSGs
def warning_msg(*objs):
  print("WARN:", *objs, file=sys.stderr)

def error_msg(*objs):
  print("ERROR:", *objs, file=sys.stdout)

def debug_msg(*objs):
  print("DEBUG:", *objs, file=sys.stderr)

def info_msg(*objs):
  print("INFO:", *objs, file=sys.stderr)

try:
  from Cheetah.Template import Template
except ImportError:
  error_msg("No Cheetah module detected! How about `pip install Cheetah`?")
  exit(10)

import os
import sys

DEFAULT_FUNCTIONS_FILE = "functions.tmpl"

def main():

  # argparse
  program_description = "Script to render kickstart template files, using Cheetah"

  parser = argparse.ArgumentParser(description=program_description, formatter_class=RawTextHelpFormatter)
  parser.add_argument('ks_template', type=str,
                      help='kickstart template file')

  parser.add_argument('-f', '--function_file', type=str, default=DEFAULT_FUNCTIONS_FILE,
                      help='File with function definitions (default: "{}")'.format(DEFAULT_FUNCTIONS_FILE))
  parser.add_argument('-v', '--variable_file', type=str,
                      help="Variable file")

  # Read arguments
  args = parser.parse_args()
  ks_template = args.ks_template
  function_file = args.function_file
  variable_file = args.variable_file

  template_string = ""

  # Read files
  handle_ks = open(ks_template, 'r')
  ks_data = handle_ks.read()

  # Possibly prepend function and variable file
  # NOTE: the order does matter!-)
  for xFile in variable_file, function_file:
    if xFile:
      handle = open(xFile, 'r')
      data = handle.read()
      template_string += data

  template_string += ks_data

  # Render template
  rendered_ks = Template( template_string )

  # Output the template to STDOUT
  print(rendered_ks)


if __name__ == "__main__":
  sys.exit(main())
