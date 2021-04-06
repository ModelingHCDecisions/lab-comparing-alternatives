import SimPy.Plots.SamplePaths as Path
import SimPy.Plots.Histogram as Hist
import SimPy.Statistics as Stat
import InputData as D


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # create a summary statistics
    survival_time_stat = Stat.SummaryStat(name='Survival time statistics',
                                          data=multi_cohort.multiCohortOutcomes.meanSurvivalTimes)

    # get mean and t-based confidence interval
    mean = survival_time_stat.get_mean()
    pred_int = survival_time_stat.get_PI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)


def draw_survival_curves_and_histograms(multi_cohort_no_drug, multi_cohort_with_drug):
    """ draws the histograms of average survival time
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # get survival curves of both treatments
    survival_curves = [
        multi_cohort_no_drug.multiCohortOutcomes.survivalCurves,
        multi_cohort_with_drug.multiCohortOutcomes.survivalCurves
    ]

    # graph survival curve
    Path.plot_sets_of_sample_paths(
        sets_of_sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step',
        y_label='Number of alive patients',
        legends=['No Drug', 'With Drug'],
        color_codes=['blue', 'orange'],
        transparency=0.25
    )

    # histograms of average survival times
    set_of_survival_times = [
        multi_cohort_no_drug.multiCohortOutcomes.meanSurvivalTimes,
        multi_cohort_with_drug.multiCohortOutcomes.meanSurvivalTimes
    ]

    # graph histograms
    Hist.plot_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of average patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=0.5,
        legends=['No Drug', 'With Drug'],
        color_codes=['blue', 'orange'],
        transparency=0.5,
        x_range=[6, 20],
    )


def print_comparative_outcomes(multi_cohort_no_drug, multi_cohort_with_drug):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase_stat = Stat.DifferenceStatIndp(
        name='Increase in mean survival time',
        x=multi_cohort_with_drug.multiCohortOutcomes.meanSurvivalTimes,
        y_ref=multi_cohort_no_drug.multiCohortOutcomes.meanSurvivalTimes
    )
    # mean and prediction interval
    mean = increase_stat.get_mean()
    pred_int = increase_stat.get_PI(alpha=D.ALPHA)

    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)

    # % increase in mean survival time
    relative_diff_stat = Stat.RelativeDifferenceIndp(
        name='% increase in mean survival time',
        x=multi_cohort_with_drug.multiCohortOutcomes.meanSurvivalTimes,
        y_ref=multi_cohort_no_drug.multiCohortOutcomes.meanSurvivalTimes
    )
    # estimate and prediction interval
    mean = relative_diff_stat.get_mean()
    pred_int = relative_diff_stat.get_PI(alpha=D.ALPHA)

    print("Expected percentage increase in mean survival time and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)
