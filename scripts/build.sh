#!/bin/bash

create_dirs() {
    echo "Creating directories ...";
    if [ ! -d "bin" ]; then 
        mkdir bin
    fi
}

# Allows to call a function based on arguments passed to the script
$*