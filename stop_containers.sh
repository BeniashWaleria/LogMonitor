# shellcheck disable=SC2046
docker stop $(docker ps -a -q)
# shellcheck disable=SC2046
docker rm $(docker ps -a -q)
