#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# author Allen.M <http://blog.allenm.me>
# date 2012-11-21
#/

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
from stylus import Stylus
import threading
import sys
import os
import re
import fnmatch


compiler = Stylus()

def compileFile( filename ):
    if os.path.isfile( filename ) and fnmatch.fnmatch( filename , '*.styl' ):
        stylusFile = open( filename, 'r' )
        content = stylusFile.read()
        stylusFile.close()
        result = compiler.compile( content )
        print 'Compile the file: %s' % ( filename )
        resultPath = filename[0:-4] + 'css'
        cssFile = open( resultPath , 'w' )
        cssFile.write( result )
        cssFile.close()

def compileDir( path ):
    ''' convert all the sylus file one time in the starting '''
    matches = []
    for root , dirnames, filenames in os.walk( path ):
        for filename in fnmatch.filter( filenames , '*.styl'):
            matches.append( os.path.join( root , filename ) )

    for filename in matches :
        compileFile( filename )


class FileChange( FileSystemEventHandler ):
    ''' File change event handler , capture the *.styl file change event '''

    def __init__(self):
        super( FileChange, self ).__init__()

    def on_any_event(self, event):
        if event.is_directory is False:
            compileFile( event.src_path )
        else:
            compileDir( event.src_path )


class Watch( threading.Thread ):

    def __init__(self, path = None ):
        threading.Thread.__init__(self)
        if path is None:
            path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.path = path
        compileDir( self.path )


    def run( self ):
        event_handler = FileChange()
        observer = Observer()
        observer.schedule(event_handler, path= self.path, recursive=True)
        observer.start()
        print 'start watching %s directory stylus file' % (self.path)

class ConvStylus:
    def __init__(self, path = None ):
        self.w = Watch( path )
        self.w.start()
