# jetsonbot
Fixing/cleaning/reproducing the Duckieracer PDF - util scripts and stuff

# Cant run agents??

This says the docker compose yamls are https://docs.duckietown.org/daffy/opmanual_duckiebot/out/setup_troubleshooting_docker.html 
basic, health, others, and core. Health doesn't matter here. So we gotta launch the other three.

We can find them here https://github.com/duckietown/duckietown-shell-commands/tree/daffy/init_sd_card/stacks

## Basic

only has portainer + dt-device-loader. Portainer is already ok. Let's add dt-device-loader to the docker launcher


