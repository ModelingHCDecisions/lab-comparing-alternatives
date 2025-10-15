import CompareInputData as D
import SupportConfidenceInterval as Support
import SurvivalModelClasses as Cls

# create a cohort of patients for when the drug is not available
cohortNoDrug = Cls.Cohort(
    id=1,
    pop_size=D.SIM_POP_SIZE,
    mortality_prob=D.MORTALITY_PROB)
# simulate the cohort
cohortNoDrug.simulate(seed=1, n_time_steps=D.TIME_STEPS)

# create a cohort of patients for when the drug is available
cohortWithDrug = Cls.Cohort(
    id=2,   # since we don't have a mechanism to pair the simulated patients in
            # cohorts with and without the drug, we chose a different random number seed
            # for these two cohorts so that they remain independent of each other.
    pop_size=D.SIM_POP_SIZE,
    mortality_prob=D.MORTALITY_PROB * D.TREATMENT_RR)
# simulate the cohort
cohortWithDrug.simulate(seed=2, n_time_steps=D.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(simulated_cohort=cohortNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(simulated_cohort=cohortWithDrug,
                       strategy_name='When drug available:')

# draw survival curves and histograms
Support.plor_survival_curves_and_histograms(cohort_no_drug=cohortNoDrug,
                                            cohort_with_drug=cohortWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(cohort_no_drug=cohortNoDrug,
                                   cohort_with_drug=cohortWithDrug)
