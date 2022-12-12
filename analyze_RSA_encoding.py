#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:19:28 2019

@author: zreagh
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns

subjects = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122]
#subjects = [101,102]

file_dir = '/Users/zreagh/Desktop/8vid_betas/'

# define global variables for ROIs and results arrays
regions = ['EVC','PMC','ANG','PHC','PRC','HPC','TempPole','MTG','mPFC']
PIC_CorrCoef = []
SPDC_CorrCoef = []
DPSC_CorrCoef = []
DPDC_CorrCoef = []
SPSimC_CorrCoef = []
DPSimC_CorrCoef = []

# set up performance summary
for subject in subjects:
    all_data = []
    files = os.listdir(file_dir + "sub-%s/" %(subject))
    sub_dir = file_dir + "sub-%s/" %(subject)
    for file in files:
        data = pd.read_csv(sub_dir + file, index_col=None, header=0)
#        print("Length of %s" %(file) + "is %d" %(np.count_nonzero(data)))
        all_data.append(data)
    all_data = pd.concat(all_data, axis=1)
    all_data.columns = files
    all_data.replace(0, np.nan, inplace=True)
    
    # z-score the data
#    cols = list(all_data.columns)
#    all_data[cols]
#    for col in cols:
#        col_zscore = col + '_zscore'
#        all_data[col_zscore] = (all_data[col] - all_data[col].mean())/all_data[col].std(ddof=0)
    
    ### PERSON-IN-CONTEXT DATA ###
    
    # set up empty lists as local variables (later fed into global lists)
    PIC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])
    
    # run the person-in-context correlations for encoding for EVC:
    person_in_context_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_nugget_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_coop_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_EVC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_EVC_avg = (np.average(person_in_context_encoding_EVC))
    # run the person-in-context correlations for encoding for PMC:
    person_in_context_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_nugget_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_coop_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PMC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_PMC_avg = (np.average(person_in_context_encoding_PMC))
    # run the person-in-context correlations for encoding for ANG:
    person_in_context_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_nugget_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_coop_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_ANG.append(np.arctanh(z[0][1]))
    person_in_context_encoding_ANG_avg = (np.average(person_in_context_encoding_ANG))
    # run the person-in-context correlations for encoding for PHC:
    person_in_context_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_nugget_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_coop_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PHC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_PHC_avg = (np.average(person_in_context_encoding_PHC))
    # run the person-in-context correlations for encoding for PRC:
    person_in_context_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_nugget_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_coop_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_PRC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_PRC_avg = (np.average(person_in_context_encoding_PRC))
    # run the person-in-context correlations for encoding for HPC:
    person_in_context_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_nugget_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_coop_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_HPC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_HPC_avg = (np.average(person_in_context_encoding_HPC))
    # run the person-in-context correlations for encoding for TempPole:
    person_in_context_encoding_TempPole = []
    person_in_context_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_coop_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    person_in_context_encoding_TempPole.append(np.arctanh(z[0][1]))
    person_in_context_encoding_TempPole_avg = (np.average(person_in_context_encoding_TempPole))
    # run the person-in-context correlations for encoding for MTG:
    person_in_context_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_nugget_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_coop_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_MTG.append(np.arctanh(z[0][1]))
    person_in_context_encoding_MTG_avg = (np.average(person_in_context_encoding_MTG))
    # run the person-in-context correlations for encoding for mPFC:
    person_in_context_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_coop_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    person_in_context_encoding_mPFC.append(np.arctanh(z[0][1]))
    person_in_context_encoding_mPFC_avg = (np.average(person_in_context_encoding_mPFC))
    # make person-in-context part of the dataframe
    #PIC_encoding_results = pd.DataFrame({'Subject':['{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject),'{0}'.format(subject).format(subject)], 'Region':['EVC','PMC','ANG','PHC','PRC','HPC','TempPole','MTG','mPFC'], 'Value':[person_in_context_encoding_EVC_avg,person_in_context_encoding_PMC_avg,person_in_context_encoding_ANG_avg,person_in_context_encoding_PHC_avg,person_in_context_encoding_PRC_avg,person_in_context_encoding_HPC_avg,person_in_context_encoding_TempPole_avg,person_in_context_encoding_MTG_avg,person_in_context_encoding_mPFC_avg]})
    PIC_encoding_results.append({'Region':['EVC','PMC','ANG','PHC','PRC','HPC','TempPole','MTG','mPFC'], 'z_Corr':[person_in_context_encoding_EVC_avg,person_in_context_encoding_PMC_avg,person_in_context_encoding_ANG_avg,person_in_context_encoding_PHC_avg,person_in_context_encoding_PRC_avg,person_in_context_encoding_HPC_avg,person_in_context_encoding_TempPole_avg,person_in_context_encoding_MTG_avg,person_in_context_encoding_mPFC_avg]},ignore_index=True)
    results_array = (person_in_context_encoding_EVC_avg,person_in_context_encoding_PMC_avg,person_in_context_encoding_ANG_avg,person_in_context_encoding_PHC_avg,person_in_context_encoding_PRC_avg,person_in_context_encoding_HPC_avg,person_in_context_encoding_TempPole_avg,person_in_context_encoding_MTG_avg,person_in_context_encoding_mPFC_avg)
    PIC_CorrCoef.append(results_array)
    

    ### SAME-PERSON-DIFFERENT-CONTEXT DATA ###
    
    # set up empty lists
    SPDC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])

    # run the person-in-context correlations for encoding for EVC:
    SPDC_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    SPDC_encoding_EVC_avg = (np.average(SPDC_encoding_EVC))
    # run the person-in-context correlations for encoding for PMC:
    SPDC_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    SPDC_encoding_PMC_avg = (np.average(SPDC_encoding_PMC))
    # run the person-in-context correlations for encoding for ANG:
    SPDC_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    SPDC_encoding_ANG_avg = (np.average(SPDC_encoding_ANG))
    # run the person-in-context correlations for encoding for PHC:
    SPDC_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    SPDC_encoding_PHC_avg = (np.average(SPDC_encoding_PHC))
    # run the person-in-context correlations for encoding for PRC:
    SPDC_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    SPDC_encoding_PRC_avg = (np.average(SPDC_encoding_PRC))
    # run the person-in-context correlations for encoding for HPC:
    SPDC_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    SPDC_encoding_HPC_avg = (np.average(SPDC_encoding_HPC))
    # run the person-in-context correlations for encoding for TempPole:
    SPDC_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    SPDC_encoding_TempPole_avg = (np.average(SPDC_encoding_TempPole))
    # run the person-in-context correlations for encoding for MTG:
    SPDC_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    SPDC_encoding_MTG_avg = (np.average(SPDC_encoding_MTG))
    # run the person-in-context correlations for encoding for mPFC:
    SPDC_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    SPDC_encoding_mPFC_avg = (np.average(SPDC_encoding_mPFC))
    results_array = (SPDC_encoding_EVC_avg,SPDC_encoding_PMC_avg,SPDC_encoding_ANG_avg,SPDC_encoding_PHC_avg,SPDC_encoding_PRC_avg,SPDC_encoding_HPC_avg,SPDC_encoding_TempPole_avg,SPDC_encoding_MTG_avg,SPDC_encoding_mPFC_avg)
    SPDC_CorrCoef.append(results_array)
    
    
    ### DIFFERENT-PERSON-SAME-CONTEXT DATA ###
    
    # set up empty lists
    DPSC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])

    # run the different-person-same-context correlations for encoding for EVC:
    DPSC_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_nugget_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_coop_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_EVC.append(np.arctanh(z[0][1]))
    DPSC_encoding_EVC_avg = (np.average(DPSC_encoding_EVC))
    # run the different-person-same-context correlations for encoding for PMC:
    DPSC_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_nugget_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_coop_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PMC.append(np.arctanh(z[0][1]))
    DPSC_encoding_PMC_avg = (np.average(DPSC_encoding_PMC))
    # run the different-person-same-context correlations for encoding for ANG:
    DPSC_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_nugget_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_coop_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_ANG.append(np.arctanh(z[0][1]))
    DPSC_encoding_ANG_avg = (np.average(DPSC_encoding_ANG))
    # run the different-person-same-context correlations for encoding for PHC:
    DPSC_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_nugget_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_coop_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PHC.append(np.arctanh(z[0][1]))
    DPSC_encoding_PHC_avg = (np.average(DPSC_encoding_PHC))
    # run the different-person-same-context correlations for encoding for PRC:
    DPSC_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_nugget_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_coop_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_PRC.append(np.arctanh(z[0][1]))
    DPSC_encoding_PRC_avg = (np.average(DPSC_encoding_PRC))
    # run the different-person-same-context correlations for encoding for HPC:
    DPSC_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_nugget_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_coop_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_HPC.append(np.arctanh(z[0][1]))
    DPSC_encoding_HPC_avg = (np.average(DPSC_encoding_HPC))
    # run the different-person-same-context correlations for encoding for TempPole:
    DPSC_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_coop_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_TempPole.append(np.arctanh(z[0][1]))
    DPSC_encoding_TempPole_avg = (np.average(DPSC_encoding_TempPole))
    # run the different-person-same-context correlations for encoding for MTG:
    DPSC_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_nugget_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_coop_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_MTG.append(np.arctanh(z[0][1]))
    DPSC_encoding_MTG_avg = (np.average(DPSC_encoding_MTG))
    # run the different-person-same-context correlations for encoding for mPFC:
    DPSC_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_coop_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSC_encoding_mPFC.append(np.arctanh(z[0][1]))
    DPSC_encoding_mPFC_avg = (np.average(DPSC_encoding_mPFC))
    results_array = (DPSC_encoding_EVC_avg,DPSC_encoding_PMC_avg,DPSC_encoding_ANG_avg,DPSC_encoding_PHC_avg,DPSC_encoding_PRC_avg,DPSC_encoding_HPC_avg,DPSC_encoding_TempPole_avg,DPSC_encoding_MTG_avg,DPSC_encoding_mPFC_avg)
    DPSC_CorrCoef.append(results_array)


    ### DIFFERENT-PERSON-DIFFERENT-CONTEXT DATA ###
    
    # set up empty lists
    DPDC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])

    # run the different-person-different-context correlations for encoding for EVC:
    DPDC_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_EVC.append(np.arctanh(z[0][1]))
    DPDC_encoding_EVC_avg = (np.average(DPDC_encoding_EVC))
    # run the different-person-different-context correlations for encoding for PMC:
    DPDC_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PMC.append(np.arctanh(z[0][1]))
    DPDC_encoding_PMC_avg = (np.average(DPDC_encoding_PMC))
    # run the different-person-different-context correlations for encoding for ANG:
    DPDC_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_ANG.append(np.arctanh(z[0][1]))
    DPDC_encoding_ANG_avg = (np.average(DPDC_encoding_ANG))
    # run the different-person-different-context correlations for encoding for PHC:
    DPDC_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PHC.append(np.arctanh(z[0][1]))
    DPDC_encoding_PHC_avg = (np.average(DPDC_encoding_PHC))
    # run the different-person-different-context correlations for encoding for PRC:
    DPDC_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_PRC.append(np.arctanh(z[0][1]))
    DPDC_encoding_PRC_avg = (np.average(DPDC_encoding_PRC))
    # run the different-person-different-context correlations for encoding for HPC:
    DPDC_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_HPC.append(np.arctanh(z[0][1]))
    DPDC_encoding_HPC_avg = (np.average(DPDC_encoding_HPC))
    # run the different-person-different-context correlations for encoding for TempPole:
    DPDC_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_TempPole.append(np.arctanh(z[0][1]))
    DPDC_encoding_TempPole_avg = (np.average(DPDC_encoding_TempPole))
    # run the different-person-different-context correlations for encoding for MTG:
    DPDC_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_MTG.append(np.arctanh(z[0][1]))
    DPDC_encoding_MTG_avg = (np.average(DPDC_encoding_MTG))
    # run the different-person-different-context correlations for encoding for mPFC:
    DPDC_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPDC_encoding_mPFC.append(np.arctanh(z[0][1]))
    DPDC_encoding_mPFC_avg = (np.average(DPDC_encoding_mPFC))
    results_array = (DPDC_encoding_EVC_avg,DPDC_encoding_PMC_avg,DPDC_encoding_ANG_avg,DPDC_encoding_PHC_avg,DPDC_encoding_PRC_avg,DPDC_encoding_HPC_avg,DPDC_encoding_TempPole_avg,DPDC_encoding_MTG_avg,DPDC_encoding_mPFC_avg)
    DPDC_CorrCoef.append(results_array)
    

    ### SAME-PERSON-SIMILAR-CONTEXT DATA ###
    # set up empty lists as local variables (later fed into global lists)
    SPSimC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])
    
    # run the person-in-context correlations for encoding for EVC:
    SPSimC_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_EVC_avg = (np.average(SPSimC_encoding_EVC))
    # run the person-in-context correlations for encoding for PMC:
    SPSimC_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_PMC_avg = (np.average(SPSimC_encoding_PMC))
    # run the person-in-context correlations for encoding for ANG:
    SPSimC_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    SPSimC_encoding_ANG_avg = (np.average(SPSimC_encoding_ANG))
    # run the person-in-context correlations for encoding for PHC:
    SPSimC_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_PHC_avg = (np.average(SPSimC_encoding_PHC))
    # run the person-in-context correlations for encoding for PRC:
    SPSimC_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_PRC_avg = (np.average(SPSimC_encoding_PRC))
    # run the person-in-context correlations for encoding for HPC:
    SPSimC_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_HPC_avg = (np.average(SPSimC_encoding_HPC))
    # run the person-in-context correlations for encoding for TempPole:
    SPSimC_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    SPSimC_encoding_TempPole_avg = (np.average(SPSimC_encoding_TempPole))
    # run the person-in-context correlations for encoding for MTG:
    SPSimC_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    SPSimC_encoding_MTG_avg = (np.average(SPSimC_encoding_MTG))
    # run the person-in-context correlations for encoding for mPFC:
    SPSimC_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_lisa_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video2_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_lisa_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    SPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    SPSimC_encoding_mPFC_avg = (np.average(SPSimC_encoding_mPFC))
    results_array = (SPSimC_encoding_EVC_avg,SPSimC_encoding_PMC_avg,SPSimC_encoding_ANG_avg,SPSimC_encoding_PHC_avg,SPSimC_encoding_PRC_avg,SPSimC_encoding_HPC_avg,SPSimC_encoding_TempPole_avg,SPSimC_encoding_MTG_avg,SPSimC_encoding_mPFC_avg)
    SPSimC_CorrCoef.append(results_array)
    
    
    ### DIFFERENT-PERSON-SIMILAR-CONTEXT DATA ###
    # set up empty lists as local variables (later fed into global lists)
    DPSimC_encoding_results = pd.DataFrame(columns=['Subject', 'Region', 'z_Corr'])
    
    # run the person-in-context correlations for encoding for EVC:
    DPSimC_encoding_EVC = []
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    y = all_data["EVC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_tommy_delta_betas.csv"]
    y = all_data["EVC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_mishkas_betas.csv"]
    y = all_data["EVC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_delta_betas.csv"]
    y = all_data["EVC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_coop_betas.csv"]
    y = all_data["EVC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video1_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    x = all_data["EVC_video2_lisa_nugget_betas.csv"]
    y = all_data["EVC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_EVC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_EVC_avg = (np.average(DPSimC_encoding_EVC))
    # run the person-in-context correlations for encoding for PMC:
    DPSimC_encoding_PMC = []
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PMC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_tommy_delta_betas.csv"]
    y = all_data["PMC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PMC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_delta_betas.csv"]
    y = all_data["PMC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_coop_betas.csv"]
    y = all_data["PMC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video1_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    x = all_data["PMC_video2_lisa_nugget_betas.csv"]
    y = all_data["PMC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PMC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_PMC_avg = (np.average(DPSimC_encoding_PMC))
    # run the person-in-context correlations for encoding for ANG:
    DPSimC_encoding_ANG = []
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    y = all_data["ANG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_tommy_delta_betas.csv"]
    y = all_data["ANG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_mishkas_betas.csv"]
    y = all_data["ANG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_delta_betas.csv"]
    y = all_data["ANG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_coop_betas.csv"]
    y = all_data["ANG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video1_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    x = all_data["ANG_video2_lisa_nugget_betas.csv"]
    y = all_data["ANG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_ANG.append(np.arctanh(z[0][1]))
    DPSimC_encoding_ANG_avg = (np.average(DPSimC_encoding_ANG))
    # run the person-in-context correlations for encoding for PHC:
    DPSimC_encoding_PHC = []
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PHC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_tommy_delta_betas.csv"]
    y = all_data["PHC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PHC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_delta_betas.csv"]
    y = all_data["PHC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_coop_betas.csv"]
    y = all_data["PHC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video1_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    x = all_data["PHC_video2_lisa_nugget_betas.csv"]
    y = all_data["PHC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PHC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_PHC_avg = (np.average(DPSimC_encoding_PHC))
    # run the person-in-context correlations for encoding for PRC:
    DPSimC_encoding_PRC = []
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    y = all_data["PRC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_tommy_delta_betas.csv"]
    y = all_data["PRC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_mishkas_betas.csv"]
    y = all_data["PRC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_delta_betas.csv"]
    y = all_data["PRC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_coop_betas.csv"]
    y = all_data["PRC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video1_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    x = all_data["PRC_video2_lisa_nugget_betas.csv"]
    y = all_data["PRC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_PRC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_PRC_avg = (np.average(DPSimC_encoding_PRC))
    # run the person-in-context correlations for encoding for HPC:
    DPSimC_encoding_HPC = []
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    y = all_data["HPC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_tommy_delta_betas.csv"]
    y = all_data["HPC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_mishkas_betas.csv"]
    y = all_data["HPC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_delta_betas.csv"]
    y = all_data["HPC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_coop_betas.csv"]
    y = all_data["HPC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video1_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    x = all_data["HPC_video2_lisa_nugget_betas.csv"]
    y = all_data["HPC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_HPC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_HPC_avg = (np.average(DPSimC_encoding_HPC))
    # run the person-in-context correlations for encoding for TempPole:
    DPSimC_encoding_TempPole = []
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    y = all_data["TempPole_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_tommy_delta_betas.csv"]
    y = all_data["TempPole_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_mishkas_betas.csv"]
    y = all_data["TempPole_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_delta_betas.csv"]
    y = all_data["TempPole_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_coop_betas.csv"]
    y = all_data["TempPole_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video1_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    x = all_data["TempPole_video2_lisa_nugget_betas.csv"]
    y = all_data["TempPole_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_TempPole.append(np.arctanh(z[0][1]))
    DPSimC_encoding_TempPole_avg = (np.average(DPSimC_encoding_TempPole))
    # run the person-in-context correlations for encoding for MTG:
    DPSimC_encoding_MTG = []
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    y = all_data["MTG_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_tommy_delta_betas.csv"]
    y = all_data["MTG_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_mishkas_betas.csv"]
    y = all_data["MTG_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_delta_betas.csv"]
    y = all_data["MTG_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_coop_betas.csv"]
    y = all_data["MTG_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video1_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    x = all_data["MTG_video2_lisa_nugget_betas.csv"]
    y = all_data["MTG_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_MTG.append(np.arctanh(z[0][1]))
    DPSimC_encoding_MTG_avg = (np.average(DPSimC_encoding_MTG))
    # run the person-in-context correlations for encoding for mPFC:
    DPSimC_encoding_mPFC = []
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video2_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    y = all_data["mPFC_video3_lisa_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_tommy_delta_betas.csv"]
    y = all_data["mPFC_video3_lisa_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video2_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_mishkas_betas.csv"]
    y = all_data["mPFC_video3_tommy_delta_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video2_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_delta_betas.csv"]
    y = all_data["mPFC_video3_tommy_mishkas_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video2_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_coop_betas.csv"]
    y = all_data["mPFC_video3_tommy_nugget_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video2_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video1_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    x = all_data["mPFC_video2_lisa_nugget_betas.csv"]
    y = all_data["mPFC_video3_tommy_coop_betas.csv"]
    z = (np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y)))
    DPSimC_encoding_mPFC.append(np.arctanh(z[0][1]))
    DPSimC_encoding_mPFC_avg = (np.average(DPSimC_encoding_mPFC))
    results_array = (DPSimC_encoding_EVC_avg,DPSimC_encoding_PMC_avg,DPSimC_encoding_ANG_avg,DPSimC_encoding_PHC_avg,DPSimC_encoding_PRC_avg,DPSimC_encoding_HPC_avg,DPSimC_encoding_TempPole_avg,DPSimC_encoding_MTG_avg,DPSimC_encoding_mPFC_avg)
    DPSimC_CorrCoef.append(results_array)
    
# make a person-in-context results dataframe
PIC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in PIC_CorrCoef:
    PIC_CorrCoef_merged += i
all_PIC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':PIC_CorrCoef_merged})
all_PIC_results_pivoted = all_PIC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# make a same-person-different-context results dataframe
SPDC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in SPDC_CorrCoef:
    SPDC_CorrCoef_merged += i
all_SPDC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':SPDC_CorrCoef_merged})
all_SPDC_results_pivoted = all_SPDC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# make a different-person-same-context results dataframe
DPSC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in DPSC_CorrCoef:
    DPSC_CorrCoef_merged += i
all_DPSC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':DPSC_CorrCoef_merged})
all_DPSC_results_pivoted = all_DPSC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# make a different-person-different-context results dataframe
DPDC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in DPDC_CorrCoef:
    DPDC_CorrCoef_merged += i
all_DPDC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':DPDC_CorrCoef_merged})
all_DPDC_results_pivoted = all_DPDC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# make a same-person-similar-context results dataframe
SPSimC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in SPSimC_CorrCoef:
    SPSimC_CorrCoef_merged += i
all_SPSimC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':SPSimC_CorrCoef_merged})
all_SPSimC_results_pivoted = all_SPSimC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# make a different-person-similar-context results dataframe
DPSimC_CorrCoef_merged = []
subject_vec = []
subject_vec_merged = []
for i in subjects:
    subject_vec.append([i]*len(regions))
for i in subject_vec:
    subject_vec_merged += i
for i in DPSimC_CorrCoef:
    DPSimC_CorrCoef_merged += i
all_DPSimC_results = pd.DataFrame({'Subjects':subject_vec_merged, 'Region':regions*len(subjects), 'z_Corr':DPSimC_CorrCoef_merged})
all_DPSimC_results_pivoted = all_DPSimC_results.pivot(index='Subjects', columns='Region', values='z_Corr')

# combine the data frames by region
EVC_encoding_final = pd.concat([all_PIC_results_pivoted['EVC'],all_DPSC_results_pivoted['EVC'],all_SPSimC_results_pivoted['EVC'],all_DPSimC_results_pivoted['EVC'],all_SPDC_results_pivoted['EVC'],all_DPDC_results_pivoted['EVC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
PMC_encoding_final = pd.concat([all_PIC_results_pivoted['PMC'],all_DPSC_results_pivoted['PMC'],all_SPSimC_results_pivoted['PMC'],all_DPSimC_results_pivoted['PMC'],all_SPDC_results_pivoted['PMC'],all_DPDC_results_pivoted['PMC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
ANG_encoding_final = pd.concat([all_PIC_results_pivoted['ANG'],all_DPSC_results_pivoted['ANG'],all_SPSimC_results_pivoted['ANG'],all_DPSimC_results_pivoted['ANG'],all_SPDC_results_pivoted['ANG'],all_DPDC_results_pivoted['ANG']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
PHC_encoding_final = pd.concat([all_PIC_results_pivoted['PHC'],all_DPSC_results_pivoted['PHC'],all_SPSimC_results_pivoted['PHC'],all_DPSimC_results_pivoted['PHC'],all_SPDC_results_pivoted['PHC'],all_DPDC_results_pivoted['PHC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
PRC_encoding_final = pd.concat([all_PIC_results_pivoted['PRC'],all_DPSC_results_pivoted['PRC'],all_SPSimC_results_pivoted['PRC'],all_DPSimC_results_pivoted['PRC'],all_SPDC_results_pivoted['PRC'],all_DPDC_results_pivoted['PRC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
HPC_encoding_final = pd.concat([all_PIC_results_pivoted['HPC'],all_DPSC_results_pivoted['HPC'],all_SPSimC_results_pivoted['HPC'],all_DPSimC_results_pivoted['HPC'],all_SPDC_results_pivoted['HPC'],all_DPDC_results_pivoted['HPC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
TempPole_encoding_final = pd.concat([all_PIC_results_pivoted['TempPole'],all_DPSC_results_pivoted['TempPole'],all_SPSimC_results_pivoted['TempPole'],all_DPSimC_results_pivoted['TempPole'],all_SPDC_results_pivoted['TempPole'],all_DPDC_results_pivoted['TempPole']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
MTG_encoding_final = pd.concat([all_PIC_results_pivoted['MTG'],all_DPSC_results_pivoted['MTG'],all_SPSimC_results_pivoted['MTG'],all_DPSimC_results_pivoted['MTG'],all_SPDC_results_pivoted['MTG'],all_DPDC_results_pivoted['MTG']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])
mPFC_encoding_final = pd.concat([all_PIC_results_pivoted['mPFC'],all_DPSC_results_pivoted['mPFC'],all_SPSimC_results_pivoted['mPFC'],all_DPSimC_results_pivoted['mPFC'],all_SPDC_results_pivoted['mPFC'],all_DPDC_results_pivoted['mPFC']], axis=1, keys=['SPSC', 'DPSC','SPSimC','DPSimC','SPDC','DPDC'])

# stack the data frames to long-format, if needed
EVC_encoding_long = EVC_encoding_final.stack().reset_index()
EVC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
PMC_encoding_long = PMC_encoding_final.stack().reset_index()
PMC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
ANG_encoding_long = ANG_encoding_final.stack().reset_index()
ANG_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
PHC_encoding_long = PHC_encoding_final.stack().reset_index()
PHC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
PRC_encoding_long = PRC_encoding_final.stack().reset_index()
PRC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
HPC_encoding_long = HPC_encoding_final.stack().reset_index()
HPC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
TempPole_encoding_long = TempPole_encoding_final.stack().reset_index()
TempPole_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
MTG_encoding_long = MTG_encoding_final.stack().reset_index()
MTG_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']
mPFC_encoding_long = mPFC_encoding_final.stack().reset_index()
mPFC_encoding_long.columns = ['Subject', 'Condition', 'z_Corr']

# make a final encoding results DF for plotting and 2-way ANOVAs
final_encoding_results_df = pd.DataFrame(columns=['Subject', 'Person', 'Context', 'EVC', 'PMC', 'ANG', 'PHC', 'PRC', 'HPC', 'TempPole', 'MTG', 'mPFC'])
subject_vec = EVC_encoding_long['Subject']
person_vec = (['Same','Different'] * 60)
context_vec = (['Same','Same','Similar','Similar','Different','Different'] * 20)
final_encoding_results_df['Person'] = person_vec
final_encoding_results_df['Context'] = context_vec
final_encoding_results_df['Subject'] = EVC_encoding_long['Subject']
final_encoding_results_df['EVC'] = EVC_encoding_long['z_Corr']
final_encoding_results_df['PMC'] = PMC_encoding_long['z_Corr']
final_encoding_results_df['ANG'] = ANG_encoding_long['z_Corr']
final_encoding_results_df['PHC'] = PHC_encoding_long['z_Corr']
final_encoding_results_df['PRC'] = PRC_encoding_long['z_Corr']
final_encoding_results_df['HPC'] = HPC_encoding_long['z_Corr']
final_encoding_results_df['TempPole'] = TempPole_encoding_long['z_Corr']
final_encoding_results_df['MTG'] = MTG_encoding_long['z_Corr']
final_encoding_results_df['mPFC'] = mPFC_encoding_long['z_Corr']

# plot and analyze
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
#from statsmodels.stats.anova import AnovaRM
from statsmodels.stats import multicomp
from scipy import stats
import seaborn as sns
#import scikit_posthocs as sp
import matplotlib.pyplot as plt

regions = ['EVC','PMC','ANG','PHC','PRC','HPC','TempPole','MTG','mPFC']

for region in regions:
    
    sns.set(style="ticks",context=("poster"),font_scale=1.25)
    fig, ax = plt.subplots()
    fig.set_size_inches(8,8)
    #ax.set_ylim(0.0,0.09)
    
    #BARPLOT VERSION
    fig = sns.barplot(x="Context", y=region, hue='Person', data=final_encoding_results_df, capsize=.1, ci=68, palette="colorblind")
    #fig = sns.boxplot(x="Context", y=region, hue='Person', data=final_encoding_results_df, palette="colorblind")
    fig = sns.swarmplot(x="Context", y=region, dodge=True, hue='Person', data=final_encoding_results_df, size=8, color="k", alpha=.5)
    #leg = fig.axes.flat[0].get_legend()
    plt.title("{} Across Task Conditions".format(region))
    plt.ylabel("Pattern Similarity (z)")
    plt.xlabel("Context")
    plt.tight_layout()
    ax.legend_.remove()
    plt.savefig('{}_plot.pdf'.format(region))
    
    def omega_squared(aov):
        mse = aov['sum_sq'][-1]/aov['df'][-1]
        aov['omega_sq'] = 'NaN'
        aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*mse))/(sum(aov['sum_sq'])+mse)
        return aov
    
    formula = '{} ~ Context + Person + Context:Person'.format(region)
    model = ols(formula, final_encoding_results_df).fit()
    aov_table = anova_lm(model, typ=3)
    omega_squared(aov_table)
    print("2-way ANOVA for {}:".format(region))
    print(aov_table)
    
    # Repeated measures ANOVA
    #aovrm2way = AnovaRM(final_encoding_results_df, '{}'.format(region), 'Subject', within=['Person', 'Context'])
    #res2way = aovrm2way.fit()
    #print(res2way)
    
    print("\nPairwise contrasts for {}:".format(region))
    
    # Tukey
    #print(multicomp.pairwise_tukeyhsd(PHC_encoding_long["z_Corr"], PHC_encoding_long["Condition"], alpha=0.05))
    
    # Holm
    pairwise_comps = multicomp.MultiComparison(PHC_encoding_long["z_Corr"], PHC_encoding_long["Condition"])
    pairwise_comps_stats = pairwise_comps.allpairtest(stats.ttest_rel, method='Holm')
    print(pairwise_comps_stats[0])
    
    with open('{}_stats_output.txt'.format(region), 'w') as f:
        print('{} ANOVA:\n'.format(region), aov_table, file=f)
        print('\n',pairwise_comps_stats[0], file=f)
    
    # Scheffe
    #sp.posthoc_scheffe(HPC_encoding_long, val_col='z_Corr', group_col='Condition')
    
    #region="mPFC"
    #sns.set(style="ticks",context=("poster"),font_scale=1.25)
    #fig, ax = plt.subplots()
    #fig.set_size_inches(8,8)
    #
    ##POINTPLOT VERSION
    #strip = sns.stripplot(x="Context", y=region, hue='Person', data=final_encoding_results_df,
    #                   palette="gray", dodge=0.25, jitter=0.05, ax=ax,
    #                   size=8)
    #point = sns.pointplot(x="Context", y=region, hue='Person', data=final_encoding_results_df, ci=68,
    #                   palette="colorblind", dodge=0.35, join=False, ax=ax, 
    #                   errwidth=5, capsize=0.2, scale=1.25)
    #plt.title("Perirhinal Cortex at Recall".format(region))
    #plt.ylabel("Pattern Similarity (z)")
    #plt.xlabel("Context")
    #handles, _ = ax.get_legend_handles_labels()
    #plt.legend(loc='lower left')
    #ax.legend_.remove()
    
    
    
    ########## DEPRECATED #############
    
    ##with sns.axes_style(style='ticks'):
    ##    g = sns.factorplot("z_Corr", "Region", data=all_SPSimC_results, kind="box")
    ##    g.set_axis_labels("z_Corr", "Region");
    #    
    ##with sns.axes_style(style='ticks'):
    ##    g = sns.swarmplot("Condition", "z_Corr", data=HPC_encoding_final)
    ##    g.set_axis_labels("Condition", "z_Corr");
    #    
    #import matplotlib.pyplot as plt
    #
    #sns.barplot(x="Condition", y="z_Corr", data=HPC_encoding_final, capsize=.1, ci=68 , palette="colorblind")
    #sns.swarmplot(x="Condition", y="z_Corr", data=HPC_encoding_final, color="0", alpha=.35)
    #
    #plt.show()
    #
    #
    #import statsmodels.api as sm
    #from statsmodels.formula.api import ols
    # 
    #mod = ols('z_Corr ~ Condition',
    #                data=HPC_encoding_final).fit()
    #                
    #aov_table = sm.stats.anova_lm(mod, typ=2)
    #print(aov_table)