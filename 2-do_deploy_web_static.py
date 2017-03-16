#!/usr/bin/python3
# Script contains do_deploy
from fabric.api import *
env.hosts = ['54.89.103.152', '54.91.31.60']

def do_deploy(archive_path):
    """
    This function deploys our archive onto our webservers!
    """
    if archive_path:
        file_name = archive_path[9:]
        notgz_tag = archive_path[9:-4]
        new_dir = ("/data/web_static/releases/" + notgz_tag)
        for ip in env.hosts:
            sudo('mkdir -p /tmp')
            put(archive_path, '/tmp/{}'.format(file_name))
            sudo('mkdir -p {}/'.format(new_dir))
            sudo('tar -xzf /tmp/{} -C {}'.format(file_name, new_dir))
            sudo('rm /tmp/{}'.format(file_name))
            sudo('cp -R {}/web_static/* {}'.format(new_dir, new_dir))
            sudo('rm -rf {}/web_static/*'.format(new_dir))
            sudo('rm -rf {}/web_static'.format(new_dir))
            sudo('rm -rf /data/web_static/current')
            sudo('ln -s {}/ /data/web_static/current'.format(new_dir))
            print("New version deployed!")
        return True
    else:
        return False
