# %% Getting Started, Reading CSV and creating a Points average across the league in wins and losses
# 
import pandas as pd

df = pd.read_csv("NFL Sportsbook 2020.csv")
df.columns	

winleagueAVEpts = df['PtsW'].mean()
losleagueAVEpts = df['PtsL'].mean()


# %% Drop some columns from dataframe 
df = pd.read_csv("NFL Sportsbook 2020.csv").drop(['Week', 'Time','TOW','TOL'],axis=1)

# %% Dropping rows from dataframe 
rows = df[ df['Unnamed: 7'] == 'preview' ].index 
df.drop(rows, inplace = True)

# %%  Clean up the data frame a bit

df['Unnamed: 5'] = df['Unnamed: 5'].str.replace('@','1')
df['Unnamed: 5'] = df['Unnamed: 5'].fillna(0)


# %% Create Variable for Team wins to date (12/16/2020)
# Cleveland Browns 
CLE_wins_td = 9
#Pittsburgh Steelers 
PITT_wins_td = 11
# Baltimore Ravens 
BAL_wins_td = 8
# Cincinnati Bengals 
CIN_wins_td = 2
# Buffalo Bills
BUF_wins_td = 10
# Miami Dolphins 
MIAMI_wins_td = 8
# New England Patriots 
NE_wins_td = 6
# New York Jets 
NYJ_wins_td = 0
# Tennessee Titans 
TEN_wins_td = 9
# Indianapolis Colts
IND_wins_td = 9
# Houston Texans
HOU_wins_td = 4
# Jacksonville Jaguars
JAX_wins_td = 1
# Kansas City Chiefs
KC_wins_td = 12
# Las Vegas Raiders
LV_wins_td = 7
# Denver Broncos 
DEN_wins_td = 5
# Los Angeles Chargers
LAC_wins_td = 4
# Washington Football Team
WAS_wins_td = 6
# New York Giants
NYG_wins_td = 5
# Philadelphia Eagles 
PHI_wins_td = 4
# Dallas Cowboys
DAL_wins_td = 4
# Green Bay Packers
GB_wins_td = 10
# Minnesota Vikings
MIN_wins_td = 6
# Chicago Bears
CHI_wins_td = 6
# Detroit Lions
DET_wins_td = 5
# New Orleans Saints
NO_wins_td = 10
# Tampa Bay Buccaneers
TB_wins_td = 8
# Atlanta Falcons
ATL_wins_td = 4
# Carolina Panthers
CAR_wins_td = 4
# Los Angeles Rams
LAR_wins_td = 9
# Seattle Seahawks
SEA_wins_td = 9
# Arizona Cardinals
ARI_wins_td = 7
# San Francisco 49ers
SF_wins_td = 5

 # %% 
 # Create a metric for Total average points scored by each team across the AFC

 # Buffalo Bills
BUF_win_ave_p = df.loc[df['Winner/tie'] == 'Buffalo Bills', 'PtsW'].mean()
BUF_los_ave_p = df.loc[df['Loser/tie'] == 'Buffalo Bills', 'PtsL'].mean()
BUF_total_ave = (BUF_win_ave_p + BUF_los_ave_p)/2

# Miami Dolphins
MIAMI_win_ave_p = df.loc[df['Winner/tie'] == 'Miami Dolphins', 'PtsW'].mean()
MIAMI_los_ave_p = df.loc[df['Loser/tie'] == 'Miami Dolphins', 'PtsL'].mean()
MIAMI_total_ave = (MIAMI_win_ave_p + MIAMI_los_ave_p)/2

# New England Patriots
NE_win_ave_p = df.loc[df['Winner/tie'] == 'New England Patriots', 'PtsW'].mean()
NE_los_ave_p = df.loc[df['Loser/tie'] == 'New England Patriots', 'PtsL'].mean()
NE_total_ave = (NE_win_ave_p + NE_los_ave_p)/2

# New York Jets
NYJ_win_ave_p = df.loc[df['Winner/tie'] == 'New York Jets', 'PtsW'].mean()
NYJ_los_ave_p = df.loc[df['Loser/tie'] == 'New York Jets', 'PtsL'].mean()
NYJ_total_ave = (NYJ_win_ave_p + NYJ_los_ave_p)/2

# PITTsburgh Steelers
PITT_win_ave_p = df.loc[df['Winner/tie'] == 'Pittsburgh Steelers', 'PtsW'].mean()
PITT_los_ave_p = df.loc[df['Loser/tie'] == 'Pittsburgh Steelers', 'PtsL'].mean()
PITT_total_ave = (PITT_win_ave_p + PITT_los_ave_p)/2

# Cleveland Browns
CLE_win_ave_p = df.loc[df['Winner/tie'] == 'Cleveland Browns', 'PtsW'].mean()
CLE_los_ave_p = df.loc[df['Loser/tie'] == 'Cleveland Browns', 'PtsL'].mean()
CLE_total_ave = (CLE_win_ave_p + CLE_los_ave_p)/2

# Baltimore Ravens
BAL_win_ave_p = df.loc[df['Winner/tie'] == 'Baltimore Ravens', 'PtsW'].mean()
BAL_los_ave_p = df.loc[df['Loser/tie'] == 'Baltimore Ravens', 'PtsL'].mean()
BAL_total_ave = (BAL_win_ave_p + BAL_los_ave_p)/2

# Cincinnati Bengals
CIN_win_ave_p = df.loc[df['Winner/tie'] == 'Cincinnati Bengals', 'PtsW'].mean()
CIN_los_ave_p = df.loc[df['Loser/tie'] == 'Cincinnati Bengals', 'PtsL'].mean()
CIN_total_ave = (CIN_win_ave_p + CIN_los_ave_p)/2

# Tennessee Titans
TEN_win_ave_p = df.loc[df['Winner/tie'] == 'Tennessee Titans', 'PtsW'].mean()
TEN_los_ave_p = df.loc[df['Loser/tie'] == 'Tennessee Titans', 'PtsL'].mean()
TEN_total_ave = (TEN_win_ave_p + TEN_los_ave_p)/2

# Indianapolis Colts
IND_win_ave_p = df.loc[df['Winner/tie'] == 'Indianapolis Colts', 'PtsW'].mean()
IND_los_ave_p = df.loc[df['Loser/tie'] == 'Indianapolis Colts', 'PtsL'].mean()
IND_total_ave = (IND_win_ave_p + IND_los_ave_p)/2

# Houston Texans 
HOU_win_ave_p = df.loc[df['Winner/tie'] == 'Houston Texans', 'PtsW'].mean()
HOU_los_ave_p = df.loc[df['Loser/tie'] == 'Houston Texans', 'PtsL'].mean()
HOU_total_ave = (HOU_win_ave_p + HOU_los_ave_p)/2

# Jacksonville Jaguars
JAX_win_ave_p = df.loc[df['Winner/tie'] == 'Jacksonville Jaguars', 'PtsW'].mean()
JAX_los_ave_p = df.loc[df['Loser/tie'] == 'Jacksonville Jaguars', 'PtsL'].mean()
JAX_total_ave = (JAX_win_ave_p + JAX_los_ave_p)/2

# Kansas City Chiefs
KC_win_ave_p = df.loc[df['Winner/tie'] == 'Kansas City Chiefs', 'PtsW'].mean()
KC_los_ave_p = df.loc[df['Loser/tie'] == 'Kansas City Chiefs', 'PtsL'].mean()
KC_total_ave = (KC_win_ave_p + KC_los_ave_p)/2

# Las Vegas Raiders
LV_win_ave_p = df.loc[df['Winner/tie'] == 'Las Vegas Raiders', 'PtsW'].mean()
LV_los_ave_p = df.loc[df['Loser/tie'] == 'Las Vegas Raiders', 'PtsL'].mean()
LV_total_ave = (LV_win_ave_p + LV_los_ave_p)/2

# Denver Broncos
DEN_win_ave_p = df.loc[df['Winner/tie'] == 'Denver Broncos', 'PtsW'].mean()
DEN_los_ave_p = df.loc[df['Loser/tie'] == 'Denver Broncos', 'PtsL'].mean()
DEN_total_ave = (DEN_win_ave_p + DEN_los_ave_p)/2

# Los Angeles Chargers
LAC_win_ave_p = df.loc[df['Winner/tie'] == 'Los Angeles Chargers', 'PtsW'].mean()
LAC_los_ave_p = df.loc[df['Loser/tie'] == 'Los Angeles Chargers', 'PtsL'].mean()
LAC_total_ave = (LAC_win_ave_p + LAC_los_ave_p)/2

# %% Same for the NFC Teams

# Washington Football Team
WAS_win_ave_p = df.loc[df['Winner/tie'] == 'Washington Football Team', 'PtsW'].mean()
WAS_los_ave_p = df.loc[df['Loser/tie'] == 'Washington Football Team', 'PtsL'].mean()
WAS_total_ave = (WAS_win_ave_p + WAS_los_ave_p)/2

# New York Giants
NYG_win_ave_p = df.loc[df['Winner/tie'] == 'New York Giants', 'PtsW'].mean()
NYG_los_ave_p = df.loc[df['Loser/tie'] == 'New York Giants', 'PtsL'].mean()
NYG_total_ave = (NYG_win_ave_p + NYG_los_ave_p)/2

# Philadelphia Eagles
PHI_win_ave_p = df.loc[df['Winner/tie'] == 'Philadelphia Eagles', 'PtsW'].mean()
PHI_los_ave_p = df.loc[df['Loser/tie'] == 'Philadelphia Eagles', 'PtsL'].mean()
PHI_total_ave = (PHI_win_ave_p + PHI_los_ave_p)/2

# Dallas Cowboys
DAL_win_ave_p = df.loc[df['Winner/tie'] == 'Dallas Cowboys', 'PtsW'].mean()
DAL_los_ave_p = df.loc[df['Loser/tie'] == 'Dallas Cowboys', 'PtsL'].mean()
DAL_total_ave = (DAL_win_ave_p + DAL_los_ave_p)/2

# Green Bay Packers
GB_win_ave_p = df.loc[df['Winner/tie'] == 'Green Bay Packers', 'PtsW'].mean()
GB_los_ave_p = df.loc[df['Loser/tie'] == 'Green Bay Packers', 'PtsL'].mean()
GB_total_ave = (GB_win_ave_p + GB_los_ave_p)/2

# Minnesota Vikings
MIN_win_ave_p = df.loc[df['Winner/tie'] == 'Minnesota Vikings', 'PtsW'].mean()
MIN_los_ave_p = df.loc[df['Loser/tie'] == 'Minnesota Vikings', 'PtsL'].mean()
MIN_total_ave = (MIN_win_ave_p + MIN_los_ave_p)/2

# Chicago Bears
CHI_win_ave_p = df.loc[df['Winner/tie'] == 'Chicago Bears', 'PtsW'].mean()
CHI_los_ave_p = df.loc[df['Loser/tie'] == 'Chicago Bears', 'PtsL'].mean()
CHI_total_ave = (CHI_win_ave_p + CHI_los_ave_p)/2

# Detroit Lions
DET_win_ave_p = df.loc[df['Winner/tie'] == 'Detroit Lions', 'PtsW'].mean()
DET_los_ave_p = df.loc[df['Loser/tie'] == 'Detroit Lions', 'PtsL'].mean()
DET_total_ave = (DET_win_ave_p + DET_los_ave_p)/2

# New Orleans Saints
NO_win_ave_p = df.loc[df['Winner/tie'] == 'New Orleans Saints', 'PtsW'].mean()
NO_los_ave_p = df.loc[df['Loser/tie'] == 'New Orleans Saints', 'PtsL'].mean()
NO_total_ave = (NO_win_ave_p + NO_los_ave_p)/2

# Tampa Bay Buccaneers
TB_win_ave_p = df.loc[df['Winner/tie'] == 'Tampa Bay Buccaneers', 'PtsW'].mean()
TB_los_ave_p = df.loc[df['Loser/tie'] == 'Tampa Bay Buccaneers', 'PtsL'].mean()
TB_total_ave = (TB_win_ave_p + TB_los_ave_p)/2

# Atlants Falcons
ATL_win_ave_p = df.loc[df['Winner/tie'] == 'Atlanta Falcons', 'PtsW'].mean()
ATL_los_ave_p = df.loc[df['Loser/tie'] == 'Atlanta Falcons', 'PtsL'].mean()
ATL_total_ave = (ATL_win_ave_p + ATL_los_ave_p)/2

# Carolina Panthers
CAR_win_ave_p = df.loc[df['Winner/tie'] == 'Carolina Panthers', 'PtsW'].mean()
CAR_los_ave_p = df.loc[df['Loser/tie'] == 'Carolina Panthers', 'PtsL'].mean()
CAR_total_ave = (CAR_win_ave_p + CAR_los_ave_p)/2

# Los Angeles Rams
LAR_win_ave_p = df.loc[df['Winner/tie'] == 'Los Angeles Rams', 'PtsW'].mean()
LAR_los_ave_p = df.loc[df['Loser/tie'] == 'Los Angeles Rams', 'PtsL'].mean()
LAR_total_ave = (LAR_win_ave_p + LAR_los_ave_p)/2

# Seattle Seahawks
SEA_win_ave_p = df.loc[df['Winner/tie'] == 'Seattle Seahawks', 'PtsW'].mean()
SEA_los_ave_p = df.loc[df['Loser/tie'] == 'Seattle Seahawks', 'PtsL'].mean()
SEA_total_ave = (SEA_win_ave_p + SEA_los_ave_p)/2

# Arizone Cardinals
ARI_win_ave_p = df.loc[df['Winner/tie'] == 'Arizona Cardinals', 'PtsW'].mean()
ARI_los_ave_p = df.loc[df['Loser/tie'] == 'Arizona Cardinals', 'PtsL'].mean()
ARI_total_ave = (ARI_win_ave_p + ARI_los_ave_p)/2

# San Francisco 49ers
SF_win_ave_p = df.loc[df['Winner/tie'] == 'San Francisco 49ers', 'PtsW'].mean()
SF_los_ave_p = df.loc[df['Loser/tie'] == 'San Francisco 49ers', 'PtsL'].mean()
SF_total_ave = (SF_win_ave_p + SF_los_ave_p)/2



# %% Creating metrics for the Divisions

AFC_win_ave_p = ((BUF_win_ave_p) + (MIAMI_win_ave_p) + (NE_win_ave_p) +
 + (PITT_win_ave_p) + (CLE_win_ave_p)+ (BAL_win_ave_p) +
 (CIN_win_ave_p) + (HOU_win_ave_p) + (JAX_win_ave_p) + (IND_win_ave_p) +
 (TEN_win_ave_p) + (KC_win_ave_p) + (DEN_win_ave_p) + (LV_win_ave_p) + 
 (LAC_win_ave_p))/16

NFC_win_ave_p = ((PHI_win_ave_p) + (NYG_win_ave_p) + (WAS_win_ave_p) +
 (DAL_win_ave_p) + (GB_win_ave_p) + (CHI_win_ave_p) + (MIN_win_ave_p) +
 (DET_win_ave_p) + (NO_win_ave_p) + (ATL_win_ave_p) + (TB_win_ave_p) +
(CAR_win_ave_p) + (LAR_win_ave_p) + (SEA_win_ave_p) + (ARI_win_ave_p) + 
(SF_win_ave_p))/16

AFC_los_ave_p =((BUF_los_ave_p) + (MIAMI_los_ave_p) + (NE_los_ave_p) +
 (NYJ_los_ave_p) + (PITT_los_ave_p) + (CLE_los_ave_p) + (BAL_los_ave_p) +
 (CIN_los_ave_p) + (HOU_los_ave_p) + (JAX_los_ave_p) + (IND_los_ave_p) +
 (TEN_los_ave_p) + (KC_los_ave_p) + (DEN_los_ave_p) + (LV_los_ave_p) + 
 (LAC_los_ave_p))/16

NFC_los_ave_p = ((PHI_los_ave_p) + (NYG_los_ave_p) + (WAS_los_ave_p) +
 (DAL_los_ave_p) + (GB_los_ave_p) + (CHI_los_ave_p) + (MIN_los_ave_p) +
 (DET_los_ave_p) + (NO_los_ave_p) + (ATL_los_ave_p) + (TB_los_ave_p) +
 (CAR_los_ave_p) + (LAR_los_ave_p) + (SEA_los_ave_p) + (ARI_los_ave_p) + 
 (SF_los_ave_p))/16

AFC_total_ave = (AFC_win_ave_p + AFC_los_ave_p)/2
NFC_total_ave = (NFC_win_ave_p + NFC_los_ave_p)/2

#%% Creating offensive and defensive metrics for AFC teams

#Buffalo Bills
BUF_off_metric = winleagueAVEpts/BUF_win_ave_p
BUF_def_metric = losleagueAVEpts/BUF_los_ave_p

# Miami Dolphins
MIAMI_off_metric = winleagueAVEpts/MIAMI_win_ave_p
MIAMI_def_metric = losleagueAVEpts/MIAMI_los_ave_p

# New England Patriots
NE_off_metric = winleagueAVEpts/NE_win_ave_p
NE_def_metric = losleagueAVEpts/NE_los_ave_p

# New York Jets
NYJ_off_metric = winleagueAVEpts/NYJ_win_ave_p
NYJ_def_metric = losleagueAVEpts/NYJ_los_ave_p

# Pittsburgh Steelers
PITT_off_metric = winleagueAVEpts/PITT_win_ave_p
PITT_def_metric = losleagueAVEpts/PITT_los_ave_p

# Cleveland Browns
CLE_off_metric = winleagueAVEpts/CLE_win_ave_p
CLE_def_metric = losleagueAVEpts/CLE_los_ave_p

# Baltimore Ravens
BAL_off_metric = winleagueAVEpts/BAL_win_ave_p
BAL_def_metric = losleagueAVEpts/BAL_los_ave_p

# Cincinnati Bengals
CIN_off_metric = winleagueAVEpts/CIN_win_ave_p
CIN_def_metric = losleagueAVEpts/CIN_los_ave_p

# Houston Texans
HOU_off_metric = winleagueAVEpts/HOU_win_ave_p
HOU_def_metric = losleagueAVEpts/HOU_los_ave_p

# Jacksonville Jaguars
JAX_off_metric = winleagueAVEpts/JAX_win_ave_p
JAX_def_metric = losleagueAVEpts/JAX_los_ave_p

# Indianapolis Colts
IND_off_metric = winleagueAVEpts/IND_win_ave_p
IND_def_metric = losleagueAVEpts/IND_los_ave_p

# Tennnessee Titans
TEN_off_metric = winleagueAVEpts/TEN_win_ave_p
TEN_def_metric = losleagueAVEpts/TEN_los_ave_p

# Kansas City Chiefs
KC_off_metric = winleagueAVEpts/KC_win_ave_p
KC_def_metric = losleagueAVEpts/KC_los_ave_p

# Denver Broncos
DEN_off_metric = winleagueAVEpts/DEN_win_ave_p
DEN_def_metric = losleagueAVEpts/DEN_los_ave_p

# Las Vegas Raiders
LV_off_metric = winleagueAVEpts/LV_win_ave_p
LV_def_metric = losleagueAVEpts/LV_los_ave_p

# Los Angeles Chargers
LAC_off_metric = winleagueAVEpts/LAC_win_ave_p
LAC_def_metric = losleagueAVEpts/LAC_los_ave_p

# %% Create offensive/defensive metrics for NFC teams

# Philadelphia Eagles
PHI_off_metric = winleagueAVEpts/PHI_win_ave_p
PHI_def_metric = losleagueAVEpts/PHI_los_ave_p

# New York Giants
NYG_off_metric = winleagueAVEpts/NYG_win_ave_p
NYG_def_metric = losleagueAVEpts/NYG_los_ave_p

# Washington Football Team
WAS_off_metric = winleagueAVEpts/WAS_win_ave_p
WAS_def_metric = losleagueAVEpts/WAS_los_ave_p

# Dallas Cowboys
DAL_off_metric = winleagueAVEpts/DAL_win_ave_p
DAL_def_metric = losleagueAVEpts/DAL_los_ave_p

# Green Bay Packers
GB_off_metric = winleagueAVEpts/GB_win_ave_p
GB_def_metric = losleagueAVEpts/GB_los_ave_p

# Chicago Bears
CHI_off_metric = winleagueAVEpts/CHI_win_ave_p
CHI_def_metric = losleagueAVEpts/CHI_los_ave_p

# Minnesota Vikings
MIN_off_metric = winleagueAVEpts/MIN_win_ave_p
MIN_def_metric = losleagueAVEpts/MIN_los_ave_p

# Detroit Lions
DET_off_metric = winleagueAVEpts/DET_win_ave_p
DET_def_metric = losleagueAVEpts/DET_los_ave_p

# New Orleans Saints
NO_off_metric = winleagueAVEpts/NO_win_ave_p
NO_def_metric = losleagueAVEpts/NO_los_ave_p

# Atlanta Falcons
ATL_off_metric = winleagueAVEpts/ATL_win_ave_p
ATL_def_metric = losleagueAVEpts/ATL_los_ave_p

# Tampa Bay Buccaneers
TB_off_metric = winleagueAVEpts/TB_win_ave_p
TB_def_metric = losleagueAVEpts/TB_los_ave_p

# Carolina Panthers
CAR_off_metric = winleagueAVEpts/CAR_win_ave_p
CAR_def_metric = losleagueAVEpts/CAR_los_ave_p

# Los Angeles Rams
LAR_off_metric = winleagueAVEpts/LAR_win_ave_p
LAR_def_metric = losleagueAVEpts/LAR_los_ave_p

# Seattle Seahawks
SEA_off_metric = winleagueAVEpts/SEA_win_ave_p
SEA_def_metric = losleagueAVEpts/SEA_los_ave_p

# Arizona Cardinals
ARI_off_metric = winleagueAVEpts/ARI_win_ave_p
ARI_def_metric = losleagueAVEpts/ARI_los_ave_p

# San Francisco 49ers
SF_off_metric = winleagueAVEpts/SF_win_ave_p
SF_def_metric = losleagueAVEpts/SF_los_ave_p

# %% Predicting winners for Week 15 games
# LAC vs LV
print(f'LAC off {LAC_off_metric} \
    LAC_def {LAC_def_metric} \
    LV_Off {LV_off_metric} \
    LV_def {LV_def_metric}'
    )

LAC_Predicted_Score = (LAC_off_metric * LV_def_metric * LAC_total_ave)
LV_Predicted_Score = (LV_off_metric * LAC_def_metric * LV_total_ave)

if LAC_Predicted_Score > LV_Predicted_Score:
    print('Los Angeles Chargers Win!')
else:
	print('Los Vegas Raiders Win!')

# CAR vs GB
print(f'CAR off {CAR_off_metric} \
    CAR_def {CAR_def_metric} \
    GB_Off {GB_off_metric} \
    GB_def {GB_def_metric}'
    )

CAR_Predicted_Score = (CAR_off_metric * GB_def_metric * CAR_total_ave)
GB_Predicted_Score = (GB_off_metric * CAR_def_metric * GB_total_ave)

if CAR_Predicted_Score > GB_Predicted_Score:
    print('Carolina Panthers Win!')
else:
	print('Green Bay Packers Win!')

# BUF vs DEN
print(f'BUF off {BUF_off_metric} \
    BUF_def {BUF_def_metric} \
    DEN_Off {DEN_off_metric} \
    DEN_def {DEN_def_metric}'
    )

BUF_Predicted_Score = (BUF_off_metric * DEN_def_metric * BUF_total_ave)
DEN_Predicted_Score = (DEN_off_metric * BUF_def_metric * DEN_total_ave)

if BUF_Predicted_Score > DEN_Predicted_Score:
    print('Buffalo Bills Win!')
else:
	print('Denver Broncos Win!')

# HOU vs IND
print(f'HOU off {HOU_off_metric} \
    HOU_def {HOU_def_metric} \
    IND_Off {IND_off_metric} \
    IND_def {IND_def_metric}'
    )

HOU_Predicted_Score = (HOU_off_metric * IND_def_metric * HOU_total_ave)
IND_Predicted_Score = (IND_off_metric * HOU_def_metric * IND_total_ave)

if HOU_Predicted_Score > IND_Predicted_Score:
    print('Houston Texans Win!')
else:
	print('Indianapolis Colts Win!')

# DET vs TEN
print(f'DET off {DET_off_metric} \
    DET_def {DET_def_metric} \
    TEN_Off {TEN_off_metric} \
    TEN_def {TEN_def_metric}'
    )

DET_Predicted_Score = (DET_off_metric * TEN_def_metric * DET_total_ave)
TEN_Predicted_Score = (TEN_off_metric * DET_def_metric * TEN_total_ave)

if DET_Predicted_Score > TEN_Predicted_Score:
    print('Detroit Lions Win!')
else:
	print('Tennessee Titans Win!')

# TB vs ATL
print(f'TB off {TB_off_metric} \
    TB_def {TB_def_metric} \
    ATL_Off {ATL_off_metric} \
    ATL_def {ATL_def_metric}'
    )

TB_Predicted_Score = (TB_off_metric * ATL_def_metric * TB_total_ave)
ATL_Predicted_Score = (ATL_off_metric * TB_def_metric * ATL_total_ave)

if TB_Predicted_Score > ATL_Predicted_Score:
    print('Tampa Bay Buccaneers Win!')
else:
	print('Atlanta Falcons Win!')

# JAX vs BAL
print(f'JAX off {JAX_off_metric} \
    JAX_def {JAX_def_metric} \
    BAL_Off {BAL_off_metric} \
    BAL_def {BAL_def_metric}'
    )

JAX_Predicted_Score = (JAX_off_metric * BAL_def_metric * JAX_total_ave)
BAL_Predicted_Score = (BAL_off_metric * JAX_def_metric * BAL_total_ave)

if JAX_Predicted_Score > BAL_Predicted_Score:
    print('Jacksonville Jaguars Win!')
else:
	print('Baltimore Ravens Win!')

# NE vs MIAMI
print(f'NE off {NE_off_metric} \
    NE_def {NE_def_metric} \
    MIAMI_Off {MIAMI_off_metric} \
    MIAMI_def {MIAMI_def_metric}'
    )

NE_Predicted_Score = (NE_off_metric * MIAMI_def_metric * NE_total_ave)
MIAMI_Predicted_Score = (MIAMI_off_metric * NE_def_metric * MIAMI_total_ave)

if NE_Predicted_Score > MIAMI_Predicted_Score:
    print('New England Patriots Win!')
else:
	print('Miami Dolphins Win!')

# CHI vs MIN
print(f'CHI off {CHI_off_metric} \
    CHI_def {CHI_def_metric} \
    MIN_Off {MIN_off_metric} \
    MIN_def {MIN_def_metric}'
    )

CHI_Predicted_Score = (CHI_off_metric * MIN_def_metric * CHI_total_ave)
MIN_Predicted_Score = (MIN_off_metric * CHI_def_metric * MIN_total_ave)

if CHI_Predicted_Score > MIN_Predicted_Score:
    print('Chicago Bears Win!')
else:
	print('Minnesota Vikings Win!')

# SEA vs WAS
print(f'SEA off {SEA_off_metric} \
    SEA_def {SEA_def_metric} \
    WAS_Off {WAS_off_metric} \
    WAS_def {WAS_def_metric}'
    )

SEA_Predicted_Score = (SEA_off_metric * WAS_def_metric * SEA_total_ave)
WAS_Predicted_Score = (WAS_off_metric * SEA_def_metric * WAS_total_ave)

if SEA_Predicted_Score > WAS_Predicted_Score:
    print('Seattle Seahawks Win!')
else:
	print('Washington Football Team Wins!')

# SF vs DAL
print(f'SF off {SF_off_metric} \
    SF_def {SF_def_metric} \
    DAL_Off {DAL_off_metric} \
    DAL_def {DAL_def_metric}'
    )

SF_Predicted_Score = (SF_off_metric * DAL_def_metric * SF_total_ave)
DAL_Predicted_Score = (DAL_off_metric * SF_def_metric * DAL_total_ave)

if SF_Predicted_Score > DAL_Predicted_Score:
    print('San Francisco 49ers Win!')
else:
	print('Dallas Cowboys Win!')

# NYJ vs LAR
print(f'NYJ off {NYJ_off_metric} \
    NYJ_def {NYJ_def_metric} \
    LAR_Off {LAR_off_metric} \
    LAR_def {LAR_def_metric}'
    )

NYJ_Predicted_Score = (NYJ_off_metric * LAR_def_metric * NYJ_total_ave)
LAR_Predicted_Score = (LAR_off_metric * NYJ_def_metric * LAR_total_ave)

if NYJ_Predicted_Score > LAR_Predicted_Score:
    print('New York Jets Win!')
else:
	print('Los Angeles Rams Win!')

# PHI vs ARI
print(f'PHI off {PHI_off_metric} \
    PHI_def {PHI_def_metric} \
    ARI_Off {ARI_off_metric} \
    ARI_def {ARI_def_metric}'
    )

PHI_Predicted_Score = (PHI_off_metric * ARI_def_metric * PHI_total_ave)
ARI_Predicted_Score = (ARI_off_metric * PHI_def_metric * ARI_total_ave)

if PHI_Predicted_Score > ARI_Predicted_Score:
    print('Philadelphia Eagles Win!')
else:
	print('Arizona Cardinals Win!')

# KC vs NO
print(f'KC off {KC_off_metric} \
    KC_def {KC_def_metric} \
    NO_Off {NO_off_metric} \
    NO_def {NO_def_metric}'
    )

KC_Predicted_Score = (KC_off_metric * NO_def_metric * KC_total_ave)
NO_Predicted_Score = (NO_off_metric * KC_def_metric * NO_total_ave)

if KC_Predicted_Score > NO_Predicted_Score:
    print('Kansas City Chiefs Win!')
else:
	print('New Orleans Saints Win!')

# CLE vs NYG
print(f'CLE off {CLE_off_metric} \
    CLE_def {CLE_def_metric} \
    NYG_Off {NYG_off_metric} \
    NYG_def {NYG_def_metric}'
    )

CLE_Predicted_Score = (CLE_off_metric * NYG_def_metric * CLE_total_ave)
NYG_Predicted_Score = (NYG_off_metric * CLE_def_metric * NYG_total_ave)

if CLE_Predicted_Score > NYG_Predicted_Score:
    print('Cleveland Browns Win!')
else:
	print('New York Giants Win!')

# PITT vs CIN
print(f'PITT off {PITT_off_metric} \
    PITT_def {PITT_def_metric} \
    CIN_Off {CIN_off_metric} \
    CIN_def {CIN_def_metric}'
    )

PITT_Predicted_Score = (PITT_off_metric * CIN_def_metric * PITT_total_ave)
CIN_Predicted_Score = (CIN_off_metric * PITT_def_metric * CIN_total_ave)

if PITT_Predicted_Score > CIN_Predicted_Score:
    print('Pittsburgh Steelers Win!')
else:
	print('Cincinnati Bengals Win!')

# %% Predict Winners for Week 16 games

# MIN vs NO
print(f'MIN off {MIN_off_metric} \
    MIN_def {MIN_def_metric} \
    NO_Off {NO_off_metric} \
    NO_def {NO_def_metric}'
    )

MIN_Predicted_Score = (MIN_off_metric * NO_def_metric * MIN_total_ave)
NO_Predicted_Score = (NO_off_metric * MIN_def_metric * NO_total_ave)

if MIN_Predicted_Score > NO_Predicted_Score:
    print('Minnesota Vikings Win!')
else:
	print('New Orleans Saints Win!')

# TB vs DET
print(f'TB off {TB_off_metric} \
    TB_def {TB_def_metric} \
    DET_Off {DET_off_metric} \
    DET_def {DET_def_metric}'
    )

TB_Predicted_Score = (TB_off_metric * DET_def_metric * TB_total_ave)
DET_Predicted_Score = (DET_off_metric * TB_def_metric * DET_total_ave)

if TB_Predicted_Score > DET_Predicted_Score:
    print('Tampa Bay Buccaneers Win!')
else:
	print('Detroit Lions Win!')

# SF vs ARI
print(f'SF off {SF_off_metric} \
    SF_def {SF_def_metric} \
    ARI_Off {ARI_off_metric} \
    ARI_def {ARI_def_metric}'
    )

SF_Predicted_Score = (SF_off_metric * ARI_def_metric * SF_total_ave)
ARI_Predicted_Score = (ARI_off_metric * SF_def_metric * ARI_total_ave)

if SF_Predicted_Score > ARI_Predicted_Score:
    print('Seattle Seahawks Win!')
else:
	print('Arizona Cardinals Win!')

# MIAMI vs LV
print(f'MIAMI off {MIAMI_off_metric} \
    MIAMI_def {MIAMI_def_metric} \
    LV_Off {LV_off_metric} \
    LV_def {LV_def_metric}'
    )

MIAMI_Predicted_Score = (MIAMI_off_metric * LV_def_metric * MIAMI_total_ave)
LV_Predicted_Score = (LV_off_metric * MIAMI_def_metric * LV_total_ave)

if MIAMI_Predicted_Score > LV_Predicted_Score:
    print('Miami Dolphins Win!')
else:
	print('Las Vegas Raiders Win!')

# TEN vs GB
print(f'TEN off {TEN_off_metric} \
    TEN_def {TEN_def_metric} \
    GB_Off {GB_off_metric} \
    GB_def {GB_def_metric}'
    )

TEN_Predicted_Score = (TEN_off_metric * GB_def_metric * TEN_total_ave)
GB_Predicted_Score = (GB_off_metric * TEN_def_metric * GB_total_ave)

if TEN_Predicted_Score > GB_Predicted_Score:
    print('Tennessee Titans Win!')
else:
	print('Green Bay Packers Win!')

# CLE vs NYJ
print(f'CLE off {CLE_off_metric} \
    CLE_def {CLE_def_metric} \
    NYJ_Off {NYJ_off_metric} \
    NYJ_def {NYJ_def_metric}'
    )

CLE_Predicted_Score = (CLE_off_metric * NYJ_def_metric * CLE_total_ave)
NYJ_Predicted_Score = (NYJ_off_metric * CLE_def_metric * NYJ_total_ave)

if CLE_Predicted_Score > NYJ_Predicted_Score:
    print('Cleveland Browns Win!')
else:
	print('New York Jets Win!')

# NYG vs BAL
print(f'NYG off {NYG_off_metric} \
    NYG_def {NYG_def_metric} \
    BAL_Off {BAL_off_metric} \
    BAL_def {BAL_def_metric}'
    )

NYG_Predicted_Score = (NYG_off_metric * BAL_def_metric * NYG_total_ave)
BAL_Predicted_Score = (BAL_off_metric * NYG_def_metric * BAL_total_ave)

if NYG_Predicted_Score > BAL_Predicted_Score:
    print('New York Giants Win!')
else:
	print('Baltimore Ravens Win!')

# CIN vs HOU
print(f'CIN off {CIN_off_metric} \
    CIN_def {CIN_def_metric} \
    HOU_Off {HOU_off_metric} \
    HOU_def {HOU_def_metric}'
    )

CIN_Predicted_Score = (CIN_off_metric * HOU_def_metric * CIN_total_ave)
HOU_Predicted_Score = (HOU_off_metric * CIN_def_metric * HOU_total_ave)

if CIN_Predicted_Score > HOU_Predicted_Score:
    print('Cincinnati Bengals Win!')
else:
	print('Houston Texans Win!')

# CHI vs JAX
print(f'CHI off {CHI_off_metric} \
    CHI_def {CHI_def_metric} \
    JAX_Off {JAX_off_metric} \
    JAX_def {JAX_def_metric}'
    )

CHI_Predicted_Score = (CHI_off_metric * JAX_def_metric * CHI_total_ave)
JAX_Predicted_Score = (JAX_off_metric * CHI_def_metric * JAX_total_ave)

if CHI_Predicted_Score > JAX_Predicted_Score:
    print('Chicago Bears Win!')
else:
	print('Jacksonville Jaguars Win!')

# ATL vs KC
print(f'ATL off {ATL_off_metric} \
    ATL_def {ATL_def_metric} \
    KC_Off {KC_off_metric} \
    KC_def {KC_def_metric}'
    )

ATL_Predicted_Score = (ATL_off_metric * KC_def_metric * ATL_total_ave)
KC_Predicted_Score = (KC_off_metric * ATL_def_metric * KC_total_ave)

if ATL_Predicted_Score > KC_Predicted_Score:
    print('Atlanta Falcons Win!')
else:
	print('Kansas City Chiefs Win!')

# IND vs PITT
print(f'IND off {IND_off_metric} \
    IND_def {IND_def_metric} \
    PITT_Off {PITT_off_metric} \
    PITT_def {PITT_def_metric}'
    )

IND_Predicted_Score = (IND_off_metric * PITT_def_metric * IND_total_ave)
PITT_Predicted_Score = (PITT_off_metric * IND_def_metric * PITT_total_ave)

if IND_Predicted_Score > PITT_Predicted_Score:
    print('Indianapolis Colts Win!')
else:
	print('Pittsburgh Steelers Win!')

# CAR vs WAS
print(f'CAR off {CAR_off_metric} \
    CAR_def {CAR_def_metric} \
    WAS_Off {WAS_off_metric} \
    WAS_def {WAS_def_metric}'
    )

CAR_Predicted_Score = (CAR_off_metric * WAS_def_metric * CAR_total_ave)
WAS_Predicted_Score = (WAS_off_metric * CAR_def_metric * WAS_total_ave)

if CAR_Predicted_Score > WAS_Predicted_Score:
    print('Carolina Panthers Win!')
else:
	print('Washington Football Team Wins!')

# DEN vs LAC
print(f'DEN off {DEN_off_metric} \
    DEN_def {DEN_def_metric} \
    LAC_Off {LAC_off_metric} \
    LAC_def {LAC_def_metric}'
    )

DEN_Predicted_Score = (DEN_off_metric * LAC_def_metric * DEN_total_ave)
LAC_Predicted_Score = (LAC_off_metric * DEN_def_metric * LAC_total_ave)

if DEN_Predicted_Score > LAC_Predicted_Score:
    print('Denver Broncos Win!')
else:
	print('Los Angeles Chargers Win!')

# LAR vs SEA
print(f'LAR off {LAR_off_metric} \
    LAR_def {LAR_def_metric} \
    SEA_Off {SEA_off_metric} \
    SEA_def {SEA_def_metric}'
    )

LAR_Predicted_Score = (LAR_off_metric * SEA_def_metric * LAR_total_ave)
SEA_Predicted_Score = (SEA_off_metric * LAR_def_metric * SEA_total_ave)

if LAR_Predicted_Score > SEA_Predicted_Score:
    print('Los Angeles Rams Win!')
else:
	print('Seattle Seahawks Win!')

# PHI vs DAL
print(f'PHI off {PHI_off_metric} \
    PHI_def {PHI_def_metric} \
    DAL_Off {DAL_off_metric} \
    DAL_def {DAL_def_metric}'
    )

PHI_Predicted_Score = (PHI_off_metric * DAL_def_metric * PHI_total_ave)
DAL_Predicted_Score = (DAL_off_metric * PHI_def_metric * DAL_total_ave)

if PHI_Predicted_Score > DAL_Predicted_Score:
    print('Philadelphia Eagles Win!')
else:
	print('Dallas Cowboys Win!')

# BUF vs NE
print(f'BUF off {BUF_off_metric} \
    BUF_def {BUF_def_metric} \
    NE_Off {NE_off_metric} \
    NE_def {NE_def_metric}'
    )

BUF_Predicted_Score = (BUF_off_metric * NE_def_metric * BUF_total_ave)
NE_Predicted_Score = (NE_off_metric * BUF_def_metric * NE_total_ave)

if BUF_Predicted_Score > NE_Predicted_Score:
    print('Buffalo Bills Win!')
else:
	print('New England Patriots Win!')

# %% Predict Winners for Week 17 Games

# GB vs CHI
print(f'GB off {GB_off_metric} \
    GB_def {GB_def_metric} \
    CHI_Off {CHI_off_metric} \
    CHI_def {CHI_def_metric}'
    )

GB_Predicted_Score = (GB_off_metric * CHI_def_metric * GB_total_ave)
CHI_Predicted_Score = (CHI_off_metric * GB_def_metric * CHI_total_ave)

if GB_Predicted_Score > CHI_Predicted_Score:
    print('Green Bay Packers Win!')
else:
	print('Chicago Bears Win!')

# MIAMI vs BUF
print(f'MIAMI off {MIAMI_off_metric} \
    MIAMI_def {MIAMI_def_metric} \
    BUF_Off {BUF_off_metric} \
    BUF_def {BUF_def_metric}'
    )

MIAMI_Predicted_Score = (MIAMI_off_metric * BUF_def_metric * MIAMI_total_ave)
BUF_Predicted_Score = (BUF_off_metric * MIAMI_def_metric * BUF_total_ave)

if MIAMI_Predicted_Score > BUF_Predicted_Score:
    print('Miami Dolphins Win!')
else:
	print('Buffalo Bills Win!')

# NO vs CAR
print(f'NO off {NO_off_metric} \
    NO_def {NO_def_metric} \
    CAR_Off {CAR_off_metric} \
    CAR_def {CAR_def_metric}'
    )

NO_Predicted_Score = (NO_off_metric * CAR_def_metric * NO_total_ave)
CAR_Predicted_Score = (CAR_off_metric * NO_def_metric * CAR_total_ave)

if NO_Predicted_Score > CAR_Predicted_Score:
    print('New Orleans Saints Win!')
else:
	print('Carolina Panthers Win!')

# BAL vs CIN
print(f'BAL off {BAL_off_metric} \
    BAL_def {BAL_def_metric} \
    CIN_Off {CIN_off_metric} \
    CIN_def {CIN_def_metric}'
    )

BAL_Predicted_Score = (BAL_off_metric * CIN_def_metric * BAL_total_ave)
CIN_Predicted_Score = (CIN_off_metric * BAL_def_metric * CIN_total_ave)

if BAL_Predicted_Score > CIN_Predicted_Score:
    print('Baltimore Ravens Win!')
else:
	print('Cincinnati Bengals Win!')

# PITT vs CLE
print(f'PITT off {PITT_off_metric} \
    PITT_def {PITT_def_metric} \
    CLE_Off {CLE_off_metric} \
    CLE_def {CLE_def_metric}'
    )

PITT_Predicted_Score = (PITT_off_metric * CLE_def_metric * PITT_total_ave)
CLE_Predicted_Score = (CLE_off_metric * PITT_def_metric * CLE_total_ave)

if PITT_Predicted_Score > CLE_Predicted_Score:
    print('Pittsburgh Steelers Win!')
else:
	print('Cleveland Browns Win!')

# MIN vs DET
print(f'MIN off {MIN_off_metric} \
    MIN_def {MIN_def_metric} \
    DET_Off {DET_off_metric} \
    DET_def {DET_def_metric}'
    )

MIN_Predicted_Score = (MIN_off_metric * DET_def_metric * MIN_total_ave)
DET_Predicted_Score = (DET_off_metric * MIN_def_metric * DET_total_ave)

if MIN_Predicted_Score > DET_Predicted_Score:
    print('Minnesota Vikings Win!')
else:
	print('Detroit Lions Win!')

# JAX vs IND
print(f'JAX off {JAX_off_metric} \
    JAX_def {JAX_def_metric} \
    IND_Off {IND_off_metric} \
    IND_def {IND_def_metric}'
    )

JAX_Predicted_Score = (JAX_off_metric * IND_def_metric * JAX_total_ave)
IND_Predicted_Score = (IND_off_metric * JAX_def_metric * IND_total_ave)

if JAX_Predicted_Score > IND_Predicted_Score:
    print('Jacksonville Jaguars Win!')
else:
	print('Indianapolis Colts Win!')

# NYJ vs NE
print(f'NYJ off {NYJ_off_metric} \
    NYJ_def {NYJ_def_metric} \
    NE_Off {NE_off_metric} \
    NE_def {NE_def_metric}'
    )

NYJ_Predicted_Score = (NYJ_off_metric * NE_def_metric * NYJ_total_ave)
NE_Predicted_Score = (NE_off_metric * NYJ_def_metric * NE_total_ave)

if NYJ_Predicted_Score > NE_Predicted_Score:
    print('New York Jets Win!')
else:
	print('New England Patriots Win!')

# TEN vs HOU
print(f'TEN off {TEN_off_metric} \
    TEN_def {TEN_def_metric} \
    HOU_Off {HOU_off_metric} \
    HOU_def {HOU_def_metric}'
    )

TEN_Predicted_Score = (TEN_off_metric * HOU_def_metric * TEN_total_ave)
HOU_Predicted_Score = (HOU_off_metric * TEN_def_metric * HOU_total_ave)

if TEN_Predicted_Score > HOU_Predicted_Score:
    print('Tennessee Titans Win!')
else:
	print('Houston Texans Win!')

# LAC vs KC
print(f'LAC off {LAC_off_metric} \
    LAC_def {LAC_def_metric} \
    KC_Off {KC_off_metric} \
    KC_def {KC_def_metric}'
    )

LAC_Predicted_Score = (LAC_off_metric * KC_def_metric * LAC_total_ave)
KC_Predicted_Score = (KC_off_metric * LAC_def_metric * KC_total_ave)

if LAC_Predicted_Score > KC_Predicted_Score:
    print('Los Angeles Chargers Win!')
else:
	print('Kansas City Chiefs Win!')

# DAL vs NYG
print(f'DAL off {DAL_off_metric} \
    DAL_def {DAL_def_metric} \
    NYG_Off {NYG_off_metric} \
    NYG_def {NYG_def_metric}'
    )

DAL_Predicted_Score = (DAL_off_metric * NYG_def_metric * DAL_total_ave)
NYG_Predicted_Score = (NYG_off_metric * DAL_def_metric * NYG_total_ave)

if DAL_Predicted_Score > NYG_Predicted_Score:
    print('Dallas Cowboys Win!')
else:
	print('New York Giants Win!')

# WAS vs PHI
print(f'WAS off {WAS_off_metric} \
    WAS_def {WAS_def_metric} \
    PHI_Off {PHI_off_metric} \
    PHI_def {PHI_def_metric}'
    )

WAS_Predicted_Score = (WAS_off_metric * PHI_def_metric * WAS_total_ave)
PHI_Predicted_Score = (PHI_off_metric * WAS_def_metric * PHI_total_ave)

if WAS_Predicted_Score > PHI_Predicted_Score:
    print('Washington Football Team Win!')
else:
	print('Philadelphia Eagles Win!')

# ATL vs TB
print(f'ATL off {ATL_off_metric} \
    ATL_def {ATL_def_metric} \
    TB_Off {TB_off_metric} \
    TB_def {TB_def_metric}'
    )

ATL_Predicted_Score = (ATL_off_metric * TB_def_metric * ATL_total_ave)
TB_Predicted_Score = (TB_off_metric * ATL_def_metric * TB_total_ave)

if ATL_Predicted_Score > TB_Predicted_Score:
    print('Atlanta Falcons Win!')
else:
	print('Tampa Bay Buccaneers Win!')

# LV vs DEN
print(f'LV off {LV_off_metric} \
    LV_def {LV_def_metric} \
    DEN_Off {DEN_off_metric} \
    DEN_def {DEN_def_metric}'
    )

LV_Predicted_Score = (LV_off_metric * DEN_def_metric * LV_total_ave)
DEN_Predicted_Score = (DEN_off_metric * LV_def_metric * DEN_total_ave)

if LV_Predicted_Score > DEN_Predicted_Score:
    print('Las Vegas Raiders Win!')
else:
	print('Denver Broncos Win!')

# ARI vs LAR
print(f'ARI off {ARI_off_metric} \
    ARI_def {ARI_def_metric} \
    LAR_Off {LAR_off_metric} \
    LAR_def {LAR_def_metric}'
    )

ARI_Predicted_Score = (ARI_off_metric * LAR_def_metric * ARI_total_ave)
LAR_Predicted_Score = (LAR_off_metric * ARI_def_metric * LAR_total_ave)

if ARI_Predicted_Score > LAR_Predicted_Score:
    print('Arizona Cardinals Win!')
else:
	print('Los Angeles Rams Win!')

# SEA vs SF
print(f'SEA off {SEA_off_metric} \
    SEA_def {SEA_def_metric} \
    SF_Off {SF_off_metric} \
    SF_def {SF_def_metric}'
    )

SEA_Predicted_Score = (SEA_off_metric * SF_def_metric * SEA_total_ave)
SF_Predicted_Score = (SF_off_metric * SEA_def_metric * SF_total_ave)

if SEA_Predicted_Score > SF_Predicted_Score:
    print('Seattle Seahawks Win!')
else:
	print('San Francisco 49ers Win!')

# %% Create Total wins per team variable including predicted wins
# Cleveland Browns 
CLE_predicted_wins = (0)
CLE_total_wins= (CLE_predicted_wins + CLE_wins_td)
# Pittsburgh Steelers
PITT_predicted_wins = (2)
PITT_total_wins = (PITT_predicted_wins + PITT_wins_td)
# Baltimore Ravens
BAL_predicted_wins = (2)
BAL_total_wins = (BAL_predicted_wins + BAL_wins_td)
# Cincinnati Bengals
CIN_predicted_wins = (0)
CIN_total_wins = (CIN_predicted_wins + CIN_wins_td)
# Buffalo Bills
BUF_predicted_wins = (3)
BUF_total_wins = (BUF_predicted_wins + BUF_wins_td)
# Miami Dolphins
MIAMI_predicted_wins = (1)
MIAMI_total_wins = (MIAMI_predicted_wins + MIAMI_wins_td)
# New England Patriots
NE_predicted_wins = (1)
NE_total_wins = (NE_predicted_wins + NE_wins_td)
# New York Jets
NYJ_predicted_wins = (1)
NYJ_total_wins = (NYJ_predicted_wins + NYJ_wins_td)
# Tennessee Titans
TEN_predicted_wins = (3)
TEN_total_wins = (TEN_predicted_wins + TEN_wins_td)
# Indianapolis Colts
IND_predicted_wins = (2)
IND_total_wins = (IND_predicted_wins + IND_wins_td)
# Houston Texans
HOU_predicted_wins = (3)
HOU_total_wins = (HOU_predicted_wins + HOU_wins_td)
# Jacksonville Jaguars
JAX_predicted_wins = (3)
JAX_total_wins = (JAX_predicted_wins + JAX_wins_td)
# Kansas City chiefs
KC_predicted_wins = (3)
KC_total_wins = (KC_predicted_wins + KC_wins_td)
# Las Vegas Raiders
LV_predicted_wins = (2)
LV_total_wins = (LV_predicted_wins + LV_wins_td)
# Denver Broncos
DEN_predicted_wins = (0)
DEN_total_wins = (DEN_predicted_wins + DEN_wins_td)
# Los Angeles Chargers
LAC_predicted_wins = (2)
LAC_total_wins = (LAC_predicted_wins + LAC_wins_td)
# Washington Football Team
WAS_predicted_wins = (0)
WAS_total_wins = (WAS_predicted_wins + WAS_wins_td)
# New York Giants
NYG_predicted_wins = (2)
NYG_total_wins = (NYG_predicted_wins + NYG_wins_td)
# Philadelphia Eagles
PHI_predicted_wins = (2)
PHI_total_wins = (PHI_predicted_wins + PHI_wins_td)
# Dallas Cowboys
DAL_predicted_wins = (0)
DAL_total_wins = (DAL_predicted_wins + DAL_wins_td)
# Green Bay Packers
GB_predicted_wins =(1)
GB_total_wins = (GB_predicted_wins + GB_wins_td)
# Minnesota Vikings
MIN_predicted_wins = (2)
MIN_total_wins = (MIN_predicted_wins + MIN_wins_td)
# Chicago Bears
CHI_predicted_wins = (0)
CHI_total_wins = (CHI_predicted_wins + CHI_wins_td)
# Detroit Lions
DET_predicted_wins = (1)
DET_total_wins = (DET_predicted_wins + DET_wins_td)
# New Orleans Saints
NO_predicted_wins = (1)
NO_total_wins = (NO_predicted_wins + NO_wins_td)
# Tampa Bay Buccs
TB_predicted_wins = (0)
TB_total_wins = (TB_predicted_wins + TB_wins_td)
# Atlanta Falcons
ATL_predicted_wins = (2)
ATL_total_wins = (ATL_predicted_wins + ATL_wins_td)
# Carolina Panthers
CAR_predicted_wins = (3)
CAR_total_wins = (CAR_predicted_wins + CAR_wins_td)
# LA Rams
LAR_predicted_wins = (1)
LAR_total_wins = (LAR_predicted_wins + LAR_wins_td)
# Seattle Seahawks
SEA_predicted_wins = (3)
SEA_total_wins = (SEA_predicted_wins + SEA_wins_td)
# Arizona Cardinals
ARI_predicted_wins = (3)
ARI_total_wins = (ARI_predicted_wins + ARI_wins_td)
# San Francisco 49ers
SF_predicted_wins = (0)
SF_total_wins = (SF_predicted_wins + SF_wins_td)

# %% Create dataframe for Total Wins this season

teams = ['Cleveland Browns', 'Pittsburgh Steelers', 'Baltimore Ravens', 'Cincinnati Bengals', 'Buffalo Bills', 
'Miami Dolphins', 'New England Patriots', 'New York Jets', 'Tennessee Titans', 'Indianapolis Colts',
 'Houston Texans', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Denver Broncos', 
 'Los Angeles Chargers', 'Washington Football Team', 'New York Giants', 'Philadelphia Eagles', 
 'Dallas Cowboys', 'Green Bay Packers', 'Minnesota Vikings', 'Chicago Bears', 'Detroit Lions', 
 'New Orleans Saints', 'Tampa Bay Buccaneers', 'Atlanta Falcons', 'Carolina Panthers', 'Los Angeles Rams', 
 'Seattle Seahawks', 'Arizona Cardinals', 'San Francisco 49ers' ]

Wins_Total = [ 9, 13, 10, 2, 13,9, 7, 1, 12, 11, 7, 4, 15, 9, 5, 6, 6, 7, 6, 4, 11, 8, 6, 6, 11, 8, 6, 7, 10,
 12, 10, 5 ]

xd = {'Team Name':teams,'Total Wins':Wins_Total}

xdf = pd.DataFrame(xd)
xdf.sort_values(by='Total Wins', ascending=False)


# %% Setting the playoff Picture for the NFC (Seeding Teams)

NFC_Teams = ['Washington Football Team', 'New York Giants', 'Philadelphia Eagles', 
 'Dallas Cowboys', 'Green Bay Packers', 'Minnesota Vikings', 'Chicago Bears', 'Detroit Lions', 
 'New Orleans Saints', 'Tampa Bay Buccaneers', 'Atlanta Falcons', 'Carolina Panthers', 'Los Angeles Rams', 
 'Seattle Seahawks', 'Arizona Cardinals', 'San Francisco 49ers' ]

NFC_Total_Wins = [6, 7, 6, 4, 11, 8, 6, 6, 11, 8, 6, 7, 10, 12, 10, 5]

dNFC = {'NFC Teams': NFC_Teams, 'Total Wins': NFC_Total_Wins}

xdNFC = pd.DataFrame(dNFC)
xdNFC.sort_values(by='Total Wins', ascending=False)

# %% Setting the Playoff Picture for the AFC (Seeding Teams)
AFC_Teams = ['Cleveland Browns', 'Pittsburgh Steelers', 'Baltimore Ravens', 'Cincinnati Bengals', 'Buffalo Bills', 
'Miami Dolphins', 'New England Patriots', 'New York Jets', 'Tennessee Titans', 'Indianapolis Colts',
 'Houston Texans', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Denver Broncos', 
 'Los Angeles Chargers']

AFC_Total_Wins = [9, 13, 10, 2, 13,9, 7, 1, 12, 11, 7, 4, 15, 9, 5, 6]

dAFC = {'AFC Teams': AFC_Teams, 'Total Wins': AFC_Total_Wins}

xdAFC = pd.DataFrame(dAFC)
xdAFC.sort_values(by='Total Wins', ascending=False)

# %% Top 7 teams from each conference make the playoffs, with the top seed getting a first round by.
# Predictions for round 1 of the Playoffs:
# Green Bay Packers vs Tampa Bay Buccaneers
print(f'GB off {GB_off_metric} \
    GB_def {GB_def_metric} \
    TB_Off {TB_off_metric} \
    TB_def {TB_def_metric}'
    )

GB_Predicted_Score = (GB_off_metric * TB_def_metric * GB_total_ave)
TB_Predicted_Score = (TB_off_metric * GB_def_metric * TB_total_ave)

if GB_Predicted_Score > TB_Predicted_Score:
    print('Green Bay Packers Win!')
else:
	print('Tampa Bay Buccaneers Win!')

# Saints vs Vikings
print(f'NO off {NO_off_metric} \
    NO_def {NO_def_metric} \
    MIN_Off {MIN_off_metric} \
    MIN_def {MIN_def_metric}'
    )

NO_Predicted_Score = (NO_off_metric * MIN_def_metric * NO_total_ave)
MIN_Predicted_Score = (MIN_off_metric * NO_def_metric * MIN_total_ave)

if NO_Predicted_Score > MIN_Predicted_Score:
    print('New Orleans Saints Win!')
else:
	print('Minnesota Vikings Win!')

# LA Rams vs Arizona Cardinals
print(f'LAR off {LAR_off_metric} \
    LAR_def {LAR_def_metric} \
    ARI_Off {ARI_off_metric} \
    ARI_def {ARI_def_metric}'
    )

LAR_Predicted_Score = (LAR_off_metric * ARI_def_metric * LAR_total_ave)
ARI_Predicted_Score = (ARI_off_metric * LAR_def_metric * ARI_total_ave)

if LAR_Predicted_Score > ARI_Predicted_Score:
    print('Los Angeles Rams Win!')
else:
	print('Arizona Cardinals Win!')

# Pittsburgh Steelers vs Cleveland Browns
print(f'PITT off {PITT_off_metric} \
    PITT_def {PITT_def_metric} \
    CLE_Off {CLE_off_metric} \
    CLE_def {CLE_def_metric}'
    )

PITT_Predicted_Score = (PITT_off_metric * CLE_def_metric * PITT_total_ave)
CLE_Predicted_Score = (CLE_off_metric * PITT_def_metric * CLE_total_ave)

if PITT_Predicted_Score > CLE_Predicted_Score:
    print('Pittsburgh Steelers Win!')
else:
	print('Cleveland Browns Win!')

# Buffalo Bills vs Baltimore Ravens
print(f'BUF off {BUF_off_metric} \
    BUF_def {BUF_def_metric} \
    BAL_Off {BAL_off_metric} \
    BAL_def {BAL_def_metric}'
    )

BUF_Predicted_Score = (BUF_off_metric * BAL_def_metric * BUF_total_ave)
BAL_Predicted_Score = (BAL_off_metric * BUF_def_metric * BAL_total_ave)

if BUF_Predicted_Score > BAL_Predicted_Score:
    print('Buffalo Bills Win!')
else:
	print('Baltimore Ravens Win!')

# Tennessee Titans vs Indianapolis Colts
print(f'TEN off {TEN_off_metric} \
    TEN_def {TEN_def_metric} \
    IND_Off {IND_off_metric} \
    IND_def {IND_def_metric}'
    )

TEN_Predicted_Score = (TEN_off_metric * IND_def_metric * TEN_total_ave)
IND_Predicted_Score = (IND_off_metric * TEN_def_metric * IND_total_ave)

if TEN_Predicted_Score > IND_Predicted_Score:
    print('Tennessee Titans Win!')
else:
	print('Indianapolis Colts Win!')

R2_NFC_teams = ['Green Bay Packers', 'New Orleans Saints', 'Arizona Cardinals', 'Seattle Seahawks']
R2_AFC_teams = ['Pittsburgh Steelers', 'Buffalo Bills', 'Tenessee Titans', 'Kansas City Chiefs']
# %% Predicting the 2nd Round of Playoffs
# Seattle Seahawks vs Arizona Cardinals
print(f'SEA off {SEA_off_metric} \
    SEA_def {SEA_def_metric} \
    ARI_Off {ARI_off_metric} \
    ARI_def {ARI_def_metric}'
    )

SEA_Predicted_Score = (SEA_off_metric * ARI_def_metric * SEA_total_ave)
ARI_Predicted_Score = (ARI_off_metric * SEA_def_metric * ARI_total_ave)

if SEA_Predicted_Score > ARI_Predicted_Score:
    print('Seattle Seahawks Win!')
else:
	print('Arizona Cardinals Win!')

# Green Bay Packers vs New Orleans Saints
print(f'GB off {GB_off_metric} \
    GB_def {GB_def_metric} \
    NO_Off {NO_off_metric} \
    NO_def {NO_def_metric}'
    )

GB_Predicted_Score = (GB_off_metric * NO_def_metric * GB_total_ave)
NO_Predicted_Score = (NO_off_metric * GB_def_metric * NO_total_ave)

if GB_Predicted_Score > NO_Predicted_Score:
    print('Green Bay Packers Win!')
else:
	print('New Orleans Saints Win!')

# Kansas City Chiefs vs Tennessee Titans
print(f'KC off {KC_off_metric} \
    KC_def {KC_def_metric} \
    TEN_Off {TEN_off_metric} \
    TEN_def {TEN_def_metric}'
    )

KC_Predicted_Score = (KC_off_metric * TEN_def_metric * KC_total_ave)
TEN_Predicted_Score = (TEN_off_metric * KC_def_metric * TEN_total_ave)

if KC_Predicted_Score > TEN_Predicted_Score:
    print('Kansas City Chiefs Win!')
else:
	print('Tennessee Titans Win!')

# Pittsburgh Steelers vs Buffalo Bills
print(f'PITT off {PITT_off_metric} \
    PITT_def {PITT_def_metric} \
    BUF_Off {BUF_off_metric} \
    BUF_def {BUF_def_metric}'
    )

PITT_Predicted_Score = (PITT_off_metric * BUF_def_metric * PITT_total_ave)
BUF_Predicted_Score = (BUF_off_metric * PITT_def_metric * BUF_total_ave)

if PITT_Predicted_Score > BUF_Predicted_Score:
    print('Pittsburgh Steelers Win!')
else:
	print('Buffalo Bills Win!')

R3_NFC_teams = ['Seattle Seahawks', 'New Orleans Saints']
R3_AFC_teams = ['Kansas City Chiefs', 'Buffalo Bills']

# %% Predicting the Semi Final round of the playoffs

# Kansas City Chiefs vs Buffalo Bills
print(f'KC off {KC_off_metric} \
    KC_def {KC_def_metric} \
    BUF_Off {BUF_off_metric} \
    BUF_def {BUF_def_metric}'
    )

KC_Predicted_Score = (KC_off_metric * BUF_def_metric * KC_total_ave)
BUF_Predicted_Score = (BUF_off_metric * KC_def_metric * BUF_total_ave)

if KC_Predicted_Score > BUF_Predicted_Score:
    print('Kansas City Chiefs Win!')
else:
	print('Buffalo Bills Win!')

# Seattle Seahawks vs New Orleans Saints
print(f'SEA off {SEA_off_metric} \
    SEA_def {SEA_def_metric} \
    NO_Off {NO_off_metric} \
    NO_def {NO_def_metric}'
    )

SEA_Predicted_Score = (SEA_off_metric * NO_def_metric * SEA_total_ave)
NO_Predicted_Score = (NO_off_metric * SEA_def_metric * NO_total_ave)

if SEA_Predicted_Score > NO_Predicted_Score:
    print('Seattle Seahawks Win!')
else:
	print('New Orleans Saints Win!')

Superbowl_teams = ['New Orleans Saints', 'Kansas City Chiefs']

# %% Superbowl Prediction 2020
# New Orleans Saints vs Kansas City Chiefs
print(f'KC off {KC_off_metric} \
    KC_def {KC_def_metric} \
    NO_Off {NO_off_metric} \
    NO_def {NO_def_metric}'
    )

KC_Predicted_Score = (KC_off_metric * NO_def_metric * KC_total_ave)
NO_Predicted_Score = (NO_off_metric * KC_def_metric * NO_total_ave)

if KC_Predicted_Score > NO_Predicted_Score:
    print('Kansas City Chiefs Win the Superbowl!')
else:
	print('New Orleans Saints Win the Superbowl!')

