# Assembly free reads accurate identification (AFRAID)

This software is used to accurate identify plant species based on next generation sequencing PE150 clean data and you can only use it in a Linux environment for now.

## Installing software

git clone https://github.com/Mycroft-behind/classify.git

cd classify

All reference data and scripts in _classify_ directory

## Software dependencies

* bwa
* samtools
* blastn
* python(>=3.7)

## Before you start
You need to construct your own databse for species which is a fasta file with sequencing named in numbers,like this:
![image](https://github.com/Mycroft-behind/classify/assets/61588264/27c3f278-686a-4c34-8331-dfffdee7938b)

## You also need to create a reference table for these numbered digits, specifying the classification levels of each sequence, including order, family, genus, species, and acceession number or ID number. Save it in a .txt format with the following structure:
![image](https://github.com/Mycroft-behind/classify/assets/61588264/6ba66f6d-1314-421e-8d62-3b8b88fc8e0f)

## Usage
python classify-pipline.py --bwa bwa_path --samtools samtools_path --blast blastn_path --database ./classify/Database/ -r1 Fastq_R1.fq.gz -r2 Fastq_R2.fq.gz --sample output_name
## Directions
--bwa bwa_path # Specify the installation directory for this software
--samtools samtools_path # Specify the installation directory for this software
--blast blastn_path # Specify the installation directory for this software
--database ./classify/Database/ # Specify the directory for the reference database
-r1 Fastq_R1.fq.gz # Specify the first direction NGS data for plant species identification
-r2 Fastq_R2.fq.gz # Specify the second direction NGS data for plant species identification
--sample output_name # give a name of the output file
## Result
The result will be saved in "output_name.count.result.xls".The results are presented in three columns. Also the results will be sorted in descending order.

|Column|Info |
|---|---|
|1|sample name|
|2|reads count|
|3|percentage|
