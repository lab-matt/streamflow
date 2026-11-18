import numpy as np
import matplotlib.pyplot as plt

def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    array1 = np.genfromtxt(filename,
                       delimiter=',',
                       dtype=str,
                       skip_header=1)

    dates = array1[:,0].astype('datetime64')
    flows = array1[:,1:].astype(float)
    return dates, flows

def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.style.use('default')
    plt.plot(dates,flows[:,0], color='purple', label ='10163000')
    plt.plot(dates,flows[:,1], color='g', label ='10155200')
    plt.plot(dates,flows[:,2], color='b', label ='10155500')
    plt.plot(dates,flows[:,3], color='y', label ='10154200')
    plt.plot(dates,flows[:,4], color='r', label ='10155000')

    plt.title('Provo River Streamflow Data (2021)')
    plt.legend(title='Site Numbers',loc='upper right')

    plt.ylabel('Flowrate (cfs)')
    plt.xlabel('Date')
    # Matplotlib chooses best date formatting.
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def summarize(dates, flows, sites):
    ''' The maximum flow (cfs) and the date and time it occurred
    The minimum flow (cfs)
    The average flow (cfs) '''
    max_flow = np.max(flows, axis=0)
    min_flow = np.min(flows, axis=0)
    avg_flow = np.mean(flows, axis=0)

    max_flow_dates = dates[np.argmax(flows, axis=0)]
    min_flow_dates = dates[np.argmin(flows, axis=0)]

    for i, site in enumerate(sites):
        print(f"Site {site}:")
        print(f"  Max Flow: {max_flow[i]} cfs on {max_flow_dates[i]}")
        print(f"  Min Flow: {min_flow[i]} cfs on {min_flow_dates[i]}")
        print(f"  Avg Flow: {avg_flow[i]:.2f} cfs\n")

# It should also save the same information to a file named streamflow_summary.csv. You can write the file with open() and write(), or put the results in a pandas DataFrame and use to_csv().'''

    with open('streamflow_summary.csv', 'w') as f:
        f.write('Site,Max Flow (cfs),Max Flow Date,Min Flow (cfs),Min Flow Date,Avg Flow (cfs)\n')
        for i, site in enumerate(sites):
            f.write(f"{site},{max_flow[i]},{max_flow_dates[i]},{min_flow[i]},{min_flow_dates[i]},{avg_flow[i]:.2f}\n")



# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
summarize(dates, flows, sites)
