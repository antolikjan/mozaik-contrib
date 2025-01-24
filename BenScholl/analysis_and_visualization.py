import os
import time
import mozaik
from mozaik.controller import Global
import json
import gc
from mozaik.analysis.analysis import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues,ExportRawSpikeData
from mozaik.storage.neo_neurotools_wrapper import pre_load
from mozaik.storage.queries import *
from mpi4py import MPI


logger = mozaik.getMozaikLogger()

def perform_analysis_and_visualization(data_store):
    logger.info("Starting analysis and visualisation")

    dsv = param_filter_query(data_store,st_name='InternalStimulus')
    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()

    dsv = param_filter_query(data_store,sheet_name='V1_Exc_L2/3',st_name='FullfieldDriftingSinusoidalGrating')
    logger.info(str(len(dsv.get_segments())))

    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()
    dsv.purge_segments()
    gc.collect()

    dsv = param_filter_query(data_store,sheet_name='V1_Inh_L2/3',st_name='FullfieldDriftingSinusoidalGrating')
    logger.info(str(len(dsv.get_segments())))

    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()
    dsv.purge_segments()
    logger.info("Finished analysis and visualisation")

def perform_analysis_and_visualization_spont(data_store):
    logger.info("Starting analysis and visualisation")

    dsv = param_filter_query(data_store,st_name='InternalStimulus',st_direct_stimulation_name=None)
    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()

    dsv = param_filter_query(data_store,sheet_name='V1_Exc_L2/3',st_direct_stimulation_name='Injection')
    logger.info(str(len(dsv.get_segments())))

    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()
    dsv.purge_segments()
    gc.collect()

    dsv = param_filter_query(data_store,sheet_name='V1_Inh_L2/3',st_direct_stimulation_name='Injection')
    logger.info(str(len(dsv.get_segments())))

    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()
    dsv.purge_segments()
    logger.info("Finished analysis and visualisation")


def perform_analysis_and_visualization_test(data_store):
    logger.info("Starting analysis and visualisation")
    start_time = time.time()  # Record the start time

    dsv = param_filter_query(data_store,sheet_name='V1_Exc_L2/3',st_direct_stimulation_name='Injection',st_orientation=0,st_contrast=8,st_trial=[0,1,3])
    logger.info(str(len(dsv.get_segments())))

    preload_time = time.time()  # Record the start time
    pre_load(dsv)
    postload_time = time.time()  # Record the start time

    TrialAveragedFiringRate(dsv,ParameterSet({})).analyse()
    dsv.purge_segments()
    gc.collect()

    end_time = time.time()  # Record the start time

    logger.info("Time taken: %f", end_time - start_time)
    logger.info("Time to load: %f", postload_time - preload_time)

    logger.info("Finished analysis and visualisation")
