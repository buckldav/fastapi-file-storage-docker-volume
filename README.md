# FastAPI File Upload to Docker Volume

## Permissions for container to access volume

Source: [https://stackoverflow.com/a/45673309](https://stackoverflow.com/a/45673309)

Essentially, find the `id` info of the running container's user and use that information to `chown` the directory on the host to the container's uid and gid. The host directory can have the base 755 permissions.

### docker-user-setup.sh

This script gets the `id` info from host and puts it in the `.env` file. You only need to run it once. That information is then used to build the storage docker container with the container user having the same uid and gid as the host user.

## Run the thing

```bash
mkdir -p staticfiles
# if needed, make sure you chown the file to the current user
chown -R staticfiles

# fastapi up
docker-compose up -d --build
```

## Endpoints

```bash
curl http://localhost:8020 # {"hello": "world"}
# write to file in volume
curl http://localhost:8020/file # {"filepath": "~/staticfiles/file"}
cat staticfiles/file
```
