import string,os,glob,sys

sample1='/home/RNA-seq/sample1/'
dirname1='/home/program/fusioncatcher/database_mouse/'
output1='/home/RNA-seq/sample1/Fusioncatcher/'
os.system('/home/program/fusioncatcher/bin/fusioncatcher -d '+dirname1+' --input '+sample1+' --output '+output1+' -p 24')

sample2='/home/RNA-seq/sample4/'
dirname2='/home/program/fusioncatcher/database_mouse/'
output2='/home/RNA-seq/sample4/Fusioncatcher/'
os.system('/home/program/fusioncatcher/bin/fusioncatcher -d '+dirname2+' --input '+sample2+' --output '+output2+' -p 24')


fp=glob.glob('/home/RNA-seq/sample1/Fusioncatcher/fusioncatcher_result/*-fusion-genes.txt')
for fname in fp:
	gene=[]
	fp1=open(fname,'r')
	fp1.readline()
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
