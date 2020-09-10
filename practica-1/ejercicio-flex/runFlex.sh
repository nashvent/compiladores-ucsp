#!/bin/sh


# compile

if flex test.l; then
    echo 'flex compile success\n'
    gcc lex.yy.c -L/lib -lfl
    echo '------------'
    echo 'INPUT'
    echo '------------'
    cat input.txt
    ./a.out < input.txt > output.txt
    echo '\n\n------------'
    echo 'OUTPUT'
    echo '------------'
    cat output.txt
    echo '\n\n'
else
    echo 'flex compile fail\n'
fi

# remove itermediate files
rm *.c
rm *.out