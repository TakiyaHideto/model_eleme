#!/bin/bash

input_dir=/E_data
if [ $# -ge 1 ]
then
    input_dir=$1
fi

output_dir=/output

#----your code start--------------------------------------------------------#
#----read input data from /E_data and write output to /output/result.txt ---#
if [ ! -d ${input_dir} ]
then
	echo "input directory \"${input_dir}\" does not exist!" >&2
	exit 0
fi

if [ ! -d ${output_dir} ]
then
	echo "output directory \"${output_dir}\" does not exist!" >&2
	exit 0
fi

python hackthon_eleme.py ${input_dir} >${output_dir}/result.txt
#----your code end here-----------------------------------------------------#
