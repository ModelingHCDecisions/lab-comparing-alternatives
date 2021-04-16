import InputData as D
import CalibrationClasses as Cls
import SupportCalibrated as Support
from definitions import CALIBRATION_ROOT_DIR

# create a calibrated model for when drug is not available
calibratedModelNoDrug = Cls.CalibratedModel(
    csv_file_name=CALIBRATION_ROOT_DIR+'\CalibrationResults.csv')
# simulate the calibrated model
calibratedModelNoDrug.simulate(num_of_simulated_cohorts=D.NUM_SIM_COHORTS,
                               cohort_size=D.SIM_POP_SIZE,
                               time_steps=D.TIME_STEPS)

# create a calibrated model when drug is available
calibratedModelWithDrug = Cls.CalibratedModel(
    csv_file_name=CALIBRATION_ROOT_DIR+'\CalibrationResults.csv',
    drug_effectiveness_ratio=D.DRUG_EFFECT_RATIO)
# simulate the calibrated model
initial_seed = D.NUM_SIM_COHORTS * D.SIM_POP_SIZE
calibratedModelWithDrug.simulate(num_of_simulated_cohorts=D.NUM_SIM_COHORTS,
                                 cohort_size=D.SIM_POP_SIZE,
                                 time_steps=D.TIME_STEPS,
                                 cohort_ids=range(initial_seed, initial_seed + D.NUM_SIM_COHORTS))

# report mean and projection interval of expected survival time
Support.print_outcomes(calibrated_model=calibratedModelNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(calibrated_model=calibratedModelWithDrug,
                       strategy_name='When drug is available:')

# draw histograms
Support.draw_survival_curves_and_histograms(calibrated_model_no_drug=calibratedModelNoDrug,
                                            calibrated_model_with_drug=calibratedModelWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(calibrated_model_no_drug=calibratedModelNoDrug,
                                   calibrated_model_with_drug=calibratedModelWithDrug)
