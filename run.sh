#!/bin/bash

case "$1" in

build_generator)
    docker build -t generator ./generator
    ;;

run_generator)
    docker run --rm -v $(pwd)/data:/data generator
    ;;

build_reporter)
    docker build -t reporter ./reporter
    ;;

run_reporter)
    docker run --rm -v $(pwd)/data:/data reporter
    ;;

structure)
    find .
    ;;

clear_data)
    rm -f data/*.csv data/*.html
    ;;

inside_generator)
    docker run --rm -v $(pwd)/data:/data generator ls -la /data
    ;;

inside_reporter)
    docker run --rm -v $(pwd)/data:/data reporter ls -la /data
    ;;


*)
    echo "Unknown command"
    ;;
esac