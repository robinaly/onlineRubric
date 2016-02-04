#!/usr/bin/env python
'''
Creates a rubric json file using a tab separated file, which was e.g. exported from MS Excel.

Usage:
./mkRubric.py in.tab out.json
'''
import os, sys, json

def main():
  data = {
    'rubric': {
      'title': '',
      'groups': [
        {
          'title': 'First',
          'categories': [
          
          ]
        },
        {
          'title': 'Second',
          'categories': [
          
          ]
        },
      ]
    },
    'users': []
  }
  for line in open(sys.argv[1]):
    line = line.strip()
    fields = line.split('\t')
    cat = {
      'title': fields[0],
      'items': []
    }
    for f in fields[1:]:
      item = {'title': f.strip()}
      cat['items'].append(item)
    data['groups'][0]['categories'].append(cat)
  out = open(sys.argv[2], 'w')
  json.dump(data, out, indent=2)
      
  
if __name__ == '__main__':
  main()