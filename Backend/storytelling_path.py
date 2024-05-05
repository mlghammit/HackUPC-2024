import matplotlib.pyplot as plt

starting_point = (0, 0)
forgot = (2, 2)
banyo = (3, 3)
checkin = (6, 0)
gate = (6, 6)

all_points = [starting_point, forgot, checkin, banyo, gate]

xx = [p[0] for p in all_points]
yy = [p[1] for p in all_points]
plt.plot(xx, yy)