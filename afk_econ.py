import json
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Tokens
# ! Fabled
# ? Is your Guild in Fabled?
# | test
# $ new

# Pandas Frame Styling
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.options.display.float_format = '{:,.5f}'.format

# json imports
with open('library/fos_chapter_df.json5') as f2:
    fos_ch = pd.DataFrame.from_dict(json.load(f2))

with open('library/fos_player_df.json5') as f3:
    fos_p = pd.DataFrame.from_dict(json.load(f3))

with open('library/vip_df.json5') as f4:
    vip = pd.DataFrame.from_dict(json.load(f4))

with open('library/idle.json5') as f5:
    idle = pd.DataFrame(json.load(f5))

with open('library/pvp_df.json5') as f6:
    pvp = pd.DataFrame(json.load(f6))

with open('library/guild_df.json5') as f7:
    guild = pd.DataFrame(json.load(f7))

with open('library/arena_division.json5') as f8:
    arena_division = pd.DataFrame(json.load(f8))

# TODO:
# Team Bounties []
# Twisted Realm []
# Challenger Rank [✓]
# Dismal Final Rewards [✓]
# Nobles Levels (Regal, CoE, TB) [✓]


# ? Variables?
PLAYER_LEVEL = '180'  # [0, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180]
VIP = '16'  # (Min: 1, Max: 18)
CHAPTER = '40'  # (Min: 1, Max: 40)

# ! PVP
ARENA_RANK = '1'  # (Min: 23, Max: 1)
CHALLENGER_RANK = '2'  # (Max: 1)

# ! Twisted / Cursed Realm
CURSED_RANK = '10%'  # '50', '200', '1%', '2%', '3%', '4%', '5%', '6%', '8%', '10%', '0'

# ! WRIZZ & SOREN
WRIZZ_CHESTS = '23'  # (Max: 23)
SOREN_CHESTS = '23'  # (Max: 23)
WRIZZ_GUILD_GOLD = 1080000  # (Max: 1080000)
WRIZZ_GUILD_COIN = 1158  # (Max: 1158)
SOREN_GUILD_GOLD = 1080000  # (Max: 1080000)
SOREN_GUILD_COIN = 1158  # (Max: 1158)

# ? TOWER PROGRESSION?
KINGS_TOWER = 350  # (Options: 250, 300, 350 | T1 Gear Drop)
FACTION_TOWER = 280  # (Options: 200, 240, 280 | T2 Gear Drop)
GOD_TOWER = 300  # (Options: 100, 200, 300 | Invigor +30%, +60%, +90%)

# ? SUBSCRIPTION?
SUBSCRIPTION = True

# ? Sell Dura Fragments?
SELL_DURA = True

# ? Is your Guild in Fabled?
FABLED = True
if FABLED:
    FABLED = 100  # Diamonds
else:
    FABLED = 0

# ! STORE
# ? Buy Dust with Gold?
dStore = True
if dStore:
    dStore = [2225000, 500]
else:
    dStore = [0, 0]

# ? Buy Poe with Gold?
pStore = True
if pStore:
    pStore = [1125000, 250]
else:
    pStore = [0, 0]

# ? Buy Shard with Gold?
sStore = True
if sStore:
    sStore = [2000000, 20]
else:
    sStore = [0, 0]

# ? Buy Dust chest with diamonds?
dChestStore = False
if dChestStore:
    dChestStore = 1
else:
    dChestStore = 0

# ? Buy Cores with diamonds?
cStore = False
if cStore:
    cStore = 1
else:
    cStore = 0

# ? Refreshes?
rStore = 2  # Max 2 currently

# ! FAST REWARDS
# ? NUMBER?
FAST = 7  # Options: 1, 2, 3, 4, 5, 6, 7, 8 | 0, 50, 80 (130), 100 (230), 100 (330), 200 (530), 300 (830), 400 (1230)

# ! PAID BUNDLES
# ? MONTHLY CARD?
MONTHLY_CARD = True

# ? MONTHLY Reward One / Two?
MONTHLY_REWARD = 'dust_hours'  # Options: dust_hours, exp_hours, gold_hours, gold_e, silver_e, shard

# ? DELUXE CARD?
DELUXE_CARD = True

# ? DELUXE Reward One / Two?
DELUXE_REWARD_ONE = 'red_e'  # Options: red_e, gold_e, silver_e
DELUXE_REWARD_TWO = 'core'  # Options: core, twisted, poe, blue

# ? REGAL?
REGAL_PAID = True

# ? CHAMPIONS OF ESPERIA?
COE_PAID = True
COE_PREMIUM = True
# ? Resource?
COE_FREE_RESOURCE = 'dust_hours'  # 'dust_hours', 'silver_e', 'gold_e', 'red_e', 'core'
COE_PAID_RESOURCE = 'dust_hours'  # 'dust_hours', 'silver_e', 'gold_e', 'red_e', 'core'
COE_PAID_PREMIUM = 'core'  # 'dust', 'silver_e', 'gold_e', 'red_e', 'core'

# ? TWISTED BOUNTIES?
TB_PAID = True
TB_PREMIUM = True
# ? Resource?
TB_FREE_RESOURCE = 'exp_hours'  # 'gold_hours', 'exp_hours', 'poe', 'twisted', 'shard'
TB_PAID_RESOURCE = 'exp_hours'  # 'gold_hours', 'exp_hours', 'poe', 'twisted', 'shard'
TB_PAID_PREMIUM = 'shard'  # 'gold', 'exp', 'poe', 'twisted', 'shard'

# ! Misty Valley
MISTY = pd.Series(dtype=int)

# ? CHOICE ONE [CHAPTER 17]
m0GOLD = False  # 288 GOLD HOURS
m0EXP = False  # 96 EXP HOURS
m0DUST = True  # 96 EXP HOURS

if m0GOLD:
    MISTY['gold_hours'] = 288
elif m0EXP:
    MISTY['exp_hours'] = 96
else:
    MISTY['dust_hours'] = 96

# ? CHOICE TWO [CHAPTER 17]
m1DIAMOND = False  # 1000 DIAMOND
m1GUILD_COIN = False  # 30,000 GUILD COINS
m1TWISTED = True  # 400 TWISTED ESSENCE

if m1DIAMOND:
    MISTY['diamond'] = 1000
elif m1GUILD_COIN:
    MISTY['guild_coin'] = 30000
else:
    MISTY['twisted'] = 400

# ? CHOICE THREE [CHAPTER 17]
m2PURPLE = True  # 60 PURPLE SHARDS
m2BLUE = False  # 720 BLUE SHARDS

if m2PURPLE:
    MISTY['purple'] = 60
else:
    MISTY['blue'] = 720

# ? CHOICE FOUR [CHAPTER 19]
m3PURPLE = False  # 60 PURPLE SHARDS
m3SCROLL = False  # 5 SCROLLS
m3POE = True  # 1000 POE COINS

if m3PURPLE:
    MISTY['purple'] = MISTY.get('purple', default=0) + 60
elif m3SCROLL:
    MISTY['scroll'] = 5
else:
    MISTY['poe'] = 1000

# ? CHOICE FIVE [CHAPTER 21]
m4SILVER_E = False  # 40 SILVER EMBLEMS
m4GOLD_E = False  # 20 GOLD EMBLEMS
m4RED_E = True  # 10 RED EMBLEMS
m4POE = False  # 1000 POE COINS

if m4SILVER_E:
    MISTY['silver_e'] = 40
elif m4GOLD_E:
    MISTY['gold_e'] = 20
elif m4RED_E:
    MISTY['red_e'] = 10
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000

# ? CHOICE SIX [CHAPTER 23]
m5T1 = False  # T1
m5T2 = False  # T2
m5T3 = True  # T3
m5POE = False  # 1000 POE COINS

if m5T1:
    MISTY['t1'] = 1
elif m5T2:
    MISTY['t2'] = 1
elif m5T3:
    MISTY['t3'] = 1
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000

# ? CHOICE SEVEN [CHAPTER 25]
m6SILVER_E = False  # 40 SILVER EMBLEMS
m6GOLD_E = False  # 20 GOLD EMBLEMS
m6RED_E = False  # 10 RED EMBLEMS
m6POE = False  # 1000 POE COINS
m6SHARD = True  # 200 SHARDS

if m6SILVER_E:
    MISTY['silver_e'] = MISTY.get('silver_e', default=0) + 40
elif m6GOLD_E:
    MISTY['gold_e'] = MISTY.get('gold_e', default=0) + 20
elif m6RED_E:
    MISTY['red_e'] = MISTY.get('red_e', default=0) + 10
elif m6SHARD:
    MISTY['shard'] = MISTY.get('shard', default=0) + 200
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000

# ? CHOICE EIGHT [CHAPTER 27]
m7PURPLE = False  # 60 PURPLE SHARDS
m7SCROLL = False  # 5 SCROLLS
m7POE = True  # 1000 POE COINS

if m7PURPLE:
    MISTY['purple'] = MISTY.get('purple', default=0) + 60
elif m7SCROLL:
    MISTY['scroll'] = MISTY.get('scroll', default=0) + 5
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000

# ? CHOICE TEN [CHAPTER 31]
m8SILVER_E = False  # 40 SILVER EMBLEMS
m8GOLD_E = False  # 20 GOLD EMBLEMS
m8RED_E = False  # 10 RED EMBLEMS
m8POE = False  # 1000 POE COINS
m8CORE = True  # 100 CORES

if m8SILVER_E:
    MISTY['silver_e'] = MISTY.get('silver_e', default=0) + 40
elif m8GOLD_E:
    MISTY['gold_e'] = MISTY.get('gold_e', default=0) + 20
elif m8RED_E:
    MISTY['red_e'] = MISTY.get('red_e', default=0) + 10
elif m8CORE:
    MISTY['core'] = MISTY.get('core', default=0) + 100
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000

# ? CHOICE ELEVEN [CHAPTER 32]
m9SILVER_E = False  # 40 SILVER EMBLEMS
m9GOLD_E = False  # 20 GOLD EMBLEMS
m9RED_E = False  # 10 RED EMBLEMS
m9SHARD = True  # 200 SHARDS

if m9SILVER_E:
    MISTY['silver_e'] = MISTY.get('silver_e', default=0) + 40
elif m9GOLD_E:
    MISTY['gold_e'] = MISTY.get('gold_e', default=0) + 20
elif m9RED_E:
    MISTY['red_e'] = MISTY.get('red_e', default=0) + 10
else:
    MISTY['shard'] = MISTY.get('shard', default=0) + 200

# ? CHOICE TWELVE [CHAPTER 33]
m10TWISTED = False  # 200 TWISTED ESSENCE
m10POE = False  # 2000 POE COINS
m10CORE = True  # 100 CORES

if m10TWISTED:
    MISTY['twisted'] = MISTY.get('twisted', default=0) + 200
elif m10POE:
    MISTY['poe'] = MISTY.get('poe', default=0) + 2000
else:
    MISTY['core'] = MISTY.get('core', default=0) + 100

# ? CHOICE THIRTEEN [CHAPTER 34]
m11SILVER_E = False  # 40 SILVER EMBLEMS
m11GOLD_E = False  # 20 GOLD EMBLEMS
m11RED_E = False  # 10 RED EMBLEMS
m11SHARD = True  # 200 SHARDS

if m11SILVER_E:
    MISTY['silver_e'] = MISTY.get('silver_e', default=0) + 40
elif m11GOLD_E:
    MISTY['gold_e'] = MISTY.get('gold_e', default=0) + 20
elif m11RED_E:
    MISTY['red_e'] = MISTY.get('red_e', default=0) + 10
else:
    MISTY['shard'] = MISTY.get('shard', default=0) + 200

# ? CHOICE Fourteen [CHAPTER 35]
m12TWISTED = False  # 200 TWISTED ESSENCE
m12POE = False  # 2000 POE COINS
m12CORE = True  # 100 CORES

if m12TWISTED:
    MISTY['twisted'] = MISTY.get('twisted', default=0) + 200
elif m12POE:
    MISTY['poe'] = MISTY.get('poe', default=0) + 2000
else:
    MISTY['core'] = MISTY.get('core', default=0) + 100

# ? CHOICE Fifteen [CHAPTER 36]
m13T1 = False  # T1
m13T2 = False  # T2
m13T3 = True  # T3
m13POE = False  # 1000 POE COINS

if m13T1:
    MISTY['t1'] = 1
elif m13T2:
    MISTY['t2'] = 1
elif m13T3:
    MISTY['t3'] = MISTY.get('t3', default=0) + 1
else:
    MISTY['poe'] = MISTY.get('poe', default=0) + 1000


def challenger_rank(target: int, rate=0):
    try:
        rate = arena_division[target]
    except KeyError:
        prev = 12431
        for i in reversed(arena_division.loc['Rank']):
            if target < i:
                prev = i
            elif target >= i:
                return arena_division[str(prev)].CoinDelta.astype(int)
    return arena_division[rate].CoinDelta.astype(int)


def t1_drop_bonus(kings_tower):
    if kings_tower >= 350: return 3
    if kings_tower >= 300: return 2
    if kings_tower >= 250: return 1
    return 0


def t2_drop_bonus(faction_tower):
    if faction_tower >= 280: return 3
    if faction_tower >= 240: return 2
    if faction_tower >= 200: return 1
    return 0


def invigor_bonus(god_tower):
    if god_tower >= 300: return 3
    if god_tower >= 200: return 2
    if god_tower >= 100: return 1
    return 0


def daily_addition(x, y):
    return (x + y).fillna(y).fillna(x)


def daily_batch(x, z: list):
    for i in z: x = daily_addition(x, i)
    return x


def daily_hours(x):
    for i in ['gold', 'exp', 'dust']: x[i] += x[i + '_hours'] * idle[i]
    return x.drop(['gold_hours', 'exp_hours', 'dust_hours'])


def monthly_gen(purchase: bool, reward: str):
    if purchase:
        monthly = pd.Series([6 * 2, 6 * 2, 6 * 8, 2, 3, 15],
                            index=['dust_hours', 'exp_hours', 'gold_hours', 'gold_e', 'silver_e', 'shard'])
        if int(VIP) >= 12:
            monthly *= 4
        else:
            monthly *= 3
        monthly["diamond"] = 300 / 30 + 100
        return monthly.loc[[reward, 'diamond']]
    return pd.Series([0, 0], index=[reward, 'diamond'])


def deluxe_gen(purchase: bool, reward_one: str, reward_two: str):
    if purchase:
        monthly = pd.Series([60, 12, 24, 240, 2, 5, 8],
                            index=['blue', 'core', 'twisted', 'poe', 'red_e', 'gold_e', 'silver_e'])
        if int(VIP) >= 14:
            return pd.Series([2 * monthly[reward_one], 2 * monthly[reward_two], 980 / 30 + 600],
                             index=[reward_one, reward_two, 'diamond'])
        elif int(VIP) >= 12:
            return pd.Series([monthly[reward_one], 2 * monthly[reward_two], 980 / 30 + 600],
                             index=[reward_one, reward_two, 'diamond'])
        else:
            return pd.Series([monthly[reward_one], monthly[reward_two], 980 / 30 + 600],
                             index=[reward_one, reward_two, 'diamond'])
    return pd.Series([0, 0, 0], index=[reward_one, reward_two, 'diamond'])


fos_p = fos_p[PLAYER_LEVEL]
fos_ch = fos_ch[CHAPTER]
idle = idle[CHAPTER]

idle['t1_g'] = t1_drop_bonus(KINGS_TOWER) / (336 * 3)
idle['t2_g'] = t2_drop_bonus(FACTION_TOWER) / (336 * 3)
idle['invigor'] *= 1 + invigor_bonus(GOD_TOWER) * 0.3


daily_card1 = monthly_gen(MONTHLY_CARD, MONTHLY_REWARD)
daily_card2 = deluxe_gen(DELUXE_CARD, DELUXE_REWARD_ONE, DELUXE_REWARD_TWO)
daily_cards = (daily_card1 + daily_card2).fillna(daily_card1).fillna(daily_card2)

if SUBSCRIPTION:
    sub = pd.Series({
        'gold': 0.1,  # Base AFK Reward Gold
        'guild_coin': 0.1,  # Bonus Guild Coins
        'maze_coin': 0.1,  # Bonus Maze Coins
        'team_bounty': 1  # Bonus Maze Coins
    })
else:
    sub = pd.Series({
        'gold': 0,  # Base AFK Reward Gold
        'guild_coin': 0,  # Bonus Guild Coins
        'maze_coin': 0,  # Bonus Maze Coins
        'team_bounty': 0  # Bonus Maze Coins
    })

if int(VIP) >= 6: guild_challenge = 3
else: guild_challenge = 2

guild_daily = pd.Series({
    'gold': guild[WRIZZ_CHESTS]['gold'] * guild_challenge + WRIZZ_GUILD_GOLD + (
                guild[SOREN_CHESTS]['gold'] * guild_challenge + SOREN_GUILD_GOLD) / 2,
    'guild_coin': guild[WRIZZ_CHESTS]['guild_coin'] * (
                1 + sub['guild_coin'] + fos_ch['guild_coin']) * guild_challenge + WRIZZ_GUILD_COIN + (guild[SOREN_CHESTS]['guild_coin'] * (1 + sub['guild_coin'] + fos_ch['guild_coin']) * guild_challenge + SOREN_GUILD_COIN) / 2,
    'diamond': (int(WRIZZ_CHESTS) + 5 * int(SOREN_CHESTS)/9) * guild_challenge * 0.1 * (0.5 * 10 + 0.4 * 30 + 0.1 * 100)
})

STORE = {
    'gold': -(1 + rStore) * (dStore[0] + pStore[0] + sStore[0]),
    'dust': (1 + rStore) * dStore[1],
    'poe': (1 + rStore) * pStore[1],
    'diamond': -(1 + rStore) * (300 * dChestStore + 200 * cStore) - rStore * 100,
    'dust_hours': (1 + rStore) * 24 * dChestStore,
    'shard': (1 + rStore) * sStore[1],
    'core': (1 + rStore) * 10 * cStore
}
store_daily = pd.Series(STORE)

# ! Fast Rewards
FAST_COST = {
    1: -0,
    2: -50,
    3: -130,
    4: -230,
    5: -330,
    6: -530,
    7: -830,
    8: -1230,
}
FAST_COST = FAST_COST[FAST]

# ! TWISTED REALM [FABLED]
twisted_normal = {
    'twisted': 380,
    'poe': 1290
}
twisted_double = {
    'twisted': 760,
    'poe': 2580
}
twisted_normal = pd.Series(twisted_normal)
twisted_double = pd.Series(twisted_double)
twisted_daily = ((twisted_normal * 8 + twisted_double * 4) / 24)

# ! QUESTS
daily_quests = {
    'gold_hours': 2,
    'dust_hours': 2,
    'arena': 2,  # Tickets
    'diamond': 100,
    'scroll': 1,
    'blue': 5
}
CHAPTER = int(CHAPTER)
if CHAPTER > 16: daily_quests['diamond'] = 150
if CHAPTER > 20: daily_quests['exp_hours'] = 2
if CHAPTER > 23: daily_quests['gold_hours'] = 4

weekly_quests = {
    'gold_hours': 16,
    'diamond': 400,
    'scroll': 3,
    'blue': 60,
    'purple': 10,
    'reset': 1
}
if CHAPTER > 22: weekly_quests['twisted'] = 50
if CHAPTER > 23: weekly_quests['poe'] = 500
if CHAPTER > 28: weekly_quests['silver_e'] = 20
if CHAPTER > 29: weekly_quests['gold_e'] = 10
if CHAPTER > 30: weekly_quests['red_e'] = 5
CHAPTER = str(CHAPTER)

daily_quests = pd.Series(daily_quests)
weekly_quests = pd.Series(weekly_quests)

quests_daily = (daily_quests + weekly_quests / 7).fillna(weekly_quests / 7).fillna(daily_quests)

# ! PVP
# ! ARENA
arena_ticket = {  # Per Ticket
    'gold': 90000 * 0.495,
    'dust': 10 * 0.495,
    'pit': 0.01
}
pit_master = {
    'dust': 500 * 0.2,
    'blue': 60 * 0.2,
    'purple': 10 * 0.3,
    'diamond': 150 * 0.15 + 300 * 0.12 + 3000 * 0.03
}
arena_ticket = pd.Series(arena_ticket)
pit_master = pd.Series(pit_master)

daily_arena = arena_ticket * (vip[VIP]['arena'] + daily_quests['arena'])
pit = pit_master * daily_arena['pit']
daily_arena = (daily_arena + pit).fillna(daily_arena).fillna(pit).drop('pit')
daily_arena['diamond'] = daily_arena['diamond'] + (13 * pvp[ARENA_RANK]['daily'] + pvp[ARENA_RANK]['biweekly']) / 14

# ! CHALLENGER
challenger = int(challenger_rank(int(CHALLENGER_RANK))) * 24

# ! OAK INN
oak_inn = {
    'gold': 1500000 * 3 / 4,
    'dust': 150 * 3 / 4,
    'diamond': 100 * 3 / 4,
    'blue': 30 * 3 / 4
}
daily_inn = pd.Series(oak_inn)

# ! NOBLES
regal_index = [['free', 'paid'], ['blue', 'purple', 'diamond']]
regal_index = pd.MultiIndex.from_product(regal_index, names=['type', 'resource'])
REGAL_6 = pd.Series([3300, 0, 0, 0, 1100, 5500], index=regal_index)
if REGAL_PAID: daily_regal_6 = (REGAL_6['free'] + REGAL_6['paid']) / 49
else: daily_regal_6 = REGAL_6['free'] / 49

CoE = {
    'free': {
        'dust_hours': 534,
        'silver_e': 192,
        'gold_e': 136,
        'red_e': 49,
        'core': 585
    },
    'paid': {
        'dust_hours': 2548,
        'silver_e': 735,
        'gold_e': 484,
        'red_e': 210,
        'core': 1960,
        'diamond': 5500
    }
}
CoE = pd.DataFrame.from_dict(CoE)

CoE_index = [['free', 'paid', 'premium'], [COE_PAID_RESOURCE, COE_PAID_PREMIUM, 'diamond']]
CoE_index = pd.MultiIndex.from_product(CoE_index, names=['type', 'resource'])
if COE_PAID:
    if COE_PREMIUM:
        CoE_6 = pd.Series([
            CoE['free'][COE_PAID_RESOURCE], 0, 0,
            CoE['paid'][COE_PAID_RESOURCE], 0, CoE['paid']['diamond'],
            0, CoE['paid'][COE_PAID_PREMIUM], 0
        ], index=CoE_index)
        daily_coe_6 = (CoE_6['free'] + CoE_6['paid'] + CoE_6['premium']) / 36
    else:
        CoE_6 = pd.Series([
            CoE['free'][COE_PAID_RESOURCE], 0, 0,
            CoE['paid'][COE_PAID_RESOURCE], 0, CoE['paid']['diamond'],
            0, 0, 0
        ], index=CoE_index)
        daily_coe_6 = (CoE_6['free'] + CoE_6['paid']) / 36
else:
    CoE_6 = pd.Series([
        CoE['free'][COE_FREE_RESOURCE], 0, 0,
        0, 0, 0,
        0, 0, 0
    ], index=CoE_index)
    daily_coe_6 = CoE_6['free'] / 36

TB = {
    'free': {
        'gold_hours': 3825,
        'exp_hours': 956,
        'poe': 9900,
        'twisted': 990,
        'shard': 1170,
    },
    'paid': {
        'gold_hours': 11472,
        'exp_hours': 3444,
        'poe': 37000,
        'twisted': 3700,
        'shard': 3920,
        'diamond': 5500
    }
}
TB = pd.DataFrame.from_dict(TB)

TB_index = [['free', 'paid', 'premium'], [TB_PAID_RESOURCE, TB_PAID_PREMIUM, 'diamond']]
TB_index = pd.MultiIndex.from_product(TB_index, names=['type', 'resource'])
if TB_PAID:
    if TB_PREMIUM:
        TB_6 = pd.Series([
                TB['free'][TB_FREE_RESOURCE], 0, 0,
                TB['paid'][TB_PAID_RESOURCE], 0, TB['paid']['diamond'],
                0, TB['paid'][TB_PAID_PREMIUM], 0
            ], index=TB_index)
        daily_tb_6 = (TB_6['free'] + TB_6['paid'] + TB_6['premium']) / 44
    else:
        TB_6 = pd.Series(
            [
                TB['free'][TB_FREE_RESOURCE], 0, 0,
                TB['paid'][TB_PAID_RESOURCE], 0, TB['paid']['diamond'],
                0, 0, 0
            ], index=TB_index)
        daily_tb_6 = (TB_6['free'] + TB_6['paid']) / 44
else:
    TB_6 = pd.Series([
        TB['free'][TB_FREE_RESOURCE], 0, 0,
        0, 0, 0,
        0, 0, 0
    ], index=TB_index)
    daily_tb_6 = TB_6['free'] / 44

# ! Maze - Complete
maze = pd.DataFrame.from_dict({
    'gold': 232 * idle['gold'],
    'exp': 52.5 * idle['exp'],
    'dust': 46.5 * idle['dust'],
    'maze_coin': (6 * 400 + 3 * 600 + 700) * (1 + vip.loc['maze_coin'] + sub['maze_coin'] + fos_ch.loc['maze_coin']),
    'glad_coin': 3333,
    'guild_coin': 1000,
    'shard': (3 / 8 * 30 + 1 / 8 * 50) * 3,
    'core': (3 / 8 * 30 + 1 / 8 * 50) * 3,
    'diamond': 50 + 100 + 200,
})
maze_daily = (maze.loc[VIP] * 8 + 2 * maze.loc[VIP] * 4) / 24

# ! Idle Rewards
value = {
    "diamond": 1,
    "gold": 2 / idle['gold'],
    "exp": 8 / idle['exp'],
    "dust": 12.5 / idle['dust'],
    "gold_hours": 2,
    "exp_hours": 8,
    "dust_hours": 12.5,
    "poe": 0.675,
    "twisted": 6.75,
    "silver_e": 10080000 * (500 * 12.5 / idle['dust']) / 2250000 / 30,
    "gold_e": 10920000 * (500 * 12.5 / idle['dust']) / 2250000 / 20,
    "red_e": 135,
    "dura": 100000 * 500 * 12.5 / idle['dust'] / 2250000,
    "class": (9000 * 0.675 + 900 * 6.75 + 2 * 3000) / (3 * 400),
    "mythic": 1000,  # Random Mythic
    "t1": 1000,
    "t2": 2000,
    "t3": 3000,
    "invigor": 1200 / 5000,
    "blue": 2.6,
    "purple": 31.2,
    "scroll": 2.6 * 60 * 1.5,
    "faction": 2.6 * 60 * 1.5 * 1.2,
    "t1_g": 1000 + 1000,
    "t2_g": 1000 + 1000 + 2000,
    "shard": 6.75,
    "core": 13.5,
    "maze_coin": (25*135*2 + 50*135 + 400*6.75 - 1000) / (37125*2 + 40000 + 64000),
    "glad_coin": 14000 / 250000
}
value = pd.Series(value)
hourly = idle.copy('deep')

if SELL_DURA:
    hourly.loc['gold'] = hourly['gold'] * (1 + vip[VIP]['gold'] + fos_p['gold'] + sub['gold']) + fos_ch['gold'] / 24 + \
                         hourly['dura'] * 100000
    hourly = hourly.drop('dura')
else:
    hourly.loc['gold'] = hourly['gold'] * (1 + vip[VIP]['gold'] + fos_p['gold'] + sub['gold']) + fos_ch['gold'] / 24

hourly.loc['exp'] = hourly['exp'] * (1 + vip[VIP]['exp'] + fos_p['exp']) + fos_ch['exp'] / 24
hourly.loc['dust'] = hourly['dust'] * (1 + fos_p['dust']) + fos_ch['dust'] / 24
hourly.loc['mythic'] = hourly['mythic'] * (1 + fos_ch['mythic'])
hourly.loc['t2'] = hourly['t2'] * (1 + fos_ch['t2'])
hourly.loc['t3'] = fos_ch['t3'] / 336

fast_rewards = (2 * hourly.copy('deep').drop(["t1_g", "t2_g", "mythic", "t2", "t3"]))
fast_daily = fast_rewards.copy('deep') * FAST
idle_daily = 24 * hourly.copy('deep')

# ! MISTY
MISTY['gold'] = MISTY.get('gold', default=0) + 7 * 1000000
MISTY['blue'] = MISTY.get('blue', default=0) + 10 * 120
MISTY['purple'] = MISTY.get('purple', default=0) + 10 * 18
MISTY['poe'] = MISTY.get('poe', default=0) + 30 * 450
MISTY['dust_hours'] = MISTY.get('dust_hours', default=0) + 7 * 4 * 8
MISTY['exp_hours'] = MISTY.get('exp_hours', default=0) + 6 * 24
misty_daily = MISTY.copy('deep') / 30

# ! BOUNTY BOARD
bounty_normal = {
    8: {
        'dust': 810,
        'gold': 152000,
        'diamond': 51,
        'blue': 24
    },
    9: {
        'dust': 929,
        'gold': 152000,
        'diamond': 68,
        'blue': 26
    },
    10: {
        'dust': 1049,
        'gold': 152000,
        'diamond': 89,
        'blue': 28
    }
}
bounty_double = {
    8: {
        'dust': 1875,
        'gold': 31000,
        'diamond': 260,
        'blue': 39
    },
    9: {
        'dust': 2114,
        'gold': 31000,
        'diamond': 324,
        'blue': 43
    },
    10: {
        'dust': 2354,
        'gold': 31000,
        'diamond': 391,
        'blue': 47
    }
}
bounty_team = {
        'dust': 160 * 0.3275 + 500 * 0.03 + 800 * 0.0075,
        'gold': 252000 * 0.35 + 366000 * 0.03,
        'diamond': 120 * 0.3275 + 200 * 0.03 + 300 * 0.0075,
        'blue': 30 * 0.1250
}
bounty_team = pd.Series(bounty_team) * (sub['team_bounty'] + vip[VIP]['team_bounty'])
bounty = (pd.DataFrame.from_dict(bounty_normal) * 16 + pd.DataFrame.from_dict(bounty_double) * 8) / 24
bounty_daily = daily_addition(bounty[vip[VIP]['bounty']], bounty_team)
print(bounty_daily)


cursed = {
    '10%': {
        'twisted': 650,
        'shard': 400,
        'core': 160,
        'stargazer': 3
    },
    '8%': {
        'twisted': 680,
        'shard': 400,
        'core': 170,
        'stargazer': 4
    },
    '6%': {
        'twisted': 710,
        'shard': 400,
        'core': 180,
        'stargazer': 5
    },
    '5%': {
        'twisted': 740,
        'shard': 400,
        'core': 200,
        'stargazer': 6
    },
    '4%': {
        'twisted': 770,
        'shard': 400,
        'core': 220,
        'stargazer': 7
    },
    '3%': {
        'twisted': 800,
        'shard': 400,
        'core': 240,
        'stargazer': 8
    },
    '2%': {
        'twisted': 850,
        'shard': 400,
        'core': 260,
        'stargazer': 9
    },
    '1%': {
        'twisted': 1000,
        'shard': 400,
        'core': 300,
        'stargazer': 10
    },
    '200': {
        'twisted': 1000,
        'shard': 400,
        'core': 300,
        'stargazer': 10
    },
    '50': {
        'twisted': 1000,
        'shard': 400,
        'core': 300,
        'stargazer': 10
    },
    '0': {
        'twisted': 0,
        'shard': 0,
        'core': 0,
        'stargazer': 0
    },
}
cursed = pd.DataFrame.from_dict(cursed)
cursed_daily = cursed[CURSED_RANK].drop('stargazer') / 7

daily_total = daily_batch(idle_daily, [
    quests_daily, fast_daily, guild_daily, daily_inn, twisted_daily, daily_cards, store_daily,
    daily_regal_6, daily_coe_6, daily_tb_6, misty_daily, maze_daily, cursed_daily, bounty_daily
])
daily_total = daily_hours(daily_total).drop('arena')
daily_total['diamond'] += (FABLED + FAST_COST)
daily_total['glad_coin'] += challenger

print('------------Daily------------')
print(daily_total)
print('----------------------------')
print('Est. Value: ', '{:,.0f}'.format(np.sum(daily_total * value)), 'Total')

print('\n-----Fast Rewards(FR)-----')
print(fast_rewards)
print('----------------------------')
print('Est. Value: ', '{:,.0f}'.format(np.sum(fast_rewards * value)), 'Per |',
      '{:,.0f}'.format(np.sum(fast_rewards * value) * FAST), 'Total |',
      '{:,.0f}'.format(np.sum(fast_rewards * value) * FAST + FAST_COST), 'Adjusted')

print('\n--------Predictions--------')
print('Elite            : ', '{:,.1f}'.format(60 / daily_total['purple']), 'Days')
print('Crystal Slot     : ', '{:,.0f}'.format(5000 / daily_total['invigor']), 'Days')
print('Level (Dura Tree): ', '{:,.1f}'.format(800 / daily_total['twisted']), 'Days')
print('\n------Signature Items------')
print('+10: ', '{:,.0f}'.format(220 / daily_total['silver_e']), 'Days')
print('+20: ', '{:,.0f}'.format(240 / daily_total['gold_e']), 'Days')
print('+30: ', '{:,.0f}'.format(300 / daily_total['red_e']), 'Days')
print('\n--------Engravings--------')
print('e30: ', '{:,.0f}'.format(3750 / daily_total['shard']), 'Days')
print('e41: ', '{:,.0f}'.format(1650 / daily_total['core']), 'Days')
print('e44: ', '{:,.0f}'.format(2100 / daily_total['core']), 'Days')
print('e60: ', '{:,.0f}'.format(4500 / daily_total['core']), 'Days')
print('\n--------Challenger--------')
print('LdV (4x)    : ', '{:,.0f}'.format(4 * 250000 / daily_total['glad_coin']), 'Days')
print('Merlin (4x) : ', '{:,.0f}'.format(4 * 250000 / daily_total['glad_coin']), 'Days')
print('God         : ', '{:,.0f}'.format(250000 / daily_total['glad_coin']), 'Days')
print('Flora       : ', '{:,.0f}'.format(150000 / daily_total['glad_coin']), 'Days')
print('Red Emb (25): ', '{:,.0f}'.format(165000 / daily_total['glad_coin']), 'Days')
print('\n-------Guild Store-------')
print('T1    : ', '{:,.1f}'.format(33879 / daily_total['guild_coin']), 'Days')
print('T2    : ', '{:,.0f}'.format(40875 / daily_total['guild_coin']), 'Days')
print('T3    : ', '{:,.0f}'.format(46900 / daily_total['guild_coin']), 'Days')
print('Mythic: ', '{:,.0f}'.format(59000 / daily_total['guild_coin']), 'Days')
print('\n-------Lab Store-------')
print('Arthur (4x)    : ', '{:,.0f}'.format(60000 * 4 / daily_total['maze_coin']), 'Days')
print('Wu Kong        : ', '{:,.0f}'.format(45000 / daily_total['maze_coin']), 'Days | ',
      '{:,.0f}'.format(10 * 45000 / daily_total['maze_coin']), 'Days (M) |',
      '{:,.0f}'.format(14 * 45000 / daily_total['maze_coin']), 'Days (A)')
print('Dim Emb (50)   : ', '{:,.0f}'.format(64000 / daily_total['maze_coin']), 'Days')
print('Twisted (400)  : ', '{:,.0f}'.format(40000 / daily_total['maze_coin']), 'Days')
print('Red Emb (25)   : ', '{:,.0f}'.format(37125 / daily_total['maze_coin']), 'Days')
print('-------------------------')


