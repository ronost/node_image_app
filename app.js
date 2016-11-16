var express = require('express');
var app = express();
var fs = require('fs');

/*** server ***/
app.listen(8000, function () {
  console.log('Listening on port 8000...');
})

/*** routes ***/
app.get('/api', function(req, res) {
  res.send({routes: app._router.stack });
})

app.get('/api/list', function(req, res) {
  fs.readFile( __dirname + "/db/img.json", 'utf8', function(err, data) {
       res.end(data);
   });
})

app.get('*', function(req, res) {
  res.sendfile('./public/index.html');
})
