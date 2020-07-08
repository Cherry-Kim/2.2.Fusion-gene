import string,os,glob,sys

'''
sample='/home/DATA/Drug/RNA-seq/LPS3/'
dirname='/home/program/fusioncatcher/database_mouse/'
output='/home/DATA/Drug/RNA-seq/Fusioncatcher/LPS3_fusioncathcer/'
os.system('/home/program/fusioncatcher/bin/fusioncatcher -d '+dirname+' --input '+sample+' --output '+output+' -p 24')

sample1='/home/DATA/Drug/RNA-seq/MEF1/'
dirname1='/home/program/fusioncatcher/database_mouse/'
output1='/home/DATA/Drug/RNA-seq/Fusioncatcher/MEF1_fusioncathcer/'
os.system('/home/program/fusioncatcher/bin/fusioncatcher -d '+dirname1+' --input '+sample1+' --output '+output1+' -p 24')

sample2='/home/DATA/Drug/RNA-seq/Poly4/'
dirname2='/home/program/fusioncatcher/database_mouse/'
output2='/home/DATA/Drug/RNA-seq/Fusioncatcher/Poly4_fusioncathcer/'
os.system('/home/program/fusioncatcher/bin/fusioncatcher -d '+dirname2+' --input '+sample2+' --output '+output2+' -p 24')
'''

fp=glob.glob('/home/DATA/Drug/RNA-seq/Fusioncatcher/fusioncatcher_result/*-fusion-genes.txt')
for fname in fp:
	print fname
	gene=[]
	fp=open(fname,'r')
	fp.readline()
	b=os.path.basename(fname)
	c=b.split('-')
	sample=c[0]
	fpout=open(sample+'_fusioncathcer.txt','w')
	for line in fp:
		line_temp=line.split('\t')
		a=line_temp[0]+'--'+line_temp[1]
		if not a in gene:
			gene.append(a)
	for i in gene:
		print i
		fpout.write(i+'\n')
fp.close()
fpout.close()
