#!/bin/bash

if[ -z "$PYFILE" ]; then
	echo "PYFILE environment variable is not set."
	exit 1
fi

python "$PYFILE"
