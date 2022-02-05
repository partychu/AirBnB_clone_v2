#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the
function do_pack
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ packs up webstatic """
    web_s = "web_static"
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    tar_path = "versions/web_static_{}.tgz".format(date)

    if os.path.isdir("versions"):
        pass
    else:
        local("mkdir versions")

    try:
        local("tar -czvf {} {}".format(tar_path, web_s))
        return tar_path
    except Exception:
        return None
