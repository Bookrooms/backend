#!/bin/bash

_term() { 
  kill -TERM "$child" 2>/dev/null
}

trap _term SIGTERM

echo "APP STARTS IN $([ "$DEVEL" -eq 1 ] && echo "DEVEL" || echo "PROD")"
uvicorn src.main:app --host 0.0.0.0 --port 80 $([ "$DEVEL" -eq 1 ] && echo "--reload" || echo "") &

child=$! 
wait "$child"

