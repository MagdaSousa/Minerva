# Peojeto: Minerva

O projeto minerva visa disponibilizar dados relacionados a taxa de crescimento percentual anual do PIB, via API.


#Instalação:

## Clonar repositório:

```bash
git clone https://github.com/MagdaSousa/Minerva.git
```
![image](https://user-images.githubusercontent.com/55951781/186849379-59a21789-4d3d-4b88-8ca3-b0aeebe3ea01.png)



## Docker
Com o repositório clonado em sua máquina, você deve rodar o seguinte comando no cmd.

```bash
docker-compose up --build
```

## Usage

Escolha uma das plataformas para teste:

Swagger: [docs/minerva](http://127.0.0.1:8000/docs/Minerva#/)
- Passo a passo para a utilização do swagger :
Após rodar o comando docker compose up, a documentação via swagger já estará disponnível, ela é interativa, ou seja, você poderá fazer as requisiçõe spór ela.
![image](https://user-images.githubusercontent.com/55951781/186851383-557a6b98-f32d-481f-8ec0-0a9b483555ed.png)


Insominia: (https://insomnia.rest/download)
![image](https://user-images.githubusercontent.com/55951781/186851560-1c8c59cf-7d04-4408-b04a-e93787dfa2ee.png)

- Passo a passo para a utilização do Insominia :




## EndPoints disponíveis:
POST- Para carregamento dos dados no sql server
```bash
http://127.0.0.1:8000/
```

GET - Para coletar todas as infos relacionadas a uma cidade:
```bash
 http://127.0.0.1:8000/gdp/rate/country/{value}
```
GET -taxa de crescimento por país ou codigo do país:
```bash
http://127.0.0.1:8000/gdp/rate/country/ABW
```
GET -Ranking dos 10 países (Nome e código) com maior e menor média de
    crescimento do PIB (GDP growth annual ) com o período sendo fornecido
    como parâmetro na API:
```bash
http://127.0.0.1:9000/gdp/rank/1989&1990
```
;

# Inforamações adicionais:

Ao rodar o docker, os dados dos arquivos csv, já serão inseridos automaticamente

## Documentação do projeto:
- Estrutura do repositório : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Estrutura-do-Reposit%C3%B3rio)
- Modelagem : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Modelagem)
- Glossário : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Glossario)
- Levantamento dos requisitos : [repos] (https://github.com/MagdaSousa/Minerva/wiki/Levantamento-de-requisitos)
- Mais infos :[repos] (https://github.com/MagdaSousa/Minerva/wiki/Projeto-Minerva)



## License
[MIT](https://choosealicense.com/licenses/mit/)
