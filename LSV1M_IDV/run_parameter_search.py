# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import CombinationParameterSearch,SlurmSequentialBackend
import numpy
import time

if True:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
				         'sheets.l4_cortex_exc.K' : [1000],
#				         'sheets.retina_lgn.params.noise.stdev' : [1.6,1.7],
				         'sheets.retina_lgn.params.gain_control.gain' : [8,9],
					 'sheets.l4_cortex_exc.AfferentConnection.base_weight' : [0.0015,0.0014,0.0013,0.0012],
				         }).run_parameter_search()



if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
				         'sheets.l4_cortex_exc.K' : [1480],
				         'sheets.l4_cortex_exc.params.sx' : [7000],
				         'sheets.l4_cortex_exc.params.density' : [600,700],
#				         'sheets.retina_lgn.params.gain_control.gain' : [10],
				         'sheets.retina_lgn.params.noise.stdev' : [1.5],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_E' : [7.5],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_I' : [13],
#				         'sheets.l4_cortex_exc.AfferentConnection.size' : [0.17],
					 'sheets.l4_cortex_exc.AfferentConnection.base_weight' : [0.0014],
#				         'sheets.l4_cortex_exc.layer23_aff_ratio' : [0.2],
#				         'sheets.l4_cortex_exc.AfferentConnection.aspect_ratio' : [0.4],
				         'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0009],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0021],
				         'sheets.l4_cortex_exc.L4ExcL4ExcConnection.short_term_plasticity.tau_rec' : [10],
				         'sheets.l4_cortex_exc.AfferentConnection.short_term_plasticity.tau_rec' : [150],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.tau_rec' : [15],
					 'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f3.params.arborization_scaler' : [1.0],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.weight_functions.f1.params.sigma' : [1.0,1.4,2.0],
#									     'sheets.l4_cortex_exc.L4ExcL4InhConnection.weight_functions.f1.params.sigma' : [1.4,2.0,3.0],
#				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.weight_functions.f1.params.sigma' : [1.2,1.4],
					 'sheets.l23_cortex_exc.L23ExcL4InhConnection.weight_functions.f1.params.arborization_constant' : [300],

				         }).run_parameter_search()


if False:
    CombinationParameterSearch(SlurmSequentialBackendIoV(num_threads=1,num_mpi=12),{
				         'sheets.retina_lgn.params.gain_control.gain' : [10],
				         'sheets.retina_lgn.params.noise.stdev' : [1.4,1.5],
				         }).run_parameter_search()


if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=16),{
#									     'sheets.l23_cortex_exc.L23ExcL4InhConnection.base_weight' : [0.0014],
				         'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0013,0.0014],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.003,0.0035],
#									     'sheets.l4_cortex_exc.inhibitory_connection_ratio' : [0.8],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.short_term_plasticity.tau_rec' : [100],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_E' : [2.0],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_I' : [7.0],
#									     'sheets.l4_cortex_exc.params.cell.params.e_rev_I' : [-80],
#									     'sheets.l4_cortex_exc.params.cell.params.v_reset' : [-60],
				         'sheets.l4_cortex_exc.K' : [1480],
				         'sheets.l4_cortex_exc.params.density' : [8000],
				         'sheets.l4_cortex_exc.params.sx' : [800.0,1200.0],
				         'sheets.l23_cortex_exc.feedback_conn_ratio' : [0.25],
				         'sheets.l4_cortex_exc.layer23_aff_ratio' : [0.25],
#									     'sheets.retina_lgn.params.gain_control.gain' : [50],
#									     'sheets.retina_lgn.params.gain_control.non_linear_gain.contrast_scaler' : [0.1,0.01],
#									     'sheets.l4_cortex_exc.AfferentConnection.short_term_plasticity.tau_rec' : [250],
				         'sheets.l4_cortex_exc.AfferentConnection.base_weight' : [0.001],
				         'sheets.l4_cortex_exc.L4ExcL4ExcConnection.base_weight' : [0.001],
#				        				     'sheets.retina_lgn.params.gain_control.non_linear_gain.contrast_scaler' : [0,1,10],
#				        				     'sheets.retina_lgn.params.gain_control.non_linear_gain.luminance_gain' : [0.0],
#									     'sheets.l4_cortex_exc.AfferentConnection.size' : [0.17],
#									     'sheets.l4_cortex_exc.AfferentConnection.num_samples' : [100],
#									     'sheets.l23_cortex_exc.feedback_conn_ratio' : [0.14],
				         'sheets.l4_cortex_inh.ExcInhAfferentRatio' : [0.0,0.5],
#									     'sheets.l4_cortex_inh.params.cell.params.v_thresh' : [-60],
#									     'sheets.l4_cortex_exc.params.cell.params.v_thresh' : [-60],
#									     'sheets.l4_cortex_exc.params.cell.params.v_rest' : [-71],
#									     'sheets.l23_cortex_inh.L4ExcL23InhConnection.num_samples' : [300],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.weight_functions.f1.params.sigma' : [1.4],
#									     'sheets.l4_cortex_exc.L4ExcL4InhConnection.weight_functions.f1.params.sigma' : [3.0],
#									     'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f3.params.arborization_scaler' : [0.1],
#									     'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f1.params.sigma' : [1.4],
#									     'sheets.l23_cortex_exc.L23ExcL23InhConnection.weight_functions.f1.params.sigma' : [3.0],
#				        				     'sheets.l23_cortex_inh.L4ExcL23InhConnection.weight_functions.f2.params.sigma' : [1.4,3.0],
#									     'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f1.params.sigma' : [1.0,1.4],
#									     'sheets.l23_cortex_inh.L4ExcL23InhConnection.weight_' : ["\\\'f1\\\'","\\\'f1*f2\\\'"],
#									     'sheets.l23_cortex_exc.L23ExcL4InhConnection.weight_functions.f1.params.arborization_constant' : [100],
				         }).run_parameter_search()



if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=16),{
#									     'sheets.l23_cortex_exc.L23ExcL4InhConnection.base_weight' : [0.0014],
				         'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0013,0.0014,0.0015],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.003,0.0035],
#									     'sheets.l4_cortex_exc.inhibitory_connection_ratio' : [0.8],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.short_term_plasticity.tau_rec' : [100],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_E' : [2.0],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_I' : [7.0,10],
#									     'sheets.l4_cortex_exc.params.cell.params.e_rev_I' : [-80],
#									     'sheets.l4_cortex_exc.params.cell.params.v_reset' : [-60],
				         'sheets.l4_cortex_exc.K' : [700,1480],
				         'sheets.l4_cortex_exc.params.density' : [8000],
				         'sheets.l4_cortex_exc.params.sx' : [800.0,1200.0],
				         'sheets.l23_cortex_exc.feedback_conn_ratio' : [0.25],
				         'sheets.l4_cortex_exc.layer23_aff_ratio' : [0.25],
				         'sheets.retina_lgn.params.noise.stdev' : [2.2],
#									     'sheets.retina_lgn.params.gain_control.gain' : [50],
#									     'sheets.retina_lgn.params.gain_control.non_linear_gain.contrast_scaler' : [0.1,0.01],
#									     'sheets.l4_cortex_exc.AfferentConnection.short_term_plasticity.tau_rec' : [250],
				         'sheets.l4_cortex_exc.AfferentConnection.base_weight' : [0.001],
				         'sheets.l4_cortex_exc.L4ExcL4ExcConnection.base_weight' : [0.001],
#				        				     'sheets.retina_lgn.params.gain_control.non_linear_gain.contrast_scaler' : [0,1,10],
#				        				     'sheets.retina_lgn.params.gain_control.non_linear_gain.luminance_gain' : [0.0],
#									     'sheets.l4_cortex_exc.AfferentConnection.size' : [0.17],
#									     'sheets.l4_cortex_exc.AfferentConnection.num_samples' : [100],
#									     'sheets.l4_cortex_exc.AfferentConnection.aspect_ratio' : [0.4],
#									     'sheets.l23_cortex_exc.feedback_conn_ratio' : [0.14],
				         'sheets.l4_cortex_inh.ExcInhAfferentRatio' : [0.0,0.5],
#									     'sheets.l4_cortex_inh.params.cell.params.v_thresh' : [-60],
#									     'sheets.l4_cortex_exc.params.cell.params.v_thresh' : [-60],
#									     'sheets.l4_cortex_exc.params.cell.params.v_rest' : [-71],
#									     'sheets.l23_cortex_inh.L4ExcL23InhConnection.num_samples' : [300],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.weight_functions.f1.params.sigma' : [1.4],
#									     'sheets.l4_cortex_exc.L4ExcL4InhConnection.weight_functions.f1.params.sigma' : [3.0],
#									     'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f1.params.sigma' : [1.4],
#									     'sheets.l23_cortex_exc.L23ExcL23InhConnection.weight_functions.f1.params.sigma' : [3.0],
#				        				     'sheets.l23_cortex_inh.L4ExcL23InhConnection.weight_functions.f2.params.sigma' : [1.4,3.0],
#									     'sheets.l23_cortex_exc.L23ExcL23ExcConnection.weight_functions.f1.params.sigma' : [1.0,1.4],
#									     'sheets.l23_cortex_inh.L4ExcL23InhConnection.weight_' : ["\\\'f1\\\'","\\\'f1*f2\\\'"],
#									     'sheets.l23_cortex_exc.L23ExcL4InhConnection.weight_functions.f1.params.arborization_constant' : [100],
				         }).run_parameter_search()


#import time
#time.sleep(5) # delays for 5 seconds

#if True:
#    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=16),{
#									     'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0020,0.0021,0.0022,0.0023],
#									     'sheets.l4_cortex_exc.inhibitory_connection_ratio' : [0.75],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.short_term_plasticity.tau_rec' : [50],
#									     'sheets.l4_cortex_exc.params.cell.params.tau_syn_I' : [2.5],
#									     'sheets.l4_cortex_exc.K' : [1000],
#									     'sheets.l4_cortex_exc.layer23_aff_ratio' : [0.35],
#									     'sheets.retina_lgn.params.noise.stdev' : [2.3,2.5],
#									     'sheets.l4_cortex_exc.params.cell.params.v_thresh' : [-56],
#									     'sheets.l23_cortex_inh.L4ExcL23InhConnection.num_samples' : [140],
#									     }).run_parameter_search()
