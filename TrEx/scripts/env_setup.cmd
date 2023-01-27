@echo off

set ENV_NAME=treeseg_dev

call conda create -y -n %ENV_NAME% python=3.9

call conda.bat activate %ENV_NAME%

call conda install -c conda-forge pdal python-pdal gdal

pause
