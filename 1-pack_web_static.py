#!/usr/bin/python3
"""Fabric script to generate .tgz archive"""

from fabric.api import local, run, env
from datetime import datetime

from fabric.decorators import runs_once

env.hosts = ['localhost']

@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        file_path = 'versions/web_static_{}.tgz'.format(current_time)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except:
        return None
