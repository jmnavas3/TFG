ARG NODE_VERSION=alpine
ARG NPM_VERSION=10.8.2
ARG NODE_ENVIRONMENT=production
FROM node:$NODE_VERSION AS build
ENV NODE_ENV=$NODE_ENVIRONMENT

RUN mkdir /app
WORKDIR /app

COPY package.json .
RUN apk update && apk upgrade && npm install && npm install -g npm@$NPM_VERSION

COPY . .

RUN npm run build


FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 3000 80
CMD ["nginx", "-g", "daemon off;"]