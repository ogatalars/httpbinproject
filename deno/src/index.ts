import express, { Request, Response } from 'express';

const app = express();
const port = 3000;

app.get('/', (req: Request, res: Response) => {
  res.send('Hello, este é um clone do httpbin escrito com TypeScript!. Supervisionado pelo Dev INACIO');
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});


app.get('/get', (req: Request, res: Response) => {
    const responseData = {
      args: req.query,
      headers: req.headers,
      origin: req.ip,
      url: req.protocol + '://' + req.get('host') + req.originalUrl
    };
    res.json(responseData);
  });
  