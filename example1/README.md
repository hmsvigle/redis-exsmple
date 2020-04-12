
1. Create network for containers to communicate through hostname
```sh
   docker network create --driver=bridge zeta
```
2. Build & run redis container
```sh
   cd redis && docker build -t redis:5.0.8 .
   docker run -itd --name=redisdb --network=zeta redis:5.0.8 
```
3. exec into redisdb container & disable protected mode.
```sh
   docker exec -it redisdb  src/redis-cli
   CONFIG SET protected-mode no
   exit
```
3. Build & run flask container
```sh
   cd ../api && docker build -t flask:3.0 .
   docker run -itd --name=flask --network=zeta flask:3.0 
```
4. on portforwarding, the apis (add_word & autocomplete) can be accessed. 

