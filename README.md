Dash CINEMA

Apesar de simples, fiz o proejto pra relembrar algumas funcionalidades e juntar a algo que eu gosto.
De ferramentas usei:
Python (pandas, sqllite3..), 
HTML, 
SQLlite,
Google Sheets,
Looker Studio.

De forma objetiva o código em python extrai informações de filmes diretamente da API do TMBD e popula uma tabela em sql, após isso gera um arquvio em CSV e epostar para uma tabela no Google Sheets. Dessa forma o Looker consegue de forma mais simplificada acessar os dados pra que possa moldar a vizualixação. 
E no Dashboard precisei fazer um campo calculado para o LUCRO, e nos cards de "Receita", "Lucro", "Popularidade", "Titulo" e "Nota"  precisei criar uma regra onde se não houvesse nenhum filme selecioandos ficasse uma mensagem "-" padronizada.

CASE
  WHEN COUNT_DISTINCT(titulo) > 1 THEN "-"
  ELSE MIN(CARD)
END

