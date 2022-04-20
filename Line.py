import matplotlib.pyplot as plt

Year = [2017, 2018, 2019, 2020]
Net_min = [-4160.1, -3646.2, -2794.7, -2320.7]
Net_max = [-4428.4, -3881.3, -2975.0, -2470.4]

plt.plot(Year, Net_min)
plt.plot(Year, Net_max)

fig, ax = plt.subplots()
ax.fill_between(Net_min, Net_max)


plt.legend()
plt.show()