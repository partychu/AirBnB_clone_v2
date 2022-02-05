#!/usr/bin/python3
"""
Fab: Creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.82.49.251', '184.72.74.246']
env.key_filename = '~/.ssh/school'


def do_pack():
    """ Packs up dir into tar archive """
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


def do_deploy(archive_path):
    """ Deploys tar archive to servers and sets up static folder """

    if os.path.exists(archive_path):
        try:
            t_tgz = archive_path.split('/')[-1]  # *.tgz
            t_file = t_tgz.split('.')[0]  # file name
            rel = "/data/web_static/releases"
            cur = "/data/web_static/current"
            put(archive_path, '/tmp/')
            run('mkdir -p {}/{}/'.format(rel, t_file))
            run('tar -xzf /tmp/{} -C {}/{}/ '.format(t_tgz, rel, t_file))
            run('rm /tmp/{}'.format(t_tgz))
            run('mv {0}/{1}/web_static/* {0}/{1}/'.format(rel, t_file))
            run('rm -rf {}/{}/web_static'.format(rel, t_file))
            run('rm -rf {}'.format(cur))
            run('ln -s {}/{}/ {}'.format(rel, t_file, cur))
            return True
        except Exception:
            return False
    else:
        return False


def do_deploy():
    """ Packs and deploys """
    try:
        archive_path = do_pack()
    except Exception:
        return False
    return = do_deploy(archive_path)
