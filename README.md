# api-movies


Servidor de busca de filmes. É possível cadastrar filmes e realizar buscas personalizadas

Como executar o script para converter o arquivo u.item para formato .json
Inserir o path para o arquivo u.item em script.py (linha 31) Obs: Se não tiver o módulo requests instalado, rodar no terminal pip install requests antes de executar o script

Como rodar o servidor:

Com o terminal na pasta api-movies, executar o comando *npm i restify* 

Rodar o servidor elastisearch

Com o terminal na pasta api-movies, executar o comando *node main.js*

Para alimentar o servidor com o array de JSONs criado, executar o método POST em http://localhost:8080/movie (inserir o array no body)

Após executar o método POST, é possível realizar as requisiçes a partir do método GET

Exemplo de requisição:

http://localhost:8080/movie?field=title&q=Batman (procurar filmes com nome Batman)
