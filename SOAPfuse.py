import os

sample_name='sample'
sample_dir='/home/DATA/Drug/RNA-seq/sample/'
sample_list='/home/DATA/Drug/RNA-seq/SOAPfuse/sample_list.txt'
output_dir='/home/DATA/Drug/RNA-seq/SOAPfuse/sample_SOAPfuse/'
os.system('perl /home/program/SOAPfuse-v1.27/SOAPfuse-RUN.pl -c /home/program/SOAPfuse-v1.27/config/config.txt -fd '+sample_dir+' -l '+sample_list+' -o '+output_dir+' -tp '+sample_name)
