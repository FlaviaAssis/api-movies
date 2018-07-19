"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const elasticsearch = require('elasticsearch');
const client = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});
class MoviesRouter {
    applyRoutes(application) {
        application.post('/movie', (req, res, next) => {
            let body = req.body;
            let bulkArray = []; //criando array json
            for (let i in body) {
                let doc = body[i];
                bulkArray.push({ index: { _index: 'movies', _type: 'movies' } });
                bulkArray.push(doc);
            }
            client.bulk({
                body: bulkArray
            }, function (err, resp) {
                if (err) {
                    res.status(400);
                }
                res.send("POST executado com sucesso", resp);
                next();
            });
        });
        application.get('/movie', (req, res, next) => __awaiter(this, void 0, void 0, function* () {
            let field = req.query.field;
            let q = req.query.q;
            if (field !== 'title' && field !== 'genres' && field !== '_id') {
                res.status(422);
                res.send("Requisição deve ser /movie?field=A&q=B . Sendo A movie/_id/genres e B o valor");
            }
            else {
                let results = yield client.search({
                    index: 'movies',
                    q: `${field}:${q}` // para transformar tudo numa string
                });
                res.send({ results, message: "Requisição executada com sucesso" });
            }
            next();
        }));
    }
}
exports.moviesRouter = new MoviesRouter();
