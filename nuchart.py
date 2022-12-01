from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path

class AMETable:
    def __init__(self):
        self.data_path = Path(__file__).parent / "data"
        self.df = pd.read_csv(  self.data_path / "AME" / "mass_nuc.txt", delim_whitespace=True, index_col=False)
        self.df['EL'] = self.df['EL'].astype('string')
        for c in self.df.columns:
            if c != 'EL':
                self.df[c] = self.df[c].astype(float)

    def select_row(self, zaid):
        a,z = from_zaid(zaid)
        mask = (self.df['A'] == a) & (self.df['Z'] == z)
        return self.df.loc[ mask ]

    def element_name(self, zaid):
        row = self.select_row(zaid)
        return row["EL"].to_string().split()[1]

def plot_binding_energy():
    ame_table = AMETable()
    df = ame_table.df
    plt.scatter(df['N'].to_numpy(), df['Z'].to_numpy(), c=df['BINDING_ENERGY/A_keV'].to_numpy()/1000, marker='s')
    plt.colorbar(label="E per nucleon [MeV/A]")
    plt.xlabel("N")
    plt.ylabel("Z")
    plt.show()

def plot_kd_wlh_dps():
    pass

def plot_FY():
    pass

if __name__ == "__main__":
    plot_binding_energy()
