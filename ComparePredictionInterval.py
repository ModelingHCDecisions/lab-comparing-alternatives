import CompareInputData as D
import MultiSurvivalModelClasses as Cls
import SupportPredictionInterval as Support

# create multiple cohorts for when the drug is not available
multiCohortNoDrug = Cls.MultiCohort(
    ids=range(D.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[D.REAL_POP_SIZE] * D.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[D.MORTALITY_PROB] * D.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortNoDrug.simulate(seeds=range(D.NUM_SIM_COHORTS), n_time_steps=D.TIME_STEPS)

# create multiple cohorts for when the drug is available
multiCohortWithDrug = Cls.MultiCohort(
    ids=range(D.NUM_SIM_COHORTS, 2 * D.NUM_SIM_COHORTS),
        # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
        # since we don't have a mechanism to pair the simulated patients in
        # cohorts with and without the drug, we chose a different random number seed
        # for these two cohorts so that they remain independent of each other.
    pop_sizes=[D.REAL_POP_SIZE] * D.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[D.MORTALITY_PROB * D.TREATMENT_RR] * D.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortWithDrug.simulate(seeds=range(D.NUM_SIM_COHORTS, 2 * D.NUM_SIM_COHORTS), n_time_steps=D.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(multi_cohort=multiCohortNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(multi_cohort=multiCohortWithDrug,
                       strategy_name='When drug is available:')

# draw histograms of average survival time
Support.plot_survival_curves_and_histograms(multi_cohort_no_drug=multiCohortNoDrug,
                                            multi_cohort_with_drug=multiCohortWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_no_drug=multiCohortNoDrug,
                                   multi_cohort_with_drug=multiCohortWithDrug)
