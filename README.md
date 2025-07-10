# 🚀 Data Cleaning Report

## ✅ Before Cleaning
**Total rows:** 128 

### Sample rows:
   LatD   "LatM"   "LatS"  "NS"   "LonD"   "LonM"   "LonS"  "EW"              "City"  "State"
0    41        5       59   "N"       80       39        0   "W"        "Youngstown"       OH
1    42       52       48   "N"       97       23       23   "W"           "Yankton"       SD
2    46       35       59   "N"      120       30       36   "W"            "Yakima"       WA
3    42       16       12   "N"       71       48        0   "W"         "Worcester"       MA
4    43       37       48   "N"       89       46       11   "W"   "Wisconsin Dells"       WI 

### Missing values:
LatD        0
 "LatM"     0
 "LatS"     0
 "NS"       0
 "LonD"     0
 "LonM"     0
 "LonS"     0
 "EW"       0
 "City"     0
 "State"    0
dtype: int64 

### Any duplicates?
False 

## ✅ After Cleaning
**Total rows:** 128 

### First 5 rows:
   latd   "latm"   "lats"  "ns"   "lond"   "lonm"   "lons"  "ew"              "city"  "state"
0    41        5       59   "N"       80       39        0   "W"        "Youngstown"       OH
1    42       52       48   "N"       97       23       23   "W"           "Yankton"       SD
2    46       35       59   "N"      120       30       36   "W"            "Yakima"       WA
3    42       16       12   "N"       71       48        0   "W"         "Worcester"       MA
4    43       37       48   "N"       89       46       11   "W"   "Wisconsin Dells"       WI 

### Missing values remaining:
latd        0
 "latm"     0
 "lats"     0
 "ns"       0
 "lond"     0
 "lonm"     0
 "lons"     0
 "ew"       0
 "city"     0
 "state"    0
dtype: int64 

### Any duplicates?
False 

### Data types:
latd         int64
 "latm"      int64
 "lats"      int64
 "ns"       object
 "lond"      int64
 "lonm"      int64
 "lons"      int64
 "ew"       object
 "city"     object
 "state"    object
dtype: object 

### Unique values in 'latd': 25 

### Summary Statistics:
              latd      "latm"      "lats"  "ns"      "lond"      "lonm"      "lons"  "ew"          "city"  "state"
count   128.000000  128.000000  128.000000   128  128.000000  128.000000  128.000000   128             128      128
unique         NaN         NaN         NaN     1         NaN         NaN         NaN     1             120       47
top            NaN         NaN         NaN   "N"         NaN         NaN         NaN   "W"   "Springfield"       CA
freq           NaN         NaN         NaN   128         NaN         NaN         NaN   128               4       12
mean     38.820312   30.765625   27.492188   NaN   93.250000   27.742188   26.960938   NaN             NaN      NaN
std       5.200596   16.426158   18.977814   NaN   15.466499   16.927937   18.727807   NaN             NaN      NaN
min      26.000000    1.000000    0.000000   NaN   71.000000    0.000000    0.000000   NaN             NaN      NaN
25%      35.000000   16.000000   11.000000   NaN   80.000000   14.000000   11.000000   NaN             NaN      NaN
50%      39.000000   31.000000   24.000000   NaN   89.500000   26.500000   23.500000   NaN             NaN      NaN
75%      42.250000   45.000000   47.000000   NaN  103.250000   40.250000   47.000000   NaN             NaN      NaN
max      50.000000   59.000000   59.000000   NaN  123.000000   58.000000   59.000000   NaN             NaN      NaN 

✅ Cleaned data saved to `data/processed/cleaned_file.csv`
