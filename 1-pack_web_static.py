#!/usr/bin/python3
# Script that generates a .tgz archive of all contents from web_static
from fabric.api import *
import time


def do_pack():
    """
    Creates a .tgz archive of all contents from web_static
    """
    now = time.strftime('%Y%m%d%H%M%S')
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_"+now+".tgz web_static/")
        print("versions/web_static_"+now+".tgz")
    except:
        return None
