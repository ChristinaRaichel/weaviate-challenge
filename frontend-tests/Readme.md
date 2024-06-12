Test server for frontend on port 3000

To run the server:
$cd my-react-app

$docker build -t frontend

$$ docker run \
    -itd \
    --rm \
    -v ${PWD}:/app \
    -v /app/node_modules \
    -p 3000:3000 \
    -e CHOKIDAR_USEPOLLING=true \
    frontend

