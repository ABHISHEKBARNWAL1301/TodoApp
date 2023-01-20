# pull the Node.js Docker image
FROM node:alpine as builder

# create the directory inside the container
WORKDIR /usr/src/app

# copy the package.json files from local machine to the workdir in container
COPY package*.json ./
COPY package-lock.json ./

# run npm install in our local machine
RUN npm install

# copy the generated modules and all other files to the container
COPY . .
RUN npm run build 

FROM nginx:1.23.1
COPY --from=builder /usr/src/app/build /usr/share/nginx/html