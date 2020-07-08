import string,os

print "Case-Control"
sample1='/home/DATA/Drug/RNA-seq/Sample_MEF1/'
sample2='/home/DATA/Drug/RNA-seq/Sample_RAW_LPS3/'
output='/home/DATA/Drug/RNA-seq/LPS_MEF1_results/'

os.system('/home/program/fusioncatcher/bin/fusioncatcher.py --input '+sample1+' --normal '+sample2+' --output '+output+' -p 24')
