# Astro & Docker

more info [here](https://docs.astronomer.io/astro/cli/get-started)



## Create directory and initialize astro
```
mkdir ~/c/astro_proj_101
cd ~/c/astro_proj_101
astro dev init
```


## Start - Stop astro container

```
astro dev start
astro dev stop
astro dev start && astro dev stop
```

## Access container and input Airflow commands 
```
docker ps
```

Take the CONTAINER_ID_webserver


```
docker exec -it CONTAINER_ID_webserver  /bin/bash

docker exec -it a6c5e01f4c00  /bin/bash
```
