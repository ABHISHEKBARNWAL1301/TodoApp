# Build react client
FROM node:alpine
WORKDIR C:\Users\ASUS\Desktop\TODO-APP\frontend\src\index
COPY package.json ./
COPY package-lock.json ./
RUN npm i 
COPY . .
EXPOSE 3000
CMD ["npm", "run", "start"]

