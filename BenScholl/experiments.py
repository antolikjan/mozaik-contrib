#!/usr/local/bin/ipython -i
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.experiments.electrical_stimulation import RandomSingleNeuronStepCurrentInjection, RandomSingleNeuronStepCurrentInjectionDuringDriftingSinusoidalGratingStimulation
from parameters import ParameterSet
import os


def create_experiments_vis(model,experiment_parameters):

    return [
        # Spont act
        NoStimulation(model, ParameterSet({'duration': 3*8*2*5*3*8*7})),

        # Measure orientation tuning with full-filed sinusoidal gratins
        MeasureOrientationTuningFullfield(model, ParameterSet(
            {'num_orientations': 4, 'spatial_frequency': 0.8, 'temporal_frequency': 2, 'grating_duration': 500, 'contrasts': [2,4], 'num_trials': 20, 'shuffle_stimuli': True})),
    ]

def create_experiments_single_cell_spont(model,experiment_parameters):

    return [
        NoStimulation(model, ParameterSet(
            {'duration': 10*3*8*2*5*3})),

        RandomSingleNeuronStepCurrentInjection(
            model,
            ParameterSet(
                {
                        'duration': 500,
                        'current' : 0.06,
                        'sheet' : "V1_Exc_L2/3",
                        'num_neurons' : 90,
                        'num_trials' : 10, 
                        'experiment_random_seed' : 513,
                        'stimulation_configuration' : ParameterSet({
                                'component' :  'mozaik.sheets.population_selector.RCAllWihinBoundry',
                                'params' : ParameterSet({
                                    'size': 2000,
                                    'offset_x' : 0, 
                                    'offset_y' : 0, 
                            }),
                        }),
                }
            ),
        ),
    ]


def create_experiments_single_cell_grat(model,experiment_parameters):

    return [
        NoStimulation(model, ParameterSet(
            {'duration': 10*3*8*2*5*3})),

        RandomSingleNeuronStepCurrentInjectionDuringDriftingSinusoidalGratingStimulation(
            model,
            ParameterSet(
                {    
                        'shuffle_stimuli' : False,
                        'duration': 500,
                        'current' : 0.06,
                        'current_onset' : 0,
                        'sheet' : "V1_Exc_L2/3",
                        'num_neurons' : 90,
                        'num_trials' : 10,
                        'experiment_random_seed' : 513,
                        'grating_spatial_frequency' : 0.8,
                        'grating_temporal_frequency' : 2,
                        'grating_contrasts' : [0,2],
                        'grating_num_orientations' : 4,
                        'stimulation_configuration' : ParameterSet({
                                'component' :  'mozaik.sheets.population_selector.RCAllWihinBoundry',
                                'params' : ParameterSet({
                                    'size' : 2000,
                                    'offset_x' : 0, 
                                    'offset_y' : 0, 
                            }),
                        }),
                }
            ),
        ),
    ]

