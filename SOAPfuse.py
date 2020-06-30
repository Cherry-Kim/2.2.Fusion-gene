import os

sample_name='sample'
sample_dir='/home/DATA/RNA-seq/sample/'
sample_list='/home/DATA/RNA-seq/SOAPfuse/sample_list.txt'
output_dir='/home/DATA/RNA-seq/SOAPfuse/sample_SOAPfuse/'

os.system('perl SOAPfuse-v1.27/SOAPfuse-RUN.pl -c SOAPfuse-v1.27/config/config.txt -fd '+sample_dir+' -l '+sample_list+' -o '+output_dir+' -tp '+sample_name)
