# Resources


# cache file /root/pluginManager/cache.json
# data file /root/pluginManager/data.json

#https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app
#https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app



import pwnagotchi.plugins as plugins
from flask import abort
from flask import render_template_string
import subprocess

import time
import json
import logging

import requests

class pluginManager(plugins.Plugin):
    __author__ = "discord@rai68"
    __version__ = "1.3.0"
    __license__ = "LGPL"
    __description__ = "Provides an easy gateway to access plugins"

    def __init__(self):
        #each time load
        self.loaded = False
        self.ready = False
        self.accessToken = None
        
        
        #first load, changes on each time load.
        self.cache = None
    
        
        #frequently updated
        self.internet = False
        
        
    def on_loaded(self):
        logging.info("[Plugin Manager] plugin loading begin")
        
        
        
        
        self.loaded = True
        
        



      
    def on_webhook(self, path, request):
        if self.ready and self.loaded is False:
            return "<html><head><title>Plugin Manager: Error</title></head><body><code>%s</code></body></html>" % "Plugin is still booting. Please try again soon"
        if self.internet is False:
            return "<html><head><title>Plugin Manager: Error</title></head><body><code>%s</code></body></html>" % "Internet is not connected. Please try again soon"
        
        
        
        if request.method == "GET":
            #all gets below
            try:
                logging.debug(path)
                if path is None:
                    #GET "/" 
                    mainHTML = []
                    
                    
                    
                    return mainHTML
                elif path == '/plugin/':
                    #GET "/plugin/PLUGINNAME" - will open a menu with plugin info and versioning
                    pluginName = path.split("/plugin/")[1]

          
            except Exception as e:
                return "<html><head><title>Plugin Manager: Error</title></head><body><code>%s</code></body></html>" % e
