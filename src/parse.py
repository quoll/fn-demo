#!/usr/bin/python
import re

def strip(s):
  return s.strip()

def not_blank(l):
  return not(re.match('^ *($|#)', l))

def prop_val(l):
  return l.split('=')

def add_map(m,(k,v)):
  m[k] = v
  return m

lines = open('redis.properties', 'r').readlines()
config = reduce(add_map,
           map(prop_val,
             filter(not_blank,
               map(strip, lines))),
           {})

print config
