__author__ = 'jnejati'

import os
from os import path as p
import numpy as np
import matplotlib

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

    t2 = [l.strip().split() for l in open(files_list[1]).read().splitlines()]
    t2 = np.asarray(t2).astype(float)

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

    line_1,  line_4 = ax2.plot(t1[:, 0], t1[:, 1], 'g--',

                                                              t2[:, 0], t2[:, 1], 'g',
                                              linewidth=2.0)
    ax2.tick_params(axis='x')
    ax2.tick_params(axis='y')
    ax2.grid(True)
    ax2.set_ylim([0, 1])
    ax2.set_xlim([0, 1])
    # t_list = file1.split('/')[-1].split('_')

    ax2.set_title('comp and net to plt ratio', fontsize=8)
    ax2.set_xlabel('Ratio')
    ax2.set_ylabel('CDF')
    line_1.set_label('comp to plt ratio')
    #line_2.set_label('comp-b20-d50')
    #line_3.set_label('comp-b20-d150')
    line_4.set_label('net to plt ratio')
    #line_5.set_label('net-b20-d50')
    #line_6.set_label('net-b20-d150')

    print(files_list[0])
    legend = plt.legend(loc='best', shadow=True, fontsize='8')
    plt.show()
    plt.savefig('../plots/ratio/new/' + 'mobile_s6_b5-d5'  + ".pdf")
    plt.close()


def main():
    path = '../OutputFiles'
    dirs = os.listdir(path)
    ratio_list_plt = []
    ratio_list_comp = []
    ratio_list_net = []
    for files in dirs:
        if files.endswith('.bench'):
            files = os.path.join(path, files)
            table_1 = read_file(files)
            # print(files)
            name1 = files.split('/')[2].split('_mixed')[0]
            a = np.array(table_1[:, 2]).astype(float) #comp
            b = np.array(table_1[:, 3]).astype(float) #net
            c = np.array(table_1[:, 4]).astype(float) #plt
            c = a + b
            d = (a / c)
            e = (b/ c)
            file1 = make_cdf(sorted(d), 'comp_ratio_' + name1)
            file2 = make_cdf(sorted(e), 'net_ratio_' + name1)
            ratio_list_plt.append(file1)
            ratio_list_plt.append(file2)

    do_plot_time(ratio_list_plt, name1)
    """for files in dirs:
        if files.endswith('.bench'):
            files = os.path.join(path, files)
            table_1 = read_file(files)
            # print(files)
            name1 = table_1[0, 1].split("/")[2] + \
                    '_and_' + table_1[0, 5].split("/")[2]

            a = np.array(table_1[:, 2]).astype(float)
            b = np.array(table_1[:, 6]).astype(float)
            c = (a / b)
            file2 = make_cdf(sorted(c), 'comp_' + name1)
            ratio_list_comp.append(file2)
    do_plot_time(ratio_list_comp, 'comp')
    for files in dirs:
        if files.endswith('.bench'):
            files = os.path.join(path, files)
            table_1 = read_file(files)
            # print(files)
            name1 = table_1[0, 1].split("/")[2] + \
                    '_and_' + table_1[0, 5].split("/")[2]

            a = np.array(table_1[:, 3]).astype(float)
            b = np.array(table_1[:, 7]).astype(float)
            c = (a / b)
            file3 = make_cdf(sorted(c), 'net_' + name1)
            ratio_list_net.append(file3)
    do_plot_time(ratio_list_net, 'net')"""
    """for files in dirs:
        if files.endswith('.bench'):
            files = os.path.join(path, files)
            table_1 = read_file(files)
            # print(files)
            name1 = table_1[0, 1].split("/")[2] + \
                    '_and_' + table_1[0, 5].split("/")[2]

            plt_lowdelay = np.array(table_1[:, 4]).astype(float)
            plt_highdelay = np.array(table_1[:, 8]).astype(float)
            net_lowdelay = np.array(table_1[:, 2]).astype(float)
            net_highdelay = np.array(table_1[:, 6]).astype(float)
            net_percentage_lowdelay = net_lowdelay/plt_lowdelay
            net_percentage_highdelay = net_highdelay/plt_highdelay

            file3 = make_cdf(sorted(net_percentage_lowdelay), 'comppercentage_lowdelay' + name1)
            file4 = make_cdf(sorted(net_percentage_highdelay), 'comppercentage_highdelay' + name1)

            ratio_list_net.append(file3)
            ratio_list_net.append(file4)"""

    #do_plot_time(ratio_list_net, 'plt_')


if __name__ == "__main__":
    main()
