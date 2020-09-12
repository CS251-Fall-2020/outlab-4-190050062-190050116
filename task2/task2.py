import argparse
import pandas as pd
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True, help="Data file path")
args = vars(ap.parse_args())

df = pd.read_csv(r"{}".format(args["data"]))

ins = df.groupby("instance")
count = 1
for instance, frame1 in ins:
    al_ep = frame1.groupby(["algorithm", "epsilon"])
    leg = []

    for l, frame2 in al_ep:
        if l[0] == "epsilon-greedy":
            leg.append("{p} with epsilon = {q}".format(p=l[0], q=l[1]))
        else:
            leg.append(str(l[0]))

        (frame2.groupby("horizon")["REG"]).mean().plot(
            kind="line", legend=True)

    plt.title("Instance {} - both in log scales".format(count))
    plt.xlabel("horizon")
    plt.ylabel("Regret")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend(leg)
    filename = "instance{}.png".format(count)
    plt.savefig(str(filename))
    plt.clf()
    count += 1
