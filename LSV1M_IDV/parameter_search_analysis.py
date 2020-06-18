import sys
from mozaik.meta_workflow.parameter_search import parameter_search_run_script_distributed_slurm_IoV
assert len(sys.argv) == 2
directory = sys.argv[1]

parameter_search_run_script_distributed_slurm_IoV("SelfSustainedPushPull",directory,'run_analysis.py',6)

CombinationParameterSearch(SlurmSequentialBackendGifNew(num_threads=64,num_mpi=1),{
				         'sheets.l4_cortex_exc.K' : [1300],
				         'sheets.l4_cortex_exc.params.sx' : [7000],
				         'sheets.l4_cortex_exc.params.density' : [600,700],
				         'sheets.retina_lgn.params.gain_control.gain' : [10],
				         'sheets.retina_lgn.params.noise.stdev' : [1.4],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_E' : [7.5],
				         'sheets.l4_cortex_exc.params.cell.params.tau_syn_I' : [13],
				         'sheets.l4_cortex_exc.AfferentConnection.size' : [0.17],
				         'sheets.l4_cortex_exc.AfferentConnection.aspect_ratio' : [0.4],
				         'sheets.l4_cortex_exc.L4ExcL4InhConnection.base_weight' : [0.0009],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.base_weight' : [0.0018],
				         'sheets.l4_cortex_exc.L4ExcL4ExcConnection.short_term_plasticity.tau_rec' : [10],
				         'sheets.l4_cortex_exc.AfferentConnection.short_term_plasticity.tau_rec' : [150],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.short_term_plasticity.tau_rec' : [15],
#									     'sheets.l4_cortex_exc.L4ExcL4ExcConnection.weight_functions.f1.params.sigma' : [1.0,1.4,2.0],
#									     'sheets.l4_cortex_exc.L4ExcL4InhConnection.weight_functions.f1.params.sigma' : [1.4,2.0,3.0],
				         'sheets.l4_cortex_inh.L4InhL4ExcConnection.weight_functions.f1.params.sigma' : [1.2,1.4],
					 'sheets.l23_cortex_exc.L23ExcL4InhConnection.weight_functions.f1.params.arborization_constant' : [300],
				         }).run_parameter_search()
