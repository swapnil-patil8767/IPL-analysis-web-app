import pandas as pd

data1 = pd.read_csv(r'C:\Users\Akashay\Desktop\ipl-matches.csv')


def preprocess(data1):
    data1.drop_duplicates()
    data1.fillna('No data', inplace=True)
    df = data1[data1['MatchNumber'] == 'Final'][['Season', 'WinningTeam']]
    df.reset_index(drop=True, inplace=True)
    return df


# wick kip rec
Most_dismissals_in_a_series = pd.read_csv(
    r"C:\Users\Akashay\Desktop\Web ipl data\Wicketkeeping records\Most dismissals in a series.csv")

Most_dismissals = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\Wicketkeeping records\Most dismissals.csv")
Most_dismissals_in_an_innings = pd.read_csv(
    r"C:\Users\Akashay\Desktop\Web ipl data\Wicketkeeping records\Most dismissals in an innings.csv")

# Fielding records

Most_catches_in_a_match = pd.read_csv(
    r"C:\Users\Akashay\Desktop\Web ipl data\Fielding records\Most catches in a match.csv")
Most_catches = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\Fielding records\Most catches.csv")

#partnership_records

Highest_partnerships_by_runs = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\Partnership records\Highest partnerships by runs.csv")
Highest_partnerships_by_wicket = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\Partnership records\Highest partnerships by wicket.csv")

def list_dis_record():
    po = ['Most dismissals in a series', 'Most dismissals', 'Most dismissals in an innings']
    return po


def Most_dismissals_in_a_series_f():
    return Most_dismissals_in_a_series


def Most_dismissals_f():
    return Most_dismissals


def Most_dismissals_in_an_innings_f():
    return Most_dismissals_in_an_innings


def list_filding_re():
    wq = ['Most catches in a match', 'Most catches']
    return wq


def Most_catches_f():
    return Most_catches


def Most_catches_in_a_match_f():
    return Most_catches_in_a_match

def list_partnership_re():
    qw=['Highest partnerships by runs','Highest partnerships by wicket']
    return qw

def Highest_partnerships_by_runs_f():
    return Highest_partnerships_by_runs

def Highest_partnerships_by_wicket_f():
    return Highest_partnerships_by_wicket