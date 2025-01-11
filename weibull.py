import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from invoice_processing import df_processor
from invoice_reader import relay_reader
from invoice_reader import light_reader
import numpy as np
columns = ("tail", 'pn', 'cost', 'tach_time', 'total_time', 'start', 'stop')

# create df and feed into the preprocessing function

light_matrix = light_reader()
nav_light = pd.DataFrame(columns= columns, data= light_matrix)
nav_light = df_processor(nav_light)

relay_matrix = relay_reader()
relay = pd.DataFrame(columns= columns, data= relay_matrix)
relay = df_processor(relay)

############################################################################################
# Relay
relay_downtime_by_tail = relay.groupby('tail')['on_gnd'].apply(list).reset_index()
relay_total_cost_by_tail = relay.groupby('tail')['cost'].apply(sum).reset_index()
relay_charges= relay.groupby('tail')['cost'].apply(list).reset_index()

###########################################################################################
# Nav Light
nav_light_downtime_by_tail = nav_light.groupby("tail")['on_gnd'].apply(list).reset_index()
nav_light_total_cost_by_tail = nav_light.groupby("tail")['cost'].apply(sum).reset_index()
nav_light_charges = nav_light.groupby("tail")['cost'].apply(list).reset_index()

###########################################################################################

# Uncomment for descriptive statistics

#print(relay_downtime_by_tail, '\n')
#print(relay_cost_by_tail, '\n')

#print(nav_light_downtime_by_tail, '\n')
#print(nav_light_cost_by_tail, '\n')

nav_light_down_data = [i for i in nav_light_downtime_by_tail['on_gnd']]
nav_light_cost_data = [i for i in nav_light_charges['cost']]

relay_down_data = [i for i in relay_downtime_by_tail['on_gnd']]
relay_cost_data = [i for i in relay_charges['cost']]

# Weibull analysis is from Chat GPT, so there may be some problems with the implementation
# I have never studied survivability statistics in detail but this is a good time to experiment

def weibull_analysis(datasets, labels=None):
    def reliability(t, shape, scale):
        return np.exp(-(t / scale) ** shape)

    def failure_rate(t, shape, scale):
        return (shape / scale) * (t / scale) ** (shape - 1)

    colors = ("blue", "orange", "green")

    plt.figure(figsize=(10, 6))
    for i, data in enumerate(datasets):
        # Fit the data to a Weibull distribution using SciPy
        params = stats.weibull_min.fit(data, floc=0)
        shape_fitted, loc_fitted, scale_fitted = params

        # Generate a Weibull probability plot for each dataset
        probplot = stats.probplot(data, dist="weibull_min", sparams=(shape_fitted, loc_fitted, scale_fitted))

        # Extract the theoretical quantiles and ordered values
        theoretical_quantiles, ordered_values = probplot[0]

        # Plot the data with the assigned color
        plt.scatter(theoretical_quantiles, ordered_values, color=colors[i % len(colors)], label=f'Dataset {i + 1}')

        # Plot the fitted line
        slope, intercept = probplot[1][0], probplot[1][1]
        plt.plot(theoretical_quantiles, slope * theoretical_quantiles + intercept, color=colors[i % len(colors)])

    plt.title('Weibull Probability Plot')
    plt.grid(True)
    if labels:
        plt.legend(labels)
    else:
        plt.legend([f'Dataset {i + 1}' for i in range(len(datasets))])
    plt.show()

    # Define time points
    max_time = max(max(data) for data in datasets)
    time_points = np.linspace(0, max_time, 100)

    plt.figure(figsize=(10, 6))

    # Reliability and failure rate plots
    for i, data in enumerate(datasets):
        params = stats.weibull_min.fit(data, floc=0)
        shape_fitted, loc_fitted, scale_fitted = params

        reliability_values = reliability(time_points, shape_fitted, scale_fitted)
        failure_rate_values = failure_rate(time_points, shape_fitted, scale_fitted)

        # Reliability plot
        plt.subplot(2, 1, 1)
        plt.plot(time_points, reliability_values, label=f'Reliability {labels[i] if labels else f"Dataset {i + 1}"}')

        # Failure rate plot
        plt.subplot(2, 1, 2)
        plt.plot(time_points, failure_rate_values, label=f'Failure Rate {labels[i] if labels else f"Dataset {i + 1}"}',
                 color=f'C{i}')

    plt.subplot(2, 1, 1)
    plt.title('Reliability Function')
    plt.xlabel('Days')
    plt.ylabel('Reliability')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.title('Failure Rate Function')
    plt.xlabel('Days')
    plt.ylabel('Failure Rate')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


#weibull_analysis(nav_light_down_data, labels=["N173WM", "N191JG", "N191SA"])

weibull_analysis(relay_down_data, labels=["N173WM", "N191JG", "N191SA"])