# -*- coding: utf-8 -*-

import pcre as re
from .pattern_lists import *
from unidecode import unidecode
import unicodedata
import sys
import nltk

#reload(sys)
#sys.setdefaultencoding("utf-8")

def split_setences(text):
	sentences = []

	results = re.split("\\.|!|\\?",text)

	for item in results:
		sentences.append(item)

	return 	sentences

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

def remove_digits(input_str):
    return re.sub(r'\d+', '', input_str)

def build_regexpression():
    pt_patterns = PortuguesePatterns()

    regex_preprositions = "|".join(pt_patterns.preprositions)
    inicio = "|".join(pt_patterns.starters + pt_patterns.stopwords)
    # print("inicio",inicio)
    regex_titles = "|".join(pt_patterns.titles)
    # print("regex_titles",regex_titles)
    regex_titles_capitalized = [title.capitalize() for title in pt_patterns.titles]
    # print("regex_titles_capitalized.0",regex_titles_capitalized)
    regex_titles_capitalized = "|".join(regex_titles_capitalized)
    # print("regex_titles_capitalized.1",regex_titles_capitalized)

    regexp_2 = "([[:upper:]]{1,}[[:alpha:]]*)+(((([[:space:]]((" + regex_preprositions + ")[[:space:]]){0,1})([[:upper:]]{1,}[[:alpha:]]*)|(((-)[[:alpha:]]*){0,1})[[:upper:]]{0,1}[[:alpha:]]*))*)"

    regexp_0 = regex_titles + "|" + regex_titles_capitalized

    regexp_1 = "\\\b(" + regexp_0 + ")"

    regexp_3a = regexp_1 + "((((-)[[:upper:]]{0,1}[[:alpha:]]+)*([[:space:]](" + regex_preprositions + ")[[:space:]][[:upper:]]{1,}[[:alpha:]]*)))\\\b"

    reg_4int = "([[:space:]](" + regex_preprositions + "){0,1}[[:space:]]{0,1}){0,1})*)"
    regexp_4a = regexp_3a + reg_4int + regexp_2

    regexp_41a = "((" + regexp_4a

    regexp_2ba = regexp_3a + "|" + regexp_41a
    # print("regexp_2ba",regexp_2ba.decode("utf8"))
    surnames = [surname for surname in pt_patterns.common_family_names]
    regex_surnames = "|".join(surnames)
    # print("regex_surnames",regex_surnames.encode("utf8"))
    
    regexp_2bat = regexp_2ba + "([[:space:]](e)[[:space:]](" + regex_surnames + ")){0,1}"

    # regex_starters = "|".join(pt_patterns.starters)
    # regexp11 = "\\\b(" + regex_starters + ") ([[:alpha:]]{1,})"
    
    # print(regexp11)
    # print(regexp_2bat)
    return regexp_2bat


# def entitytext(text): R function name
def extract_entities(text,deduplication=False):
    sentences = split_setences(text)
    text_preprocessed = remove_accents(text)
    text_preprocessed = remove_digits(text_preprocessed)
    
    regexp2bat = build_regexpression()
    matches = re.finditer(regexp2bat, text_preprocessed)
    
    pt_patterns = PortuguesePatterns()
    
    phase_0_entities = []
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        phase_0_entities.append(match.group())
    
    unique_tokens = []
    for token in phase_0_entities:
        if(token != '' and len(token) > 2):
            token = token.strip()
            if not(token in pt_patterns.stopwords or token in pt_patterns.preprositions):
                
                if(deduplication):
                    if not(token in unique_tokens):
                        unique_tokens.append(token)
                else:
                    unique_tokens.append(token)
                        
    return unique_tokens
    
    # rodar regex11
    # ######################################################################
#     #######################################################################
#
#     Entities<-unlist(docs6)
#
#     Table_paragraph<-c("")
#     for(j in 1:length(docs6)){
#       docsaux<-docs6[[j]]
#       Table_paragraphaux<-merge(j,docsaux)
#       if(j==1){Table_paragraph<-Table_paragraphaux
#       }
#       if(j>1){Table_paragraphs<-rbind(Table_paragraph,Table_paragraphaux)
#               Table_paragraph<-Table_paragraphs
#       }
#     }
#     Table_sentences_para<-c()
#     if(length(Table_paragraph)>0 ){
#     names(Table_paragraph)[1:2] = c('Paragraph','Entity')#
#
#     ###############
#     #
#     # Analyse by sentence in each paragraph
#     #
#     ###############
#
#     Table_sentences<-c()
#
#     for(u in 1:length(sentences)){
#       docs6o<-str_extract_all(sentences[[u]],regexp2bat)
#       if(length(docs6o)>0){
#       for(i in 1:length(docs6o)){
#         docs6o[[i]]<-stripWhitespace(docs6o[[i]])
#         docs6o[[i]]<-gsub(pattern = regexp11, replacement = "\\2",  x = docs6o[[i]])
#       }
#       tab_doc2<-c("")
#       for(j in 1:length(docs6o)){
#         docsaux<-docs6o[[j]]
#         tab_docaux<-merge(j,docsaux)
#         if(j==1){tab_doc2<-tab_docaux
#         }
#         if(j>1){tab_Mbook_parts<-rbind(tab_doc2,tab_docaux) #Constroi a tabela
#                 tab_doc2<-tab_Mbook_parts
#         }
#       }
#
#       Table<-rbind(Table_sentences,tab_doc2)
#       Table_sentences<-Table
#     }
#     }
#     names(Table_sentences)[1:2] = c('Sentence','Entity')
#
#     Table_sentences_para<-cbind(Table_paragraph[,1],Table_sentences)
#     names(Table_sentences_para)[1:3] = c('Paragraph','Sentence','Entity')
#     }
#     Table_sentences_para
# > Table_sentences_para
#    Paragraph Sentence                                       Entity
# 1          1        1                                            A
# 2          1        1                                         UFPB
# 3          1        1                  Cariri Ocidental da Paraíba
# 4          1        2                                      Segundo
# 5          1        2                        Lucindo José Quintans
# 6          1        3                                          Sem
# 7          1        4                                        Agora
# 8          1        5                                     Quintans
# 9          1        5                                       Cariri
# 10         1        6                                      Segundo
# 11         1        6                                     Nordeste
# 12         1        6                                   Cabaceiras
# 13         1        6                             Cariri Ocidental
# 14         1        6                                       Sudene
# 15         1        7                                          Nos
# 16         1        7                             Cariri Ocidental
# 17         1        8                            Estado da Paraíba
# 18         1        9                                           De
# 19         1        9                             Lucindo Quintans
# 20         1        9                                   Cabaceiras
# 21         1        9                             Cariri Ocidental
# 22         1        9                                    Borborema
# 23         1        9                                      Paraíba
# 24         1        9                        Paraíba de Pernambuco
# 25         1       10                                      Segundo
# 26         1       10                             Oceano Atlântico
# 27         1       11 Dados da Secretaria da Agricultura do Estado
# 28         1       12                                     Quintans
# 29         1       13                                  Fazendeiros
# 30         1       13                                      Estados
# 31         1       14                                     Quintans
# 32         1       15                                           Se
# >

# noticia = """
# A pesquisa da UFPB revela que a região do Cariri Ocidental da Paraíba está em avançado estágio de desertificação por causa da seca. Segundo o professor Lucindo José Quintans, 46, a vegetação nativa está se extinguindo em consequência da seca.
# Sem meios para sobreviver, a população retirou todo tipo de planta para usar na alimentação. Agora, os habitantes estão destruindo a vegetação seca para fazer carvão e ter alguma fonte de renda. Quintans afirma que seriam necessários de 20 a 30 anos para o Cariri se recuperar do processo de desertificação.
# Segundo o professor, o epicentro da seca no Nordeste é o município de Cabaceiras, a leste do Cariri Ocidental, cuja média pluviométrica anual é de 250 mm, de acordo com dados da Sudene. Nos 12 municípios do Cariri Ocidental, a média de chuvas varia, em anos normais, de 250 mm a 410 mm. No Estado da Paraíba, a média é de 900 mm.
# De acordo com Lucindo Quintans, tanto Cabaceiras como o Cariri Ocidental ficam entre o planalto da Borborema, na Paraíba, e as serras que separam a Paraíba de Pernambuco. Segundo ele, essa configuração geográfica faz com que as correntes de ar do Oceano Atlântico passem por cima da região e afastem as chuvas.
# Dados da Secretaria da Agricultura do Estado indicam que não choveu nem 50 mm na região em 1993. Quintans estima que a seca dizimou mais de 80% do rebanho bovino da região. Fazendeiros e trabalhadores rurais informam que o gado bovino foi vendido a outros Estados a preços abaixo dos de mercado para não morrer por falta de pasto e água.
# Quintans afirma que a previsão é de que este ano também será seco. 'Se a seca se prolongar em 1994 e 1995, todos os animais serão extintos e metade da população deixará a região', afirmou.
# """
#
# result = extract_entities(noticia,deduplication=False)
# print("\n".join(result))
