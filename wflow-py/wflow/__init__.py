__all__ = ['wflow_funcs','wflow_adapt','wflow_lib','pcrut','wf_DynamicFramework','stats']
__version__='1.0.master'
__release__='1.0.master.1'
__versionnr__='1.0.1'
__build__='2017-09-05 10:33:57.580000'

import os, sys
import osgeo.gdal as gdal

if getattr(sys, 'frozen', False):
    # running in a bundle
    # sys._MEIPASS is set by PyInstaller
    basedir = getattr(sys, '_MEIPASS', None)
    # support also other bundlers
    if not basedir:
        basedir = os.path.dirname(sys.executable)

    # use the included gdal-data
    gdal_data_path = os.path.join(basedir, 'gdal-data')
    gdal.SetConfigOption('GDAL_DATA', gdal_data_path)

    # set environment variable instead of pyproj_datadir such
    # that child processes will inherit it
    os.environ['PROJ_DIR'] = os.path.join(basedir, 'proj-data')
    # Fiona expects PROJ_LIB instead
    os.environ['PROJ_LIB'] = os.path.join(basedir, 'proj-data')
