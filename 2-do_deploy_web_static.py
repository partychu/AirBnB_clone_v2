#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['54.82.49.251', '184.72.74.246']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ deploy web static """

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
            print('EXC Nope')
            return False
    else:
        print('F Nope')
        return False
