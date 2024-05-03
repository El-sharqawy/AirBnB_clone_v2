#!/usr/bin/python3
""" a fabrit script to create backup archive."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """pack an archive"""
    try:
        curDt = datetime.now().strftime("%Y%m%d%H%M%S")
        fileName = f"web_static_{curDt}.tgz"
        fullPath = f"versions/{fileName}"
        local('mkdir -p versions')
        local(f'tar -cvzf {fullPath}')
        return (fullPath)
    except Exception:
        return None
