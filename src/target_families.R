options(stringsAsFactors=F)
#setwd('~/d/sci/src/gene_lists')

wget(url='http://www.guidetopharmacology.org/DATA/targets_and_families.csv')

system("cat targets_and_families.csv | cut -d ',' -f 11 | sed 's/\"//g' | tail -n +2 | sort | uniq | python src/update_symbols.py --hgnc gene_with_protein_product.txt > lists/gpcr.tsv")

system("wget -O- http://www.uniprot.org/docs/pkinfam.txt | egrep -o \"\w*_HUMAN\" | sed 's/_HUMAN//g' | src/update_symbols.py --hgnc gene_with_protein_product_2018_09_13.txt > lists/kinases.tsv")
data = read.table('targets_and_families.csv',sep=',',quote='"',header=T)
colnames(data) = gsub('[^a-z0-9_]','_',tolower(colnames(data)))

gpcrs = data[data$type=='gpcr','hgnc_symbol']

write.table(gpcrs,'lists/gpcr.tsv',row.names=F,quote=F,col.names=F)

