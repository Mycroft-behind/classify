![image](https://github.com/Mycroft-behind/classify/assets/61588264/aa979151-75b4-4d25-a6ae-746b7042015c)# Assembly free reads accurate identification (AFRAID)

This software is used to accurate identify plant species based on next generation sequencing PE150 clean data and you can only use it in a Linux environment for now.


## Installing software

`git clone https://github.com/Mycroft-behind/classify.git`

`cd classify`

All reference data and scripts in _classify_ directory

## Software dependencies

* bwa
* samtools
* blastn
* python(>=3.7)

## Before you start
You need to construct your own databse for species which is a fasta file with sequencing named in numbers,like this:
>1
ATCGATTTTCGATCGATCGATCG
>2
ATCGATCGATCCCCCCATCG
>3
ATCGATCGATTTTCGATCGATCG
## You also need to create a reference table for these numbered digits, specifying the classification levels of each sequence, including order, family, genus, species, and acceession number or ID number. Save it in a .txt format with the following structure:
Sequence number	Kingdom	Phylum	Order	Class	Family	Genus	Species	Accession_number
1	Plantae	Angiospermae	Dicotyledoneae	Juglandales	Juglandaceae	Carya	aguatica	ENC850518
2	Plantae	Angiospermae	Dicotyledoneae	Juglandales	Juglandaceae	Carya	alba	ENC850519
3	Plantae	Angiospermae	Dicotyledoneae	Juglandales	Juglandaceae	Carya	allida	ENC850515


## Usage
`python classify-pipline.py --bwa bwa_path --samtools samtools_path --blast blastn_path --database ./classify/Database/ -r1 Fastq_R1.fq.gz -r2 Fastq_R2.fq.gz --sample output_name`

## Result
The result will be saved in "output_name.count.result.xls".The results are presented in three columns. Also the results will be sorted in descending order.

|Column|Info |
|---|---|
|1|sample name|
|2|reads count|
|3|percentage|
