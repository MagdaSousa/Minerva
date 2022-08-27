O projeto Minerva tem como objetivo, fornecer via API, dados relacionados ao cresciemnto do PID por Pais, o objetivo é disponibilizar dados para o usuário final(analise de dados)..

Foram utilizadas as seguintes técnologias:

* [Python](https://www.python.org/doc/) 
* [Pandas](https://pandas.pydata.org/docs) 
* [SqlAlchemy](https://docs.sqlalchemy.org/en/14/) 
* [Banco de Dados Postgresql](https://www.postgresql.org) 

E para os testes da api, utilizei:

* [Insominia](https://insomnia.rest/download) 


# Requisitos para rodar o projeto localmente:

Para esse projeto é necessário ter o python instalado(versão 3.8 ou superior)

Nesta aplicação o banco de dados está sendo disponibilizado via imagem docker, em um arquivo docker-file, caso seja de sua preferencia rodar o projeto com o banco físico será necessária a instalação e configuração do seu SGBD de sua preferencia.


# Iniciando a instalação dos requisitos:

Baixar o repositório do git diretamente, basta executar o comando abaixo no cmd :

 ``` https://github.com/MagdaSousa/Minerva.git ```
 
 Caso queira via CLI do github, basta usar a opção abaixo:
 
GitHub CLI
 
 ``` gh repo clone MagdaSousa/Minerva ```
 
 ![image](https://user-images.githubusercontent.com/55951781/187002012-ab3bca16-4240-4677-b4b6-d117b3e6ca76.png)



# Gerando Imagem Docker:
Antes de inciar a criação da imagem, vc precisa criar um arquivo .env, na raiz do seu projeto, com as seguintes configuraçõeds, elas são necessárias para que a imagem e o banco do docker sejam criados corretamente:

As enviromentes, descritas no arquivos devem estar exatamente iguais ao exemplo, pois no arquivo no docker-compose está apontando para essas enviroments, então certifique-se que esteja tudo correto, segue um arquivo de exemplo, já montado:[env](https://github.com/MagdaSousa/Minerva/wiki/criar-um-arquivo-.env,-na-raiz-do-projeto-com-esse-conteudo-abaixo:)


![aruivo env](https://user-images.githubusercontent.com/55951781/187001650-26b3edd7-e828-4f1a-92f7-737328c3606f.jpg)



Com o repositório clonado/baixado, você deverá gerar a imagem docker do projeto, pois tando o banco de dados como a aplicação são orquestrados pelo docker, segue o passo a passo:

 Acesse o terminal e rode o comendo abaixo o comando abaixo:

 ```  docker-compose up --build ```
 Conforme imagem abaixo:
 ![image](https://user-images.githubusercontent.com/55951781/186996031-78fa384e-e81a-4c6a-8521-5f64e7a3ba34.png)
 ![image](https://user-images.githubusercontent.com/55951781/186996102-cf404cda-6d85-42ee-987d-8e3c217842f3.png)



Ao rodar o comando anterior, será gerada uma imagem docker do banco de dados e também irá iniciar a aplicação...

# Observações:
Ao rodar o docker e iniciar o banco de dados e a aplicação, o banco inicialmente está vazio, apenas com as tabelas, neste projeto foi criado uma rota específica para o carregamento dos dados, a qual deve ser a primeira a ser carregada, para que o banco seja populado.Foi escolhido ess processo, para demonstrar como seria o processo de ingestão de dados de uma fonte extena( no caso o excel), que foi processado e modelado usando o pandas e ingetado no banco de dados, seguindo a seguinte modelagem :[repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)

# Rodando o projeto
Após rodar o comando docker, o banco será criado e a aplicação levantada, como na imagem abaixo:
![image](https://user-images.githubusercontent.com/55951781/186996725-091f4e70-2431-4797-808c-1bcb7d199835.png)

# Acessando a api para popular o banco de dados:

Como citei anteriormente, vou mostrar como testar a plicação no Insominia e no Swagger que é disponibilizado pelo FastAPI


testando via Insominia- Passo a passo: [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)






# Estruturas Relevantes:
![image](https://user-images.githubusercontent.com/55951781/187005050-3ecb8f4b-67d0-4b0b-a90f-a7446f60ce8d.png)

Este projeto consiste em uma aplicação de backend, a qual não possui uma rota raiz (/) atualmente, possuindo apenas 3 estruturas de rotas, conforme a necessidade do usuário:

• common:pasta que contém dados utilizados em várias partes do projeto

• database: configurações do banco de dados

* ingestion: Processo de inserção dos dados com pandas

*domains: models, actions e outros arquivos responsáveis pelo fluxo



# EndPoints



### Request  
` "POST" : Rota que faz a carga dos dados no postgres

### Response  
Neste caso não só retorna o código 200, ao finalizar o processo de ingestão dos dados
`[200
]`
 
---
'GET  http://127.0.0.1:8000/api/gdp/country/<nome ou code>:Todos os dados relacionados a um país informado (indicadores e descrição,
    com exceção da coluna SpecialNotes). input: Nome ou código do país
    
    
###Response
'[
	200,
	{
		"country_name": "Africa Eastern and Southern",
		"country_code": "AFE",
		"region_name": "inexistente",
		"indicator_name": "GDP growth (annual %)",
		"list_values_indicators": [
			{
				"1960": 0.0,
				"1961": 0.24,
				"1962": 7.98,
				"1963": 5.16,
				"1964": 4.58,
				"1965": 5.33,
				"1966": 3.91,
				"1967": 5.26,
				"1968": 4.02,
				"1969": 5.28,
				"1970": 4.7,
				"1971": 5.37,
				"1972": 2.15,
				"1973": 4.44,
				"1974": 5.89,
				"1975": 1.73,
				"1976": 2.85,
				"1977": 1.23,
				"1978": 1.03,
				"1979": 2.8,
				"1980": 5.42,
				"1981": 4.33,
				"1982": 0.51,
				"1983": 0.15,
				"1984": 3.01,
				"1985": -0.45,
				"1986": 2.29,
				"1987": 4.23,
				"1988": 4.0,
				"1989": 2.9,
				"1990": -0.04,
				"1991": 0.11,
				"1992": -1.98,
				"1993": -0.39,
				"1994": 2.03,
				"1995": 4.29,
				"1996": 5.44,
				"1997": 4.42,
				"1998": 1.85,
				"1999": 2.64,
				"2000": 3.35,
				"2001": 3.66,
				"2002": 3.89,
				"2003": 3.08,
				"2004": 5.51,
				"2005": 6.12,
				"2006": 6.55,
				"2007": 6.6,
				"2008": 4.34,
				"2009": 0.76,
				"2010": 5.15,
				"2011": 3.68,
				"2012": 0.92,
				"2013": 4.2,
				"2014": 3.98,
				"2015": 2.95,
				"2016": 2.22,
				"2017": 2.56,
				"2018": 2.49,
				"2019": 2.03,
				"2020": -2.89,
				"2021": 4.3
			}
		]
	}
]'


### Request
` "GET http://127.0.0.1:8000/api/gdp/rate/country/<nome ou code>` :Taxa de crescimento do PIB por país. input: Nome ou código do país




### Response
[
	200,
	{
		"country_name": "Aruba",
		"country_code": "ABW",
		"GDP growth annual %": [
			{
				"1987": "16 %",
				"1988": "19 %",
				"1989": "12 %",
				"1990": "4 %",
				"1991": "8 %",
				"1992": "6 %",
				"1993": "7 %",
				"1994": "8 %",
				"1995": "3 %",
				"1996": "1 %",
				"1997": "7 %",
				"1998": "2 %",
				"1999": "1 %",
				"2000": "8 %",
				"2001": "4 %",
				"2002": "-1 %",
				"2003": "1 %",
				"2004": "7 %",
				"2005": "0 %",
				"2006": "1 %",
				"2007": "3 %",
				"2008": "2 %",
				"2009": "-12 %",
				"2010": "-3 %",
				"2011": "3 %",
				"2012": "-1 %",
				"2013": "6 %",
				"2014": "0 %",
				"2015": "4 %",
				"2016": "2 %",
				"2017": "5 %",
				"2018": "1 %",
				"2019": "-2 %",
				"2020": "-22 %",
				"2021": "0 %",
				"1960": "0 %",
				"1961": "0 %",
				"1962": "0 %",
				"1963": "0 %",
				"1964": "0 %",
				"1965": "0 %",
				"1966": "0 %",
				"1967": "0 %",
				"1968": "0 %",
				"1969": "0 %",
				"1970": "0 %",
				"1971": "0 %",
				"1972": "0 %",
				"1973": "0 %",
				"1974": "0 %",
				"1975": "0 %",
				"1976": "0 %",
				"1977": "0 %",
				"1978": "0 %",
				"1979": "0 %",
				"1980": "0 %",
				"1981": "0 %",
				"1982": "0 %",
				"1983": "0 %",
				"1984": "0 %",
				"1985": "0 %",
				"1986": "0 %"
			}
		]
	}
]

### Request
` "GET http://127.0.0.1:8000/api/gdp/rank/<PERIODO INICIAL> &<PERIODO FINAL> : Ranking dos 10 países (Nome e código) com maior e menor média de
    crescimento do PIB (GDP growth annual )



### Response
	200,
	{
		"highest average": {
			"Country_name": {
				"144": "Iraq",
				"193": "Eswatini",
				"10": "Turkmenistan",
				"166": "United Arab Emirates",
				"122": "Belize",
				"254": "Thailand",
				"264": "Lao PDR",
				"190": "Singapore",
				"194": "Botswana",
				"32": "Iran, Islamic Rep."
			},
			"avarage": {
				"144": 27.349646564987324,
				"193": 16.964552304477202,
				"10": 15.56461930077464,
				"166": 15.33293840795025,
				"122": 12.2263049294711,
				"254": 11.6788347156201,
				"264": 10.44760765995747,
				"190": 9.989864098053335,
				"194": 9.916113918230526,
				"32": 9.863521060382025
			}
		}
	}
]`



### Request
` "GET http://127.0.0.1:8000/api/gdp/region/<NOME DA REGIAO>' : Consulta do PIB dos países por região (ordem alfabética). input: Região


### Response  
`[
	200,
	{
		"Region": "Latin America & Caribbean",
		"Honduras": {
			"GDP growth annual %": [
				{
					"1960": "0 %",
					"1961": "2 %",
					"1962": "6 %",
					"1963": "4 %",
					"1964": "5 %",
					"1965": "9 %",
					"1966": "5 %",
					"1967": "6 %",
					"1968": "7 %",
					"1969": "1 %",
					"1970": "4 %",
					"1971": "4 %",
					"1972": "6 %",
					"1973": "8 %",
					"1974": "-1 %",
					"1975": "2 %",
					"1976": "10 %",
					"1977": "10 %",
					"1978": "6 %",
					"1979": "6 %",
					"1980": "1 %",
					"1981": "-1 %",
					"1982": "-2 %",
					"1983": "1 %",
					"1984": "6 %",
					"1985": "6 %",
					"1986": "5 %",
					"1987": "7 %",
					"1988": "2 %",
					"1989": "3 %",
					"1990": "3 %",
					"1991": "-3 %",
					"1992": "6 %",
					"1993": "6 %",
					"1994": "0 %",
					"1995": "6 %",
					"1996": "2 %",
					"1997": "5 %",
					"1998": "4 %",
					"1999": "-1 %",
					"2000": "7 %",
					"2001": "3 %",
					"2002": "4 %",
					"2003": "5 %",
					"2004": "6 %",
					"2005": "6 %",
					"2006": "7 %",
					"2007": "6 %",
					"2008": "4 %",
					"2009": "-2 %",
					"2010": "4 %",
					"2011": "4 %",
					"2012": "4 %",
					"2013": "3 %",
					"2014": "3 %",
					"2015": "4 %",
					"2016": "4 %",
					"2017": "5 %",
					"2018": "4 %",
					"2019": "3 %",
					"2020": "-9 %",
					"2021": "13 %"
				}
			]
		},`

---



## Documentação do projeto:
- Estrutura do repositório : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Estrutura-do-Reposit%C3%B3rio)
- Modelagem : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)
- Glossário : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Glossario)
- Levantamento dos requisitos : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Levantamento-de-requisitos)
- Mais infos :[repos] (https://github.com/MagdaSousa/Minerva/wiki/Projeto-Minerva)



