var fs = require('fs');

function not_blank(l) {
  return !/^ *($|#)/.test(l)
}

function prop_val(l) {return l.split('=')}

function add_map(m,[k,v]) {
  m[k] = v
  return m
}

lines = fs.readFileSync('redis.properties').toString().split('\n')

config = lines.filter(not_blank).map(prop_val).reduce(add_map, {})

console.log(config)

