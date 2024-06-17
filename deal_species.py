import sys
file_1 = sys.argv[1].strip()
data_index = open(file_1, "r")
index_info = {}
for each_line in data_index:
    if "Sequence" in each_line:continue
    each_line_tmp = each_line.strip().split("\t")
    if len(each_line_tmp) > 2:
        index_info[each_line_tmp[0]] = each_line_tmp[1] + " " + each_line_tmp[2]
    else:
        index_info[each_line_tmp[0]] = each_line_tmp[1]
data_index.close()
#print(index_info)
blast_result_file = sys.argv[2].strip()
blast_result = open(blast_result_file, "r")
for each_info in blast_result:
    blast_info_tmp = each_info.strip().split("\t")
    result = blast_info_tmp[0] + "\t" + index_info[blast_info_tmp[1]] + "\t" + "\t".join(blast_info_tmp[2:])
    print(result)
