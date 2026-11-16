const dotenv = require(`dotenv`).config();

const PORT = process.env.API_PORT;

const app = require(`./app`);

app.listen(PORT, () => {
    console.log(`API rodando na porta: http://localhost:${PORT}/`);
});