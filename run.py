import pandas as pd
import numpy as np
import mne
mne.set_log_level('error')

df = "data.nir"

nf = open(df, "r")
line = nf.readline()

while not line.startswith("-4"):
    line = nf.readline()

line = nf.readline().split()
n = int((len(line)-2)/3)
arr = []

while line[0]!='-1':
    ln = []
    for i in range(n):
        ln.append(int(line[i*3+1]))
        ln.append(int(line[i*3+3]))
    arr.append(ln)
    ln = []
    line = nf.readline().split()

arr = np.array(arr).transpose()
pd.DataFrame(arr).to_csv("data.csv")
data = pd.read_csv("data.csv")

ch_names = [
    "S1_D1 730","S2_D1 850",
    "S1_D2 730","S2_D2 850",
    "S1_D3 730","S2_D3 850",
    "S1_D4 730","S2_D4 850",
    "S1_D5 730","S2_D5 850",
    "S1_D6 730","S2_D6 850",
    "S1_D7 730","S2_D7 850",
    "S1_D8 730","S2_D8 850",
    "S1_D9 730","S2_D9 850",
    "S1_D10 730","S2_D10 850",
    "S1_D11 730","S2_D11 850",
    "S1_D12 730","S2_D12 850",
    "S1_D13 730","S2_D13 850",
    "S1_D14 730","S2_D14 850",
    "S1_D15 730","S2_D15 850",
    "S1_D16 730","S2_D16 850",
    "S1_D17 730","S2_D17 850",
    "S1_D18 730","S2_D18 850"
]

ch_types = ["fnirs_od"] * 36
sfreq = 10.0

info = mne.create_info(ch_names=ch_names, ch_types=ch_types, sfreq=sfreq)
raw = mne.io.RawArray(data, info)
raw.load_data()