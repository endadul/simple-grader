#!/bin/bash

set -e

# Modify as required
TEST_PROG_DIR="../"
PROGRAM="stack-prog"

# Commands
stdbuf -oL ${TEST_PROG_DIR}/${PROGRAM}
