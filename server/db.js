const Pool = require("pg").Pool;
require('dotenv').config()


const pool = new Pool({
  host: "postgres_db",
  //host: "127.0.0.1",
  user: "httpdwgp",
  password: "aa0074",
  database: "todo_list_penn",
});

module.exports = pool;
