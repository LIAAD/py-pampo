# py-pampo
Python package for PAMPO (PAttern Matching and POs tagging based algorithm for NER)

Package to extract named entities from texts written in Portuguese and potentially applicable to other languages

* Free software: GNU General Public License v3
* Paper: PAMPO: using pattern matching and pos-tagging for effective Named Entities recognition in Portuguese.
https://arxiv.org/abs/1612.09535

## Installation
Using python3.

	pip install git+https://github.com/LIAAD/py-pampo.git

## Features
Extract entities from Portuguese texts.

## Usage

To use PAMPO from the terminal:

	pampo [INPUT_FILE]

To use in a project:

	import ner

	pt_news = """
	A pesquisa da UFPB revela que a região do Cariri Ocidental da Paraíba está em avançado estágio de desertificação por causa da seca. Segundo o professor Lucindo José Quintans, 46, a vegetação nativa está se extinguindo em consequência da seca.
	Sem meios para sobreviver, a população retirou todo tipo de planta para usar na alimentação. Agora, os habitantes estão destruindo a vegetação seca para fazer carvão e ter alguma fonte de renda. Quintans afirma que seriam necessários de 20 a 30 anos para o Cariri se recuperar do processo de desertificação.
	Segundo o professor, o epicentro da seca no Nordeste é o município de Cabaceiras, a leste do Cariri Ocidental, cuja média pluviométrica anual é de 250 mm, de acordo com dados da Sudene. Nos 12 municípios do Cariri Ocidental, a média de chuvas varia, em anos normais, de 250 mm a 410 mm. No Estado da Paraíba, a média é de 900 mm.
	De acordo com Lucindo Quintans, tanto Cabaceiras como o Cariri Ocidental ficam entre o planalto da Borborema, na Paraíba, e as serras que separam a Paraíba de Pernambuco. Segundo ele, essa configuração geográfica faz com que as correntes de ar do Oceano Atlântico passem por cima da região e afastem as chuvas.
	Dados da Secretaria da Agricultura do Estado indicam que não choveu nem 50 mm na região em 1993. Quintans estima que a seca dizimou mais de 80% do rebanho bovino da região. Fazendeiros e trabalhadores rurais informam que o gado bovino foi vendido a outros Estados a preços abaixo dos de mercado para não morrer por falta de pasto e água.
	Quintans afirma que a previsão é de que este ano também será seco. 'Se a seca se prolongar em 1994 e 1995, todos os animais serão extintos e metade da população deixará a região', afirmou.
	"""

	response = ner.extract_entities(pt_news)

	print("\n".join(response))

	UFPB
	Cariri Ocidental da Paraiba
	Segundo
	Lucindo Jose Quintans
	Sem
	Agora
	Quintans
	Cariri
	Segundo
	Nordeste
	Cabaceiras
	Cariri Ocidental
	Sudene
	Nos
	Cariri Ocidental
	No Estado da Paraiba
	Lucindo Quintans
	Cabaceiras
	Cariri Ocidental
	Borborema
	Paraiba
	Paraiba de Pernambuco
	Segundo
	Oceano Atlantico
	Dados da Secretaria da Agricultura do Estado
	Quintans
	Fazendeiros
	Estados
	Quintans

## Credits
- Conceicao Rocha, Ph.D, conceicaonunesrocha@gmail.com
- Arian Pasquali, Msc., arrp@inesctec.pt
- Alípio Jorge,
- Roberta Sionara, Msc.
- Paula Brito, Ph.D
- Carlos Pimenta, Ph.D
- Solange Rezende, Ph.D

## Citation
If you use this library in academy please cite our paper:

	@ARTICLE{2016arXiv161209535R,
	   author = {{Rocha}, C. and {Jorge}, A. and {Sionara}, R. and {Brito}, P. and
	        {Pimenta}, C. and {Rezende}, S.},
	    title = "{PAMPO: using pattern matching and pos-tagging for effective Named Entities recognition in Portuguese}",
	  journal = {ArXiv e-prints},
	archivePrefix = "arXiv",
	   eprint = {1612.09535},
	 primaryClass = "cs.IR",
	 keywords = {Computer Science - Information Retrieval, Computer Science - Computation and Language},
	     year = 2016,
	    month = dec,
	   adsurl = {http://adsabs.harvard.edu/abs/2016arXiv161209535R},
	  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
	}	
