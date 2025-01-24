# -*- coding: utf-8 -*-
"""
This is implementation of model of corresponding to the pre-print `Large scale model of cat primary visual cortex`
Antolík, J., Cagnol, R., Rózsa, T., Monier, C., Frégnac, Y., & Davison, A. P. (2018).
https://www.biorxiv.org/content/10.1101/416156v5.abstract
"""
import matplotlib

matplotlib.use("Agg")

from mpi4py import MPI
from mozaik.storage.datastore import Hdf5DataStore, PickledDataStore
from parameters import ParameterSet
from analysis_and_visualization import perform_analysis_and_visualization, perform_analysis_and_visualization_spont
from model import SelfSustainedPushPull
from mozaik.controller import Global
from experiments import create_experiments_single_cell_grat
import mozaik
from mozaik.controller import run_workflow, setup_logging
import mozaik.controller
import sys
from pyNN import nest

from mpi4py import MPI

mpi_comm = MPI.COMM_WORLD


Global.root_directory = sys.argv[1]+'/'

setup_logging()
data_store = PickledDataStore(load=True, parameters=ParameterSet(
    {'root_directory': sys.argv[1], 'store_stimuli': None}), replace=True)

perform_analysis_and_visualization_spont(data_store)
data_store.save()