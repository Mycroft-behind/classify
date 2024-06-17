from itertools import islice
from collections import Counter
import os,re,sys,argparse

#reload(sys)
#sys.setdefaultencoding('utf-8')
# info={}
parse = argparse.ArgumentParser(prog="report",description="a report program",usage='%(prog)s.py [options] -i input file \n\n\033[1;31;40m\tconfig file format\033[0m\n\n\t\033\033\n\n')
parse.add_argument("-i",help="input file",type=str,required=True,default='/public/mygeno/pangxx/CarV1_S009/S005') 
args = parse.parse_args()
sample = []
blast_file_info = open ('%s'%(args.i),'r')
for info in blast_file_info:
   info = info.strip("\n")
   line = re.split('\t',info)
     # print '%s'%info
     # print line[0]
 # name=re.split(' ',line[1])
   if '%s'%line[0] in sample:
      # print line[0]
     pass
   else:
      sample.append('%s'%line[0])  ######
#f.close()
# print sample
for i in range(0,len(sample)):
  # print i
  tmp = 0
  zifu = str()
  zhong = str()
  for data in open('%s'%(args.i),'r'):
    data = data.strip()
    data_each = data.split('\t')
    # tmp = 0
     #print data_each
    if data_each[0] == sample[i]:
       # print data_each[0]
       if len(data_each) < 3:
           print (data_each[0])
           with open('%s_filter.xls'%(args.i),'a') as fa:
               fa.write(data_each[0]+"\t"+"null"+"\t"+"null"+"\n")
           fa.close()    
           break
       else:
           bidui = float(data_each[11])
           if bidui > tmp:
               tmp = float(data_each[2])
               zifu = data_each[1].split(' ')[0]
               zhong = data_each[1].split(' ')[1]
               # print a
               # print sample[i]
               # a += 1
           elif float(data_each[11]) == tmp:
    #        # print zifu
               if data_each[1].split(' ')[0] == zifu:
                   if data_each[1].split(' ')[1] == zhong:
                       zhong = data_each[1].split(' ')[1]
                   else:
                       zhong = ''
               else:
                   zifu = 'null'
    #    a = '%s' % i + '\t' + '%s' % zifu + '' + '%s'%zhong + '\t' + '%f' % tmp
    #            print a
    else:
       pass
  a = sample[i] + '\t' + zifu + ' ' + zhong + '\t' + '%s'%tmp + '\n'
  with open('%s_filter.xls'%(args.i),'a') as fa:
    fa.write(a)
  fa.close()
 # f.close()
    # else:
    #     break

               # break

   # print (a)










