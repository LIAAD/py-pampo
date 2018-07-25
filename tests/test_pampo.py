#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pampo
----------------------------------

Tests for `pampo` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from pampo import ner
from pampo import pampo

def test_news_a():
    """Test entity detection from Portuguese news
    """

    pt_news = """
    O Euro atingiu seu menor valor em relação ao dólar após a derrota do primeiro-ministro Matteo Renzi no referendo constitucional deste domingo (4) e seu anúncio de renúncia ao cargo.
    A moeda está valendo 1,0506 em relação ao dólar, o pior resultado em 20 meses, segundo a agência de notícias especializada em economia Bloomberg. O valor é ainda menor do que o registrado após os britânicos aprovarem a saída do Reino Unido da União Europeia.
    Os temores do mercado é de que o futuro governo italiano, possivelmente ligado ao Movimento Cinco Estrelas (M5S), tente tirar o país da zona do euro, dando mais um duro golpe na estabilidade econômica da Europa.
    Apesar de as Bolsas europeias não terem aberto ainda, os mercados asiáticos já começam a repercutir os efeitos da derrota de Renzi. A Bolsa de Valores de Tóquio já abriu em queda de 0,41% e o euro apresentou uma desvalorização de mais de 1,2% em relação ao iene.
     """

    response = ner.extract_entities(pt_news)

    assert u'Bloomberg' in response
    assert u'Europa' in response
    assert u'Toquio' not in response
    assert u'Reino Unido da Uniao Europeia' in response
    assert u"Movimento Cinco Estrelas" in response
    assert u"Matteo Renzi" in response    
    
def test_news_b():
    """Test entity detection from Portuguese news
    """
    pt_news = """
    A delegação brasileira nos Jogos Olímpicos de Atenas 2004 será a maior da história. Após os resultados do Troféu Brasil de Atletismo, no último final de semana, em São Paulo, a delegação brasileira atingiu um total de 234 atletas, superando a marca anterior de 225 atletas nos Jogos Olímpicos de Atlanta 1996.
    Até o momento são 118 atletas homens e 116 atletas mulheres. E este número ainda pode crescer. O COB aguarda a definição do tênis, cujo anúncio, de acordo com o ranking, acontecerá na próxima semana pela Federação Internacional de Tênis. Isso ocorrendo, o Brasil terá a participção em 26 esportes. O recorde anterior era de 24 esportes, em Sydney 2000.
    Na natação também háa expectativa de o Brasil classificar os revezamentos femininos pelo ranking da Federação Internacional de Natação. Há também chances no remo, cuja última seletiva acontece a partir de domingo, em Lucerne, Suíça.
    Esse recorde demonstra a evolução qualitativa do esporte olíımpico brasileiro. Isso vem ocorrendo desde os Jogos Olíımpicos de Atlanta 1996, graças ao trabalho que vem sendo feito pelas Confederações Brasileiras Olímpicas em conjunto com o COB. Com a Lei Agnelo/Piva, essa evolução vem sendo aindamais efetiva, já que estamos podendo fazer um planejamento e executá-lo de forma contínua. Vale ressaltar que todos os países também estão evoluindo. 'Estou muito feliz com esse recorde, até porque nenhum atleta está indo por meio de convite. Todos garantiram as vagas pelos critérios técnicos de suas Federações Internacionais', afirmou o presidente do COB, Carlos Arthur Nuzman.
     """

    response = ner.extract_entities(pt_news)
    
    assert u'Lucerne' in response
    assert u'Sydney' in response
    assert u'Atlanta' in response
    assert u'Brasil' in response
    assert u'COB' in response
    assert u'Carlos Arthur Nuzman' in response
    
    assert u'Confederacoes Brasileiras Olimpicas' in response
    assert u'Sao Paulo' in response
    assert u'Trofeu Brasil de Atletismo' in response
    
    #TODO support utf8 and special characters
    # assert u'Confederações Brasileiras Olímpicas' in response
    # assert u'São Paulo' in response
    # assert u'Troféu Brasil de Atletismo' in response

def test_news_c():
    """Test entity detection from Portuguese news
    """
    
    pt_news = """
    A pesquisa da UFPB revela que a região do Cariri Ocidental da Paraíba está em avançado estágio de desertificação por causa da seca. Segundo o professor Lucindo José Quintans, 46, a vegetação nativa está se extinguindo em consequência da seca.
    Sem meios para sobreviver, a população retirou todo tipo de planta para usar na alimentação. Agora, os habitantes estão destruindo a vegetação seca para fazer carvão e ter alguma fonte de renda. Quintans afirma que seriam necessários de 20 a 30 anos para o Cariri se recuperar do processo de desertificação.
    Segundo o professor, o epicentro da seca no Nordeste é o município de Cabaceiras, a leste do Cariri Ocidental, cuja média pluviométrica anual é de 250 mm, de acordo com dados da Sudene. Nos 12 municípios do Cariri Ocidental, a média de chuvas varia, em anos normais, de 250 mm a 410 mm. No Estado da Paraíba, a média é de 900 mm.
    De acordo com Lucindo Quintans, tanto Cabaceiras como o Cariri Ocidental ficam entre o planalto da Borborema, na Paraíba, e as serras que separam a Paraíba de Pernambuco. Segundo ele, essa configuração geográfica faz com que as correntes de ar do Oceano Atlântico passem por cima da região e afastem as chuvas.
    Dados da Secretaria da Agricultura do Estado indicam que não choveu nem 50 mm na região em 1993. Quintans estima que a seca dizimou mais de 80% do rebanho bovino da região. Fazendeiros e trabalhadores rurais informam que o gado bovino foi vendido a outros Estados a preços abaixo dos de mercado para não morrer por falta de pasto e água.
    Quintans afirma que a previsão é de que este ano também será seco. 'Se a seca se prolongar em 1994 e 1995, todos os animais serão extintos e metade da população deixará a região', afirmou.
    """

    response = ner.extract_entities(pt_news,deduplication=False)

    assert u"UFPB" in response
    assert u"Cariri Ocidental da Paraiba" in response
    assert u"Segundo" in response
    assert u"Lucindo Jose Quintans" in response
    assert u"Sem" in response
    assert u"Agora" in response
    assert u"Quintans" in response
    assert u"Cariri" in response
    assert u"Segundo" in response
    assert u"Nordeste" in response
    assert u"Cabaceiras" in response
    assert u"Cariri Ocidental" in response
    assert u"Sudene" in response
    assert u"Nos" in response
    assert u"Cariri Ocidental" in response
    assert u"No Estado da Paraiba" in response
    assert u"Lucindo Quintans" in response
    assert u"Cabaceiras" in response
    assert u"Cariri Ocidental" in response
    assert u"Borborema" in response
    assert u"Paraiba" in response
    assert u"Paraiba de Pernambuco" in response
    assert u"Segundo" in response
    assert u"Oceano Atlantico" in response
    assert u"Dados da Secretaria da Agricultura do Estado" in response
    assert u"Quintans" in response
    assert u"Fazendeiros" in response
    assert u"Estados" in response
    assert u"Quintans" in response

def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(pampo.main)
    assert result.exit_code == 2
    help_result = runner.invoke(pampo.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
