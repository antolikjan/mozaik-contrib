# -*- coding: utf-8 -*-
import sys
from mozaik.meta_workflow.parameter_search import ( CombinationParameterSearch,  SlurmSequentialBackend)
import numpy
import time

CombinationParameterSearch(
        SlurmSequentialBackend(
            num_threads=1,
            num_mpi=32,
            slurm_options=["--hint=nomultithread", "-N 1-1","-x w[1-8,10,12]"],
            path_to_mozaik_env="/home/antolikjan/virt_env/mozaikluca/bin/activate",
        ),
        {
            "trial" : [1],
            "null_stimulus_period": [150],
        },
    ).run_parameter_search()