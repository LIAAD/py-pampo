# -*- coding: utf-8 -*-

import pcre as re
from .pattern_lists import *
from unidecode import unidecode
import unicodedata
import sys
import nltk

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

    regex_titles = "|".join(pt_patterns.titles)

    regex_titles_capitalized = [title.capitalize() for title in pt_patterns.titles]

    regex_titles_capitalized = "|".join(regex_titles_capitalized)


    regexp_2 = "([[:upper:]]{1,}[[:alpha:]]*)+(((([[:space:]]((" + regex_preprositions + ")[[:space:]]){0,1})([[:upper:]]{1,}[[:alpha:]]*)|(((-)[[:alpha:]]*){0,1})[[:upper:]]{0,1}[[:alpha:]]*))*)"

    regexp_0 = regex_titles + "|" + regex_titles_capitalized

    regexp_1 = "\\\b(" + regexp_0 + ")"

    regexp_3a = regexp_1 + "((((-)[[:upper:]]{0,1}[[:alpha:]]+)*([[:space:]](" + regex_preprositions + ")[[:space:]][[:upper:]]{1,}[[:alpha:]]*)))\\\b"

    reg_4int = "([[:space:]](" + regex_preprositions + "){0,1}[[:space:]]{0,1}){0,1})*)"
    regexp_4a = regexp_3a + reg_4int + regexp_2

    regexp_41a = "((" + regexp_4a

    regexp_2ba = regexp_3a + "|" + regexp_41a

    surnames = [surname for surname in pt_patterns.common_family_names]
    regex_surnames = "|".join(surnames)
    
    regexp_2bat = regexp_2ba + "([[:space:]](e)[[:space:]](" + regex_surnames + ")){0,1}"
    
    return regexp_2bat

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
