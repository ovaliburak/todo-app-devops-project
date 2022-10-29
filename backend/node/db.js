const Pool = require("pg").Pool;
require('dotenv').config()
console.log(process.env.POSTGRES_HOST)
console.log(process.env.POSTGRES_DB)
console.log(process.env.POSTGRES_PASSWORD)
console.log(process.env.POSTGRES_USER)


const pool = new Pool({
  host: process.env.POSTGRES_HOST,
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
});

// const pool = new Pool({
//   host: 'postgres-service',
//   user: 'httpdwgp',
//   password: 'aa0074',
//   database: 'todo_list_penn',
//   port: 5432,
// });

module.exports = pool;
