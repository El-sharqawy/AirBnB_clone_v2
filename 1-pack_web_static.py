#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

""" a Fabric script that generates a tgz archive
from the contents of web_static.
"""


def do_pack():
    """pack an archive"""

    try:
        local("mkdir -p versions")
        curDt = str(datetime.now().strftime("%Y%m%d%H%M%S"))
        fileName = f"web_static_{curDt}.tgz"
        fullPath = f"versions/{fileName}"
        local(f"tar -cvzf {fullPath}")
        return (fullPath)
    except Exception:
        return None
