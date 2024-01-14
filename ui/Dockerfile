FROM node:20.10.0

WORKDIR /app

# These two steps are done separately because Docker will cache the install making the container rebuild faster
COPY ./package.json ./
RUN yarn

COPY . .

EXPOSE 5173

CMD yarn dev --host 

# TODO Run commands for production build