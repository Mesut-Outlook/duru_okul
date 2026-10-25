#!/usr/bin/env bash
# Runs Antigravity CLI with automatic permission approval (--dangerously-skip-permissions)
exec agy --dangerously-skip-permissions "$@"
