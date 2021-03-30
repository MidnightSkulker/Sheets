#!/usr/local/bin/bash
# Need bash 4 or greater.
# Argument 1 is month abbreviation, e.g. Jan, Feb.
# Argument 2 is mode, which must be 'Preview' or 'Live'.
# Argument 3 is an optional flag, if this is a reminder or not

# Arrays of sheetID and sheet names, indexed by teachers name
declare -A sheetID
declare -A sheetName

if [[ $# -eq 2 ]]; then
	echo "Processing for month ${1}, in mode ${2}"
  python3 main.py --SheetID=1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc --SheetName=GracesClass --Mode=$2 --Month=$1
elif [[ $# -eq 3 ]]; then
  echo "Processing for month ${1}, in mode ${2}, with flag $3"
  python3 main.py --SheetID=1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc --SheetName=GracesClass --Mode=$2 --Month=$1 --Reminder
else
	echo "Must have 1 argument: Arg1 is month abbreviation (e.g. Jan, Feb ...)"
	echo "arg2 is mode (Preview or Live)"
	echo "arg3 (optional) is the Reminder flag"
fi
