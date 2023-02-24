
# extrai o link da mensagem
link_inicio = mensagem_texto.find('https://www.bet365.com/')
link_fim = mensagem_texto.find('\n', link_inicio)
link = mensagem_texto[link_inicio:link_fim]