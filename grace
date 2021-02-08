#!/usr/local/bin/bash
# Need bash 4 or greater.
# Argument 1 is month abbreviation, e.g. Jan, Feb.
# Argument 2 is mode, which must be 'Preview' or 'Live'.

# Arrays of sheetID and sheet names, indexed by teachers name
declare -A sheetID
declare -A sheetName

if [[ $# -ne 2 ]]
then
	echo "Must have 1 argument: Arg1 is month abbreviation (e.g. Jan, Feb ...)"
	echo "and arg2 is mode (Preview or Live)"
else
	echo "Processing for month ${1}, in mode ${2}"
  python3 main.py --SheetID=1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc --SheetName=GracesClass --Mode=$2 --Month=$1
fi
