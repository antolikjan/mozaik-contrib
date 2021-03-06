#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
from mozaik.experiments.direct_stimulations_mixins import *


def create_experiments_short(model):

    return  [

                #Spontaneous Activity 
                MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/4.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 3.0,
                                                                    'steps' : 2,
                                                                    'duration' : 400,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0,
                                                                    'num_trials' : 2
                                                                    })),
                                                                    
                # Measure orientation tuning with full-filed sinusoidal gratins
                MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [5,100],
                                                                      'num_trials' : 2
                                                                      })),


            ]



def create_experiments_bar(model):

    return  [

                #Spontaneous Activity 
                NoStimulation(model,ParameterSet({'duration' : 2*5*3*8*7})),

                MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0,
                                                                    'num_trials' : 5
                                                                    })),
                                                                    
                MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 5
                                                                    })),
            ]


def create_experiments(model):

    return  [

                #Spontaneous Activity 
                NoStimulation(model,ParameterSet({'duration' : 2*5*3*8*7})),

                # Measure orientation tuning with full-filed sinusoidal gratins
                MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 8,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [5,100],
                                                                      'num_trials' : 10
                                                                      })),

                MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 10
                                                                    })),

                MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0.0,
                                                                    'num_trials' : 10
                                                                    })),


            ]


def create_experiments_old(model):

    return  [
                #Lets kick the network up into activation

                #Spontaneous Activity 
                NoStimulation(model,ParameterSet({'duration':8*2*5*3*8*7})),

                # Measure response to natural image with simulated eye movement
                MeasureNaturalImagesWithEyeMovement(model,ParameterSet({'stimulus_duration':2*143*7,'num_trials':10})),

                # Measure orientation tuning with full-filed sinusoidal gratins
                MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 8,'spatial_frequency' : 0.8,'temporal_frequency':2,'grating_duration':2*143*7,'contrasts':[5,100],'num_trials':10})),


            ]


def create_experiments_old_short(model):

    return  [
                #Lets kick the network up into activation

                #Spontaneous Activity 
                NoStimulation(model,ParameterSet({'duration':8*2*5*3*8*7})),

                # Measure response to natural image with simulated eye movement
                MeasureNaturalImagesWithEyeMovement(model,ParameterSet({'stimulus_duration':2*143*7,'num_trials':10})),

                # Measure orientation tuning with full-filed sinusoidal gratins
                MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,'spatial_frequency' : 0.8,'temporal_frequency':2,'grating_duration':2*143*7,'contrasts':[5,100],'num_trials':10})),
            ]




def create_experiments_conn(model):
    
    return  [
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration':100})),
            ]




def create_experiments_curr_inj(model):

    return  [
                # SPONT
                add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                # GRATING
                add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [100],
                                                                      'num_trials' : 10
                                                                      })),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [100],
                                                                      'num_trials' : 10
                                                                      })),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [100],
                                                                      'num_trials' : 10
                                                                      })),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                add_per_stimulus_current_injection(
                                 MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations' : 2,
                                                                      'spatial_frequency' :0.8,
                                                                      'temporal_frequency' : 2,
                                                                      'grating_duration' : 2*143*7,
                                                                      'contrasts' : [100],
                                                                      'num_trials' : 10
                                                                      })),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                   


                # BARS rel_lum 1.0
                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 1.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                # BARS rel_lum 0.0
                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                add_per_stimulus_current_injection(
                                 MapPhaseResponseWithBarStimulus(model,ParameterSet({
                                                                    'x' : 0,
                                                                    'y' : 0,
                                                                    'length' : 1/0.8/2.0 * 6.0,
                                                                    'width' :  1/0.8/12.0,
                                                                    'orientation' : 0,
                                                                    'max_offset' : 1/0.8/2.0 * 1.5,
                                                                    'steps' : 18,
                                                                    'duration' : 300,
                                                                    'flash_duration' : 200, 
                                                                    'relative_luminance' : 0.0,
                                                                    'num_trials' : 10
                                                                    })),

                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.5,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 0.1,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

            ]











def create_experiments_RF_estimation(model):
     return			[



                           # SPONT
                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = 0.1,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),

                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.1,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),


                           add_per_stimulus_current_injection(
                                 NoStimulation(model,ParameterSet({'duration' : 10*147*7})),
                                 stimulation_sheet = 'V1_Exc_L4',
                                 stimulation_current = -0.2,
                                 stimulation_configuration = {

                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            ),



                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image': 21, 
                                   'blank_time': 140, 
                                   'stim_size' : 2.4,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : -0.2,
                                   'stimulation_configuration' : {
                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }
                            })),


                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image': 21, 
                                   'blank_time': 140, 
                                   'stim_size' : 2.4,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : -0.1,
                                   'stimulation_configuration' : {
                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                         } 
                                       }
                            })),

                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image': 21, 
                                   'blank_time': 140, 
                                   'stim_size' : 2.4,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : 0.1,
                                   'stimulation_configuration' : {
                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }

                            })),


                           #RF estimation with current injection
                           MeasureSparseWithCurrentInjection(model,ParameterSet({
                                   'time_per_image':21, 
                                   'blank_time': 140, 
                                   'stim_size' : 2.4,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 8,
                                   'grid' : True,
                                   'stimulation_sheet' : 'V1_Exc_L4',
                                   'stimulation_current' : 0,
                                   'stimulation_configuration' : {
                                              'component' :  'mozaik.sheets.population_selector.SimilarAnnotationSelectorRegion',
                                              'params' :  {
                                                                 'size': 200.0,  # the size of the grid (it is assumed to be square) - it has to be multiple of spacing (micro meters)
                                                                 'offset_x' : 0.0, # the x axis offset from the center of the sheet (micro meters)
                                                                 'offset_y' : 0.0, # the y axis offset from the center of the sheet (micro meters)
                                                                 'num_of_cells' : 30,
                                                                 'annotation' : 'LGNAfferentOrientation',
                                                                 'distance' : 2.2,
                                                                 'value': 0.0,
                                                                 'period' :  3.14159265359, 
                                              }
                                       }

                            })),


                           #RF estimation
                           MeasureSparse(model,ParameterSet({
                                   'time_per_image': 70, 
                                   'blank_time' : 0,
                                   'stim_size' : 2.4,
                                   'total_number_of_images' : 3000,
                                   'num_trials' : 1,
                                   'experiment_seed' : 17,
                                   'grid_size' : 8,
                                   'grid' : True
                            })),
	    ]

