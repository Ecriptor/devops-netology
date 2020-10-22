FROM node
WORKDIR "/nodejs"
RUN git clone https://github.com/simplicitesoftware/nodejs-demo.git . && \
    npm install
EXPOSE 3000
CMD ["npm", "start", "0.0.0.0"]
