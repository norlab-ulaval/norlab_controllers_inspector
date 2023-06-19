# Norlab controllers inspector

## Description
The Norlab's robots are collecting datasets and capturing LiDAR maps in subarctic forests using an autonomous teach-and-repeat system designed to be robust to kilometre-scale navigation, severe weather, and GNSS-denied conditions. During the teach phase, the robot is driven along a specific path by a human operator. A reference map and a reference path are meanwhile recorded and stored in the robot’s database. Then, during the repeat phase, a path following algorithm computes the output system commands to steer the vehicle along the reference path. Meanwhile, the path taken by robot is also recorded. The Model Predictive Control (MPC) based path following algorithm ([norlab_controllers_ros](https://github.com/norlab-ulaval/norlab_controllers_ros)) was implemented by the laboratory. For it to work effectively, some of its parameters need to be experimentally deducted.

This project retrieves the teach and repeat paths and computes the Cross-Track Error (XTE) between them. The median of the XTE along the path is then computed to estimate the controller’s performance 
during the repeat phase. After multiple runs, each time changing slightly one of the controller’s parameters, the controller may be fine-tuned, and its ideal parameter set may be found for a given environment. Moreover, this project also generates visualisation and diagnostics figures to estimate the controller’s performance.

## ROS tool
First, a Robot Operating System (ROS) package (named norlab_controllers_inspector) retrieves the data (teach and repeat paths) and exports it. It does so by calling a custom service declared in the [norlab_controllers_msgs](https://github.com/norlab-ulaval/norlab_controllers_msgs) package. 

At the start of the repeat phase, the inspector_node may be executed by writting the following command in a stand-alone robot terminal.
```bash
ros2 run norlab_controllers_inspector inspector_node
```

Then, before shutting down the inspector_node, the ExportData service may be called by writting the following command in another robot terminal.
```bash
ros2 service call /export_data norlab_controllers_msgs/srv/ExportData "export_path: data: 'Downloads/'"
```

## Analysis scripts
Secondly, once the data have been retrieved and saved locally, a non-ROS python script (named PathFollowingAnalysis) is used to compute the XTE along the path and its median. It also generates the 3 following figures :
* plot of the teach and repeat paths,
* boxplot of the XTE computed along the path,
* plot of the teach and repeat paths with color gradient according to the XTE computed along the path. 

Finally, after a few runs with slightly different controller’s parameters each time, a second non-ROS python script (named BoxPlotsComparison) may be used to generate an overview boxplot. This boxplot may help to visually express the increase or decrease of performance between different sets of parameters.



