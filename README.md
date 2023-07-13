# Arriba 

https://arriba.readthedocs.io/en/v1.1.0/quickstart/)https://arriba.readthedocs.io/en/v1.1.0/quickstart/

wget https://github.com/suhrig/arriba/releases/download/v1.1.0/arriba_v1.1.0.tar.gz

tar -xzf arriba_v1.1.0.tar.gz

cd arriba_v1.1.0 && make

#Downloading assembly: ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz 

./download_references.sh GRCh38+ENSEMBL93 

#ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

#ftp://ftp.ensembl.org/pub/release-93/gtf/homo_sapiens/Homo_sapiens.GRCh38.93.chr.gtf.gz
