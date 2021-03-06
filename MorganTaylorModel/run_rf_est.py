# -*- coding: utf-8 -*-
"""

"""
import matplotlib
matplotlib.use('Agg')
from mpi4py import MPI 
from pyNN import nest
import sys
import mozaik.controller
from mozaik.controller import run_workflow, setup_logging
import mozaik
from experiments import create_experiments_RF_estimation
from model import SelfSustainedPushPull
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import HirschFigure
from parameters import ParameterSet


mpi_comm = MPI.COMM_WORLD

if True:
    data_store,model = run_workflow('MorganTaylorModel',SelfSustainedPushPull,create_experiments_RF_estimation)
    data_store.save() 
else: 
    setup_logging()
    data_store = PickledDataStore(load=True,parameters=ParameterSet({'root_directory':'MorganTaylorModel_visual_space_update=1ms_RF_resolution=1ms','store_stimuli' : False}),replace=True)

if mpi_comm.rank == 0:
   print "Starting visualization" 
   HirschFigure(data_store)
