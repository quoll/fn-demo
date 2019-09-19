var fs = require('fs');

lines = fs.readFileSync('redis.properties').toString().split('\n')

config = lines.filter(s => !/^ *($|#)/.test(s))
              .map(s => s.split('='))
              .reduce((o,[k,v]) => {o[k] = v; return o}, {})

console.log(config)

