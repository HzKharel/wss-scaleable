FROM nginx
COPY ./src/templates/ /usr/share/nginx/html
EXPOSE "80:80"