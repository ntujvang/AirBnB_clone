#!/usr/bin/python3
# Script contains do_deploy, do_pack and deploy!!!!
from fabric.api import *
import time
env.hosts = ['54.89.103.152', '54.91.31.60']


def do_pack():
    """
    Creates a .tgz archive of all contents from web_static
    """
    now = time.strftime('%Y%m%d%H%M%S')
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_"+now+".tgz web_static/")
        print("versions/web_static_"+now+".tgz")
        return("versions/web_static_"+now+".tgz")
    except:
        return None


def do_deploy(archive_path):
    """
    This function deploys our archive onto our webservers!
    """
    try:
        file_name = archive_path[9:]
        notgz_tag = archive_path[9:-4]
        new_dir = ("/data/web_static/releases/" + notgz_tag)
        run('sudo mkdir -p /tmp')
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(new_dir))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, new_dir))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo cp -R {}/web_static/* {}'.format(new_dir, new_dir))
        run('sudo rm -rf {}/web_static/*'.format(new_dir))
        run('sudo rm -rf {}/web_static'.format(new_dir))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}/ /data/web_static/current'.format(new_dir))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    This function calls both do_pack and do_deploy
    """
    mypath = do_pack()
    if not mypath:
        return False
    working = do_deploy(mypath)
    return working
