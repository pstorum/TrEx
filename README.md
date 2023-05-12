# Getting Started

<h3> Download and Install:</h3>

      https://www.qgis.org/en/site/

      https://www.anaconda.com/

      Download our plugin as .zip

1. After installing Anaconda be sure to set system environment variables.

    (path to installation)\anaconda3

    (path to installation)\anaconda3\Scripts

    (path to installation)\anaconda3\Library\bin



2. Open QGIS, and on the top bar navigate to Plugins --> Manage and Install

3. Install from Zip

4. Then navigate to the Installed tab and check off Tree Segmentation

5. Restart QGIS

6. You are ready to begin using the plugin.

(Note: currently there is some conflict with automated dependency setup, and some extra steps are needed to get the plugin running. See below for instructions to manually get dependencies working)

# Using the plugin

1. Open the plugin
2. Select a .las or .laz file to start segmenting.
3. Set your parameters and press start segmentation.
4. Depending on the size of the LiDAR file used, computation time will vary.
5. Save the data a Shape file for direct use within QGIS.


# Manual Dependency Setup
1. Open a command prompt
2. Change directory to the install location of QGIS, and navigate to the following folder "QGIS\QGIS3\profiles\default\python\plugins\Tree-Seg-Plug\TrEx\scripts"
3. Run "env_setup" and enter yes when prompted to.
4. Run "env_activate"
5. Run "env_qgis_setup"
6. A new file should be created called "env_vars.json"
7. Move that file to the main working directory of the plugin. "/Tree-Seg_Plug"
