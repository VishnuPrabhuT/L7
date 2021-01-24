Steps to run

1) docker compose up

(OR)

2) docker build -t benfords-law .
3) docker run -p 5001:5000 -d --name benfords-law  benfords-law
4) docker start benfords-law
5) open -> http://localhost:5001/