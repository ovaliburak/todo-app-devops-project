cd ./frontend/client \
&& docker build -t burakovali/client:latest . \
&& cd ../../backend/node/ \
&& docker build -t burakovali/server-node:latest . \
&& cd ../django/ \
&& docker build -t burakovali/server-django:latest . \
&& docker push burakovali/client:latest \
&& docker push burakovali/server-node:latest \
&& docker push burakovali/server-django:latest
