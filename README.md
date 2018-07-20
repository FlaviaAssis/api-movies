# api-movies


Servidor de busca de filmes. É possível cadastrar filmes e realizar buscas personalizadas

**1. Como executar o script para converter o arquivo u.item para formato .json

Inserir o path para o arquivo u.item (./movies-files) em script.py (linha 31). 
Obs: Se não tiver o módulo requests instalado, rodar no terminal pip install requests antes de executar o script

Executar no terminal *python script.py*. Será gerado o arquivo movies.json

**2. Como rodar o servidor:

Para executar o projeto, é necessário ter o Elasticsearch e Node.js instalados

* Com o terminal na pasta api-movies, executar o comando *npm i restify* e em seguida o comando *npm install --save elasticsearch*

* Rodar o servidor elastisearch: 
- Para rodar o servidor do elasticsearch: Localizar o terminal na pasta do elastiserch e executar o comando ./bin/elasticsearch

* Com o terminal na pasta api-movies, executar o comando *node main.js*

Para alimentar o servidor com o array de JSONs criado, executar o método POST em http://localhost:8080/movie (inserir o array no body)

Após executar o método POST, é possível realizar as requisiçes a partir do método GET

Exemplo de requisição:

http://localhost:8080/movie?field=title&q=Batman (procurar filmes com nome Batman)

