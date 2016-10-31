#!/bin/bash

# Figuring out the location of this script ...
pushd `dirname $0` > /dev/null
script_path=`pwd -P`
popd > /dev/null

# ... and deriving the root of the project.
project_root=$(dirname ${script_path})

# Helper functions to build UI files
function build_qt {
    echo "o Building $2"

    # Compile ui/qrc files to python.
    $1 $2 > $3
}

function build_ui {
    for ui_file in `find ${project_root} -name "*.ui"`; do
        py_file=${ui_file/\.ui/_ui.py}
        build_qt "pyuic4" ${ui_file} ${py_file}
    done
}

function build_res {
    for qrc_file in `find ${project_root} -name "*.qrc"`; do
        py_file=${qrc_file/\.qrc/_rc.py}
        build_qt "pyrcc4" ${qrc_file} ${py_file}
    done
}

# Build UIs ...
echo "Building user interfaces ..."
build_ui

# Build resources ...
echo "Building resources ..."
build_res
