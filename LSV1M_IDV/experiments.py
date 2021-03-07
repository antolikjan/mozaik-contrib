#!/usr/local/bin/ipython -i
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
from mozaik.experiments.direct_stimulations_mixins import *


def create_experiments(model):

    return [
        # Lets kick the network up into activation

        # Spontaneous Activity
        NoStimulation(model, ParameterSet(
            {'duration': 3*8*2*5*3*8*7})),

        # Measure orientation tuning with full-filed sinusoidal gratins
        MeasureOrientationTuningFullfield(model, ParameterSet(
            {'num_orientations': 10, 'spatial_frequency': 0.8, 'temporal_frequency': 2, 'grating_duration': 2*143*7, 'contrasts': [30, 100], 'num_trials':10})),

        # Measure response to natural image with simulated eye movement
        MeasureNaturalImagesWithEyeMovement(model, ParameterSet(
            {'stimulus_duration': 2*143*7, 'num_trials': 10})),


        # GRATINGS WITH EYEMOVEMENT
        # MeasureDriftingSineGratingWithEyeMovement(model,spatial_frequency=0.8,temporal_frequency=6,stimulus_duration=3*143*7,num_trials=15,contrast=100),

    ]


def create_experiments_spont(model):

    return [
        #PoissonNetworkKick(model,duration=8*8*7,drive_period=200.0,sheet_list=["V1_Exc_L4","V1_Inh_L4"],stimulation_configuration={'component' : 'mozaik.sheets.population_selector.RCRandomPercentage','params' : {'percentage' : 100.0}},lambda_list=[400.0,400.0],weight_list=[0.0012,0.0012]),
        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 3*2*5*3*8*7})),
    ]


def create_experiments_or(model):

    return [
                           # Spontaneous Activity
                           #NoStimulation(model, ParameterSet({'duration': 3*8*2*5*3*8*7})),
                           # Measure orientation tuning with full-filed sinusoidal gratins
                           #MeasureOrientationTuningFullfield(model, ParameterSet(
                           #    {'num_orientations': 2, 'spatial_frequency': 0.8, 'temporal_frequency': 2, 'grating_duration': 2*143*7, 'contrasts': [100, 10], 'num_trials': 5})),

                           # Measure response to natural image with simulated eye movement
                           #MeasureNaturalImagesWithEyeMovement(model, ParameterSet(
                           #    {'stimulus_duration': 2*143*7, 'num_trials': 5})),



                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({
                                                                                 'num_orientations' : 2,
                                                                                 'spatial_frequency' : 0.8,
                                                                                 'temporal_frequency'  : 2,
                                                                                 'grating_duration' : 2*147*7,
                                                                                 'contrasts' : [100],
                                                                                 'num_trials' : 10})),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({
                                                                                 'num_orientations' : 2,
                                                                                 'spatial_frequency' : 0.8,
                                                                                 'temporal_frequency'  : 2,
                                                                                 'grating_duration' : 2*147*7,
                                                                                 'contrasts' : [100],
                                                                                 'num_trials' : 10})),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({
                                                                                 'num_orientations' : 2,
                                                                                 'spatial_frequency' : 0.8,
                                                                                 'temporal_frequency'  : 2,
                                                                                 'grating_duration' : 2*147*7,
                                                                                 'contrasts' : [100],
                                                                                 'num_trials' : 10})),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),

                           add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({
                                                                                 'num_orientations' : 2,
                                                                                 'spatial_frequency' : 0.8,
                                                                                 'temporal_frequency'  : 2,
                                                                                 'grating_duration' : 2*147*7,
                                                                                 'contrasts' : [100],
                                                                                 'num_trials' : 10})),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                           ),




                          
                        ]




def create_experiments_stc(model):

    return [

        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 2*5*3*8*7})),

        # Size Tuning
        MeasureSizeTuning(model, ParameterSet({'num_sizes': 12, 'max_size': 5.0, 'log_spacing': True, 'orientation': 0,
                                               'spatial_frequency': 0.8, 'temporal_frequency': 2, 'grating_duration': 2*143*7, 'contrasts': [30, 100], 'num_trials': 10})),
    ]


def create_experiments_octc(model):

    return [

        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 2*5*3*8*7})),

        # OCTC
        MeasureOrientationContrastTuning(model, ParameterSet({'num_orientations': 8, 'orientation': 0, 'center_radius': 0.9, 'surround_radius': 20.0,
                                                              'spatial_frequency': 0.8, 'temporal_frequency': 2, 'grating_duration': 10*2*143*7, 'contrasts': [100], 'num_trials': 1})),
    ]


def create_experiments_conn(model):

    return [
        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 100})),
    ]


def create_experiments_or_small(model):

    return [
        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 2*5*3*8*7})),
        # Measure orientation tuning with full-filed sinusoidal gratins
        #MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations':2,'spatial_frequency':0.8,'temporal_frequency':2,'grating_duration':2*143*7,'contrasts':[100,10],'num_trials': 2})),
    ]


def create_experiments_RF_estimation(model):
    return [
        # Spontaneous Activity
        NoStimulation(model, ParameterSet({'duration': 3*147*7})),

        # RF estimation
        MeasureSparse(model, ParameterSet({
            'time_per_image': 70,
            'stim_size': 3.2,
            'total_number_of_images': 2000,
            'num_trials': 1,
            'experiment_seed': 13,
            'grid_size': 8,
            'grid': True
        })),

        # RF estimation
        MeasureSparse(model, ParameterSet({
            'time_per_image': 70,
            'stim_size': 3.2,
            'total_number_of_images': 2000,
            'num_trials': 1,
            'experiment_seed': 17,
            'grid_size': 8,
            'grid': True
        })),

        # RF estimation
        MeasureSparse(model, ParameterSet({
            'time_per_image': 70,
            'stim_size': 3.2,
            'total_number_of_images': 2000,
            'num_trials': 1,
            'experiment_seed': 23,
            'grid_size': 8,
            'grid': True
        })),

        # RF estimation
        MeasureSparse(model, ParameterSet({
            'time_per_image': 70,
            'stim_size': 3.2,
            'total_number_of_images': 2000,
            'num_trials': 1,
            'experiment_seed': 513,
            'grid_size': 8,
            'grid': True
        })),

    ]
