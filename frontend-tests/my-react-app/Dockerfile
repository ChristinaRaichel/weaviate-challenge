FROM node:16

WORKDIR /my-react-app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install 
RUN npm install react-scripts@3.4.1 -g 
RUN npm install axios

COPY . ./


EXPOSE 3000

CMD ["npm", "start"]