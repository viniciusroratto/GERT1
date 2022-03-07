FROM node:16-alpine3.13

WORKDIR /usr/src/app

EXPOSE 4200

CMD npm install -g @angular/cli && npm --force install  \ 
 && ng serve --host 0.0.0.0 --port 4200
