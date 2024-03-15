import pandas as pd

data1 = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\ipl-matches.csv")
data2 = pd.read_csv(r'C:\Users\Akashay\Desktop\IPL_Ball_by_Ball_2008_2022.csv')

file_path = r"C:\Users\Akashay\Desktop\IPL project\most_runs_average_strikerate.csv"
run = pd.read_csv(file_path)
teams = pd.read_csv(r"C:\Users\Akashay\Desktop\IPL project\teams.csv")

data = data1.merge(data2, on='ID', how='inner')

data1.drop_duplicates()
data.drop_duplicates()
data2.drop_duplicates()

data1.fillna('No data', inplace=True)
data.fillna('No data', inplace=True)
data2.fillna('No data', inplace=True)

# batting csv

high_run = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\most run.csv")

strike_rate = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\Highest strike rates.csv")

high_avg = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\top avg.csv")

Most_hundreds = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\Most hundreds.csv")

most_sixes = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\Most sixes.csv")

most_ducks = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\batting\most 0.csv")

# bolling record

most_wickets = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\bolling\Most wickets.csv")

best_economy_rates = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\bolling\Best economy rates.csv")

best_strike_rates = pd.read_csv(r"C:\Users\Akashay\Desktop\Web ipl data\bolling\Best strike rates.csv")

five_wickets_in_an_innings = pd.read_csv(
    r"C:\Users\Akashay\Desktop\Web ipl data\bolling\List of five-wickets-in-an-innings.csv")

best_bowling_fig_in_an_innings = pd.read_csv(
    r"C:\Users\Akashay\Desktop\Web ipl data\bolling\Best bowling figures in an_innings.csv")


def year_list():
    year = data['Season'].unique()
    return year


def top_batsman(season):
    df = data[data['Season'] == season]
    return df.groupby('batter')['total_run'].sum().sort_values(ascending=False).head(10)


def top_bowler(season):
    df = data[data['Season'] == season]
    return df.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).head(10)


def batter() -> object:
    return data['batter'].drop_duplicates()


def top_batsman_player(batter):
    df = data[data['batter'] == batter]
    df = df.groupby('Season')['total_run'].sum().reset_index()
    return df


def performance(player):
    return run[run['batsman'] == player]


def all_teams():
    te = teams['team']
    return te


def teams_info(selected_teams):
    return teams[teams['team'] == selected_teams]


def ground_name():
    gh = data.groupby('Venue').size().sort_values(ascending=False).head(15).reset_index()
    gh.rename(columns={0: 'Total_Matches', 1: 'Venue'}, inplace=True)
    return gh


def ground_win_info():
    toss_win_same_as_winner = data[data['TossWinner'] == data['WinningTeam']].groupby('Venue').size()

    total_matches = data.groupby('Venue').size()

    percentage_wins = (toss_win_same_as_winner / total_matches) * 100

    venue_summary = pd.DataFrame({

        'No_of Toss winnner Team & match winning ': toss_win_same_as_winner,
        'Percentage_of match Wins': percentage_wins
    })
    return venue_summary


def list_batting_record():
    z = ['High_run', 'High strike rate', 'High avg', 'Most hundreds', 'most sixes', 'most ducks']
    return z


def high_run_f():
    return high_run


def strike_rate_f():
    return strike_rate


def high_avg_f():
    return high_avg


def Most_hundreds_f():
    return Most_hundreds


def most_sixes_f():
    return most_sixes


def most_ducks_f():
    return most_ducks


def list_bolling_record():
    op = ['Most_wickets', 'Best_economy_rates', 'Best_strike_rates', 'Five_wickets_in_an_innings',
          'Best_bowling_fig_in_an_innings']
    return op


def most_wickets_f():
    return most_wickets


def best_economy_rates_f():
    return best_economy_rates


def best_strike_rates_f():
    return best_strike_rates


def five_wickets_in_an_innings_f():
    return five_wickets_in_an_innings


def best_bowling_fig_in_an_innings_f():
    return best_bowling_fig_in_an_innings


