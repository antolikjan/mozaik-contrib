# rearrange analogsignalarray and spiketrains
from mozaik.storage.datastore import Hdf5DataStore, PickledDataStore
import mozaik.tools.mozaik_parametrized as MP
from mozaik.storage.queries import *
from mozaik.controller import run_experiments,  setup_logging
import quantities as pq
import neo
import cPickle
import numpy
import sys
sys.path.append('/home/jan/projects/mozaik/')
# /////////////////////////////////////////////////////////////////////////////


def swapAnalogSignals(segment, unitOnTop='mV'):
    analogOnTop = 0
    idxOnTop = -1
    # take the first analogsignal
    analogSwap = segment.analogsignalarrays[0]
    # search for 'unit' array
    for idx, ansig in enumerate(segment.analogsignalarrays):
        # check its unit, if it's mV
        if getattr(pq, unitOnTop) == ansig.units:
            # if the searched idx is not the first
            if idx > 0:
                # set the analogsignal and idx for swap
                analogOnTop = ansig
                idxOnTop = idx
                break
            else:  # if is already on top, return the same segment
                return segment
    # swap analogsignals
    if idxOnTop != -1:
        segment.analogsignalarrays[0] = analogOnTop
        segment.analogsignalarrays[idxOnTop] = analogSwap
    # result
    return segment


# assumes the first channel is already the one
def swapSpikeTrains(segment, anLabel='source_ids', stLabel='source_id', separator=' '):
    # convert source_ids into a list
    id_list = []
    id_list = str(segment.analogsignalarrays[0].annotations[anLabel]).strip(
        '[]').split(separator)  # map(int, ...)
    # print id_list
    # swap spiketrains
    stSwap = 0
    idxSwap = 0
    for idx, train in enumerate(segment.spiketrains):
        # search annotation value inside id_list
        if str(train.annotations[stLabel]) in id_list:
            # if found, swap it with the top ones
            # print "%i - source_id: %s" % (idx,train.annotations[stLabel])
            # save
            stSwap = segment.spiketrains[idxSwap]
            segment.spiketrains[idxSwap] = train
            segment.spiketrains[idx] = stSwap
            # increment idx for next swap
            idxSwap = idxSwap+1
    # result
    return segment


def createFileFromSegmentList(list_segment, fileName):
    """
    Store the list of segments in elphy file
    """
    bl = neo.Block()
    for seg in list_segment:
        new_seg = swapAnalogSignals(seg)
        new_seg = swapSpikeTrains(new_seg)
        bl.segments.append(new_seg)
    # Neo -> Elphy
    r = neo.io.ElphyIO(filename=fileName)
    r.write_block(bl)


def addSpikes(segment, threshold):
    ids = segment.get_stored_vm_ids()

    for a in segment.analogsignalarrays:
        if a.name == 'v':
            vs = a

    for i in ids:
        index = vs.annotations['source_ids'].tolist().index(i)
        for time in segment.get_spiketrain(i):
            if vs[int(time/vs.sampling_period)+1, index].magnitude == threshold:
                vs[int(time/vs.sampling_period)+1, index] = -20 * pq.mV
            elif vs[int(time/vs.sampling_period)+2, index].magnitude == threshold:
                vs[int(time/vs.sampling_period)+2, index] = -20 * pq.mV
            else:
                raise ValueError("The Vm was not at the threshold level after the spike as expected:  [%g , %g]  Tr: %g" % (
                    vm[int(time/vm.sampling_period)+1], vm[int(time/vm.sampling_period)+2], threshold))


def exportToElphy(data_store_location, elphy_export_location, sheets=None, threshold=None):
    import os.path
    if not os.path.isdir(elphy_export_location):
        if os.path.exists(elphy_export_location):
            raise ValueError("The elphy export path is not a directory")
        else:
            os.makedirs(elphy_export_location)

    setup_logging()
    data_store = PickledDataStore(load=True, parameters=ParameterSet(
        {'root_directory': data_store_location, 'store_stimuli': False}))
    ps = MP.parameter_value_list([MP.MozaikParametrized.idd(
        s) for s in data_store.get_stimuli()], 'name')
    for i, sn in enumerate(ps):
        if sheets == None:
            sheets = data_store.sheets()

        for shn in sheets:
            dsv = param_filter_query(data_store, st_name=sn, sheet_name=shn)
            if dsv.get_stimuli() == []:
                continue
            varying_parameters = MP.varying_parameters(
                [MP.MozaikParametrized.idd(s) for s in dsv.get_stimuli()])

            segments, stimuli = MP.colapse(dsv.get_segments(), [MP.MozaikParametrized.idd(
                s) for s in dsv.get_stimuli()], parameter_list=['trial'], allow_non_identical_objects=True)
            j = 0
            for segs, st in zip(segments, stimuli):
                # just make sure all segments are fully loaded, in future this should probably soreted out such that this line can be deleted
                for s in segs:
                    s.load_full()

                # create file name:
                filename = "name=" + sn + "#" + "sheet_name=" + shn
                for pn in varying_parameters:
                    if pn != "trial":
                        filename += "#" + \
                            str(pn) + "=" + \
                            str(getattr(MP.MozaikParametrized.idd(st), pn))
                path = os.path.join(elphy_export_location, filename+".dat")

                # if the threshold is defined add spikes into Vms
                if threshold != None:
                    for seg in segs:
                        addSpikes(seg, threshold)

                createFileFromSegmentList(segs, path)
                print "Finished saving file %d/%d for sheet %s and %d-th stimulus" % (j+1, len(segments), shn, i)
                # release segments from memory
                for s in segs:
                    s.release()
                j = j + 1
        print "Finished saving %d/%d stimulus" % (i+1, len(ps))
