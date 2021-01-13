docker build -t proxy . --no-cache
docker stack rm  proxy
docker stack deploy -c docker-compose.yml proxy
docker service logs -f proxy_web
