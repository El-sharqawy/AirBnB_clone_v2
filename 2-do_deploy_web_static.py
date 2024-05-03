#!/usr/bin/python3
"""generating an tgz archive"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['52.205.14.105', '52.3.220.148']


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if exists(archive_path) is False:
        return False
    try:
        c_szFile = archive_path.split("/")[-1]
        fExt = c_szFile.split(".")[0]
        fPath = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(fPath, fExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(c_szFile, fPath, fExt))
        run('rm /tmp/{}'.format(c_szFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(fPath, fExt))
        run('rm -rf {}{}/web_static'.format(fPath, fExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(fPath, fExt))
        return True
    except Exception as e:
        return False
