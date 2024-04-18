import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('data/performance_capas.csv')
    last_epoch = data[data['epoch']==20].iloc[:,1:].round(4)
    last_epoch_mean = last_epoch.mean().round(4)
    last_epoch_std = last_epoch.std().round(4)
    last_epoch['run'] = data['run']
    print(last_epoch)
    print(last_epoch_mean)
    print(last_epoch_std)
    last_epoch.to_csv('stats.csv')     