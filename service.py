# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcaddon

# Addon info
__addon__        = xbmcaddon.Addon(id='script.webui')
__addonpath__    = __addon__.getAddonInfo('path')
__setting__      = __addon__.getSetting

# Include paths
sys.path.insert(0, __addonpath__)
sys.path.insert(0, os.path.join(__addonpath__, 'resources'))
sys.path.insert(0, os.path.join(__addonpath__, 'resources', 'lib'))

# Default Settings
HOST = '127.0.0.1'
PORT = 8100
WEBROOT = ''

# Get addon settings
if __setting__('port') and __setting__('port').isdigit():
    PORT = int(__setting__('port'))

if __setting__('hostname'):
    HOST = __setting__('hostname')

if __setting__('webroot'):
    WEBROOT = __setting__('webroot')


# Setup the web server
import cheroot.wsgi
from app import app

if WEBROOT:
    if WEBROOT[0] != '/':
        WEBROOT = '/' + WEBROOT
        d = cheroot.wsgi.WSGIPathInfoDispatcher({WEBROOT: app})
else:
    d = cheroot.wsgi.WSGIPathInfoDispatcher({'/': app})


server_params = {
    'bind_addr': (HOST, PORT),
    'wsgi_app': d
}
        
SERVER = cheroot.wsgi.WSGIServer(**server_params)

if __name__ == '__main__':
    from modules import index
    SERVER.start()
    while not xbmc.abortRequested:
        SERVER.tick()


