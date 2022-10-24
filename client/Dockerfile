FROM node:12.18.3 as react_build 
WORKDIR /client
COPY . /client/ 
RUN npm install
RUN npm run build 

FROM nginx:1.16.0-alpine
COPY --from=react_build /client/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80 
CMD ["nginx","-g","daemon off;"]