import express from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app = express();

app.get('/', (req, res) => {
  res.send('Hellos world');
});

app.listen(3030, () => {
  console.log('App listenings on port 3030');
});
