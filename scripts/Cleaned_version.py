{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bae11888-d0b7-41b6-b8c7-4be350a185d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b3b9146d-64ee-424a-936c-fec7a05d6b7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = pd.read_csv('heart.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c454f925-b8b2-442b-a7c2-eaf0faee2c0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['age']=d['age']/365"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b6bc79d5-3681-43fa-a023-ff8fe3c5768a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0        50.391781\n",
      "1        55.419178\n",
      "2        51.663014\n",
      "3        48.282192\n",
      "4        47.873973\n",
      "           ...    \n",
      "69995    52.712329\n",
      "69996    61.920548\n",
      "69997    52.235616\n",
      "69998    61.454795\n",
      "69999    56.273973\n",
      "Name: age, Length: 70000, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(d['age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b3e7d662-d71f-4f2e-a93d-151dcd61d287",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(70000, 12)\n"
     ]
    }
   ],
   "source": [
    "print(d.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f7ceee88-01b5-4839-9eca-fb7bb9cde1ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol',\n",
      "       'gluc', 'smoke', 'alco', 'active', 'cardio'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(d.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f6355a83-e64c-407d-9aff-7379e1ffd66b",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.rename(columns={\n",
    "    'active':'phy_activity',\n",
    "},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "caa6416d-27c8-4350-a05e-b07d4200df28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol',\n",
      "       'gluc', 'smoke', 'alco', 'phy_activity', 'cardio'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(d.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e57d5549-e836-4f92-bc1d-58e77c42cb7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.columns = d.columns.str.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5acbd440-c787-4321-9f9e-6125bab9c950",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['AGE', 'GENDER', 'HEIGHT', 'WEIGHT', 'AP_HI', 'AP_LO', 'CHOLESTEROL',\n",
      "       'GLUC', 'SMOKE', 'ALCO', 'PHY_ACTIVITY', 'CARDIO'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(d.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ecbb98f7-bece-436c-be9f-ea6372520bb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         AGE  GENDER  HEIGHT  WEIGHT  AP_HI  AP_LO  CHOLESTEROL  GLUC  SMOKE  \\\n",
      "0  50.391781       2     168    62.0    110     80            1     1      0   \n",
      "1  55.419178       1     156    85.0    140     90            3     1      0   \n",
      "2  51.663014       1     165    64.0    130     70            3     1      0   \n",
      "3  48.282192       2     169    82.0    150    100            1     1      0   \n",
      "4  47.873973       1     156    56.0    100     60            1     1      0   \n",
      "\n",
      "   ALCO  PHY_ACTIVITY  CARDIO  \n",
      "0     0             1       0  \n",
      "1     0             1       1  \n",
      "2     0             0       1  \n",
      "3     0             1       1  \n",
      "4     0             0       0  \n"
     ]
    }
   ],
   "source": [
    "print(d.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6eca2405-d489-4aaf-9921-63c356b2df02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AGE             0\n",
      "GENDER          0\n",
      "HEIGHT          0\n",
      "WEIGHT          0\n",
      "AP_HI           0\n",
      "AP_LO           0\n",
      "CHOLESTEROL     0\n",
      "GLUC            0\n",
      "SMOKE           0\n",
      "ALCO            0\n",
      "PHY_ACTIVITY    0\n",
      "CARDIO          0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(d.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f177ba45-b747-4ae5-b6d4-2453ae1b62fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "print(d.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d9a6664e-baed-4fe2-98ec-7a78ef62b203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             AGE  GENDER  HEIGHT  WEIGHT  AP_HI  AP_LO  CHOLESTEROL  GLUC  \\\n",
      "1142   47.926027       2     169    74.0    120     80            1     1   \n",
      "1204   46.008219       1     165    68.0    120     80            1     1   \n",
      "1568   60.123288       1     165    60.0    120     80            1     1   \n",
      "1612   55.597260       1     162    70.0    110     70            1     1   \n",
      "2305   56.150685       1     165    70.0    120     80            1     1   \n",
      "2677   60.484932       1     175    69.0    120     80            1     1   \n",
      "6325   39.868493       1     158    64.0    120     80            1     1   \n",
      "8190   59.665753       1     160    58.0    120     80            1     1   \n",
      "10494  46.402740       2     170    70.0    120     80            1     1   \n",
      "10562  56.150685       1     165    70.0    120     80            1     1   \n",
      "10777  52.021918       1     164    65.0    120     80            1     1   \n",
      "16333  54.405479       1     165    68.0    120     80            1     1   \n",
      "17101  44.273973       1     168    65.0    120     80            1     1   \n",
      "17168  58.164384       1     164    62.0    120     80            1     1   \n",
      "20040  52.216438       1     165    65.0    120     80            1     1   \n",
      "21784  46.008219       1     165    68.0    120     80            1     1   \n",
      "21871  58.301370       1     165    65.0    120     80            1     1   \n",
      "22694  50.282192       1     169    67.0    120     80            1     1   \n",
      "24356  56.208219       1     164    66.0    120     80            1     1   \n",
      "28300  46.041096       1     157    67.0    120     80            1     1   \n",
      "28997  49.890411       1     160    60.0    120     80            1     1   \n",
      "32683  48.041096       2     165    65.0    120     80            1     1   \n",
      "38505  52.021918       1     164    65.0    120     80            1     1   \n",
      "38589  57.860274       1     160    60.0    120     80            1     1   \n",
      "40301  60.117808       1     165    65.0    120     80            1     1   \n",
      "40365  39.868493       1     158    64.0    120     80            1     1   \n",
      "42450  50.282192       1     169    67.0    120     80            1     1   \n",
      "44653  46.402740       2     170    70.0    120     80            1     1   \n",
      "45125  58.301370       1     165    65.0    120     80            1     1   \n",
      "45748  60.484932       1     175    69.0    120     80            1     1   \n",
      "45810  58.164384       1     164    62.0    120     80            1     1   \n",
      "47733  51.997260       1     165    65.0    120     80            1     1   \n",
      "48917  60.123288       1     165    60.0    120     80            1     1   \n",
      "50432  47.926027       2     169    74.0    120     80            1     1   \n",
      "52552  60.117808       1     165    65.0    120     80            1     1   \n",
      "54716  51.931507       1     165    75.0    120     80            1     1   \n",
      "56643  48.041096       2     165    65.0    120     80            1     1   \n",
      "56906  55.597260       1     162    70.0    110     70            1     1   \n",
      "57946  51.931507       1     165    75.0    120     80            1     1   \n",
      "58730  54.405479       1     165    68.0    120     80            1     1   \n",
      "60453  56.208219       1     164    66.0    120     80            1     1   \n",
      "60474  46.041096       1     157    67.0    120     80            1     1   \n",
      "62318  51.997260       1     165    65.0    120     80            1     1   \n",
      "64169  44.273973       1     168    65.0    120     80            1     1   \n",
      "65079  49.890411       1     160    60.0    120     80            1     1   \n",
      "65622  59.665753       1     160    58.0    120     80            1     1   \n",
      "66190  52.216438       1     165    65.0    120     80            1     1   \n",
      "68281  57.860274       1     160    60.0    120     80            1     1   \n",
      "\n",
      "       SMOKE  ALCO  PHY_ACTIVITY  CARDIO  \n",
      "1142       0     0             1       1  \n",
      "1204       0     0             1       0  \n",
      "1568       0     0             1       0  \n",
      "1612       0     0             1       0  \n",
      "2305       0     0             1       0  \n",
      "2677       0     0             1       1  \n",
      "6325       0     0             1       0  \n",
      "8190       0     0             1       0  \n",
      "10494      0     0             0       0  \n",
      "10562      0     0             1       0  \n",
      "10777      0     0             1       0  \n",
      "16333      0     0             1       0  \n",
      "17101      0     0             1       1  \n",
      "17168      0     0             1       0  \n",
      "20040      0     0             1       1  \n",
      "21784      0     0             1       0  \n",
      "21871      0     0             1       0  \n",
      "22694      0     0             1       0  \n",
      "24356      0     0             0       0  \n",
      "28300      0     0             1       0  \n",
      "28997      0     0             1       0  \n",
      "32683      0     0             1       0  \n",
      "38505      0     0             1       0  \n",
      "38589      0     0             0       1  \n",
      "40301      0     0             1       1  \n",
      "40365      0     0             1       0  \n",
      "42450      0     0             1       0  \n",
      "44653      0     0             0       0  \n",
      "45125      0     0             1       0  \n",
      "45748      0     0             1       1  \n",
      "45810      0     0             1       0  \n",
      "47733      0     0             0       0  \n",
      "48917      0     0             1       0  \n",
      "50432      0     0             1       1  \n",
      "52552      0     0             1       1  \n",
      "54716      0     0             1       1  \n",
      "56643      0     0             1       0  \n",
      "56906      0     0             1       0  \n",
      "57946      0     0             1       1  \n",
      "58730      0     0             1       0  \n",
      "60453      0     0             0       0  \n",
      "60474      0     0             1       0  \n",
      "62318      0     0             0       0  \n",
      "64169      0     0             1       1  \n",
      "65079      0     0             1       0  \n",
      "65622      0     0             1       0  \n",
      "66190      0     0             1       1  \n",
      "68281      0     0             0       1  \n"
     ]
    }
   ],
   "source": [
    "a = d[d.duplicated(keep=False)]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "93336990-cf90-4f11-828c-4977d497e1e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AGE             24\n",
      "GENDER           2\n",
      "HEIGHT          10\n",
      "WEIGHT          12\n",
      "AP_HI            2\n",
      "AP_LO            2\n",
      "CHOLESTEROL      1\n",
      "GLUC             1\n",
      "SMOKE            1\n",
      "ALCO             1\n",
      "PHY_ACTIVITY     2\n",
      "CARDIO           2\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(a.nunique()) #prints unique "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "bc46cde8-b91c-4cc7-989a-746b8ea38e4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CARDIO\n",
       "0    35021\n",
       "1    34979\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d['CARDIO'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f5fa5ef9-0bdf-4c83-94f5-5062300059ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "AGE\n",
       "54.084932    32\n",
       "49.961644    32\n",
       "56.005479    31\n",
       "55.824658    31\n",
       "50.008219    31\n",
       "             ..\n",
       "47.235616     1\n",
       "44.046575     1\n",
       "53.241096     1\n",
       "60.446575     1\n",
       "58.769863     1\n",
       "Name: count, Length: 8076, dtype: int64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d['AGE'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "86151a53-2241-4c6e-ad77-0f8bd91b079e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GENDER\n",
       "1    45530\n",
       "2    24470\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d['GENDER'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f39b5eef-278a-4911-90a0-d544a97d06bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.columns = d.columns.str.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6a0b845a-fdba-4937-829e-f0c93f5de3a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol',\n",
      "       'gluc', 'smoke', 'alco', 'phy_activity', 'cardio'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(d.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "68c6ec10-9612-4a3a-9642-9f3c69edf9c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>128.817286</td>\n",
       "      <td>96.630414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>154.011419</td>\n",
       "      <td>188.472530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-150.000000</td>\n",
       "      <td>-70.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>16020.000000</td>\n",
       "      <td>11000.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              ap_hi         ap_lo\n",
       "count  70000.000000  70000.000000\n",
       "mean     128.817286     96.630414\n",
       "std      154.011419    188.472530\n",
       "min     -150.000000    -70.000000\n",
       "25%      120.000000     80.000000\n",
       "50%      120.000000     80.000000\n",
       "75%      140.000000     90.000000\n",
       "max    16020.000000  11000.000000"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[['ap_hi','ap_lo']].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9f769058-8401-419b-a562-e4fa9a630661",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''d = d[(d['ap_hi'] > 50) & (d['ap_hi'] < 250)]\n",
    "d = d[(d['ap_lo'] > 30) & (d['ap_lo'] < 150)]\n",
    "\n",
    "\n",
    "Rows with ❌ negative values → removed\n",
    "Rows with ❌ very high values → removed\n",
    "Rows with ❌ ap_hi ≤ ap_lo → removed\n",
    "\n",
    "d = d[d['ap_hi'] > d['ap_lo']] #Systolic > Diastolic (always)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "947181ac-407e-4aba-9db6-fdee41e604bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>126.666715</td>\n",
       "      <td>81.298886</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>16.678923</td>\n",
       "      <td>9.417035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>60.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>240.000000</td>\n",
       "      <td>140.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              ap_hi         ap_lo\n",
       "count  68665.000000  68665.000000\n",
       "mean     126.666715     81.298886\n",
       "std       16.678923      9.417035\n",
       "min       60.000000     40.000000\n",
       "25%      120.000000     80.000000\n",
       "50%      120.000000     80.000000\n",
       "75%      140.000000     90.000000\n",
       "max      240.000000    140.000000"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[['ap_hi','ap_lo']].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "495b8c4b-fc7f-49a7-8f4f-ab403a72eb44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(68665, 12)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>phy_activity</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.00000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "      <td>68665.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>53.327234</td>\n",
       "      <td>1.348620</td>\n",
       "      <td>164.36065</td>\n",
       "      <td>74.117986</td>\n",
       "      <td>126.666715</td>\n",
       "      <td>81.298886</td>\n",
       "      <td>1.364611</td>\n",
       "      <td>1.225690</td>\n",
       "      <td>0.087978</td>\n",
       "      <td>0.053361</td>\n",
       "      <td>0.803350</td>\n",
       "      <td>0.494677</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.762144</td>\n",
       "      <td>0.476537</td>\n",
       "      <td>8.18382</td>\n",
       "      <td>14.332117</td>\n",
       "      <td>16.678923</td>\n",
       "      <td>9.417035</td>\n",
       "      <td>0.678857</td>\n",
       "      <td>0.571563</td>\n",
       "      <td>0.283265</td>\n",
       "      <td>0.224753</td>\n",
       "      <td>0.397469</td>\n",
       "      <td>0.499975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>29.583562</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>55.00000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>60.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>48.375342</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>159.00000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>53.975342</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>165.00000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>58.421918</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>170.00000</td>\n",
       "      <td>82.000000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.967123</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>250.00000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>240.000000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        gender       height        weight         ap_hi  \\\n",
       "count  68665.000000  68665.000000  68665.00000  68665.000000  68665.000000   \n",
       "mean      53.327234      1.348620    164.36065     74.117986    126.666715   \n",
       "std        6.762144      0.476537      8.18382     14.332117     16.678923   \n",
       "min       29.583562      1.000000     55.00000     11.000000     60.000000   \n",
       "25%       48.375342      1.000000    159.00000     65.000000    120.000000   \n",
       "50%       53.975342      1.000000    165.00000     72.000000    120.000000   \n",
       "75%       58.421918      2.000000    170.00000     82.000000    140.000000   \n",
       "max       64.967123      2.000000    250.00000    200.000000    240.000000   \n",
       "\n",
       "              ap_lo   cholesterol          gluc         smoke          alco  \\\n",
       "count  68665.000000  68665.000000  68665.000000  68665.000000  68665.000000   \n",
       "mean      81.298886      1.364611      1.225690      0.087978      0.053361   \n",
       "std        9.417035      0.678857      0.571563      0.283265      0.224753   \n",
       "min       40.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "25%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "50%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "75%       90.000000      2.000000      1.000000      0.000000      0.000000   \n",
       "max      140.000000      3.000000      3.000000      1.000000      1.000000   \n",
       "\n",
       "       phy_activity        cardio  \n",
       "count  68665.000000  68665.000000  \n",
       "mean       0.803350      0.494677  \n",
       "std        0.397469      0.499975  \n",
       "min        0.000000      0.000000  \n",
       "25%        1.000000      0.000000  \n",
       "50%        1.000000      0.000000  \n",
       "75%        1.000000      1.000000  \n",
       "max        1.000000      1.000000  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(d.shape)\n",
    "d.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2737d72e-c39d-467b-989b-740b42fc1d11",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = d[(d['height'] > 120) & (d['height'] < 220)]\n",
    "'''Normal adult range ≈ 140 cm – 200 cm\n",
    "Extreme but possible:\n",
    "Min ≈ 120 cm\n",
    "Max ≈ 220 cm'''\n",
    "d = d[(d['weight'] > 30) & (d['weight'] < 150)]\n",
    "'''Typical adults: 40 – 120 kg\n",
    "Extreme cases:\n",
    "Min ≈ 30 kg\n",
    "Max ≈ 150 kg'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "78ab47c9-483f-4ede-87a3-f8771b9ac699",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = d[(d['ap_hi'] > 80) & (d['ap_hi'] < 200)]\n",
    "d = d[(d['ap_lo'] > 50) & (d['ap_lo'] < 120)]\n",
    "'''Systolic (ap_hi)\n",
    "Normal: ~120\n",
    "Safe range: 90 – 180\n",
    "Diastolic (ap_lo)\n",
    "Normal: ~80\n",
    "Safe range: 60 – 120'''\n",
    "d = d[d['ap_hi'] > d['ap_lo']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "e0c1cdb1-a672-471b-b215-4407c110425a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(68087, 12)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>phy_activity</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>53.328960</td>\n",
       "      <td>1.348378</td>\n",
       "      <td>164.440451</td>\n",
       "      <td>74.008391</td>\n",
       "      <td>126.452069</td>\n",
       "      <td>81.193811</td>\n",
       "      <td>1.363153</td>\n",
       "      <td>1.224889</td>\n",
       "      <td>0.087755</td>\n",
       "      <td>0.053138</td>\n",
       "      <td>0.803457</td>\n",
       "      <td>0.493486</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.761301</td>\n",
       "      <td>0.476460</td>\n",
       "      <td>7.840451</td>\n",
       "      <td>14.005436</td>\n",
       "      <td>16.074694</td>\n",
       "      <td>9.031674</td>\n",
       "      <td>0.677964</td>\n",
       "      <td>0.570867</td>\n",
       "      <td>0.282941</td>\n",
       "      <td>0.224310</td>\n",
       "      <td>0.397386</td>\n",
       "      <td>0.499961</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>29.583562</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>125.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>85.000000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>48.382192</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>159.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>53.978082</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>165.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>58.424658</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>170.000000</td>\n",
       "      <td>82.000000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.967123</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>207.000000</td>\n",
       "      <td>149.000000</td>\n",
       "      <td>197.000000</td>\n",
       "      <td>119.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        gender        height        weight         ap_hi  \\\n",
       "count  68087.000000  68087.000000  68087.000000  68087.000000  68087.000000   \n",
       "mean      53.328960      1.348378    164.440451     74.008391    126.452069   \n",
       "std        6.761301      0.476460      7.840451     14.005436     16.074694   \n",
       "min       29.583562      1.000000    125.000000     31.000000     85.000000   \n",
       "25%       48.382192      1.000000    159.000000     65.000000    120.000000   \n",
       "50%       53.978082      1.000000    165.000000     72.000000    120.000000   \n",
       "75%       58.424658      2.000000    170.000000     82.000000    140.000000   \n",
       "max       64.967123      2.000000    207.000000    149.000000    197.000000   \n",
       "\n",
       "              ap_lo   cholesterol          gluc         smoke          alco  \\\n",
       "count  68087.000000  68087.000000  68087.000000  68087.000000  68087.000000   \n",
       "mean      81.193811      1.363153      1.224889      0.087755      0.053138   \n",
       "std        9.031674      0.677964      0.570867      0.282941      0.224310   \n",
       "min       52.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "25%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "50%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "75%       90.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "max      119.000000      3.000000      3.000000      1.000000      1.000000   \n",
       "\n",
       "       phy_activity        cardio  \n",
       "count  68087.000000  68087.000000  \n",
       "mean       0.803457      0.493486  \n",
       "std        0.397386      0.499961  \n",
       "min        0.000000      0.000000  \n",
       "25%        1.000000      0.000000  \n",
       "50%        1.000000      0.000000  \n",
       "75%        1.000000      1.000000  \n",
       "max        1.000000      1.000000  "
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(d.shape)\n",
    "d.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "6455868e-3ed7-4c7b-8b90-268e07130454",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1913"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "70000-68087"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "eb602cb5-a785-4293-95ee-65154847076a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(68087, 12)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>phy_activity</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "      <td>68087.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>53.328960</td>\n",
       "      <td>1.348378</td>\n",
       "      <td>164.440451</td>\n",
       "      <td>74.008391</td>\n",
       "      <td>126.452069</td>\n",
       "      <td>81.193811</td>\n",
       "      <td>1.363153</td>\n",
       "      <td>1.224889</td>\n",
       "      <td>0.087755</td>\n",
       "      <td>0.053138</td>\n",
       "      <td>0.803457</td>\n",
       "      <td>0.493486</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.761301</td>\n",
       "      <td>0.476460</td>\n",
       "      <td>7.840451</td>\n",
       "      <td>14.005436</td>\n",
       "      <td>16.074694</td>\n",
       "      <td>9.031674</td>\n",
       "      <td>0.677964</td>\n",
       "      <td>0.570867</td>\n",
       "      <td>0.282941</td>\n",
       "      <td>0.224310</td>\n",
       "      <td>0.397386</td>\n",
       "      <td>0.499961</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>29.583562</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>125.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>85.000000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>48.382192</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>159.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>53.978082</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>165.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>58.424658</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>170.000000</td>\n",
       "      <td>82.000000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.967123</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>207.000000</td>\n",
       "      <td>149.000000</td>\n",
       "      <td>197.000000</td>\n",
       "      <td>119.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        gender        height        weight         ap_hi  \\\n",
       "count  68087.000000  68087.000000  68087.000000  68087.000000  68087.000000   \n",
       "mean      53.328960      1.348378    164.440451     74.008391    126.452069   \n",
       "std        6.761301      0.476460      7.840451     14.005436     16.074694   \n",
       "min       29.583562      1.000000    125.000000     31.000000     85.000000   \n",
       "25%       48.382192      1.000000    159.000000     65.000000    120.000000   \n",
       "50%       53.978082      1.000000    165.000000     72.000000    120.000000   \n",
       "75%       58.424658      2.000000    170.000000     82.000000    140.000000   \n",
       "max       64.967123      2.000000    207.000000    149.000000    197.000000   \n",
       "\n",
       "              ap_lo   cholesterol          gluc         smoke          alco  \\\n",
       "count  68087.000000  68087.000000  68087.000000  68087.000000  68087.000000   \n",
       "mean      81.193811      1.363153      1.224889      0.087755      0.053138   \n",
       "std        9.031674      0.677964      0.570867      0.282941      0.224310   \n",
       "min       52.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "25%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "50%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "75%       90.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "max      119.000000      3.000000      3.000000      1.000000      1.000000   \n",
       "\n",
       "       phy_activity        cardio  \n",
       "count  68087.000000  68087.000000  \n",
       "mean       0.803457      0.493486  \n",
       "std        0.397386      0.499961  \n",
       "min        0.000000      0.000000  \n",
       "25%        1.000000      0.000000  \n",
       "50%        1.000000      0.000000  \n",
       "75%        1.000000      1.000000  \n",
       "max        1.000000      1.000000  "
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(d.shape)\n",
    "d.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "2ed851b9-ef78-4f69-8881-00c59d20bc29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>phy_activity</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, phy_activity, cardio]\n",
       "Index: []"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[d['ap_hi'] < d['ap_lo']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9f508a75-0c68-45a6-a2ec-5fadb16d7edd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cardio\n",
       "0    34487\n",
       "1    33600\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d['cardio'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "92fefb76-5b76-4488-a403-5a617373376e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#d['bmi'] = d['weight'] / ((d['height']/100) ** 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "551e29a8-76d4-45d5-8da0-bbd99021d565",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.drop(columns=['bmi'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "cd9e2dcb-50fd-4c44-85c5-6aed0bff653b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  \\\n",
      "0      50.391781       2     168    62.0    110     80            1     1   \n",
      "1      55.419178       1     156    85.0    140     90            3     1   \n",
      "2      51.663014       1     165    64.0    130     70            3     1   \n",
      "3      48.282192       2     169    82.0    150    100            1     1   \n",
      "4      47.873973       1     156    56.0    100     60            1     1   \n",
      "...          ...     ...     ...     ...    ...    ...          ...   ...   \n",
      "69995  52.712329       2     168    76.0    120     80            1     1   \n",
      "69996  61.920548       1     158   126.0    140     90            2     2   \n",
      "69997  52.235616       2     183   105.0    180     90            3     1   \n",
      "69998  61.454795       1     163    72.0    135     80            1     2   \n",
      "69999  56.273973       1     170    72.0    120     80            2     1   \n",
      "\n",
      "       smoke  alco  phy_activity  cardio  \n",
      "0          0     0             1       0  \n",
      "1          0     0             1       1  \n",
      "2          0     0             0       1  \n",
      "3          0     0             1       1  \n",
      "4          0     0             0       0  \n",
      "...      ...   ...           ...     ...  \n",
      "69995      1     0             1       0  \n",
      "69996      0     0             1       1  \n",
      "69997      0     1             0       1  \n",
      "69998      0     0             0       1  \n",
      "69999      0     0             1       0  \n",
      "\n",
      "[68087 rows x 12 columns]\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4144ee5a-6e37-41e4-9b05-478e2030920a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''cols = list(d.columns)\n",
    "\n",
    "# remove bmi and cardio\n",
    "cols.remove('bmi')\n",
    "cols.remove('cardio')\n",
    "\n",
    "# add bmi and then cardio at end\n",
    "cols = cols + ['bmi', 'cardio']\n",
    "\n",
    "# reorder dataframe\n",
    "d = d[cols]'''\n",
    "#to add the column bmi right before the target column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "593e9a54-91e5-45e6-9bf1-5b22f2e6cd26",
   "metadata": {},
   "outputs": [],
   "source": [
    "d.to_csv(\"cleaned_data.csv\", index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
