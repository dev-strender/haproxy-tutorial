# HAProxy Tutorial

실행 

```bash
docker compose -f docker-compose.yaml up -d --build
```

동시에 여러개 요청 (ex 100개)

```bash
seq 100 | xargs -n1 -P100 -I{} curl http://localhost:20080/receipt
```