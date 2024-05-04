#!/usr/bin/python3
"""a fabric Script that generates an archive from web_static"""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['52.205.14.105	', '52.3.220.148']


def do_pack():
    """generate an archive"""
    local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(current_date)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception as execption:
        return None


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        fileName = archive_path.split("/")[-1]
        noExt = fileName.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(noExt))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(fileName, noExt))
        run("rm /tmp/{}".format(fileName))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(noExt, noExt))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(noExt))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(noExt))
        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to my web servers."""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
