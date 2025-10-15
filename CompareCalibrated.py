import calib_src.classes as Cls
import CompareInputData as D
import SupportCalibrated as Support
from calib_defs import CALIBRATION_ROOT_DIR

#TODO: to be updated

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
    drug_effectiveness_ratio=D.TREATMENT_RR)
# simulate the calibrated model
calibratedModelWithDrug.simulate(num_of_simulated_cohorts=D.NUM_SIM_COHORTS,
                                 cohort_size=D.SIM_POP_SIZE,
                                 time_steps=D.TIME_STEPS)

# report mean and projection interval of expected survival time
Support.print_outcomes(calibrated_model=calibratedModelNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(calibrated_model=calibratedModelWithDrug,
                       strategy_name='When drug is available:')

# draw histograms
Support.plot_survival_curves_and_histograms(calibrated_model_no_drug=calibratedModelNoDrug,
                                            calibrated_model_with_drug=calibratedModelWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(calibrated_model_no_drug=calibratedModelNoDrug,
                                   calibrated_model_with_drug=calibratedModelWithDrug)
