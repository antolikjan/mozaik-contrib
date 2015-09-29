# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import CombinationParameterSearch,SlurmSequentialBackend
import numpy

if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
									     'retina_lgn.params.gain' : [0.1],
									     'l4_cortex_exc.params.density' : [10],
									     }).run_parameter_search()





if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
									     'l4_cortex_exc.AfferentConnection.base_weight' : [0.0015],
									     'l23_cortex_exc.L23ExcL23InhConnection.base_weight' : [0.003],
									     'l23_cortex_exc.L4ExcL23ExcConnection.base_weight' : [0.003],
									     'l23_cortex_inh.L4ExcL23InhConnection.base_weight' : [0.0001],
									     'l23_cortex_inh.L23InhL23ExcConnection.base_weight' : [0.0025],
									     'l23_cortex_inh.L23InhL23InhConnection.base_weight' : [0.0017],
									     'l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0004],
									     'l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.002,0.0025,0.003],
									     'l4_cortex_inh.ExcInhAfferentRatio' : [1.7],
									     'l4_cortex_exc.params.density' : [300],
									     'only_afferent' : [False],
									     'l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.U' : [0.1,0.13,0.16],
									     }).run_parameter_search()

if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
									     'l23_cortex_exc.L23ExcL23InhConnection.base_weight' : [0.002,0.001],
									     'l23_cortex_exc.L4ExcL23ExcConnection.base_weight' : [0.002,0.001],
									     'l23_cortex_inh.L4ExcL23InhConnection.base_weight' : [0.0001,0.001],
									     'l23_cortex_inh.L23InhL23ExcConnection.base_weight' : [0.0025,0.003,0.0035],
									     'l23_cortex_inh.L23InhL23InhConnection.base_weight' : [0.0017],
									     'l4_cortex_exc.L4ExcL4ExcConnection.base_weight' : [0.0005],
									     'l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0007,0.00075],
									     'l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0018],
									     'l4_cortex_inh.ExcInhAfferentRatio' : [1.4,1.3],
									     'l4_cortex_exc.params.density' : [300],
									     'l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.tau_rec' : [25],
									     }).run_parameter_search()


if False:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
									     'l4_cortex_exc.AfferentConnection.base_weight' : [0.002],
									     'l4_cortex_exc.AfferentConnection.num_samples' : [15,20],
									     'l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0007],
									     'l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.00065],
									     'l23_cortex_exc.L23ExcL23InhConnection.base_weight' : [0.0015],
									     'l23_cortex_inh.L23InhL23ExcConnection.base_weight' : [0.003],
									     'l23_cortex_exc.L4ExcL23ExcConnection.base_weight' : [0.0015],
									     'l4_cortex_inh.ExcInhAfferentRatio' : [0.7,0.8,0.9],
									     'l4_cortex_exc.params.density' : [300],
									     'l23_cortex_exc.params.density' : [300],
									     'l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.tau_fac' : [300,250,350],
									     'l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.U' : [0.1,0.11,0.9],
									     }).run_parameter_search()



if True:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=1,num_mpi=64),{
									     'l4_cortex_exc.AfferentConnection.base_weight' : [0.0005,0.0006],
									     'l4_cortex_exc.AfferentConnection.num_samples' : [45,50],
									     'l23_cortex_exc.L23ExcL23InhConnection.base_weight' : [0.002],
									     'l23_cortex_exc.L4ExcL23ExcConnection.base_weight' : [0.0024],
									     'l23_cortex_inh.L4ExcL23InhConnection.base_weight' : [0.0001],
									     'l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0026],
									     'l4_cortex_inh.L4InhL4InhConnection.base_weight' : [0.0002,0.0003],
									     'l4_cortex_inh.ExcInhAfferentRatio' : [1.25,1.2],
									     'l4_cortex_exc.AfferentConnection.short_term_plasticity.tau_rec' : [60],
									     'l4_cortex_exc.params.density' : [300],
									     'l4_cortex_exc.params.sx' : [6000],
									     }).run_parameter_search()


