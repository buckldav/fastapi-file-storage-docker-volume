# get the current user ids to be used by Dockerfile with write permissions to volumes.
HOST_UID=$(id | awk '{print $1}' | grep -Eo -m 1 "[0-9]+")
HOST_GID=$(id | awk '{print $2}' | grep -Eo -m 1 "[0-9]+")
echo -e "\n" >> .env
echo "HOST_UID=$HOST_UID" >> .env
echo "HOST_GID=$HOST_GID" >> .env