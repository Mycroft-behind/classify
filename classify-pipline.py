import argparse, sys, os
def main(bwa, samtools, blastn, ref_dir, fastq_1, fastq_2, sample, script_dir):
    os.system(f"{bwa} mem -t 4 {ref_dir}/reference-database.fasta  {fastq_1} {fastq_2} |{samtools} view -Sbh -o {sample}.bam")
    os.system(f"{samtools} view -b -h -F 4 {sample}.bam > {sample}.filter.bam")
    os.system(f"{samtools} fasta -1 {sample}.filter_R1.fa -2 {sample}.filter_R2.fa {sample}.filter.bam")
    os.system(f"{blastn} -query {sample}.filter_R1.fa -db test-blast -outfmt 6 -out {sample}.filter_1.blast.txt")
    os.system(f"{blastn} -query {sample}.filter_R2.fa -db test-blast -outfmt 6 -out {sample}.filter_2.blast.txt")
    os.system(f"cat {sample}.filter_1.blast.txt {sample}.filter_2.blast.txt > {sample}.filter.blast.txt")
    os.system(f"python deal_species.py species-index.txt {sample}.filter.blast.txt >  {sample}.deal.name.txt")
    os.system(f"python {script_dir}/blastsolve-2.py -i {sample}.deal.name.txt")
    os.system(f"python {script_dir}/blast.count.py blast.filter.xls > {sample}.count.result.xls")
if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--samtools", help="Path to samtools", required=True, metavar="")
    parse.add_argument("--bwa", help="Path to BWA", required=True, metavar="")
    parse.add_argument("--blast", help="Path to blast", required=True, metavar="")
    parse.add_argument("--database", help="Path to database", required=True, default="{default}/Database".format(default=os.path.dirname(os.path.abspath(__file__))), metavar="")
    parse.add_argument("--fastq1", "-r1", help="FASTQ1", required=True, metavar="")
    parse.add_argument("--fastq2", "-r2", help="FASTQ2", required=True, metavar="")
    parse.add_argument("--sample", "-s", help="Sample name", required=True, metavar="")
    args = parse.parse_args()
    bwa_path = args.bwa
    samtools_path = args.samtools
    database_path = args.database
    fastq1 = args.fastq1
    fastq2 = args.fastq2
    blast_path = args.blast
    sample_name = args.sample

    script_dir = os.path.dirname(os.path.abspath(__file__))
    main(bwa_path, samtools_path, blast_path, database_path, fastq1, fastq2, sample_name, script_dir)

"""
bwa mem -t 4 reference-database.fasta  Carya_alba_ENC850519_1.fq.gz Carya_alba_ENC850519_2.fq.gz |samtools view -Sbh -o Carya_alba.bam
samtools view -b -h -F 4 Carya_alba.bam > Carya_alba.filter.bam
samtools fasta -1 Carya_alba.filter_R1.fa -2 Carya_alba.filter_R2.fa Carya_alba.filter.bam
blastn -query Carya_alba.filter_R1.fa -db test-blast -outfmt 6 -out Carya_alba.filter_1.blast.txt
blastn -query Carya_alba.filter_R2.fa -db test-blast -outfmt 6 -out Carya_alba.filter_2.blast.txt
cat Carya_alba.filter_1.blast.txt Carya_alba.filter_2.blast.txt > Carya_alba.filter.blast.txt
python deal_species.py Carya_alba.filter.blast.txt species-index.txt >  Carya_alba.deal.name.txt
python /public/software/blastsolve-2.py -i Carya_alba.deal.name.txt
python /public/software/blast.count.py blast.filter.xls > Carya_alba.count.result.xls

"""
