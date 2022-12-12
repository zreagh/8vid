#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:19:28 2019

RSA analysis\\plotting script for the 8vid encoding data.

This script reads in all vectorized beta files for each ROI, computes all of
the relevant pairwise correlations across trial types, stores them in a pandas
data frame, and then analyzes and plots the data.

@author: zreagh
"""
import numpy as np
from scipy import stats

x = np.array([0, 0, 0, 1, 1, 1, 1])
y = np.array([.05,.03,.04,.82,.58,.72,.83])
stats.pointbiserialr(x,y)

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

subjects = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122]
#PMC subjects = [101,101,101,101,120,102]
#subjects = [102,104,107,108,111]
#subjects = [102]

file_dir = 'D:\\Users\\Owner\\Desktop\\8vid_betas\\'

# make global plot size parameter
plt.rcParams["figure.figsize"] = [10,10]

# create model matrices for our effects
x_lab = ['Tommy Cafe1', 'Lisa Cafe1', 'Tommy Cafe2', 'Lisa Cafe2',
     'Tommy Grocery1', 'Lisa Grocery1', 'Tommy Grocery2', 'Lisa Grocery2']
y_lab = ['Tommy Cafe1', 'Lisa Cafe1', 'Tommy Cafe2', 'Lisa Cafe2',
     'Tommy Grocery1', 'Lisa Grocery1', 'Tommy Grocery2', 'Lisa Grocery2']

#x_lab = ['Tommy Delta', 'Lisa Delta', 'Tommy Mishkas', 'Lisa Mishkas',
#     'Tommy CoOp', 'Lisa CoOp', 'Tommy Nugget', 'Lisa Nugget']
#y_lab = ['Tommy Delta', 'Lisa Delta', 'Tommy Mishkas', 'Lisa Mishkas',
#     'Tommy CoOp', 'Lisa CoOp', 'Tommy Nugget', 'Lisa Nugget']

person_mat = ([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]])
person_mat_flat = np.hstack(person_mat)
    
context_mat  = ([[1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1]])
context_mat_flat = np.hstack(context_mat)

schema_mat  = ([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1]])
schema_mat_flat = np.hstack(schema_mat)    

episodic_mat  = ([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]])
episodic_mat_flat = np.hstack(episodic_mat)

# plot model matrices (uncomment if desired) #

#plt.imshow(person_mat)
#plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
#plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#plt.show()
#
#plt.imshow(context_mat)
#plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
#plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#plt.show()
#
#plt.imshow(schema_mat)
#plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
#plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#plt.show()
#
#plt.imshow(episodic_mat)
#plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
#plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#plt.show()

# define global variables for ROIs
#ROIs = ['EVC','PMC','ANG','PHC','PRC','HPC','TempPole','MTG','mPFC']
ROIs = ['HPC']
results = {}

# Matrix of matrices across subjects (later averaged)
running_matrix = []
running_matrix_results = dict.fromkeys(ROIs,[])

# Empty lists of stats comparisons
person_mat_corrs = []
context_mat_corrs = []
schema_mat_corrs = []
episodic_mat_corrs = []

# loop through each subject
for subject in subjects:
    # grab all of our data from the beta CSV files
    all_data = []
    files = os.listdir(file_dir + "sub-%s\\" %(subject))
    sub_dir = file_dir + "sub-%s\\" %(subject)
    for file in files:
        data = pd.read_csv(sub_dir + file, index_col=None, header=0)
#        print("Length of %s" %(file) + " is %d" %(np.count_nonzero(data)))
        all_data.append(data)
    all_data = pd.concat(all_data, axis=1)
    all_data.columns = files
    all_data.replace(0, np.nan, inplace=True)

    # loop through our ROIs
    for region in ROIs:
        matrix = []
        
        ### TOMMY ###
        # MISHKAS #
        # get the TT MM correlations
        varname = "tt_mm_{}".format(region)
        ### IN PROGRESS, SHOULD LET US APPEND REGIONAL MATRIX COMPARISON LISTS
        ROI = "{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video3_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        
        # get the TT MD correlations
        varname = "tt_md_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video2_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video3_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas.csv"]
        y = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        y = all_data[region+"_video3_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the TT MN correlations
        varname = "tt_mn_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video2_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video3_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas.csv"]
        y = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        y = all_data[region+"_video3_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TT MC correlations
        varname = "tt_mc_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video2_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_mishkas_betas.csv"]
        y = all_data[region+"_video3_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        y = all_data[region+"_video3_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
    
        # COOP #
        # get the TT CC correlations
        varname = "tt_cc_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video3_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas_new.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
    
        # get the TT CD correlations
        varname = "tt_cd_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video2_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video3_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas_new.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas.csv"]
        y = all_data[region+"_video1_tommy_coop_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        y = all_data[region+"_video3_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the TT CN correlations
        varname = "tt_cn_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video2_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_coop_betas.csv"]
        y = all_data[region+"_video3_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas_new.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas.csv"]
        y = all_data[region+"_video1_tommy_coop_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        y = all_data[region+"_video3_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # DELTA #
        # get the TT DD correlations
        varname = "tt_dd_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas.csv"]
        y = all_data[region+"_video3_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas_new.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the TT DN correlations
        varname = "tt_dn_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_tommy_delta_betas.csv"]
        y = all_data[region+"_video2_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_delta_betas.csv"]
        y = all_data[region+"_video3_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas_new.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas.csv"]
        y = all_data[region+"_video1_tommy_delta_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        y = all_data[region+"_video3_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the TT NN correlations
        varname = "tt_nn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_tommy_nugget_betas.csv"]
        y = all_data[region+"_video3_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_nugget_betas_new.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        
        ### LISA ###
        # MISHKAS #
        # get the ll MM correlations
        varname = "ll_mm_{}".format(region)
        ### IN PROGRESS, SHOULD LET US APPEND REGIONAL MATRIX COMPARISON LISTS
        ROI = "{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video3_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        
        # get the ll MD correlations
        varname = "ll_md_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video2_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video3_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas.csv"]
        y = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        y = all_data[region+"_video3_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the ll MN correlations
        varname = "ll_mn_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video2_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video3_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas.csv"]
        y = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        y = all_data[region+"_video3_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the ll MC correlations
        varname = "ll_mc_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video2_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_mishkas_betas.csv"]
        y = all_data[region+"_video3_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas_new.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        y = all_data[region+"_video3_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
    
        # COOP #
        # get the ll CC correlations
        varname = "ll_cc_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video3_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas_new.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
    
        # get the ll CD correlations
        varname = "ll_cd_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video2_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video3_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas_new.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas.csv"]
        y = all_data[region+"_video1_lisa_coop_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        y = all_data[region+"_video3_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the ll CN correlations
        varname = "ll_cn_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video2_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_coop_betas.csv"]
        y = all_data[region+"_video3_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas_new.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas.csv"]
        y = all_data[region+"_video1_lisa_coop_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        y = all_data[region+"_video3_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # DELTA #
        # get the ll DD correlations
        varname = "ll_dd_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas.csv"]
        y = all_data[region+"_video3_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas_new.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the ll DN correlations
        varname = "ll_dn_{}".format(region)
        corrlist = []

        x = all_data[region+"_recall_lisa_delta_betas.csv"]
        y = all_data[region+"_video2_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_delta_betas.csv"]
        y = all_data[region+"_video3_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas_new.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas.csv"]
        y = all_data[region+"_video1_lisa_delta_betas.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        y = all_data[region+"_video3_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
        # get the ll NN correlations
        varname = "ll_nn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_recall_lisa_nugget_betas.csv"]
        y = all_data[region+"_video3_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_nugget_betas_new.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
        
    
    
        ### TOMMY-LISA ###
        # MISHKAS #
        # get the TL MM correlations
        varname = "tl_mm_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))

        results[varname] = (np.average(corrlist))
                
        # get the TL MD correlations
        varname = "tl_md_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TL MN correlations
        varname = "tl_mn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TL MC correlations
        varname = "tl_mc_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_mishkas_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_mishkas_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_mishkas_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
    
        # COOP #
        # get the TL CC correlations
        varname = "tl_cc_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
    
        # get the TL CD correlations
        varname = "tl_cd_{}".format(region)
        corrlist = []
        
        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TL CN correlations
        varname = "tl_cn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_coop_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_coop_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_coop_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # DELTA #
        # get the TL DD correlations
        varname = "tl_dd_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TL DN correlations
        varname = "tl_dn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_delta_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_delta_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_delta_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
        
        # get the TL NN correlations
        varname = "tl_nn_{}".format(region)
        corrlist = []

        x = all_data[region+"_video1_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_tommy_nugget_betas.csv"]
        y = all_data[region+"_recall_lisa_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video1_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video2_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        x = all_data[region+"_video3_lisa_nugget_betas.csv"]
        y = all_data[region+"_recall_tommy_nugget_betas_new.csv"]
        z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
        corrlist.append(np.arctanh(z[0][1]))
        
        results[varname] = (np.average(corrlist))
       # print('results in loop:/n {}'.format(results))
        
        ###### BUILD EACH SUBJECT'S CORRELATION MATRICES ######
        
        
        # matrix= [[results['tt_dd_PRC'], results['tl_dd_PRC'], results['tt_md_PRC'], results['tl_md_PRC'], results['tt_cd_PRC'], results['tl_cd_PRC'], results['tt_dn_PRC'], results['tl_dn_PRC']],
        #       [results['tl_dd_PRC'], results['ll_dd_PRC'], results['tl_md_PRC'], results['ll_md_PRC'], results['tl_mc_PRC'], results['ll_cd_PRC'], results['tl_dn_PRC'], results['ll_dn_PRC']],
        #       [results['tt_md_PRC'], results['tl_md_PRC'], results['tt_mm_PRC'], results['tl_md_PRC'], results['tt_mc_PRC'], results['tl_mc_PRC'], results['tt_mn_PRC'], results['tl_mn_PRC']],
        #       [results['tl_md_PRC'], results['ll_md_PRC'], results['tl_mm_PRC'], results['ll_mm_PRC'], results['tl_mc_PRC'], results['ll_mc_PRC'], results['tl_mn_PRC'], results['ll_mn_PRC']],
        #       [results['tt_cd_PRC'], results['tl_cd_PRC'], results['tt_mc_PRC'], results['tl_mc_PRC'], results['tt_cc_PRC'], results['tl_cc_PRC'], results['tt_cn_PRC'], results['tl_cn_PRC']],
        #       [results['tl_cd_PRC'], results['ll_cd_PRC'], results['tl_mc_PRC'], results['ll_mc_PRC'], results['tl_cc_PRC'], results['ll_cc_PRC'], results['tl_cn_PRC'], results['ll_cn_PRC']],
        #       [results['tt_dn_PRC'], results['tl_dn_PRC'], results['tt_mn_PRC'], results['tl_mn_PRC'], results['tt_cn_PRC'], results['tl_cn_PRC'], results['tt_nn_PRC'], results['tl_nn_PRC']],
        #       [results['tl_dn_PRC'], results['ll_dn_PRC'], results['tl_mn_PRC'], results['ll_mn_PRC'], results['tl_cn_PRC'], results['ll_cn_PRC'], results['tl_nn_PRC'], results['ll_nn_PRC']]]

        matrix= [[results['tt_dd_'+region], results['tl_dd_'+region], results['tt_md_'+region], results['tl_md_'+region], results['tt_cd_'+region], results['tl_cd_'+region], results['tt_dn_'+region], results['tl_dn_'+region]],
                [results['tl_dd_'+region], results['ll_dd_'+region], results['tl_md_'+region], results['ll_md_'+region], results['tl_mc_'+region], results['ll_cd_'+region], results['tl_dn_'+region], results['ll_dn_'+region]],
                [results['tt_md_'+region], results['tl_md_'+region], results['tt_mm_'+region], results['tl_md_'+region], results['tt_mc_'+region], results['tl_mc_'+region], results['tt_mn_'+region], results['tl_mn_'+region]],
                [results['tl_md_'+region], results['ll_md_'+region], results['tl_mm_'+region], results['ll_mm_'+region], results['tl_mc_'+region], results['ll_mc_'+region], results['tl_mn_'+region], results['ll_mn_'+region]],
                [results['tt_cd_'+region], results['tl_cd_'+region], results['tt_mc_'+region], results['tl_mc_'+region], results['tt_cc_'+region], results['tl_cc_'+region], results['tt_cn_'+region], results['tl_cn_'+region]],
                [results['tl_cd_'+region], results['ll_cd_'+region], results['tl_mc_'+region], results['ll_mc_'+region], results['tl_cc_'+region], results['ll_cc_'+region], results['tl_cn_'+region], results['ll_cn_'+region]],
                [results['tt_dn_'+region], results['tl_dn_'+region], results['tt_mn_'+region], results['tl_mn_'+region], results['tt_cn_'+region], results['tl_cn_'+region], results['tt_nn_'+region], results['tl_nn_'+region]],
                [results['tl_dn_'+region], results['ll_dn_'+region], results['tl_mn_'+region], results['ll_mn_'+region], results['tl_cn_'+region], results['ll_cn_'+region], results['tl_nn_'+region], results['ll_nn_'+region]]]


        matrix_flat = np.hstack(matrix)
        
        # append the running matrix list with each subject's data
        running_matrix.append(matrix_flat)
        running_matrix_results[region].append(matrix_flat)
#        print(running_matrix)

#        plt.imshow(matrix)
#        plt.colorbar()
#        plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
#        plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#        plt.show()
#        print(subject)
        
        # append matrix correlation results for reach subject
        person_mat_corrs.append(stats.pointbiserialr(matrix_flat,person_mat_flat))
        context_mat_corrs.append(stats.pointbiserialr(matrix_flat,context_mat_flat))
        schema_mat_corrs.append(stats.pointbiserialr(matrix_flat,schema_mat_flat))
        episodic_mat_corrs.append(stats.pointbiserialr(matrix_flat,episodic_mat_flat))

###### MOCK-UP! NOT REAL RESULTS! ######

# hpc_matrix=[[0.152, results['tl_dd_HPC'], results['tt_md_HPC'], results['tl_md_HPC'], results['tt_cd_HPC'], 0.005, results['tt_dn_HPC'], results['tl_dn_HPC']],
#               [results['tl_dd_HPC'], 0.135, results['tl_md_HPC'], results['ll_md_HPC'], results['tl_mc_HPC'], -0.014, results['tl_dn_HPC'], results['ll_dn_HPC']],
#               [results['tt_md_HPC'], results['tl_md_HPC'], 0.142, results['tl_md_HPC'], 0.001, -0.005, -0.01, results['tl_mn_HPC']],
#               [results['tl_md_HPC'], results['ll_md_HPC'], results['tl_mm_HPC'], 0.125, -0.015, results['ll_mc_HPC'], results['tl_mn_HPC'], results['ll_mn_HPC']],
#               [results['tt_cd_HPC'], results['tl_cd_HPC'], 0.001, -0.015, results['tt_cc_HPC'], -0.02, -0.011, 0.01],
#               [0.005, -0.014, -0.005, results['ll_mc_HPC'], -0.02, 0.131, 0.001, -.003],
#               [results['tt_dn_HPC'], results['tl_dn_HPC'], -0.01, results['tl_mn_HPC'], -0.011, 0.001, 0.144, results['tl_nn_HPC']],
#               [results['tl_dn_HPC'], results['ll_dn_HPC'], results['tl_mn_HPC'], results['ll_mn_HPC'], 0.01, -0.003, results['tl_nn_HPC'], 0.146]]
# hpc_matrix_flat = np.hstack(hpc_matrix)  

# stats.pointbiserialr(hpc_matrix_flat,person_mat_flat)

# plt.imshow(hpc_matrix)
# plt.colorbar()
# plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
# plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
# plt.show()


# mPFC_matrix=[[results['tt_dd_mPFC'], results['tl_dd_mPFC'], 0.25, 0.27, 0.025, results['tl_cd_mPFC'], results['tt_dn_mPFC'], results['tl_dn_mPFC']],
#               [results['tl_dd_mPFC'], results['ll_dd_mPFC'], 0.24, results['ll_md_mPFC'], results['tl_mc_mPFC'], results['ll_cd_mPFC'], results['tl_dn_mPFC'], results['ll_dn_mPFC']],
#               [0.25, 0.24, 0.28, results['tl_md_mPFC'], results['tt_mc_mPFC'], results['tl_mc_mPFC'], results['tt_mn_mPFC'], results['tl_mn_mPFC']],
#               [0.27, results['ll_md_mPFC'], results['tl_mm_mPFC'], 0.29, results['tl_mc_mPFC'], results['ll_mc_mPFC'], results['tl_mn_mPFC'], results['ll_mn_mPFC']],
#               [0.025, results['tl_cd_mPFC'], results['tt_mc_mPFC'], results['tl_mc_mPFC'], results['tt_cc_mPFC'], results['tl_cc_mPFC'], 0.26, 0.25],
#               [results['tl_cd_mPFC'], results['ll_cd_mPFC'], results['tl_mc_mPFC'], results['ll_mc_mPFC'], results['tl_cc_mPFC'], 0.305, 0.244, 0.295],
#               [results['tt_dn_mPFC'], results['tl_dn_mPFC'], results['tt_mn_mPFC'], results['tl_mn_mPFC'], 0.26, 0.244, results['tt_nn_mPFC'], 0.275],
#               [results['tl_dn_mPFC'], results['ll_dn_mPFC'], results['tl_mn_mPFC'], results['ll_mn_mPFC'], 0.25, 0.295, 0.275, 0.308]]
# mPFC_matrix_flat = np.hstack(mPFC_matrix)                

# plt.imshow(mPFC_matrix)
# plt.colorbar()
# plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
# plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
# plt.show()


# #subject 113
# PMC_matrix=[[0.65, results['tl_dd_PMC'], 0.51, results['tl_md_PMC'], results['tt_cd_PMC'], results['tl_cd_PMC'], results['tt_dn_PMC'], results['tl_dn_PMC']],
#               [results['tl_dd_PMC'], 0.6, results['tl_md_PMC'], 0.55, results['tl_mc_PMC'], results['ll_cd_PMC'], results['tl_dn_PMC'], results['ll_dn_PMC']],
#               [0.51, results['tl_md_PMC'], 0.66, 0.64, 0.51, results['tl_mc_PMC'], results['tt_mn_PMC'], results['tl_mn_PMC']],
#               [results['tl_md_PMC'], 0.55, 0.64, results['ll_mm_PMC'], results['tl_mc_PMC'], results['ll_mc_PMC'], results['tl_mn_PMC'], results['ll_mn_PMC']],
#               [results['tt_cd_PMC'], results['tl_cd_PMC'], 0.51, results['tl_mc_PMC'], 0.62, 0.57, results['tt_cn_PMC'], results['tl_cn_PMC']],
#               [results['tl_cd_PMC'], results['ll_cd_PMC'], results['tl_mc_PMC'], results['ll_mc_PMC'], 0.57, 0.66, results['tl_cn_PMC'], results['ll_cn_PMC']],
#               [results['tt_dn_PMC'], results['tl_dn_PMC'], results['tt_mn_PMC'], results['tl_mn_PMC'], results['tt_cn_PMC'], results['tl_cn_PMC'], 0.67, 0.655],
#               [results['tl_dn_PMC'], results['ll_dn_PMC'], results['tl_mn_PMC'], results['ll_mn_PMC'], results['tl_cn_PMC'], results['ll_cn_PMC'], 0.655, 0.68]]
# PMC_matrix_flat = np.hstack(PMC_matrix)              
    
# plt.imshow(PMC_matrix)
# plt.colorbar()
# plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
# plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
# plt.show() 


#subject 107
#PRC_matrix=[[0.31, results['tl_dd_PRC'], results['tt_md_PRC'], results['tl_md_PRC'], 0.32, results['tl_cd_PRC'], results['tt_dn_PRC'], results['tl_dn_PRC']],
#               [results['tl_dd_PRC'], 0.299, results['tl_md_PRC'], results['ll_md_PRC'], results['tl_mc_PRC'], 0.35, results['tl_dn_PRC'], 0.34],
#               [results['tt_md_PRC'], results['tl_md_PRC'], 0.36, results['tl_md_PRC'], results['tt_mc_PRC'], results['tl_mc_PRC'], results['tt_mn_PRC'], results['tl_mn_PRC']],
#               [results['tl_md_PRC'], results['ll_md_PRC'], 0.17, results['ll_mm_PRC'], results['tl_mc_PRC'], 0.29, results['tl_mn_PRC'], results['ll_mn_PRC']],
#               [0.32, results['tl_cd_PRC'], results['tt_mc_PRC'], results['tl_mc_PRC'], 0.37, results['tl_cc_PRC'], results['tt_cn_PRC'], results['tl_cn_PRC']],
#               [results['tl_cd_PRC'], 0.35, results['tl_mc_PRC'], 0.29, results['tl_cc_PRC'], 0.36, results['tl_cn_PRC'], results['ll_cn_PRC']],
#               [results['tt_dn_PRC'], results['tl_dn_PRC'], results['tt_mn_PRC'], results['tl_mn_PRC'], results['tt_cn_PRC'], results['tl_cn_PRC'], 0.37, 0.18],
#               [results['tl_dn_PRC'], 0.34, results['tl_mn_PRC'], results['ll_mn_PRC'], results['tl_cn_PRC'], results['ll_cn_PRC'], 0.18, results['ll_nn_PRC']]]
#PRC_matrix_flat = np.hstack(PRC_matrix)  

# Avg matrix
avg_matrix = np.average(running_matrix,axis=0)
avg_matrix_reshaped = avg_matrix.reshape(8,8)
avg_matrix_flat = np.hstack(avg_matrix_reshaped)

# Avg matrix stats
print(stats.pointbiserialr(avg_matrix_flat,person_mat_flat))
print(stats.pointbiserialr(avg_matrix_flat,context_mat_flat))
print(stats.pointbiserialr(avg_matrix_flat,schema_mat_flat))
print(stats.pointbiserialr(avg_matrix_flat,episodic_mat_flat))

# Plot the matrix

plt.imshow(avg_matrix_reshaped,cmap='viridis')
plt.colorbar()
plt.title(region, fontsize=60)
plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
#plt.savefig('{}_recall_mat.pdf'.format(region),bbox_inches = "tight")
#plt.savefig('test.pdf',bbox_inches = "tight")
plt.show()



# Isolate the z-scored correlation coefficients and make lists

person_corr_vec = []
context_corr_vec = []
schema_corr_vec = []
episodic_corr_vec = []

for i in range(0,20):
    person_corr_vec.append(person_mat_corrs[i][0])
    context_corr_vec.append(context_mat_corrs[i][0])
    schema_corr_vec.append(schema_mat_corrs[i][0])
    episodic_corr_vec.append(episodic_mat_corrs[i][0])

# Create a dataframe of the lists

corr_df = pd.DataFrame(list(zip(person_corr_vec,context_corr_vec,schema_corr_vec,
                                episodic_corr_vec)), columns=(['person','context','schema','episodic']))

# Convert to a 'long' format dataframe for 1-way ANOVA
corr_df_stacked = corr_df.stack().reset_index()
corr_df_stacked.columns = ['subject','model','zscore']

# One-way ANOVA

#import statsmodels.api as sm
#from statsmodels.formula.api import ols

#model = ols('zscore ~ C(model)', data=corr_df_stacked).fit()
#aov_table = sm.stats.anova_lm(model, typ=2)
#print(aov_table)

# One-way repeated-measures ANOVA

from statsmodels.stats.anova import AnovaRM

AOV = AnovaRM(data=corr_df_stacked, depvar='zscore', subject='subject', within=['model']).fit()
print(AOV)

# Post-hoc tests

import statsmodels.stats.multicomp as mc

comp = mc.MultiComparison(corr_df_stacked['zscore'], corr_df_stacked['model'])
post_hoc_res = comp.tukeyhsd()
print(post_hoc_res.summary())

import seaborn as sns

#BARPLOT VERSION

corr_df_stacked = corr_df.stack().reset_index()
corr_df_stacked.columns = ['subject','model','zscore']

sns.set(style="ticks",context=("poster"),font_scale=1.25)
fig, ax = plt.subplots()
fig.set_size_inches(8,8)

fig = sns.barplot(x="model", y='zscore', data=corr_df_stacked, capsize=.1, ci=68, palette="colorblind")
#fig = sns.boxplot(x="Context", y=region, hue='Person', data=final_encoding_results_df, palette="colorblind")
fig = sns.swarmplot(x="model", y='zscore', dodge=True, data=corr_df_stacked, size=8, color="k", alpha=.5)
#leg = fig.axes.flat[0].get_legend()
plt.title("HPC Model Matrix Fits")
plt.ylabel("Model fit (z-score)")
plt.xlabel("Model")
plt.tight_layout()
#ax.legend_.remove()
#plt.savefig('mPFC_model_matrix_fits_recall.pdf')


# ##### FOR COLLAPSING ACROSS ROIS #####

# ANG_mat = avg_matrix_reshaped
# ANG_mat_flat = avg_matrix_flat
# ANG_corr_df = corr_df
# ANG_corr_df_stacked = corr_df_stacked

# dfs = [PMC_corr_df,PHC_corr_df,ANG_corr_df]
# PMN_corr_df = pd.concat([each.stack() for each in dfs],axis=1)\
#               .apply(lambda x:x.mean(),axis=1)\
#               .unstack()
# PMN_corr_df_stacked = PMN_corr_df.stack().reset_index()
# PMN_corr_df_stacked.columns = ['subject','model','zscore']

# PMN_mat = np.mean([PMC_mat,ANG_mat,PHC_mat],axis=0)

# PMN_mat_flat = np.hstack(PMN_mat)

# # print(stats.pointbiserialr(PMN_mat_flat,person_mat_flat))
# # print(stats.pointbiserialr(PMN_mat_flat,context_mat_flat))
# # print(stats.pointbiserialr(PMN_mat_flat,schema_mat_flat))
# # print(stats.pointbiserialr(PMN_mat_flat,episodic_mat_flat))

# # AOV = AnovaRM(data=PMN_corr_df_stacked, depvar='zscore', subject='subject', within=['model']).fit()
# # print(AOV)

# # comp = mc.MultiComparison(PMN_corr_df_stacked['zscore'], PMN_corr_df_stacked['model'])
# # post_hoc_res = comp.tukeyhsd()
# # print(post_hoc_res.summary())



# import seaborn as sns

# sns.set(style="ticks",context=("poster"),font_scale=1.25)
# fig, ax = plt.subplots()
# fig.set_size_inches(8,8)
# #ax.set_ylim(0.0,0.09)

# #BARPLOT VERSION
# fig = sns.barplot(x="model", y='zscore', data=PMN_corr_df_stacked, capsize=.1, ci=68, palette="colorblind")
# #fig = sns.boxplot(x="Context", y=region, hue='Person', data=final_encoding_results_df, palette="colorblind")
# fig = sns.swarmplot(x="model", y='zscore', dodge=True, data=PMN_corr_df_stacked, size=8, color="k", alpha=.5)
# #leg = fig.axes.flat[0].get_legend()
# plt.title("PM Network Model Matrix Fits")
# plt.ylabel("Model fit (z-score)")
# plt.xlabel("Model")
# plt.tight_layout()
# #ax.legend_.remove()
# plt.savefig('ATN_model_matrix_fits_recall.pdf')

# # MATRIX
# plt.imshow(ATN_mat,cmap='viridis')
# plt.colorbar()
# plt.title('PM Network', fontsize=60)
# plt.xticks(range(len(x_lab)), x_lab, fontsize=30, rotation=90)
# plt.yticks(range(len(y_lab)), y_lab, fontsize=30)
# plt.savefig('ATN_encoding_mat.pdf',bbox_inches = "tight")
# plt.show()