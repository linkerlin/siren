#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2013-06-05
@author: shell.xu
'''
import os, sys

outfile = open('output.txt', 'w')
def result(worker, req, rslt):
    outfile.write('\n%s\n\n' % rslt['title'][0].encode('utf-8'))
    outfile.write('\n%s\n\n' % str(rslt['content'][0]))
