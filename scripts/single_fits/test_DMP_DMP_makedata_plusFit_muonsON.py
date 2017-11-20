

import os, sys
#modules_dir = '/home/trwood/JP_fraction_original_jan26_test/modules'
modules_dir = '/gs/project/ngw-282-ac/trwood/jasper_home/JP_fraction_original_jan26_test_lessbins/modules'
#modules_dir = '/project/d/dgrant/trwood/jasper_home/JP_fraction_original_jan26_test_lessbins/modules'
sys.path.append(modules_dir)


# Importing modules
import argparse
import math
import pickle
import dataLoader
import numpy as np
import oscfit_default_values as defs
from copy import deepcopy
import jp_mpl as jplot

import oscFit_JP as oscFit


#HERE USING TRUE_axis_Mu_8, E5, but changed the names bc am lazy. need to change the dataloading here into loops.  THIS WEEKD?
#true_axis_mu9 = np.array([[0., 8.],[8., 15.], [15., 25.],[25., 40.], [40.,70.], [70., 120.], [120., 180.], [180., 1000.]])
#true_axis_e4  = np.array( [ [0., 9.], [9., 15.], [15., 30.],[30., 70.], [70.,1000.]])

true_axis_mu9 = np.array([[0., 8.],[8., 15.], [15., 25.],[25., 40.], [40.,70.], [70., 120.], [120., 180.], [180., 1000.]])

true_axis_e4  = np.array( [ [0., 9.], [9., 15.], [15., 30.],[30., 70.], [70.,1000.]])

sysfile_use = '/gs/project/ngw-282-ac/trwood/jasper_home/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematicstA_lowchiBAK.pckl'


#sysfile_use ='/gs/project/ngw-282-ac/trwood/jasper_home/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematicstABC_gil_nov10_EPOS.pckl'
#sysfile_use = '/home/d/dgrant/trwood/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematicstA_lowchiBAK.pckl'
#sysfile_use ='/project/d/dgrant/trwood/jasper_home/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematics_gpc.pckl'

#true_axis_mu9 = np.array([[0., 6.],[6., 10.], [10., 15.], [15., 25.],[25., 40.], [40., 63.], [63., 100.], [100., 160.], [160., 1000.]])
#true_axis_e4  = np.array( [ [0., 7.], [7., 15.], [15., 30.], [30.,1000.]])
#true_axis_e6  = np.array( [ [0., 7.], [7., 15.], [15., 30.], [30.,50.],[50.,70. ], [70.,1000.]  ])

#####
# NEUTRINOS ONLY LOADERS
#####

### NUMU

print '\n\nLoader A'
loader_nobkrd_a = dataLoader.dataLoader(observables =
      ['reco_energy', 'reco_zenith', 'delta_llh'],
      bin_edges   =
      #no events below 10GeV so start binning at 1
      #smarter way cut out the frist 3 bins.  
      #retain the same binning but get rid of below 10GeV
      #was 10**np.linspace([0.75,1.25,2])
      [10**np.linspace(0.75,2.25,11),
	 np.arccos(np.linspace(-1.,1.,9))[::-1],
	 np.array([-3, 2, np.inf])],	

      user = 'Chi2msu_no_background_noData_baselineONLY_flat_uncontained_numu',

      LEaxis = [],#np.linspace(1, 3.2, 21),      
      detsys_nuspecs = {},
      detsys_muspecs = {},
      #weight_keys = ['tweight_newflat_e', 'tweight_newflat_mu_k', 'tweight_newflat_mu_p'],
      #WHY WOULD JP USE THESE INSTEAD OF THE FLAT WEIGHTS HERE?? MC SHOULD HAVE FLAT >>>
      # weight_keys = ['tweight_e', 'tweight_mu_k', 'tweight_mu_p'],
      weight_keys = ['tweight_DMP_GH_flat_e_jaspert', 'tweight_DMP_GH_flat_mu_k_jaspert','tweight_DMP_GH_flat_mu_p_jaspert'],
      extra_cuts = {'energy':true_axis_mu9[0]},
      detsys_redo = False,
      verbose = False,
      table_nbins = -1,
      #   sysfile = '/gs/project/ngw-282-ac/trwood/jasper_home/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematicstA.pckl')
      sysfile = sysfile_use)
#sysfile = '/home/trwood/pbs_submit/Andreis_daydream_for_Tests/DRAGON_detector_systematicstA.pckl')


# make a fully new copy of loader_dict, ie don't just copy the location of the pointer
from copy import deepcopy
loader_dict_numu = deepcopy(loader_nobkrd_a.iniDict)

print '\n\nLoader B'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[1]}
loader_nobkrd_b= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader C'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[2]}
loader_nobkrd_c= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader D'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[3]}
loader_nobkrd_d= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader E'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[4]}
loader_nobkrd_e= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader F'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[5]}
loader_nobkrd_f= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader G'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[6]}
loader_nobkrd_g= dataLoader.dataLoader(**loader_dict_numu)

print '\n\nLoader H'
loader_dict_numu['extra_cuts'] =  {'energy':true_axis_mu9[7]}
loader_nobkrd_h= dataLoader.dataLoader(**loader_dict_numu)



###   NU E Loaders only 
print '\n\nLoader I'
loader_dict_nue = deepcopy(loader_dict_numu)
loader_dict_nue['user'] = 'Chi2msu_no_background_noData_baselineONLY_flat_uncontained_nue'
loader_dict_nue['extra_cuts'] = {'energy':true_axis_e4[0]}
loader_nobkrd_i = dataLoader.dataLoader(**loader_dict_nue)

print '\n\nLoader J'
loader_dict_nue['extra_cuts'] =  {'energy':true_axis_e4[1]}
loader_nobkrd_j= dataLoader.dataLoader(**loader_dict_nue)

print '\n\nLoader K'
loader_dict_nue['extra_cuts'] =  {'energy':true_axis_e4[2]}
loader_nobkrd_k= dataLoader.dataLoader(**loader_dict_nue)

print '\n\nLoader L'
loader_dict_nue['extra_cuts'] =  {'energy':true_axis_e4[3]}
loader_nobkrd_l= dataLoader.dataLoader(**loader_dict_nue)

print '\n\nLoader M'
loader_dict_nue['extra_cuts'] =  {'energy':true_axis_e4[4]}
loader_nobkrd_m= dataLoader.dataLoader(**loader_dict_nue)


##
# ATMOSPHERIC MUONS ONLY LOADER
##

loader_dict_atmos = deepcopy(loader_dict_numu)
loader_dict_atmos['extra_cuts'] =  {}
loader_dict_atmos['user'] = 'Chi2msu_BKGRND_only_flat_uncontained'
loader_pureBkrd = dataLoader.dataLoader(**loader_dict_atmos)


###i###data_histo_bkrd_PlusNu = pickle.load(open('/home/d/dgrant/trwood/pbs_submit/FractionForwdFold/tw_scripts/Checks_Binning_Berlin/DRAGON_pseudoset_flux_001a_DPM_GH_sysA.pckl'))

#########
## LOADING THE DATA
#########

data_hist = pickle.load(open('/home/trwood/pbs_submit/FractionForwdFold/tw_scripts/Checks_Binning_Berlin/DRAGON_pseudoset_flux_001a_DPM_GH_sysA.pckl')) #DRAGON_pseudoset_flux_001a_DPM_GH_0GeVStartTrue_jasper85.pckl'))


#start_fractions_numu        = pickle.load(open('/home/trwood/pbs_submit/FractionForwdFold/DRAGON_fractions_guess_a.pckl')) 

#start_fractions_numu = pickle.load(open('/home/trwood/pbs_submit/FractionForwdFold/tw_scripts/Checks_Binning_Berlin/DRAGON_fractions_guess_a_mu8_DPM_GH_sysA.pckl')) #DRAGON_fractions_guess_a_mu8_DPM_GH_0GeVStartTrue_jasper.pckl'))
#start_fractions_nue  = pickle.load(open('/home/trwood/pbs_submit/FractionForwdFold/tw_scripts/Checks_Binning_Berlin/DRAGON_fractions_guess_a_e5_DPM_GH_sysA.pckl')) #DRAGON_fractions_guess_a_e5_DPM_GH_0GeVStartTrue_jasper.pckl'))
#print 'Start fractions\n', start_fractions_numu
#print 'Start fractions\n', start_fractions_nue


#start_fractions_nue = np.array([ 0.051,  0.046,  0.058,  0.03,   0.008])

#start_fractions_numu = np.array([ 0.15,   0.217,  0.166,  0.118,  0.088,  0.045,  0.015,  0.008])

#print 'Start fractions\n', start_fractions_numu
#print 'Start fractions\n', start_fractions_nue

####################################
##  CREATE the data now instead and clalcuate the fractinos now ... this needs to MACtch!
####################################



loader = dataLoader.dataLoader(observables =
      ['reco_energy', 'reco_zenith', 'delta_llh'],
      bin_edges   = [10**np.linspace(0.75,2.25,11),
	 np.arccos(np.linspace(-1.,1.,9))[::-1],
	 np.array([-3, 2, np.inf])],
      user = 'Chi2msu_no_background_noData_baselineONLY_flat_uncontained_mus', 
      LEaxis = [],
      detsys_nuspecs = {},
      detsys_muspecs = {},
      weight_keys = ['tweight_DMP_GH_e_jaspert', 'tweight_DMP_GH_mu_k_jaspert', 'tweight_DMP_GH_mu_p_jaspert'],
      detsys_redo = False,
      sysfile = sysfile_use,
      verbose = False, # # Never again set to true. It dumps SO MUCH GARBAGE
      table_nbins = -1)


#the data settings
data_settings = {
      'dm31':                  0.0025,
      'theta23':                  0.74,
      'theta13':                  0.155,
      'mix_angle':                1.,
      'norm_tau':                 1.,
      'axm_qe':                   0.,
      'axm_res':                  0.,
      'norm_nu':                  3.02, # In years!
      'norm_e':                   1.,
      'domeff':                   1.,
      'nu_pi_scale':              1.,
      'hole_ice':                 0.02,
      'atmmu_template':           'data',
      'simulation':               'baseline',
      'oscTables':                False,
      'gamma':                    0.,
      'ma_variations':            False,
      'add_detector_systematics': False,
      #'norm_atmmu':                0.4,               <----- run w this instead 
      # 'pid_bias':                 0.,
      'hi_fwd':                   0., # MSU parameterization of the forward impact angle
      'had_escale':               1.,
      'oscMode':                  'TwoNeutrino',
      'ma_variations':            False,
      'norm_noise':                0.0,
      'atmmu_f':                  0.05  }   #  <------------------------------------ causes nans

####################  
# try re-normalizing to correct norm_Nu basically ... 
###########################

data_hist2 = loader.loadMCasData(data_settings, statistical_fluctuations=False)
#data_hist2 = deepcopy(original_data)
#print np.sum(data_hist2)
# Scaling the data to the observed events in the sample (with containment cut)
#msu_observed = 41599.
#data_hist *= msu_observed/np.sum(data_hist)
#print 'Events in data', np.sum(data_hist2)
'''

######################
# checks !
##########################
# Check that TANIA can reproduce her own data (duh!)
#data_to_data = data_histo_bkrd_PlusNu/data_hist
#print 'Mean', data_to_data.mean()
print 'Panic if its not EXACTLY one'


#################################
## Calculate the fractions.. shoudl we really do this again and again? means twice the loaders i think ... soooo
## still it is cleaner and less time then the fit .... (But a lot) .. minutes to hours. let's do it. 
#################################

#IN CASE I HAVE to calculate the fractions right meow 
'''
split_full_histo = np.zeros_like(data_hist2)
split_data = []

loader_dict = deepcopy(loader.iniDict)
split_data = []
loader_dict['user'] = 'Chi2msu_no_background_noData_baselineONLY_flat_uncontained_numu'
for one_axis in true_axis_mu9:
   loader_dict['extra_cuts'] = {'energy':one_axis}
   new_loader = dataLoader.dataLoader(**loader_dict)
   this_data = new_loader.loadMCasData(data_settings)
   split_full_histo += this_data
   split_data.append(np.sum(this_data))

#split_data = np.array(split_data)
#fractions_numu = split_data/np.sum(split_data) #pickle.dump(fractions_numu, open('DRAGON_fractions_guess_a_mu.pckl', 'w'))
		       #######################
loader_dict_e = deepcopy(loader.iniDict)
split_data_e = []
loader_dict_e['user'] = 'Chi2msu_no_background_noData_baselineONLY_flat_uncontained_nue'
for one_axisE in true_axis_e4:
   loader_dict_e['extra_cuts'] = {'energy':one_axisE}
   new_loader_e = dataLoader.dataLoader(**loader_dict_e)
   this_data = new_loader_e.loadMCasData(data_settings)
   split_full_histo += this_data
   split_data_e.append(np.sum(this_data))
   

split_data = np.array(split_data)

split_data_e = np.array(split_data_e)
print 'split data nue'
print split_data_e
fractions_numu = split_data/( np.sum(split_data) + np.sum(split_data_e) )
fractions_e = split_data_e/( np.sum(split_data) + np.sum(split_data_e))


print 'split data numu'
print split_data

####
## Verify that the fractions and the data sum up to the same
####

print '\n*****SUMMARY*****\n'
print 'This is the sum of split data', np.sum(split_full_histo)
#print 'Sum(abs(split-original)):', np.sum(np.abs(original_data-split_full_histo))
print 'Sum of fractions', np.sum(fractions_e) + np.sum(fractions_numu)


print '\nFractions'
print 'Nue fractions:'
print fractions_e
print 'NuMu fractions: '
print fractions_numu


start_fractions_numu = np.array(fractions_numu)
start_fractions_nue = np.array(fractions_e)

#########
##
# ATMOSPHERIC MUONS ONLY LOADER
##

#loader_dict_atmos = deepcopy(loader_dict_numu)
#loader_dict_atmos['extra_cuts'] =  {}
#loader_dict_atmos['user'] = 'Chi2msu_BKGRND_only_flat_uncontained'
#loader_pureBkrd = dataLoader.dataLoader(**loader_dict_atmos)




########
## FIT SETTINGS
########
fit_settings = deepcopy(defs.default_fit_settings)
fit_settings_fix    = {
      'simulation':     'baseline',
      'dm31':           [0.0025, False, 'NH'],
      'theta23':        [0.74, False],
      'theta13':        [0.155, False],
      'oscMode':        'TwoNeutrino',
      'oscTables':      False,         #used to be False.  need to think about the tables.  need to understand resolution to set n bins
      'norm':           [1., True],    #try once with this true and once with this false, same settings


      # These are good starting values for the realistic spectrum
      #starting values for numu
      'nu_frac1':       [start_fractions_numu[0], False],
      'nu_frac2':       [start_fractions_numu[1], False],
      'nu_frac3':       [start_fractions_numu[2], False],
      'nu_frac4':       [start_fractions_numu[3], False],
      'nu_frac5':       [start_fractions_numu[4], False],
      'nu_frac6':       [start_fractions_numu[5], False],
      'nu_frac7':       [start_fractions_numu[6], False],
      'nu_frac8':       [start_fractions_numu[7], False],
      #  'nu_frac9':       [start_fractions_numu[8], False],  #only one fraction needs to be 'not fit' to require all to be summed to one. 
      # move this burden to nue spectrum now


      #starting fractions for nue
      'nu_frac9':	       [start_fractions_nue[0], False],  
      'nu_frac10':       [start_fractions_nue[1], False],
      'nu_frac11':       [start_fractions_nue[2], False],
      'nu_frac12':       [start_fractions_nue[3], False],
      # The last fraction is not fit, but calculated


      'norm_e':         [1., True],
      'norm_tau':       [1., True],
      'nu_nubar':       [1., True],
      'nubar_ratio':    [0., True],
      'uphor_ratio':    [0., True],
      'nu_pi_scale':    [1., False],
      'hi_fwd':         [0.0, False],
      'gamma':          [0., True],
      'axm_qe':         [0., True],
      'axm_res':        [0., False],
      'pid_bias':       [0., True],
      'hole_ice':       [0.02, False],           # Fix these to true for this test???

      'mix_angle':      [1.0,False, 1.5],

      'minimizer':      'migrad', # 'SLSQP', #'migrad',

      'norm_nc':        [1., False],
      'domeff':         [1., False],
      'had_escale':     [1., True],
    'atmmu_f':        [0.05, False, 'data'],
    'noise_f':        [0.0, True],
    'detector_syst':   True,
    'include_priors': True,
    'printMode':      -1}  # (-1) this is printing each step



import iminuit
fitter = oscFit.fitOscParams()


fit_priors = {'hole_ice':[0.02, 0.01],
      #            'gamma':[0.05, 0.1],
      'norm_e':[1., 0.2]}


oscFitResults_fixed =fitter(data_histograms=[data_hist2],
      data_loaders=[loader_nobkrd_a,  #NuMu loaders
	 loader_nobkrd_b,
	 loader_nobkrd_c,
	 loader_nobkrd_d,
	 loader_nobkrd_e,
	 loader_nobkrd_f,
	 loader_nobkrd_g,
	 loader_nobkrd_h,
	 loader_nobkrd_i,
	 # nue loaders
	 loader_nobkrd_j,
	 loader_nobkrd_k,
	 loader_nobkrd_l,
	 loader_nobkrd_m,
	 loader_pureBkrd],
      fit_settings=fit_settings_fix,
      ncalls               = 8000,  # For migrad. Simplex will use twice the number.
      tol 		 = 0.01,  # condition, edm < edm_max, where edm_max = 0.0001 * tol* UP  ( UP = 1.0 chi2, -.5 llh, defalut 1.0).
      store_fit_details    = True)

pickle.dump(oscFitResults_fixed,open('/home/trwood/pbs_submit/outfiles/test_DMP_DMP_makedata_plusFit_muonsON.pckl', 'w'))

#pickle.dump(oscFitResults_fixed,open('/home/d/dgrant/trwood/pbs_submit/FractionForwdFold/tw_scripts/Checks_Binning_Berlin/one_script_checkBmod_noMuonsF.pckl', 'w'))

