
MORTALITY_PROB = 0.1        # annual probability of mortality
TREATMENT_RR = 0.75         # relative risk (RR) of mortality under treatment:
                            # ratio of the annual mortality probability when using the drug
                            # to when not using the drug.
TIME_STEPS = 1000    # simulation length
ALPHA = 0.05        # significance level

# settings to calculate confidence interval of mean survival time
SIM_POP_SIZE = 1000     # population size of the simulated cohort

# settings to calculate prediction interval of mean survival time
REAL_POP_SIZE = 100     # size of the real cohort for which we'd like to project its outcomes
NUM_SIM_COHORTS = 200  # number of simulated cohorts used for making projections
