#!/bin/sh

# compile

PARSER_FILE=$1
INPUT_FILE=$2

if flex $PARSER_FILE; then
    echo 'flex compile success\n'
    gcc lex.yy.c -L/lib -lfl
    echo '------------'
    echo 'INPUT'
    echo '------------'
    cat $INPUT_FILE
    ./a.out < $INPUT_FILE > output.txt
    echo '\n\n------------'
    echo 'OUTPUT'
    echo '------------'
    cat output.txt
    echo '\n\n'
    # remove itermediate files
    rm *.c
    rm *.out
else
    echo 'flex compile fail\n'
fi

