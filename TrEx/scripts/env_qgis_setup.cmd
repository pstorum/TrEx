@echo off

setlocal

pushd "%~dp0"\.\
call conda init cmd.exe
call conda activate treeseg_dev
call conda list
echo "test2"
call python qgis_setup_env.py

popd

endlocal
pause