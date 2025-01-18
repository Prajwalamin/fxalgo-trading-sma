import matplotlib.pyplot as plt

def plot_data(data, cols=["SMA_S", "SMA_M" , "SMA_L", "price"], title="Price Data"):
    """Plots the specified columns from the data."""
    # data = data[data.index.year == 2017]
    # data[cols].plot(figsize=(12, 8), title=title)
    # data["position"].plot(figsize=(12, 8), title=title)
    data.loc[:, ["price", "SMA_S", "SMA_M", "SMA_L", "position"]].plot(figsize = (12, 8), fontsize = 12, secondary_y = "position")
    plt.show()

