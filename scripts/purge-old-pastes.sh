#!/bin/sh

# This script is intend to be run as a cron job (every day for ex) to purge
# old pastes.

pastedir="$(python3 -c 'import config; print(config.pastedir)')"
timeout="$(python3 -c 'import config; print(config.timeout)')"
find "$pastedir" -type f -mtime +"$timeout" -exec rm {} \;
