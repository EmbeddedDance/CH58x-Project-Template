#!/bin/sh

if [ -d "build/" ]; then
    echo "Found build/"
    cd build
    cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -GNinja ..
    ninja
else
    echo "Not Found build/"
    mkdir build
    cd build
    cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -GNinja ..
    ninja
fi
