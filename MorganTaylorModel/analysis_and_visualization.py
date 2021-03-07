import mozaik
from mozaik.visualization.plotting import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore
from mozaik.controller import Global

import sys
sys.path.append('/home/antolikjan/projects/mozaik/contrib')
#import Kremkow_plots
#from Kremkow_plots import *
from lsv1m_paper import *


logger = mozaik.getMozaikLogger()

import os


class AAA(Analysis):
      """
      """
      def perform_analysis(self):

	    spike_ids = param_filter_query(self.datastore,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_spike_train_ids()
	    spike_ids_inh = param_filter_query(self.datastore,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_spike_train_ids()

            mmax5 = param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation max of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids)
            mmax100 = param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation max of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids)
            responsive_spike_ids_l4E = numpy.array(spike_ids)[numpy.logical_and(numpy.array(mmax5) > 2.0,numpy.array(mmax100) > 2.0)]

	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(mmax5),period=None,value_name = 'Tuning Height LC',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(mmax100),period=None,value_name = 'Tuning Height HC',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        

            mmax5 = param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation max of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids_inh)
            mmax100 = param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation max of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids_inh)
            responsive_spike_ids_l4I = numpy.array(spike_ids_inh)[numpy.logical_and(numpy.array(mmax5) > 2.0,numpy.array(mmax100) > 2.0)]

	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(mmax5),period=None,value_name = 'Tuning Height LC',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(mmax100),period=None,value_name = 'Tuning Height HC',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        


            hwhh_hc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(responsive_spike_ids_l4E))
            hwhh_lc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(responsive_spike_ids_l4E))

            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(hwhh_hc[hwhh_hc<1000]),period=None,value_name = 'Mean HWHH of responsive neurons',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(abs(hwhh_hc-hwhh_lc)[abs(hwhh_hc-hwhh_lc)<1000]),period=None,value_name = 'Mean HWHH difference',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    print numpy.mean(abs(hwhh_hc-hwhh_lc)[abs(hwhh_hc-hwhh_lc)<1000])
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.sum(numpy.logical_or(hwhh_hc<=0,hwhh_hc>=100)),period=None,value_name = 'Faild fits HC',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.sum(numpy.logical_or(hwhh_lc<=0,hwhh_lc>=100)),period=None,value_name = 'Faild fits LC',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    
            hwhh_hc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(responsive_spike_ids_l4I))
            hwhh_lc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name="None",st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(responsive_spike_ids_l4I))

            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(hwhh_hc[hwhh_hc<1000]),period=None,value_name = 'Mean HWHH of responsive neurons',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(abs(hwhh_hc-hwhh_lc)[abs(hwhh_hc-hwhh_lc)<1000]),period=None,value_name = 'Mean HWHH difference',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    print numpy.mean(abs(hwhh_hc-hwhh_lc)[abs(hwhh_hc-hwhh_lc)<1000])
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.sum(numpy.logical_or(hwhh_hc<=0,hwhh_hc>=100)),period=None,value_name = 'Faild fits HC',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.sum(numpy.logical_or(hwhh_lc<=0,hwhh_lc>=100)),period=None,value_name = 'Faild fits LC',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        


class AAA1(Analysis):
      """
      """
      def perform_analysis(self):
	    TrialMean(self.datastore,ParameterSet({'vm': False,  'cond_exc': True, 'cond_inh': True})).analyse()
	    dsv = param_filter_query(self.datastore,analysis_algorithm='TrialMean',st_name='FullfieldDriftingSinusoidalGrating',sheet_name='V1_Exc_L4',y_axis_name=['inh. conductance trial-to-trial mean','exc. conductance trial-to-trial mean'],st_orientation=0,st_contrast=100)
	    mozaik.analysis.analysis.AnalogSignal_PerNeuronBetweenSignalCorrelation(dsv,ParameterSet({'value_name1':'inh. conductance trial-to-trial mean','value_name2' : 'exc. conductance trial-to-trial mean'})).analyse()

	    dsv = param_filter_query(self.datastore,analysis_algorithm='AnalogSignal_PerNeuronBetweenSignalCorrelation')	    
	    PopulationMeanAndVar(dsv,ParameterSet({})).analyse()
	    PopulationMedian(dsv,ParameterSet({})).analyse()

	    spike_ids = param_filter_query(self.datastore,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_spike_train_ids()
	    spike_ids_inh = param_filter_query(self.datastore,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_spike_train_ids()

	    wellfit5 = param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation fitting error of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids)
	    wellfit100 = param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation fitting error of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids)
	    print wellfit5
	    print wellfit100
            wellfit_spike_ids_l4E = numpy.array(spike_ids)[numpy.logical_and(numpy.array(wellfit5) < 0.2,numpy.array(wellfit100) < 0.2)]

	    wellfit5 = param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation fitting error of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids_inh)
	    wellfit100 = param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation fitting error of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(spike_ids_inh)
	    print wellfit5
	    print wellfit100
            wellfit_spike_ids_l4I = numpy.array(spike_ids_inh)[numpy.logical_and(numpy.array(wellfit5) < 0.2,numpy.array(wellfit100) < 0.2)]


            hwhh_hc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(wellfit_spike_ids_l4E))
            hwhh_lc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Exc_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(wellfit_spike_ids_l4E))

            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(hwhh_hc),period=None,value_name = 'Mean HWHH of responsive neurons',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(abs(hwhh_hc-hwhh_lc)),period=None,value_name = 'Mean HWHH difference',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.median(hwhh_hc),period=None,value_name = 'Median HWHH of responsive neurons',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.median(abs(hwhh_hc-hwhh_lc)),period=None,value_name = 'Median HWHH difference',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=(len(spike_ids) - len(wellfit_spike_ids_l4E))/len(spike_ids),period=None,value_name = 'Faild fits percantage',sheet_name='V1_Exc_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    
            hwhh_hc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=100,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(wellfit_spike_ids_l4I))
            hwhh_lc = numpy.array(param_filter_query(self.datastore,sheet_name='V1_Inh_L4',st_direct_stimulation_name=None,st_name=['FullfieldDriftingSinusoidalGrating'],st_contrast=5,value_name=['orientation HWHH of Firing rate'],ads_unique=True).get_analysis_result()[0].get_value_by_id(wellfit_spike_ids_l4I))

            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(hwhh_hc),period=None,value_name = 'Mean HWHH of responsive neurons',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.mean(abs(hwhh_hc-hwhh_lc)),period=None,value_name = 'Mean HWHH difference',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.median(hwhh_hc),period=None,value_name = 'Median HWHH of responsive neurons',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
            self.datastore.full_datastore.add_analysis_result(SingleValue(value=numpy.median(abs(hwhh_hc-hwhh_lc)),period=None,value_name = 'Median HWHH difference',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    self.datastore.full_datastore.add_analysis_result(SingleValue(value=(len(spike_ids_inh) - len(wellfit_spike_ids_l4E))/len(spike_ids_inh),period=None,value_name = 'Faild fits percentage',sheet_name='V1_Inh_L4',tags=self.tags,analysis_algorithm=self.__class__.__name__,stimulus_id=None))        
	    
	    param_filter_query(self.datastore,sheet_name=["V1_Exc_L4","V1_Exc_L4"],identifier=['SingleValue','PerNeuronValue']).remove_ads_outside_of_dsv()





def ana1(data_store):
    print "DSADSA"
    sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4','V1_Inh_L4']))
    exc_sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4']))
    TrialAveragedFiringRate(param_filter_query(data_store,st_name="FullfieldDriftingSinusoidalGrating"),ParameterSet({})).analyse()

    dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name='V1_Exc_L4',value_name='Firing rate')    
    GaussianTuningCurveFit(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()

    dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name='V1_Inh_L4',value_name='Firing rate')
    GaussianTuningCurveFit(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()

    PSTH(param_filter_query(data_store),ParameterSet({'bin_length' : 10.0 })).analyse()
    NeuronToNeuronAnalogSignalCorrelations(param_filter_query(data_store,analysis_algorithm='PSTH',st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({'convert_nan_to_zero' : True})).analyse()

    dsv = param_filter_query(data_store,analysis_algorithm='NeuronToNeuronAnalogSignalCorrelations')
    PopulationMeanAndVar(dsv,ParameterSet({})).analyse()

    #dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0,st_trial=1)
    Irregularity(param_filter_query(data_store,st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({})).analyse()
    PopulationMeanAndVar(param_filter_query(data_store,st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({})).analyse()


    AAA1(data_store,ParameterSet({})).analyse()

    data_store.save()


def analysis(data_store,analog_ids,analog_ids_inh,gratings,bars):
    sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4','V1_Inh_L4']))
    exc_sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4']))

    TrialAveragedFiringRate(param_filter_query(data_store,st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({})).analyse()

    if bars:
        TrialAveragedFiringRate(param_filter_query(data_store,st_name="FlashedBar"),ParameterSet({})).analyse()

    if gratings:
        TrialAveragedFiringRate(param_filter_query(data_store,st_name="FullfieldDriftingSinusoidalGrating"),ParameterSet({})).analyse()

    Irregularity(param_filter_query(data_store,st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({})).analyse()

    PSTH(param_filter_query(data_store),ParameterSet({'bin_length' : 10.0 })).analyse()

    NeuronToNeuronAnalogSignalCorrelations(param_filter_query(data_store,analysis_algorithm='PSTH',st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({'convert_nan_to_zero' : True})).analyse()
    PopulationMeanAndVar(param_filter_query(data_store,st_direct_stimulation_name="None",st_name='InternalStimulus'),ParameterSet({})).analyse()

    dsv = param_filter_query(data_store,sheet_name=exc_sheets)
    ActionPotentialRemoval(dsv,ParameterSet({'window_length': 5.0})).analyse()

    dsv = param_filter_query(data_store,analysis_algorithm='ActionPotentialRemoval')
    TrialVariability(data_store,ParameterSet({'vm': True,  'cond_exc': True, 'cond_inh': True})).analyse()
    TrialMean(data_store,ParameterSet({'vm': True,  'cond_exc': True, 'cond_inh': True})).analyse()

    dsv = param_filter_query(data_store,st_name='InternalStimulus',st_direct_stimulation_name="None")
    Analog_MeanSTDAndFanoFactor(dsv,ParameterSet({})).analyse()

    if gratings:

        dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name=sheets)    
        GaussianTuningCurveFit(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()
        dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name=sheets)   
        Analog_F0andF1(dsv,ParameterSet({})).analyse()

        dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name=sheets)  
        PeriodicTuningCurvePreferenceAndSelectivity_VectorAverage(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()

        ModulationRatio(param_filter_query(data_store,sheet_name=exc_sheets,st_contrast=[100]),ParameterSet({})).analyse()

        dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate')    
        CircularVarianceOfTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()

    data_store.save()



def perform_analysis_and_visualization(data_store,gratings,bars,nat_movies=False):
    
    sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4','V1_Inh_L4']))
    exc_sheets = list(set(data_store.sheets()) & set(['V1_Exc_L4']))
    
    NeuronAnnotationsToPerNeuronValues(data_store,ParameterSet({})).analyse()
    
    analog_ids = param_filter_query(data_store,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_esyn_ids()
    analog_ids_inh = param_filter_query(data_store,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_esyn_ids()
    spike_ids = param_filter_query(data_store,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_spike_train_ids()
    spike_ids_inh = param_filter_query(data_store,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_spike_train_ids()
    
    
    l4_exc_or = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentOrientation', sheet_name = 'V1_Exc_L4')
    l4_exc_phase = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentPhase', sheet_name = 'V1_Exc_L4')
    l4_exc = analog_ids[numpy.argmin([circular_dist(o,numpy.pi/2,numpy.pi)  for (o,p) in zip(l4_exc_or[0].get_value_by_id(analog_ids),l4_exc_phase[0].get_value_by_id(analog_ids))])]
    l4_inh_or = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentOrientation', sheet_name = 'V1_Inh_L4')
    l4_inh_phase = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentPhase', sheet_name = 'V1_Inh_L4')
    l4_inh = analog_ids_inh[numpy.argmin([circular_dist(o,numpy.pi/2,numpy.pi)  for (o,p) in zip(l4_inh_or[0].get_value_by_id(analog_ids_inh),l4_inh_phase[0].get_value_by_id(analog_ids_inh))])]
    l4_exc_or_many = numpy.array(l4_exc_or[0].ids)[numpy.nonzero(numpy.array([circular_dist(o,0,numpy.pi)  for (o,p) in zip(l4_exc_or[0].values,l4_exc_phase[0].values)]) < 0.1)[0]]
    
    l4_exc_or_many = list(set(l4_exc_or_many) &  set(spike_ids))
        
    orr = list(set([MozaikParametrized.idd(s).orientation for s in queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',st_contrast=100).get_stimuli()]))                
        
    l4_exc_or_many_analog = numpy.array(analog_ids)[numpy.nonzero(numpy.array([circular_dist(l4_exc_or[0].get_value_by_id(i),0,numpy.pi)  for i in analog_ids]) < 0.1)[0]]
    l4_inh_or_many_analog = numpy.array(analog_ids_inh)[numpy.nonzero(numpy.array([circular_dist(l4_inh_or[0].get_value_by_id(i),0,numpy.pi)  for i in analog_ids_inh]) < 0.15)[0]]
    
    lgn_on_ids = param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_spike_train_ids()
    lgn_off_ids = param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_spike_train_ids()    

    #analysis(data_store,analog_ids,analog_ids_inh,gratings,bars)

    if bars:
        dsv = queries.param_filter_query(data_store,st_name='FlashedBar')
        for ads in dsv.get_analysis_result():
            sid = MozaikParametrized.idd(ads.stimulus_id)
            sid.x=0
            ads.stimulus_id = str(sid)
        for seg in dsv.get_segments():    
            sid = MozaikParametrized.idd(seg.annotations['stimulus'])
            sid.x=0
            seg.annotations['stimulus'] = str(sid)

    def overviews(dsv,name_prefix):

        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4ExcAnalog1.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[0], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4InhAnalog1.png').plot()    
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[1], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4ExcAnalog2.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[1], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4InhAnalog2.png').plot()    
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[2], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4ExcAnalog3.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[2], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'L4InhAnalog3.png').plot()    

        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : spike_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'SSExcRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neurons' : spike_ids_inh,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'SSInhRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})
    
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neurons' : lgn_on_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'XONRaster.png').plot({'SpikeRasterPlot.group_trials':True})
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neurons' : lgn_off_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name=name_prefix+'XOFFRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})



    # self sustained plotting
    dsv = param_filter_query(data_store,st_name='InternalStimulus')   
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSExcAnalog1.png').plot()
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[0], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSInhAnalog1.png').plot()    
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[1], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSExcAnalog2.png').plot()
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[1], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSInhAnalog2.png').plot()    
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[2], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSExcAnalog3.png').plot()
    OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[2], 'sheet_activity' : {}, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSInhAnalog3.png').plot()    
    
    RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : spike_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSExcRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})
    RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neurons' : spike_ids_inh,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSInhRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})

    if bars:
        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',sheet_name = 'V1_Exc_L4',st_relative_luminance=1)
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='BarExcAnalog1.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[1], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='BarExcAnalog2.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[2], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='BarExcAnalog3.png').plot()


        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=1)
        PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[:4]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOnBar1.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})
        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=0)
        PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[:4]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOffBar1.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})

        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=1)
        PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[4:8]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOnBar2.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})
        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=0)
        PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[4:8]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOffBar2.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})

        #dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=1)
        #PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[8:12]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOnBar3.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})
        #dsv = queries.param_filter_query(data_store,st_name='FlashedBar',y_axis_name=['Vm (no AP) trial-to-trial mean','exc. conductance trial-to-trial mean','inh. conductance trial-to-trial mean'],sheet_name = 'V1_Exc_L4',analysis_algorithm='TrialMean',st_relative_luminance=0)
        #PlotTemporalTuningCurve(dsv, ParameterSet({'parameter_name' : 'y', 'neurons': list(analog_ids[8:12]), 'sheet_name' : 'V1_Exc_L4','mean' : False}),fig_param={'dpi' : 100,'figsize': (20,10)},plot_file_name='AnalogSignalEvolutionOffBar3.png').plot({'*.x_lim'  :(0,200),'*.y_label'  : 'offset'})
	
	if False:
            dsv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=1.0,y_axis_name=['exc. conductance trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
	    mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanExcCondON.png').plot()
	    dv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=1.0,y_axis_name=['inh. conductance trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
	    mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanInhCondON.png').plot()
            dsv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=1.0,y_axis_name=['vm trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
            mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanVmON.png').plot()

            dsv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=0.0,y_axis_name=['exc. conductance trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
            mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanExcCondOFF.png').plot()
            dsv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=0.0,y_axis_name=['inh. conductance trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
            mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanInhCondOFF.png').plot()
            dsv = param_filter_query(data_store,st_name='FlashedBar',analysis_algorithm='TrialMean',st_relative_luminance=0.0,y_axis_name=['vm trial-to-trial mean'],sheet_name='V1_Exc_L4',st_y=-0.5769230769230769)
            mozaik.visualization.plotting.AnalogSignalListPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4','neurons' : analog_ids.tolist(), 'mean' : True}),fig_param={'dpi' : 100,'figsize': (10,4)},plot_file_name='BarMeanVmOFF.png').plot()

        dsv = queries.param_filter_query(data_store,st_name='FlashedBar',st_relative_luminance=1.0)
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neurons' : lgn_on_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='Bar_XONRaster.png').plot({'SpikeRasterPlot.group_trials':True})
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neurons' : lgn_off_ids,'trial_averaged_histogram': False, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='Bar_XOFFRasterL4.png').plot({'SpikeRasterPlot.group_trials':True})
	
	#dsv = param_filter_query(data_store,st_name=['FlashedBar'],st_relative_luminance=0,st_y=-0.5769230769230769)    
	#RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neurons' : lgn_off_ids, 'trial_averaged_histogram' : True, 'spontaneous' : False}),plot_file_name="Bar_LGN_OFF_Bar_OFF.png",fig_param={'dpi' : 100,'figsize': (14,4)}).plot()
	#RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neurons' : lgn_on_ids, 'trial_averaged_histogram' : True, 'spontaneous' : False}),plot_file_name="Bar_LGN_ON_Bar_OFF.png",fig_param={'dpi' : 100,'figsize': (14,4)}).plot()

	#dsv = param_filter_query(data_store,st_name=['FlashedBar'],st_relative_luminance=1,st_y=-0.5769230769230769)    
	#RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neurons' : lgn_off_ids, 'trial_averaged_histogram' : True, 'spontaneous' : False}),plot_file_name="Bar_LGN_OFF_Bar_ON.png",fig_param={'dpi' : 100,'figsize': (14,4)}).plot()
	#RasterPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neurons' : lgn_on_ids, 'trial_averaged_histogram' : True, 'spontaneous' : False}),plot_file_name="Bar_LGN_ON_Bar_ON.png",fig_param={'dpi' : 100,'figsize': (14,4)}).plot()

    


    if nat_movies:        
	dsv = param_filter_query(data_store,st_name='NaturalImageWithEyeMovement')   
        overviews(dsv,"NI_")

        TrialToTrialVariabilityComparison(data_store,ParameterSet({'sheet_name1' : 'V1_Exc_L4','sheet_name2' : 'V1_Exc_L4','data_dg' : 0.93 , 'data_ni' : 1.19}),fig_param={'dpi' : 200,'figsize': (15,7.5)},plot_file_name='TrialToTrialVariabilityComparison.png').plot()

        dsv = param_filter_query(data_store,st_name='NaturalImageWithEyeMovement')    
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : l4_exc, 'sheet_activity' : {}, 'spontaneous' : True}),plot_file_name='NMExc.png',fig_param={'dpi' : 100,'figsize': (28,12)}).plot({'Vm_plot.y_lim' : (-70,-50),'Conductance_plot.y_lim' : (0,50.0)})
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : l4_inh, 'sheet_activity' : {}, 'spontaneous' : True}),plot_file_name='NMInh.png',fig_param={'dpi' : 100,'figsize': (28,12)}).plot({'Vm_plot.y_lim' : (-70,-50),'Conductance_plot.y_lim' : (0,50.0)})
                    
        #TrialCrossCorrelationAnalysis(data_store,ParameterSet({'neurons1' : list(analog_ids),'sheet_name1' : 'V1_Exc_L4','neurons2' : list([]),'sheet_name2' : 'V1_Exc_L2/3', 'window_length' : 250}),fig_param={"dpi" : 100,"figsize": (15,6.5)},plot_file_name="trial-to-trial-cross-correlation.png").plot({'*.Vm.title' : None, '*.fontsize' : 19})


    if gratings:    
	dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0,st_trial=1)
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : list(spike_ids),'trial_averaged_histogram': False, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='EvokedExcRasterTrial1.png').plot({'SpikeRasterPlot.group_trials':True})
	dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0,st_trial=2)
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : list(spike_ids),'trial_averaged_histogram': False, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='EvokedExcRasterTrial2.png').plot({'SpikeRasterPlot.group_trials':True})
	dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0,st_trial=3)
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : list(spike_ids),'trial_averaged_histogram': False, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='EvokedExcRasterTrial3.png').plot({'SpikeRasterPlot.group_trials':True})
	dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0,st_trial=4)
        RasterPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neurons' : list(spike_ids),'trial_averaged_histogram': False, 'spontaneous' : True}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='EvokedExcRasterTrial4.png').plot({'SpikeRasterPlot.group_trials':True})

        dsv = queries.param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name = 'V1_Exc_L4',st_orientation=0)
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='GratingExcAnalog1.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[1], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='GratingBarExcAnalog2.png').plot()
        OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[2], 'sheet_activity' : {}, 'spontaneous' : False}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='GratingBarExcAnalog3.png').plot()

        # tuninc curves
        #dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm=['TrialAveragedFiringRate','Analog_F0andF1'])    
        #PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids[:6]), 'sheet_name' : 'V1_Exc_L4','centered'  : True,'mean' : False, 'polar' : False, 'pool'  : False}),plot_file_name='TCsExcL4.png',fig_param={'dpi' : 100,'figsize': (15,7.5)}).plot({'TuningCurve F0_Inh_Cond.y_lim' : (0,180) , 'TuningCurve F0_Exc_Cond.y_lim' : (0,80)})
        #PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids_inh[:6]), 'sheet_name' : 'V1_Inh_L4','centered'  : True,'mean' : False, 'polar' : False, 'pool'  : False}),plot_file_name='TCsInhL4.png',fig_param={'dpi' : 100,'figsize': (15,7.5)}).plot({'TuningCurve F0_Inh_Cond.y_lim' : (0,180) , 'TuningCurve F0_Exc_Cond.y_lim' : (0,80)})


        Kremkow_plots.OrientationTuningSummary(data_store,ParameterSet({'exc_sheet_name': 'V1_Exc_L4','inh_sheet_name': 'V1_Inh_L4'}),fig_param={'dpi' : 100,'figsize': (15,9)},plot_file_name='OrientationTuningSummaryL4.png').plot()            

        OrientationTuningSummaryAnalogSignals(data_store,ParameterSet({'exc_sheet_name1': 'V1_Exc_L4','inh_sheet_name1': 'V1_Inh_L4','exc_sheet_name2': 'None','inh_sheet_name2': 'None'}),fig_param={'dpi' : 200,'figsize': (18,12)},plot_file_name='OrientationTuningSummaryAnalogSignals.png').plot({'*.fontsize' : 19,'*.y_lim' : (0,None)})            
        
	
        MRfig(param_filter_query(data_store,sheet_name=['V1_Exc_L4'],st_contrast=[100],st_name='FullfieldDriftingSinusoidalGrating'),ParameterSet({'SimpleSheetName' : 'V1_Exc_L4','ComplexSheetName' : 'None'}),plot_file_name='MR.png',fig_param={'dpi' : 100,'figsize': (19,12)}).plot()
        #MRfigReal(param_filter_query(data_store,sheet_name=['V1_Exc_L4'],st_contrast=[100],st_name='FullfieldDriftingSinusoidalGrating'),ParameterSet({'SimpleSheetName' : 'V1_Exc_L4','ComplexSheetName' : 'None'}),plot_file_name='MR.png',fig_param={'dpi' : 100,'figsize': (19,12)}).plot()
        
	TrialToTrialVariabilityComparison(data_store,ParameterSet({'sheet_name1' : 'V1_Exc_L4','sheet_name2' : 'V1_Exc_L4','data_dg' : 0.93 , 'data_ni' : 1.19}),fig_param={'dpi' : 200,'figsize': (15,7.5)},plot_file_name='TrialToTrialVariabilityComparison.png').plot()
        
        TrialCrossCorrelationAnalysis(data_store,ParameterSet({'neurons1' : list(analog_ids),'sheet_name1' : 'V1_Exc_L4','neurons2' : [],'sheet_name2' : 'V1_Exc_L2/3', 'window_length' : 250}),fig_param={"dpi" : 100,"figsize": (15,6.5)},plot_file_name="trial-to-trial-cross-correlation.png").plot({'*.Vm.title' : None, '*.fontsize' : 19})

    SpontActOverview(data_store,ParameterSet({'l4_exc_neuron' : analog_ids[0], 'l4_inh_neuron' : analog_ids_inh[0],'l23_exc_neuron' : -1,'l23_inh_neuron' : -1}),plot_file_name='SpontActOverview.png', fig_param={'dpi' : 200,'figsize': (18,14.5)}).plot()
    SpontStatisticsOverview(data_store,ParameterSet({}), fig_param={'dpi' : 200,'figsize': (18,12)},plot_file_name='SpontStatisticsOverview.png').plot()



def HirschFigure(data_store,):


    NeuronAnnotationsToPerNeuronValues(data_store,ParameterSet({})).analyse()
    analog_ids = param_filter_query(data_store,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_esyn_ids()
    analog_ids_inh = param_filter_query(data_store,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_esyn_ids()

    class ExportStimulusResponseData(Analysis):
          """
          This analysis exports paired stimulus vs response data. Its intended use is to generate input to
          ML models for identification of stimulus-response function. 

          If signal_type= Vm or cond_Eor cond_I, corresponding recorded signal will be exported.
          If signal_type=ASL, the analysis assumes a datastore filled with AnalogSignalList data structures of identical parametrization with the exception of stimulus.

          Stimulus-response pairs will be concatenated across all different segments or AnalogSignalList data structures in the data store view. 

          For each semgent or AnalogSignalList of signal length X ms, X/period data pairs (A,B) will be exported, where
          A is 2D matrix corresponding to the pixels of the stimulus presented during the given period in the visual field 
          (the stimulus is assumed to be constant during the period). B is the response signal averaged over the given period.

          Following structure will be dumped using the cpickle.dump method into the export file:
          {
            "stim" : ndarray,  #contains 3D ndarray of size (X,Y,T), where X,Y are the visual field dimensions, and T corresponds to the number of periods across all the segments or AnalogSignalLists in the provided data store view. 
            "resp" : ndarray,  #contains 2D ndarray of size (T,N), where T was explained above and N us the number of neurons.      
          }



          Other parameters
          ------------------- 
          period : float (ms)
                         The period over which to average the response signal. The stimulus has to be constant over this period of time.

          neurons : list(int)
                         List of neuron ids for which to export the response

          signal_type : str
                         Currently understood are [Vm,cond_E,cond_I, ASL]. The first three are the corresponding recorded signals. ASL is any AnalogSignalList deposited in the analysis data store. 

          file_name : str
                         The name of the file into which data will be stored. The file will be created in the directory containing the datastore. 
          """    
          required_parameters = ParameterSet({
              'period': float,  
              'neurons' : list,
              'signal_type' : str,
              'file_name' : str
          })      

          def perform_analysis(self):
                if self.parameters.signal_type == 'ASL':
                    assert queries.equal_ads(self.datastore,except_params=['stimulus_id'])
                    assert queries.ads_with_equal_stimulus_type(self.datastore)
                    # make sure that the length of all stimuli is multiple of frame length
                    assert all([(MozaikParametrized.idd(s).duration % MozaikParametrized.idd(asl.stimulus_id).frame_duration) == 0 for asl in self.datastore.get_analysis_result()])
                    frame_duration = MozaikParametrized.idd(self.datastore.get_analysis_result()[0].stimulus_id).frame_duration
                else:
                    assert queries.equal_stimulus_type(self.datastore)
                    # make sure that the length of all stimuli is multiple of frame length
                    assert all([(MozaikParametrized.idd(s).duration % MozaikParametrized.idd(s).frame_duration) == 0 for s in self.datastore.get_stimuli()])
                    frame_duration = MozaikParametrized.idd(self.datastore.get_stimuli()[0]).frame_duration


                if self.parameters.signal_type == 'ASL':
                    signals,stims = zip(*[(asl.get_asl_by_id(self.parameters.neurons),self.datastore.get_sensory_stimulus([asl.stimulus_id])[0]) for asl in queries.param_filter_query(self.datastore,identifier='AnalogSignalList').get_analysis_result()])
                elif self.parameters.signal_type == 'Vm':
                    signals,stims = zip(*[([seg.get_vm(n) for n in self.parameters.neurons],self.datastore.get_sensory_stimulus([st])[0]) for seg,st in zip(self.datastore.get_segments(),self.datastore.get_stimuli())])
                elif self.parameters.signal_type == 'cond_E':
                    signals,stims = zip(*[([seg.get_esyn(n) for n in self.parameters.neurons],self.datastore.get_sensory_stimulus([st])[0]) for seg,st in zip(self.datastore.get_segments(),self.datastore.get_stimuli())])                
                elif self.parameters.signal_type == 'cond_I':
                    signals,stims = zip(*[([seg.get_isyn(n) for n in self.parameters.neurons],self.datastore.get_sensory_stimulus([st])[0]) for seg,st in zip(self.datastore.get_segments(),self.datastore.get_stimuli())])

                signals = numpy.array([[numpy.reshape(s.magnitude[1:],(int((s.duration.rescale(qt.ms).magnitude-1)/self.parameters.period),-1)) for s in sig] for sig in signals])            
                # push neurons into first axes           
                signals = numpy.swapaxes(signals,0,1)  
                # concatenate over the different recordings or ASLs if there are multiple
                signals = [numpy.concatenate(s,axis=0)  for s in signals]  
                # push neurons last           
                signals = numpy.swapaxes(signals,0,1)
                signals = numpy.swapaxes(signals,1,2)  
                raw_signals = signals.copy()
                logger.info(numpy.shape(raw_signals))
                # average over the signal period
                signals = numpy.mean(signals[:,35:,:],axis=1)
                logger.info(numpy.shape(signals))

                # concatenate over the different recordings or ASLs
                stims = numpy.concatenate(stims)  
                logger.info(numpy.shape(stims))

                #cut up for the indiviudal stimulus presentations of length period
                sh = numpy.shape(stims)
                stims = numpy.reshape(stims,(-1,int(self.parameters.period/frame_duration),sh[1],sh[2]))
                logger.info(numpy.shape(stims))

                # check if the inputs are the same within each period 
                #for i in xrange(0,int(self.parameters.period/frame_duration)):
                #    assert numpy.all(stims[:,0,:,:]==stims[:,i,:,:])
                # remove the same stimuli by averaging over them
                stims = numpy.mean(stims[:,:2,:],axis=1)
                logger.info(numpy.shape(stims))
                return signals,raw_signals,stims

    dsv = param_filter_query(data_store,st_name='SparseNoise',sheet_name='V1_Exc_L4',st_direct_stimulation_name=None)
    signals,raw_signals,stims = ExportStimulusResponseData(dsv,ParameterSet({'period' : 70, 'neurons' : analog_ids.tolist(), 'signal_type' : "Vm", 'file_name' : "Vm.export"})).perform_analysis()        

    dsv = param_filter_query(data_store,st_name='SparseNoise',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=0)
    signals0,raw_signals0,stims0 = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "Vm", 'file_name' : "Vm.export"})).perform_analysis()
    signals_e,raw_signals_e,_ = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "cond_E", 'file_name' : "Vm.export"})).perform_analysis()
    signals_i,raw_signals_i,_ = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "cond_I", 'file_name' : "Vm.export"})).perform_analysis()

    dsv = param_filter_query(data_store,st_name='SparseNoise',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=-0.2)
    signals1,raw_signals1,stims1 = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "Vm", 'file_name' : "Vm.export"})).perform_analysis()

    dsv = param_filter_query(data_store,st_name='SparseNoise',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=0.1)
    signals01,raw_signals01,stims01 = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "Vm", 'file_name' : "Vm.export"})).perform_analysis()

    dsv = param_filter_query(data_store,st_name='SparseNoise',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=-0.1)
    signalsn02,raw_signalsn02,stimsn02 = ExportStimulusResponseData(dsv,ParameterSet({'period' : 161, 'neurons' : analog_ids.tolist(), 'signal_type' : "Vm", 'file_name' : "Vm.export"})).perform_analysis()
    
    # determine spontaneuos activity for each neuron and each current injection level
    dsv = param_filter_query(data_store,st_name='InternalStimulus')
    Analog_MeanSTDAndFanoFactor(dsv,ParameterSet({})).analyse()

    dsv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=0.0,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)')
    mean_spont_vm = dsv.get_analysis_result()[0].get_value_by_id(analog_ids)

    dsv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=-0.2,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)')
    mean_spont_vm_hyp2 =  dsv.get_analysis_result()[0].get_value_by_id(analog_ids)

    dsv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=0.1,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)')
    mean_spont_vm_dep =  dsv.get_analysis_result()[0].get_value_by_id(analog_ids)

    dsv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',st_direct_stimulation_name='Injection',st_current=-0.1,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)')
    mean_spont_vm_hyp1 = dsv.get_analysis_result()[0].get_value_by_id(analog_ids)

    rescaled_stims = (stims-50.0)/50.0
    pos = rescaled_stims[0]*0
    neg = rescaled_stims[0]*0
    for i in xrange(stims.shape[0]):
        pos += numpy.clip(rescaled_stims[i],a_min=0,a_max=None)
        neg += numpy.clip(rescaled_stims[i],a_max=0,a_min=None)

    RFs=[]
    for j in xrange(0,25):
        apos = rescaled_stims[0]*0
        aneg = rescaled_stims[0]*0
        for i in xrange(stims.shape[0]):
            apos += numpy.clip(rescaled_stims[i],a_min=0,a_max=None)*signals[i,j]
            aneg += numpy.clip(rescaled_stims[i],a_min=None,a_max=0)*signals[i,j]
    
        b = numpy.divide(apos,pos) - numpy.divide(aneg,neg)
        RFs.append(b)

    RFs=numpy.nan_to_num(RFs)

    def cond(stims,I1,I2,I3,I4,raw_signals_I1,raw_signals_I2,raw_signals_I3,raw_signals_I4,RFs,neuron_indexes,coordsx,coordsy,centerx,centery,excitatory_polarities,raw_signalsE,raw_signalsI):
        period= 21#70#105
        blank = 140
        pylab.figure(figsize=(15,10))
        pylab.subplots_adjust(wspace=None, hspace=None)


        for j in xrange(1,25):
            pylab.subplot(4,10,j)
            pylab.imshow(RFs[j-1][25:55,25:55])
        pylab.savefig("RFs.png")


        def RF_contour_plot(RFs,s,sign,cenx,ceny):
            RF = RFs[cenx-9:cenx+9,ceny-9:ceny+9][numpy.arange(0,18,3),:][:,numpy.arange(0,18,3)]
            mmin=numpy.min(numpy.array(RFs))
            mmax=numpy.max(numpy.array(RFs))

            pylab.imshow(RF*0,vmin=-max(-mmin,mmax),vmax=max(-mmin,mmax),cmap='gray')
            pylab.contour(RF,
                          levels=[mmin,mmin*0.9,mmin*0.8,mmin*0.7,mmin*0.6,mmin*0.5,mmin*0.4,mmin*0.3,mmin*0.2,mmax*0.2,mmax*0.3,mmax*0.4,mmax*0.5,mmax*0.6,mmax*0.7,mmax*0.8,mmax*0.9,mmax],
                          colors=[(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.2,0.2,0.2),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8),(0.8,0.8,0.8)])
            pylab.contourf(RF,
                          levels=[mmin,mmin*0.9,mmin*0.8,mmin*0.7,mmin*0.6,mmin*0.5,mmin*0.4,mmin*0.3,mmin*0.2],
                          colors=[(0.1,0.1,0.1),(0.14,0.14,0.14),(0.18,0.18,0.18),(0.22,0.22,0.22),(0.26,0.26,0.26),(0.3,0.3,0.3),(0.34,0.34,0.34),(0.38,0.38,0.38)])
            pylab.contourf(RF,
                          levels=[mmax*0.2,mmax*0.3,mmax*0.4,mmax*0.5,mmax*0.6,mmax*0.7,mmax*0.8,mmax*0.9,mmax],
                          colors=[(0.62,0.62,0.62),(0.66,0.66,0.66),(0.7,0.7,0.7),(0.74,0.74,0.74),(0.78,0.78,0.78),(0.82,0.82,0.82),(0.86,0.86,0.86),(0.9,0.9,0.9)])

            layer=numpy.mean(s,axis=0)[cenx-9:cenx+9,ceny-9:ceny+9][numpy.arange(0,18,3),:][:,numpy.arange(0,18,3)]
            if sign == 1:
	        masked = numpy.ma.masked_where(layer != 100, layer)
            else:
	        masked = numpy.ma.masked_where(layer != 0, layer)
            pylab.imshow(masked,vmin=0,vmax=100,cmap='gray',zorder=15) 
            for x in range(7):
                pylab.axhline(x-0.5, lw=2, color=(0.3,0.3,0.3), zorder=5)
                pylab.axvline(x-0.5, lw=2, color=(0.3,0.3,0.3), zorder=5)
            pylab.xticks([])
            pylab.yticks([])

        def plot_Vm(raw_signals,sign,neuron,msvm,scalebar=False,esyn=None,isyn=None):
            #vm = numpy.concatenate([raw_signals[sign-1,:,neuron],raw_signals[sign,:,neuron],raw_signals[sign+1,:,neuron],raw_signals[sign+2,:,neuron]],axis=1)
            vm = numpy.concatenate([raw_signals[sign-1,:,neuron],raw_signals[sign,:,neuron]],axis=1)[:,140:]
            vm = numpy.squeeze(numpy.mean(vm[:,:],axis=0))
            pylab.plot(vm,'k',lw=2)
            mmin=min(numpy.min(vm),msvm)
            pylab.ylim(mmin-4,mmin+40)
            #pylab.plot([period,2*period-blank],[mmin-1,mmin-1],'k',lw=6)
            pylab.plot([21,63],[mmin-3,mmin-3],'k',lw=6)
            pylab.plot([0,len(vm)],[msvm,msvm],'k--',lw=1)
	    pylab.axis('off')
            if scalebar:
               pylab.plot([len(vm)-21,len(vm)],[mmin-1.5,mmin-1.5],'k',lw=2)
               pylab.plot([len(vm),len(vm)-0.01],[mmin-1.5,mmin+8.5],'k',lw=2)

            if esyn is not None:
                esyn = numpy.concatenate([esyn[sign-1,:,neuron],esyn[sign,:,neuron]],axis=1)
                esyn = numpy.squeeze(numpy.mean(esyn[:,140:],axis=0)*1000)
                isyn = numpy.concatenate([isyn[sign-1,:,neuron],isyn[sign,:,neuron]],axis=1)
                isyn = numpy.squeeze(numpy.mean(isyn[:,140:],axis=0)*1000)
		ax2 = pylab.gca().twinx()
                pylab.ylim(-30,30)
                pylab.gca().spines['left'].set_visible(False)
	        pylab.gca().spines['top'].set_visible(False)
	        pylab.gca().spines['bottom'].set_visible(False)
                if scalebar:
	    	    pylab.gca().spines['right'].set_bounds(0, 30)
            	    pylab.yticks([0,15,30])
		    pylab.ylabel('nS')
                else: 
                    pylab.gca().spines['right'].set_visible(False)
            	    pylab.yticks([])            
        	pylab.plot(esyn,'r',lw=2)
        	pylab.plot(isyn,'b',lw=2)

        def plot_cond_change(I1,I2,raw_signals1,raw_signals2,sign,neuron,first):
            #b = numpy.squeeze(numpy.mean(numpy.concatenate([raw_signals1[sign-1,:,neuron],raw_signals1[sign,:,neuron],raw_signals1[sign+1,:,neuron],raw_signals1[sign+2,:,neuron]],axis=1),axis=0))
            #c = numpy.squeeze(numpy.mean(numpy.concatenate([raw_signals2[sign-1,:,neuron],raw_signals2[sign,:,neuron],raw_signals2[sign+1,:,neuron],raw_signals2[sign+2,:,neuron]],axis=1),axis=0))
            b = numpy.squeeze(numpy.mean(numpy.concatenate([raw_signals1[sign-1,:,neuron],raw_signals1[sign,:,neuron]],axis=1),axis=0))
            c = numpy.squeeze(numpy.mean(numpy.concatenate([raw_signals2[sign-1,:,neuron],raw_signals2[sign,:,neuron]],axis=1),axis=0))
            cond_change = (I1-I2)/(b-c)
            #cond_change = cond_change/numpy.mean(cond_change[period-blank:period])*100
	    cond_change = cond_change/numpy.mean(cond_change[blank+period-35:period+blank])*100
            pylab.plot(cond_change[140:],'k',lw=2)
            pylab.ylim(70,300)
            #pylab.plot([period,2*period-blank],[-9,-9],'k',lw=6)
            pylab.plot([21,63],[72,72],'k',lw=6)
	    pylab.gca().spines['right'].set_visible(False)
	    pylab.gca().spines['top'].set_visible(False)
	    pylab.gca().spines['bottom'].set_visible(False)
            pylab.xticks([])
            if first:
		    pylab.ylabel(r"$\Delta g(\%)$",fontsize=15)
	            pylab.gca().spines['left'].set_linewidth(2)
	            pylab.yticks([100,200,300],fontsize=15)
	            pylab.gca().tick_params(direction='out', length=3, width=2, colors='k')
            else:
		    pylab.gca().spines['left'].set_visible(False)
		    pylab.yticks([])
            

        pylab.figure(figsize=(10,15))
        for i in range(0,len(neuron_indexes)):    
            if i == 3: 
		sb = True 
	    else: 
		sb = False
            logger.info(i)
            plus=numpy.where(stims[:,coordsx[i],coordsy[i]]==100)[0]
            minus=numpy.where(stims[:,coordsx[i],coordsy[i]]==0)[0]
            exc_stim = plus if excitatory_polarities[i]==1 else minus
            inh_stim = plus if excitatory_polarities[i]==-1 else minus

	    logger.info("B:"+str(numpy.shape(exc_stim)))


            n=len(neuron_indexes)
            pylab.subplot(8,n,1+i)
            RF_contour_plot(RFs[neuron_indexes[i]],stims[exc_stim],excitatory_polarities[i],centerx[i],centery[i])
            
            pylab.subplot(8,n,1*n+1+i)
            plot_Vm(raw_signals_I1,exc_stim,neuron_indexes[i],mean_spont_vm[neuron_indexes[i]],scalebar=sb,esyn=raw_signalsE,isyn=raw_signalsI)

            pylab.subplot(8,n,2*n+1+i)
            RF_contour_plot(RFs[neuron_indexes[i]],stims[inh_stim],-excitatory_polarities[i],centerx[i],centery[i])

            pylab.subplot(8,n,3*n+1+i)
            plot_Vm(raw_signals_I1,inh_stim,neuron_indexes[i],mean_spont_vm[neuron_indexes[i]],scalebar=sb,esyn=raw_signalsE,isyn=raw_signalsI)

            pylab.subplot(8,n,4*n+1+i)
            plot_Vm(raw_signals_I2,inh_stim,neuron_indexes[i],mean_spont_vm_dep[neuron_indexes[i]],scalebar=sb)

            pylab.subplot(8,n,5*n+1+i)
            plot_Vm(raw_signals_I3,inh_stim,neuron_indexes[i],mean_spont_vm_hyp1[neuron_indexes[i]],scalebar=sb)

            pylab.subplot(8,n,6*n+1+i)
            plot_Vm(raw_signals_I4,inh_stim,neuron_indexes[i],mean_spont_vm_hyp2[neuron_indexes[i]],scalebar=sb)

            pylab.subplot(8,n,7*n+1+i)
            plot_cond_change(I1,I3,raw_signals_I1,raw_signals_I3,inh_stim,neuron_indexes[i],i==0)
    logger.info("S:"+str(numpy.shape(raw_signals0)))

    cond(stims0,0,0.2,-0.1,-0.2,raw_signals0,raw_signals01,raw_signalsn02,raw_signals1,RFs,[5,6,7,19],[44,40,35,35],[47,37,38,31],[43,40,37,37],[43,34,43,37],[-1,1,-1,1],raw_signals_e,raw_signals_i)
    pylab.savefig('Hirsch1.png',dpi=300)
    cond(stims0,0,0.2,-0.1,-0.2,raw_signals0,raw_signals01,raw_signalsn02,raw_signals1,RFs,[10,12,13,15],[34,37,35,32],[34,40,37,34],[37,43,37,37],[37,43,37,37],[1,1,1,1],raw_signals_e,raw_signals_i)
    pylab.savefig('Hirsch2.png',dpi=300)
    cond(stims0,0,0.2,-0.1,-0.2,raw_signals0,raw_signals01,raw_signalsn02,raw_signals1,RFs,[5,6,10,19],[44,40,34,35],[47,37,34,31],[43,40,37,37],[43,34,37,37],[-1,1,1,1],raw_signals_e,raw_signals_i)
    pylab.savefig('Hirsch.png',dpi=300)
