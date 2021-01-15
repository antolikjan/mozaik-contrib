#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    
def create_experiments(model):
    return              [
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration' : 147*7})),

                           #GRATINGS
                           MeasureOrientationTuningFullfield(model,ParameterSet({
                                                                                 'num_orientations' : 2,
                                                                                 'spatial_frequency' : 0.8,
                                                                                 'temporal_frequency'  : 2,
                                                                                 'grating_duration' : 2*147*7,
                                                                                 'contrasts' : [100],
                                                                                 'num_trials' : 3})),
                       
                           
                           #MeasureFrequencySensitivity(model,ParameterSet({
                           #                                                 'orientation' : 0,
                           #                                                 'spatial_frequencies' : [0.01,0.8,1.5],
                           #                                                 'temporal_frequencies' : [2.0],
                           #                                                 'grating_duration'  : 147*7*2,
                           #                                                 'contrasts' : [100],
                           #                                                 'num_trials' : 1})),                           
                           
                           #IMAGES WITH EYEMOVEMENT
                           #MeasureNaturalImagesWithEyeMovement(model,ParameterSet({
                           #                                                            'stimulus_duration' : 2*147*7,
                           #                                                            'num_trials' : 10})),

                           #GRATINGS WITH EYEMOVEMENT
                           #MeasureDriftingSineGratingWithEyeMovement(model,ParameterSet({
                           #                                                                 'spatial_frequency' : 0.8,
                           #                                                                 'temporal_frequency' :2,
                           #                                                                 'stimulus_duration' : 147*7,
                           #                                                                 'num_trials' : 10,
                           #                                                                 'contrast' : 100),
                        ]

def create_experiments_spont(model):
    return              [
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
			]

def create_experiments_RF_estimation1(model):
     return			[
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration' : 3*147*7})),

                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : -1,
                                   'stimulation_configuration' : {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                            })),


                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : -0.4,
                                   'stimulation_configuration' : {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                            })),

                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : 0.4,
                                   'stimulation_configuration' : {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                            })),


                           #RF estimation
                           MeasureSparse(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True
                            })),

                           #RF estimation
                           MeasureSparse(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 17,
                                   'grid_size' : 8,
                                   'grid' : True
                            })),

			]


def create_experiments_RF_estimation(model):
     return			[
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration' : 3*147*7})),

                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : -1,
                                   'stimulation_configuration' : {
                                           'component' :  'mozaik.sheets.population_selector.RCGrid',
                                           'params' :  {
                                                         'size' : 1000,
                                                         'spacing' : 200,
                                                         'offset_x' : 0,
                                                         'offset_y' : 0
                                                        }
                                         } 
                            })),


                           #RF estimation
                           MeasureSparse(model,ParameterSet({
                                   'time_per_image':70, 
                                   'stim_size' : 4.8,
                                   'total_number_of_images' : 1000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True
                            })),

                ]