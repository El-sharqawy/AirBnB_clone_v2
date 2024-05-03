#!/usr/bin/python3
"""create archive backup using fabric"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """pack a folder into archive"""
    try:
        curDt = datetime.now().strftime('%Y%m%d%H%M%S')
        c_szArch = f'web_static_{curDt}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{c_szArch} web_static')
        return f'versions/{c_szArch}'
    except Exception:
        return None
