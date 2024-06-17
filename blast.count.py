import sys
blast_result_file = sys.argv[1].strip()
file_open = open(blast_result_file, "r")
total_count = 0
reads_count = {}
for each_line in file_open:
    total_count += 1
    each_line_tmp = each_line.strip().split("\t")
    if each_line_tmp[1] not in reads_count:
        reads_count[each_line_tmp[1]] = 1
    else:
        reads_count[each_line_tmp[1]] += 1
file_open.close()

for each_type in sorted(reads_count.items() , key = lambda x: x[1], reverse=True):
    print(each_type[0], each_type[1], each_type[1]/total_count, sep="\t")
