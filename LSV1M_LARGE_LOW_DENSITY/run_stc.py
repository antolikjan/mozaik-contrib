# -*- coding: utf-8 -*-
"""
This is implementation of model of self-sustained activitity in balanced networks from: 
Vogels, T. P., & Abbott, L. F. (2005). 
Signal propagation and logic gating in networks of integrate-and-fire neurons. 
The Journal of neuroscience : the official journal of the Society for Neuroscience, 25(46), 10786–95. 
"""
import matplotlib
matplotlib.use('Agg')


from pyNN import nest
import sys
import mozaik.controller
from mozaik.controller import run_workflow, setup_logging
import mozaik
from experiments import create_experiments_stc
from model import SelfSustainedPushPull
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import perform_analysis_and_visualization_stc
from parameters import ParameterSet

from mpi4py import MPI 
mpi_comm = MPI.COMM_WORLD


if True:
    data_store,model = run_workflow('SelfSustainedPushPull',SelfSustainedPushPull,create_experiments_stc)
    data_store.save() 


if mpi_comm.rank == 0:
   print "Starting visualization" 
   perform_analysis_and_visualization_stc(data_store)
   data_store.save() 
