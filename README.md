# Classify pipline software

This software is used to

## Installing software

`git clone https://github.com/Mycroft-behind/classify.git`

`cd classify`

All reference data and scripts in _classify_ directory

## Software dependencies

* bwa
* samtools
* blastn
* python(>=3.7)

## Usage
`python classify-pipline.py --bwa bwa_path --samtools samtools_path --blast blastn_path --database ./classify/Database/ -r1 Fastq_R1.fq.gz -r2 Fastq_R2.fq.gz --sample output_name`

## Result
The result will be saved in "output_name.count.result.xls".The results are presented in three columns. Also the results will be sorted in descending order.

|Column|Info |
|---|---|
|1|sample name|
|2|reads count|
|3|percentage|
