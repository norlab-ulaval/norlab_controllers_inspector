"""
Author: Cyril Goffin
Last modified: 23/06/2023
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

save_path = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3'
parameter_name = 'kappa'

files_path1 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.001'
param_values1 = 0.001

files_path2 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.002'
param_values2 = 0.002

files_path3 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.005'
param_values3 = 0.005

files_path4 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.01'
param_values4 = 0.01

files_path5 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.02'
param_values5 = 0.02

files_path6 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.05'
param_values6 = 0.05

files_path7 = '/home/nicolas//Desktop/TeachAndRepeat_Husky_v3/variation_kappa/kappa_0.1'
param_values7 = 0.1


def data_analysis(path1, path2, path3, path4, path5, path6, path7):
    f_odom = 10
    # importing the data

    # 1
    actual_path_df1 = pd.read_pickle('%s/loc.pkl' % path1)
    target_path_df1 = pd.read_pickle('%s/ref_path.pkl' % path1)
    actual_path1 = actual_path_df1.to_numpy()
    target_path1 = target_path_df1.to_numpy()
    time_path_1 = round(len(actual_path1[:, 0])*1/f_odom, 0)
    print('# 1 Target path size:', len(target_path1[:, 0]), ' |  Actual path size:', len(actual_path1[:, 0]),
          ' |  Time it took:', time_path_1, 's')

    # 2
    actual_path_df2 = pd.read_pickle('%s/loc.pkl' % path2)
    target_path_df2 = pd.read_pickle('%s/ref_path.pkl' % path2)
    actual_path2 = actual_path_df2.to_numpy()
    target_path2 = target_path_df2.to_numpy()
    time_path_2 = len(actual_path2[:, 0]) * 1 / f_odom
    print('# 2 Target path size:', len(target_path2[:, 0]), ' |  Actual path size:', len(actual_path2[:, 0]),
          ' |  Time it took:', time_path_2, 's')

    # 3
    actual_path_df3 = pd.read_pickle('%s/loc.pkl' % path3)
    target_path_df3 = pd.read_pickle('%s/ref_path.pkl' % path3)
    actual_path3 = actual_path_df3.to_numpy()
    target_path3 = target_path_df3.to_numpy()
    time_path_3 = len(actual_path3[:, 0]) * 1 / f_odom
    print('# 3 Target path size:', len(target_path3[:, 0]), ' |  Actual path size:', len(actual_path3[:, 0]),
          ' |  Time it took:', time_path_3, 's')

    # 4
    actual_path_df4 = pd.read_pickle('%s/loc.pkl' % path4)
    target_path_df4 = pd.read_pickle('%s/ref_path.pkl' % path4)
    actual_path4 = actual_path_df4.to_numpy()
    target_path4 = target_path_df4.to_numpy()
    time_path_4 = len(actual_path4[:, 0]) * 1 / f_odom
    print('# 4 Target path size:', len(target_path4[:, 0]), ' |  Actual path size:', len(actual_path4[:, 0]),
          ' |  Time it took:', time_path_4, 's')

    # 5
    actual_path_df5 = pd.read_pickle('%s/loc.pkl' % path5)
    target_path_df5 = pd.read_pickle('%s/ref_path.pkl' % path5)
    actual_path5 = actual_path_df5.to_numpy()
    target_path5 = target_path_df5.to_numpy()
    time_path_5 = len(actual_path5[:, 0]) * 1 / f_odom
    print('# 5 Target path size:', len(target_path5[:, 0]), ' |  Actual path size:', len(actual_path5[:, 0]),
          ' |  Time it took:', time_path_5, 's')

    # 6
    actual_path_df6 = pd.read_pickle('%s/loc.pkl' % path6)
    target_path_df6 = pd.read_pickle('%s/ref_path.pkl' % path6)
    actual_path6 = actual_path_df6.to_numpy()
    target_path6 = target_path_df6.to_numpy()
    time_path_6 = len(actual_path6[:, 0]) * 1 / f_odom
    print('# 6 Target path size:', len(target_path6[:, 0]), ' |  Actual path size:', len(actual_path6[:, 0]),
          ' |  Time it took:', time_path_6, 's')

    # 7
    actual_path_df7 = pd.read_pickle('%s/loc.pkl' % path7)
    target_path_df7 = pd.read_pickle('%s/ref_path.pkl' % path7)
    actual_path7 = actual_path_df7.to_numpy()
    target_path7 = target_path_df7.to_numpy()
    time_path_7 = len(actual_path7[:, 0]) * 1 / f_odom
    print('# 7 Target path size:', len(target_path7[:, 0]), ' |  Actual path size:', len(actual_path7[:, 0]),
          ' |  Time it took:', time_path_7, 's')

    # computing a KDTree (nearest-neighbor lookup) to find the nearest target path point for each actual path point

    # 1
    ref_path_tree1 = KDTree(target_path1)
    nearest_distances1, distance_id1 = ref_path_tree1.query(actual_path1)
    median1 = np.median(nearest_distances1)
    print('# 1 Error median:', np.round(median1, 4), 'm')

    # 2
    ref_path_tree2 = KDTree(target_path2)
    nearest_distances2, distance_id2 = ref_path_tree2.query(actual_path2)
    median2 = np.median(nearest_distances2)
    print('# 2 Error median:', np.round(median2, 4), 'm')

    # 3
    ref_path_tree3 = KDTree(target_path3)
    nearest_distances3, distance_id3 = ref_path_tree3.query(actual_path3)
    median3 = np.median(nearest_distances3)
    print('# 3 Error median:', np.round(median3, 4), 'm')

    # 4
    ref_path_tree4 = KDTree(target_path4)
    nearest_distances4, distance_id4 = ref_path_tree4.query(actual_path4)
    median4 = np.median(nearest_distances4)
    print('# 4 Error median:', np.round(median4, 4), 'm')

    # 5
    ref_path_tree5 = KDTree(target_path5)
    nearest_distances5, distance_id5 = ref_path_tree5.query(actual_path5)
    median5 = np.median(nearest_distances5)
    print('# 5 Error median:', np.round(median5, 4), 'm')

    # 6
    ref_path_tree6 = KDTree(target_path6)
    nearest_distances6, distance_id6 = ref_path_tree6.query(actual_path6)
    median6 = np.median(nearest_distances6)
    print('# 6 Error median:', np.round(median6, 4), 'm')

    # 7
    ref_path_tree7 = KDTree(target_path7)
    nearest_distances7, distance_id7 = ref_path_tree7.query(actual_path7)
    median7 = np.median(nearest_distances7)
    print('# 7 Error median:', np.round(median7, 4), 'm')

    # evaluating the XTE (i.e. shortest distance)

    # variables used
    param_values = [param_values1, param_values2, param_values3,
                    param_values4, param_values5, param_values6, param_values7]
    box_plot_data = [nearest_distances1, nearest_distances2, nearest_distances3,
                     nearest_distances4, nearest_distances5, nearest_distances6, nearest_distances7]
    time_paths = [time_path_1, time_path_2, time_path_3, time_path_4, time_path_5, time_path_6, time_path_7]
    boxes_pos = [1, 2, 3, 4, 5, 6, 7]

    # plot itself
    plt.rc('font', family='serif')
    plt.rc('axes', axisbelow=True)

    fig, ax1 = plt.subplots(figsize=(5.5, 4), tight_layout='True')
    # ax1_color_light = '#ffce84'
    # ax1_color = '#d48000'
    ax1_color_light = '#E2D1F9'
    ax1_color = '#9c5af3'

    ax1.boxplot(box_plot_data,
                showfliers=False,
                patch_artist=True,
                boxprops=dict(facecolor=ax1_color_light, color=ax1_color),
                medianprops=dict(linestyle='-', linewidth=1.5, color=ax1_color),
                capprops=dict(color=ax1_color),
                whiskerprops=dict(color=ax1_color))
    ax1.set_ylim(top=0.75)
    ax1.set_ylabel('Cross-track error (XTE) / m', color=ax1_color)
    # phi_title = "Angular velocity gain \u03C6 (\u03BB=1 and \u03BA=0.01)"
    # lambda_title = "State cost translational \u03BB (\u03C6=1 and \u03BA=0.01)"
    kappa_title = "Input cost wheel \u03BA (\u03C6=1 and \u03BB=2)"
    ax1.set_xlabel(kappa_title)
    ax1.set_xticks(boxes_pos, param_values, fontsize='small')
    ax1.xaxis.set_tick_params(labelbottom=True, labeltop=False, bottom=True, direction='out')
    ax1.tick_params(axis='y', labelcolor=ax1_color)

    ax2 = ax1.twinx()
    ax2_color = '#156a65'
    ax2.set_ylim(bottom=0, top=450)
    start, end = ax2.get_ylim()
    ax2.yaxis.set_ticks(np.arange(start, end, 60))
    ax2.set_ylabel('$t_{path}$ / s', color=ax2_color)
    ax2.plot(boxes_pos, time_paths, '-.', color=ax2_color, linewidth=1.5)
    ax2.tick_params(axis='y', labelcolor=ax2_color)

    plt.savefig('%s/husky_variation_%s' % (save_path, parameter_name), dpi=300)
    plt.show()


if __name__ == '__main__':
    data_analysis(files_path1, files_path2, files_path3, files_path4, files_path5, files_path6, files_path7)
