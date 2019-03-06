
MORTALITY_PROB = 0.1        # annual probability of mortality
DRUG_EFFECT_RATIO = 0.75    # drug effectiveness:
                            # ratio of the annual mortality probability when using the drug to when not using the drug.
TIME_STEPS = 1000    # simulation length
ALPHA = 0.05        # significance level

# settings for steady-state simulation
SIM_POP_SIZE = 2000     # population size of the simulated cohort

# settings for transient-state simulation
REAL_POP_SIZE = 100     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000  # number of simulated cohorts used for making projections
