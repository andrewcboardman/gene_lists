all: lists/universe.tsv lists/drug_targets.tsv lists/disease_genes.tsv

lists/universe.tsv:
	src/create_universe.bash

lists/disease_genes.tsv:
	src/get_disease_genes.bash

lists/drug_targets.tsv: data/drugbank.xml
	src/drugbank_parse.py

lists/model_organisms.tsv:
	src/get_model_phenotypes.bash
