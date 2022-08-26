O projeto Minerva tem como objetivo, fornecer via API, dados relacionados ao cresciemnto do PID por Pais, o objetivo é disponibilizar dados para o usuário final(analise de dados)..

Foram utilizadas as seguintes técnologias:

* [Python](https://www.python.org/doc/) 
* [Pandas](https://pandas.pydata.org/docs) 
* [SqlAlchemy](https://docs.sqlalchemy.org/en/14/) 
* [Banco de Dados Postgresql](https://www.postgresql.org) 

E para os testes da api, utilizei:

* [Insominia](https://insomnia.rest/download) 

E como estou utilizando o FastApi e também disponibiliza, uma doc com base no Swagge, para que possamos testar fazendo as requisições, durante o passoa a passo mostrarei como utilizar..


* [FAstAp iDocs](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/?h=docs#description-from-docstring) 



# Requisitos para rodar o projeto localmente:

Para esse projeto é necessário ter o python instalado(versão 3.8 ou superior)

Nesta aplicação o banco de dados está sendo disponibilizado via imagem docker, em um arquivo docker-file, caso seja de sua preferencia rodar o projeto com o banco físico será necessária a instalação e configuração do seu SGBD de sua preferencia.


# Iniciando a instalação dos requisitos:

Baixar o repositório do git diretamente, basta executar o comando abaixo no cmd :

 ``` git clone https://github.com/VitorinoAssuncao/hadesBanking.git ```
 
 Caso queira via CLI do github, basta usar a opção abaixo:
 
GitHub CLI
 
 ``` gh repo clone VitorinoAssuncao/hadesBanking ```


# Gerando Imagem Docker:
Antes de inciar a criação da imagem, vc precisa criar um arquivo .env, na raiz do seu projeto, com as seguintes configuraçõeds, elas são necessárias para que a imagem e o banco do docker sejam criados corretamente:

As enviromentes, descritas no arquivos devem estar exatamente iguais ao exemplo, pois no arquivo no docker-compose está apontando para essas enviroments, então certifique-se que esteja tudo correto, segue um arquivo de exemplo, já montado:


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


tedtando via Insominia- Passo a passo: [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)

edtando via Swagger - Passo a passo: [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)





# Estruturas Relevantes:

Este projeto consiste em uma aplicação de backend, a qual não possui uma rota raiz (/) atualmente, possuindo apenas 3 estruturas de rotas, conforme a necessidade do usuário:

• common: Referente aos dados de conta, gerais e individuais. E a partir do ID do usuário que será possível acessar o saldo da conta através das rotas (/accounts/balancce) e uma listagem de contas gerais (/accounts). Além disso, é possível se fazer nessa rota o login do usuário em questão (/accounts/login)

• transfers: Rota responsável pelas ações de transfêrencia entre duas contas, só sendo permitido realizar as mesmas quando realizado previamente um login. Deverá obrigatoriamente enviar um token no header das requisições.

# EndPoints


## Accounts

### Request  
` "POST" : Rota que faz a carga dos dados no postgre

### Response  
Neste caso não só retorna o código 200, ao finalizar o processo de ingestão dos dados
`[200
]`
 
---

### Request
` "GET  http://127.0.0.1:8000/gdp/rate/<nome_pais>" : `

### Response
`  [
	200,
	{
		"country_name": "Aruba",
		"country_code": "ABW",
		"GDP growth annual %": [
			{
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
				"1986": "0 %",
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
				"2021": "0 %"
			}
		]`



### Request
` "GET [/account/balance](http://127.0.0.1:8000/gdp/rate/country/<codigo_ou_nome_do_pais>)" : Rota validar o saldo atual da conta, deve-se passar o token de acesso, recebido ao logar`

- Header 
`{
	Authorization: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ4OTI0NzIsImlzcyI6InZpdG9yaW5vIiwiVXNlcl9pZCI6MX0.dlyrFzbfBz7QPBQOaq9c1_gCVmv2JcjkI0SGWZ6ZsVU"
}`


### Response
`{
  "balance": 10.00
}`

### Request
` "POST /account/login" : Rota para realizar o login na conta`

- Body (JSON)
`{
	"cpf": "57857751099",
	"secret":"12345"
}`

### Response
`{
	"authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOiJjMDM2NDc1Zi1iN2EwLTRmMzQtOGYxZi1jNDM1MTVkMzE3MjQifQ.Vzl8gI6gYbDMTDPhq878f_Wq_b8J0xz81do8XmHeIFI"
}`

## Transfer

### Request
` "GET /transfers" : Rota para retornar os dados de todas as transfêrencias (recebidas ou realizadas) do usuário`

- Header 
`{
	Authorization: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ4OTI0NzIsImlzcyI6InZpdG9yaW5vIiwiVXNlcl9pZCI6MX0.dlyrFzbfBz7QPBQOaq9c1_gCVmv2JcjkI0SGWZ6ZsVU"
}`

### Response  
`[
	{
		"id": "5ccbb3f0-9351-45c2-80cb-cfffbee767c2",
		"account_origin_id": "c036475f-b7a0-4f34-8f1f-c43515d31724",
		"account_destiny_id": "4cc7fe98-9996-408c-bff7-06cee3e6c519",
		"value": 0.01,
		"created_at": "2022-01-10T11:46:37Z"
	},
  	{
		"id": "5ccbb3f0-9351-45c2-80cb-cfffbee767c2",
		"account_origin_id": "c036475f-b7a0-4f34-8f1f-c43515d31724",
		"account_destiny_id": "4cc7fe98-9996-408c-bff7-06cee3e6c519",
		"value": 0.01,
		"created_at": "2022-01-10T11:46:37Z"
	}
]`

---

### Request
` "POST /transfer" : Cria uma nova transfêrencia do usuário informado no token, para o destinatário.`

- Header 
`{
	Authorization: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ4OTI0NzIsImlzcyI6InZpdG9yaW5vIiwiVXNlcl9pZCI6MX0.dlyrFzbfBz7QPBQOaq9c1_gCVmv2JcjkI0SGWZ6ZsVU"
}`

- Body (JSON):
`{
	"account_destiny_id":"4cc7fe98-9996-408c-bff7-06cee3e6c519",
	"amount":1
}`

### Response

`{
	"id": "5ccbb3f0-9351-45c2-80cb-cfffbee767c2",
	"account_origin_name": "c036475f-b7a0-4f34-8f1f-c43515d31724",
	"account_destiny_name": "4cc7fe98-9996-408c-bff7-06cee3e6c519",
	"value": 0.01,
	"created_at": "2022-01-10T11:46:37Z"
}`

# Inforamações adicionais:

Ao rodar o docker, os dados dos arquivos csv, já serão inseridos automaticamente

## Documentação do projeto:
- Estrutura do repositório : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Estrutura-do-Reposit%C3%B3rio)
- Modelagem : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)
- Glossário : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Glossario)
- Levantamento dos requisitos : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Levantamento-de-requisitos)
- Mais infos :[repos] (https://github.com/MagdaSousa/Minerva/wiki/Projeto-Minerva)



