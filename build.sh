#!/bin/sh

set -xe

CFLAGS="-Wall -Wextra  -pedantic"
cc $CFLAGS -o todoc main.c
