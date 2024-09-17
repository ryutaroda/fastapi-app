# fastapi-app
 

```
docker-compose up -d --build
```

ユーザーを登録するには（例）
```
curl -X POST "http://localhost:8080/users/" -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@example.com"}'
```

ユーザーを取得するには（例）
```
curl -X GET "http://localhost:8080/users/1"
curl "http://localhost:8080/users/1"
```

PostgreSQL コンテナに接続
```
docker-compose exec db psql -U user dbname
```

ユーザーを取得するには（例）
```
SELECT * FROM users;
SELECT * FROM users WHERE id = 1;
```