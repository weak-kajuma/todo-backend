# Todo-Backend

このソフトはTodoリストのバックエンドをなしています

## Deployの方法

```
$ docker-compose build
$ docker-compose run --entrypoint "poetry install" todo-backend
$ docker-compose up -d --build
$ docker-compose exec todo-backend poetry run python -m api.migrate_db
```
