#!/usr/bin/env python
#coding=utf-8

import sys, os
import time
import requests
try:
    import simplejson as json
except:
    import json

reload(sys)
sys.setdefaultencoding('utf8')    

def save_file(path, data):
    f = file(path, 'w')
    f.write(data)
    f.close()

def get_file_path(parent_dir, chi_list, path_list):
    for chi in chi_list:
        cur_path = os.path.join(parent_dir, chi['name'])
        if chi.has_key('children'):
            get_file_path(cur_path, chi['children'], path_list)
        else:
            path_list.append(cur_path[1:])

def get_file_list():
    url = 'https://down.52pojie.cn/list.js'
    headers = {
        'Host': 'down.52pojie.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    res = requests.get(url, headers = headers)
    data = res.content
    data = data.replace('__jsonpCallbackDown52PojieCn(', '')
    data = data.replace(');', '')

    data = json.loads(data)
    path_list = []
    get_file_path('', [data], path_list)

    return path_list

def download(pdir, url):
    try:
        path = os.path.join(pdir, url)
        if os.path.exists(path):
            return
        dir1 = os.path.dirname(path)
        if not os.path.exists(dir1):
            os.makedirs(dir1)
        url = u'https://down.52pojie.cn/' + url
        print 'downloading ', url
        res = requests.get(url)
        data = res.content
        save_file(path, data)
    except Exception as e:
        print e

def filter_download(dir, filter, path_list):
    download_list = []
    for path in path_list:
        ret = [f for f in filter if path.find(f) != -1]
        if len(ret) > 0:
            download_list.append(path)
            download(dir, path)

    data = '\n'.join(path for path in download_list)
    save_file('download.txt', data.encode('utf8'))

if __name__ == '__main__':
    print '*********************************'
    print '* A downloader for 52pojie aipan '
    print '* Site: https://down.52pojie.cn  '
    print '* Author: anhkgg'
    print '* Site: github.com/anhkgg, anhkgg.com'
    print '* CopyRight (c) 2019 '
    print '*********************************'
    
    print ' \n Start downloading ... '
    filter = [
        'Tools/',
    ]
    print ' You want to download these dir: '
    for f in filter:
        print ' ->', f

    start_time = time.time()
    path_list = get_file_list()
    pdir = os.getcwd()
    filter_download(pdir, filter, path_list)
    print ' Finish the job. %.2fs' % (time.time() - start_time)
