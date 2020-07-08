import string,os

print "Case-Control"
sample1='/home/RNA-seq/sample1/'
sample2='/home/RNA-seq/sample2/'
output='/home/RNA-seq/sample1_sample2/'

os.system('/home/program/fusioncatcher/bin/fusioncatcher.py --input '+sample1+' --normal '+sample2+' --output '+output+' -p 24')
