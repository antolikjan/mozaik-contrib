# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import CombinationParameterSearch, SlurmSequentialBackendUNIC
import numpy
import time


if True:
    CombinationParameterSearch(SlurmSequentialBackendUNIC(num_threads=1, num_mpi=64,path_to_mozaik_env='/home/antolikjan/virt_env/mozaik/bin/activate',slurm_options=['--exclude=node08']), {
        'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight': [0.0023,0.002,0.0026],
        'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight': [0.0007,0.0006,0.0005],
        'sheets.l4_cortex_exc.params.cell.params.tau_syn_I': [17],
    }).run_parameter_search()



