import deampy.plots.histogram as hist
import deampy.plots.sample_paths as path
import deampy.statistics as stats

import CompareInputData as D


def print_outcomes(calibrated_model, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param calibrated_model: calibrated model
    :param strategy_name: the name of the selected therapy
    """

    # print expected mean survival time
    print(strategy_name)
    print("  Expected mean survival time (years) and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0),
          calibrated_model.get_mean_survival_time_proj_interval(alpha=D.ALPHA))


def draw_survival_curves_and_histograms(calibrated_model_no_drug, calibrated_model_with_drug):
    """ draws the histograms of average survival time
    :param calibrated_model_no_drug: calibrated model simulated when drug is not available
    :param calibrated_model_with_drug: calibrated model simulated when drug is available
    """

    # get survival curves of both treatments
    survival_curves = [
        calibrated_model_no_drug.multiCohorts.multiCohortOutcomes.survivalCurves,
        calibrated_model_with_drug.multiCohorts.multiCohortOutcomes.survivalCurves
    ]

    # graph survival curve
    path.plot_sets_of_sample_paths(
        sets_of_sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step',
        y_label='Number of alive patients',
        legends=['No Drug', 'With Drug'],
        color_codes=['blue', 'orange'],
        transparency=0.25,
        file_name='figs/calibrated/survival_curves.png'
    )

    # histograms of average survival times
    set_of_survival_times = [
        calibrated_model_no_drug.multiCohorts.multiCohortOutcomes.meanSurvivalTimes,
        calibrated_model_with_drug.multiCohorts.multiCohortOutcomes.meanSurvivalTimes
    ]

    # graph histograms
    hist.plot_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of average patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=0.5,
        legends=['No Drug', 'With Drug'],
        color_codes=['blue', 'orange'],
        transparency=0.5,
        x_range=[6, 20],
        file_name='figs/calibrated/survival_times.png'
    )


def print_comparative_outcomes(calibrated_model_no_drug, calibrated_model_with_drug):
    """ prints expected and percentage increase in average survival time when drug is available
    :param calibrated_model_no_drug: calibrated model simulated when drug is not available
    :param calibrated_model_with_drug: calibrated model simulated when drug is available
    """
    # increase in survival time
    increase_stat =

    # mean and prediction interval
    mean = increase_stat.get_mean()
    pred_int = increase_stat.get_PI(alpha=D.ALPHA)

    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)

    # % increase in mean survival time
    relative_diff_stat =


    # estimate and prediction interval
    mean = relative_diff_stat.get_mean()
    pred_int = relative_diff_stat.get_PI(alpha=D.ALPHA)

    print("Expected percentage increase in mean survival time and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)
