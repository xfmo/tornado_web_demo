#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Web Service: Tornado + SQLAlchemy '''

from datetime import datetime

import os
import random
import functools
import uuid
import logging
from  hashlib  import md5



logger = logging.getLogger(__name__)

def get_md5(args):
    return md5(args).hexdigest()

def get_random_string(length=32):
    allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join([random.choice(allowed_chars) for i in range(length)])

def get_cookie_expires_string(days=0):
    expiration = datetime.now()+datetime.timedelta(days)
    return expiration.strftime('%a, %d-%b-%Y %H:%M:%S PST')

def get_function_by_name(obj, function_name):
      func = None
      try:
          func = getattr(obj, function_name)
      except:
          pass
      return func

def get_pagination(count, limit, p):
    pages = []
    pages_max = 9
    pages_half = 4
    page_numb = 0
    # calc page numb
    if count % limit == 0:
        page_numb = count / limit
    else:
        page_numb = int(count / limit) + 1
    # process prev and next
    if p <= 1:
        prev = -1
    else:
        prev = p - 1
    if p >= page_numb:
        next = -1
    else:
        next = p + 1
    # generate pages
    if p <= pages_half+1:
        end = pages_max
        if page_numb < pages_max : end = page_numb
        for n in range(1, end+1): pages.append(n)
    elif p >=page_numb-pages_half:
        start = 1
        if page_numb-pages_max+1 > 1: start = page_numb-pages_max+1
        for n in range(start, page_numb+1): pages.append(n)
    else:
        for n in range(-pages_half, pages_half+1): pages.append(p+n)

    if len(pages)>0 and prev==-1: prev=pages[0]
    if len(pages)>0 and next==-1: next=pages[-1]

    return dict(prev=prev, pages=pages, next=next)

def get_now():
    return datetime.now()

def is_empty(src):
    return ( len(src) == 0 )

def grant_permission(type, permission, add=True):
    if add:
        return type | permission
    else:
        return ~(~type | permission)

def str2time(time_str, fmt='%Y-%m-%d'):
    rc = None
    try:
        rc = datetime.strptime(time_str, fmt)
    except:
        pass
    return rc

def get_uuid(type=4):
    if type == 1:
        return uuid.uuid1()
    return uuid.uuid4()

def create_folder(folder_path, folder_name):
    newpath = os.path.join(folder_path, folder_name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def save_file(filepath, filename, content):
    f = open(os.path.join(filepath, filename), 'wb')
    f.write(content.encode('utf8'))
    f.close()

def read_file(filepath, filename):
    try:
        f = open(os.path.join(filepath, filename), 'rb')
        return ''.join(line for line in f.readlines())
    except:
        return ''

