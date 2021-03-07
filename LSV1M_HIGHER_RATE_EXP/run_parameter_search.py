# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import CombinationParameterSearch, SlurmSequentialBackend
import numpy
import time


if True:
    CombinationParameterSearch(SlurmSequentialBackend(num_threads=8, num_mpi=1,path_to_mozaik_env='/home/jantolik/virt_env/mozaik/bin/activate',slurm_options=['--hint=nomultithread']), {
        'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight': [0.0023,0.0028,0.0029],
        'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight': [0.0009,0.0008,0.0007,0.0006],
        'sheets.l4_cortex_exc.params.cell.params.tau_syn_I': [11,15],
    }).run_parameter_search()



