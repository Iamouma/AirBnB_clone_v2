#!/usr/bin/python3
"""
A module for Fabric scritp that provides a function to create
a .tzg archive from web_static folder.
"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """Archives the static files"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")

    archived = local("tar -cvzf {} web_static".format(archive_path))

    if archived.return_code != 0:
        return None
    else:
        return archive_path
