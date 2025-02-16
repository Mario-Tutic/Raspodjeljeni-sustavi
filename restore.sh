#!/bin/bash
set -e

# Restore the PostgreSQL dump file into the database
pg_restore -U myuser -d mydb -v /backup.dump