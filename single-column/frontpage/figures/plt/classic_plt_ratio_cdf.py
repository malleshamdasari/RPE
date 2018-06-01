from operator import itemgetter
from tldextract import tldextract

__author__ = 'jnejati'

import os
from os import path as p
import numpy as np
import matplotlib
import bench
import copy

matplotlib.use('svg')
import matplotlib.pyplot as plt


def read_file(f):
    table = [l.strip().split() for l in open(f).read().splitlines()]
    table = np.asarray(table)
    return table


def make_cdf(values, key):
    cdfvalues = []
    cdffile = open("../OutputFiles/CDF/ratio/" + key + "_cdf_ratio.txt", "w")
    index = 1
    for value in values:
        cdfvalue = index / (len(values) * 1.0)
        cdfvalues.append(cdfvalue)
        cdffile.write(str(value) + "\t" + str(cdfvalue) + "\n")
        index += 1
    return cdffile.name


def do_plot_time(files_list, param):
    """"fig.set_size_inches((7,5))\n",
        "line_1, line_2, line_3, line_4 = ax1.plot(table_1[:,0], table_1[:,1],'b-', table_10[:,0], table_10[:,1],'c-', table_2[:,0], table_2[:,1], 'r', table_8[:,0], table_8[:,1], 'm',linewidth=4.0)\n",
        "\n",
        "ax1.tick_params(axis='x')\n",
        "ax1.tick_params(axis='y')\n",
        "ax1.grid(True)\n",
        "ax1.set_ylim([0, 1])\n",
        "ax1.set_xlim([0,35])\n",
        "ax1.set_title('Time on render on desktop vs phone')\n",
        "ax1.set_xlabel('Seconds')\n",
        "ax1.set_ylabel('CDF')\n",
        "line_1.set_label('desktop dpage top200')\n",
        "line_2.set_label('desktop mpage top200')\n",
        "line_3.set_label('phone dpage top200_2')\n",
        "line_4.set_label('phone mpage top200_2')\n",
        "legend = plt.legend(loc='lower right', shadow=True, fontsize='medium') """
    t1 = [l.strip().split() for l in open(files_list[0]).read().splitlines()]
    t1 = np.asarray(t1).astype(float)
    print(t1)
    
    #t2 = [l.strip().split() for l in open(files_list[1]).read().splitlines()]
    #t2 = np.asarray(t2).astype(float)
    
    """t3 = [l.strip().split() for l in open(files_list[2]).read().splitlines()]
        t3 = np.asarray(t3).astype(float)
        
        t4 = [l.strip().split() for l in open(files_list[3]).read().splitlines()]
        t4 = np.asarray(t4).astype(float)"""
    
    #t5 = [l.strip().split() for l in open(files_list[4]).read().splitlines()]
    #t5 = np.asarray(t5).astype(float)
    
    #t6 = [l.strip().split() for l in open(files_list[5]).read().splitlines()]
    #t6 = np.asarray(t6).astype(float)
    
    fig = plt.figure()
    ax2 = fig.add_subplot(1, 1, 1)
    fig.set_size_inches((7, 5))
    """line_1, line_2, line_3, line_4, line_5, line_6 = ax2.plot(t1[:, 0], t1[:, 1], 'g--',
        t2[:, 0], t2[:, 1], 'y--',
        t3[:, 0], t3[:, 1], 'b--',
        t4[:, 0], t4[:, 1], 'g',
        t5[:, 0], t5[:, 1], 'y',
        t6[:, 0], t6[:, 1], 'b',
        linewidth=2.0)"""
    
    line_1, line_2 = ax2.plot(t1[:, 0], t1[:, 1], 'g--', t1[:, 0], t1[:, 1], 'g--',
                              linewidth=2.0)
                              ax2.tick_params(axis='x')
                              ax2.tick_params(axis='y')
                              ax2.grid(True)
                              ax2.set_ylim([0, 1])
                              ax2.set_xlim([0, 10])
                              # t_list = file1.split('/')[-1].split('_')
                              
                              #ax2.set_title('PLT ratio: mobile/desktop', fontsize=8)
                              ax2.set_xlabel('Ratio')
                              ax2.set_ylabel('CDF')
                              #line_1.set_label('')
                              #line_2.set_label('comp-b20-d50')
                              #line_3.set_label('comp-b20-d150')
                              #line_4.set_label('net-b5-d150')
                              #line_5.set_label('net-b20-d50')
                              #line_6.set_label('net-b20-d150')
                              
                              print(files_list[0])
                              legend = plt.legend(loc='best', shadow=True, fontsize='8')
                              plt.show()
                              plt.savefig('../plots/ratio/' + 'mobile_desktop_plt_ratio'  + ".pdf")
                              plt.close()


def plt_files(file1, file2):
    path = '../OutputFiles'
    site_stats = {}
    sitename_set_list = []
    my_file1 = os.path.join(path, file1)
    my_file2 = os.path.join(path, file2)
    table_1 = read_file(my_file1)
    table_2 = read_file(my_file2)
    #print(table_1)
    a = [table_1[i][0] for i in range(len(table_1))]
    b = [table_2[i][0] for i in range(len(table_2))]
    a = sorted(a, key=itemgetter(0))
    b = sorted(b, key=itemgetter(0))
    a = set(a)
    b = set(b)
    print('set a: ', a)
    print('set b: ', b)
    sitename_set_list.append(a)
    sitename_set_list.append(b)
    pairwise_intersection = set.intersection(*sitename_set_list)
    print(pairwise_intersection)
    return pairwise_intersection

def common_plt_sites(file1, file2, common_sites):
    path = '../OutputFiles'
    my_list_plt = set()
    my_file1 = os.path.join(path, file1)
    my_file2 = os.path.join(path, file2)
    table_1 = read_file(my_file1)
    table_2 = read_file(my_file2)
    for sites in common_sites:
        print('site: ',sites)
        for my_line_a in table_1:
            for my_line_b in table_2:
                if my_line_a[0] == my_line_b[0] and my_line_a[0] == sites:
                    #print(float(my_line_a[4]), float(my_line_b[4]), float(my_line_b[4])/float(my_line_a[4]))
                    my_list_plt.add(float(my_line_b[4])/float(my_line_a[4]))
    return my_list_plt


def main():
    file_list = []
    ratio_list_plt = []
    
    #file_list.append('desktop_wifi-b1-d5_mixed200_orig_minification.bench')
    #file_list.append('desktop_wifi-b1-d150_mixed200_orig_minification.bench')
    file_list.append('desktop_wifi-b20-d5_mixed200_orig_minification.bench')
    #file_list.append('desktop_wifi-b20-d150_mixed200_orig_minification.bench')
    #file_list.append('mobile_wifi-b1-d5_mixed200_orig_minification.bench')
    #file_list.append('mobile_wifi-b1-d150_mixed200_orig_minification.bench')
    #file_list.append('mobile_wifi-b20-d5_mixed200_orig_minification.bench')
    file_list.append('mobile_wifi-b20-d5_mixed200_orig_minification.bench')
    
    common_sites1 = plt_files(file_list[0], file_list[1])
    common_plt1 = common_plt_sites(file_list[0], file_list[1], common_sites1)
    print(common_plt1)
    
    """common_sites2 = plt_files(file_list[1], file_list[5])
        common_sites2 = common_sites2 - common_sites1
        common_plt2 = common_plt_sites(file_list[1], file_list[5], common_sites1)
        
        common_sites3 = plt_files(file_list[2], file_list[6])
        common_sites3 = (common_sites3 - common_sites2 )- common_sites1
        common_plt3 = common_plt_sites(file_list[2], file_list[6], common_sites1)
        
        common_sites4 = plt_files(file_list[3], file_list[7])
        common_sites4 = ((common_sites4 - common_sites3) - common_sites2 ) - common_sites1
        common_plt4 = common_plt_sites(file_list[3], file_list[7], common_sites1)
        print(common_plt4)
        common_plt_total = ((common_plt1 | common_plt2) | common_plt3) | common_plt4"""
    common_plt_total = common_plt1
    print(common_plt_total)
    print(len(common_plt_total))
    file1 = make_cdf(sorted(list(common_plt_total)), 'plt_mobile_desktop')
    ratio_list_plt.append(file1)
    do_plot_time(ratio_list_plt, 'ratio')


if __name__ == "__main__":
    main()
