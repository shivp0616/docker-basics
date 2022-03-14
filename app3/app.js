const express = require('express')
const http = require('http');

const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('{message: Hello World from app 3!}')
});


app.get('/another-app', function(req, res) {
  var request = http.request({
    host: 'localhost',
    port: 3001,
    path: '/',
    method: 'GET',
    headers: {
      // headers such as "Cookie" can be extracted from req object and sent to /test
    }
  }, function(response) {
    var data = '';
    response.setEncoding('utf8');
    response.on('data', (chunk) => {
      data += chunk;
    });
    response.on('end', () => {
      res.end(data);
    });
  });
  request.end();
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
