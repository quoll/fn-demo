#!/usr/bin/python
import re

lines = open('redis.properties', 'r').readlines()
config = {k: v for k, v in
           [l.split('=')
             for l in
                 map(lambda s: s.strip(), lines)
             if not(re.match('^ *($|#)', l))]}

print config
