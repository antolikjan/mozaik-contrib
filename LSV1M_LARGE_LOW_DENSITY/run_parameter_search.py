# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import CombinationParameterSearch,SlurmSequentialBackendUK
import numpy
import time

if True:
    CombinationParameterSearch(SlurmSequentialBackendUK(num_threads=16,num_mpi=1),{
				         'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.001],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0021,0.0022],
				         }).run_parameter_search()


