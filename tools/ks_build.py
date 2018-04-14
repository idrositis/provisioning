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
DEFAULT_VARIABLE_FILE  = "variables"

def main():

  # argparse
  program_description = "Script to render kickstart template files, using Cheetah"

  parser = argparse.ArgumentParser(description=program_description, formatter_class=RawTextHelpFormatter)
  parser.add_argument('ks_template', type=str,
                      help='kickstart template file')

  parser.add_argument('-f', '--function_file', type=str, default=DEFAULT_FUNCTIONS_FILE,
                      help='Common functions (default: "{}")'.format(DEFAULT_FUNCTIONS_FILE))
  parser.add_argument('-v', '--variable_file', type=str, default=DEFAULT_VARIABLE_FILE,
                      help='Host-specific variables; YOU SHOULD PROVIDE THAT FILE (default: "{}")'.format(DEFAULT_VARIABLE_FILE))

  # Read arguments
  args = parser.parse_args()
  ks_template = args.ks_template
  function_file = args.function_file
  variable_file = args.variable_file

  template_string = ""

  # Read files
  handle_ks = open(ks_template, 'r')
  ks_data = handle_ks.read()

  # Prepend function and variable files
  # NOTE: the order does matter!-)
  for xFile in variable_file, function_file:
    if xFile:
      try:
        handle = open(xFile, 'r')
      except IOError:
        error_msg('Cannot access file "{}"!'.format(xFile))
        return 1

      data = handle.read()
      template_string += data

  template_string += ks_data

  # Render template
  rendered_ks = Template( template_string )

  # Output the template to STDOUT
  print(rendered_ks)

# Main
if __name__ == "__main__":
  sys.exit(main())
