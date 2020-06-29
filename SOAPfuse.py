import os

'''
sample='LPS3'
sample_list='LPS3_list.txt'
output_dir='/home/DATA/Drug/RNA-seq/LPS3_SOAPfuse/'
os.system('perl /home/program/SOAPfuse-v1.27/SOAPfuse-RUN.pl -c /home/program/SOAPfuse-v1.27/config/config.txt -fd '+sample+' -l '+sample_list+' -o '+output_dir+' -tp '+sample)
'''

sample_name='Poly4'
sample_dir='/home/DATA/Drug/RNA-seq/Poly4/'
sample_list='/home/DATA/Drug/RNA-seq/SOAPfuse/Poly4_list.txt'
output_dir='/home/DATA/Drug/RNA-seq/SOAPfuse/Poly4_SOAPfuse/'
os.system('perl /home/program/SOAPfuse-v1.27/SOAPfuse-RUN.pl -c /home/program/SOAPfuse-v1.27/config/config.txt -fd '+sample_dir+' -l '+sample_list+' -o '+output_dir+' -tp '+sample_name)
