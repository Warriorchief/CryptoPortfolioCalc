"""Crypto Holdings (h)"""

import urllib.request, urllib.response, json

h=[['Aeon', 'AEON', '193.06'],
['Aiden', 'ADN', '12,967'],
['AntShares', 'ANS', '136.02'],
['Ardor', 'ARDR', '1,945'],
['Ark', 'ARK', '427.5'],
['ArtByte', 'ABY', '106,864'],
['AsiaDigiCoin', 'ADCN', '761'],
['Augur', 'REP', '19'],
['AuroraCoin', 'AUR', '103.2'],
['Bantam', 'BNT', '41,895'],
['Belacoin', 'BELA', '6,000'],
['BitCrystals', 'BCY', '721.3'],
['BitShares', 'BTS', '3,325'],
['Bitbay', 'BAY', '12,871'],
['Bitcoin', 'BTC', '1.3124'],
['BitcoinPlus', 'XBC', '5.00'],
['Bitcoindark', 'BTCD', '4.146'],
['Bitmark', 'BTM', '208'],
['Bitsend', 'BSD', '374.06'],
['Bitstar', 'BITS', '751.88'],
['Blackcoin', 'BLK', '2,316'],
['Boolberry', 'BBR', '1,201'],
['BoostCoin', 'BOST', '422.3'],
['Burst', 'BURST', '33,173'],
['Bytecoin', 'BCN', '1,007,453'],
['CannabisCoin', 'CANN', '8,750'],
['Capricoin', 'CPC', '105.88'],
['Centurion', 'CNT', '868'],
['ChronobankTime', 'TIME', '3.325'],
['Clams', 'CLAM', '9.13'],
['CloakCoin', 'CLOAK', '54.58'],
['ClubCoin', 'CLUB', '176.51'],
['Coin2.1', 'C2', '46,038'],
['CounterParty', 'XCP', '8.33'],
['Crown', 'CRW', '99.75'],
['CryptoCarbon', 'CCRB', '72.7'],
['Cryptonite', 'XCN', '16,625'],
['CureCoin', 'CURE', '266.7'],
['DNotes', 'NOTE', '2,114.42'],
['DT-Token', 'DRACO', '23,454'],
['Dash', 'DASH', '6.0'],
['Decred', 'DCR', '3.91'],
['DeusCoin', 'DEUS', '125.7'],
['Diem', 'DIEM', '1,496,250'],
['Digibyte', 'DGB', '20,781'],
['DigitalCoin', 'DGC', '484'],
['DigitalNote', 'XDN', '66,500'],
['DigixDao', 'DGD', '1.44'],
['Dogecoin', 'DOGE', '218,605'],
['DubaiCoin', 'DBIC', '150.3'],
['Einsteinium', 'EMC2', '41,563'],
['Emercoin', 'EMC', '436'],
['Ethereum', 'ETH', '6.15'],
['EthereumClassic', 'ETC', '25.26'],
['Expanse', 'EXP', '22.35'],
['Factom', 'FCT', '23'],
['FairCoin', 'FAIR', '898'],
['Feathercoin', 'FTC', '518.25'],
['Florincoin', 'FLO', '4,819'],
['Fluttercoin', 'FLT', '139,650'],
['FoldingCoin', 'FLDC', '19,183'],
['Fuel2Coin', 'FC2', '1,231.5'],
['Gambit', 'GAM', '66.3'],
['GameCredits', 'GAME', '196.6'],
['GeoCoin', 'GEO', '449.3'],
['GlobalReserveCoin', 'GCR', '1,279'],
['GoldCoin', 'GLD', '765.3'],
['Golem', 'GNT', '3,470'],
['Golos', 'GOLOS', '1767.36'],
['Gridcoin', 'GRC', '11,212'],
['GroestlCoin', 'GRS', '7,312'],
['Gulden', 'NLG', '3,476'],
['HackGold', 'HKG', '427.5'],
['Heat', 'HEAT', '369.26'],
['HiCoin', 'XHI', '5,714'],
['Horizon', 'HZ', '124,688'],
['Huntercoin', 'HUC', '3,325'],
['Agoras', 'AGRS', '133'],
['InternetofPeople', 'IOP', '5.74'],
['Iocoin', 'IOC', '159.9'],
['JIOToken', 'JIO', '7,904'],
['Komodo', 'KMD', '166.25'],
['LBRY-Credits', 'LBC', '1,514'],
['LIQUID', 'LQD', '24.17'],
['LePen', 'LEPEN', '76,923'],
['Lisk', 'LSK', '49.67'],
['Litecoin', 'LTC', '12.54'],
['Lomocoin', 'LMC', '2493.75'],
['Magi', 'XMG', '2,000'],
['MaidSafeCoin', 'MAID', '479.66'],
['MaxCoin', 'MAX', '674'],
['Megacoin', 'MEC', '347.7'],
['Melon', 'MLN', '.855'],
['MemoryCoin', 'MMC', '5,700'],
['MonaCoin', 'MONA', '189'],
['Monero', 'XMR', '14.51'],
['MonetaryUnit', 'MUE', '997.5'],
['Myriadcoin', 'MYR', '349,125'],
['NXT', 'NXT', '1,960'],
['NameCoin', 'NMC', '159.6'],
['NautilusCoin', 'NAUT', '524'],
['Navajo', 'NAV', '1,343'],
['Neoscoin', 'NEOS', '164.75'],
['NewEconomyMovement', 'XEM', '15,036'],
['Nexium', 'NXC', '437.5', '24.56'],
['Nexus', 'NXS', '99.75'],
['NobleCoin', 'NOBL', '114,000'],
['Novacoin', 'NVC', '16.74'],
['NuShares', 'NSR', '19,950'],
['Nubits', 'NBT', '50.09'],
['Okcash', 'OK', '8,312.5'],
['Omni', 'OMNI', '12.1'],
['OroCoin', 'ORO', '26,534'],
['PascalCoin', 'PASCAL', '199.5'],
['Pebblecoin', 'XPB', '498.75'],
['Peercoin', 'PPC', '177'],
['Pesobit', 'PSB', '2,222'],
['Piggycoin', 'PIGGY', '200,000'],
['Pinkcoin', 'PINK', '49,875'],
['Pivx', 'PIVX', '42.75'],
['PoSW', 'POSW', '1137'],
['Potcoin', 'POT', '20,002'],
['PresidentSanders', 'BURN', '11,648'],
['PrimeChain', 'PRIME', '1,350'],
['Primecoin', 'XPM', '282'],
['PureVidz', 'VIDZ', '13,315'],
['Qibuck', 'QBK', '90.68'],
['Qora', 'QORA', '623,438'],
['Quatloo', 'QTL', '2,667'],
['Qwark', 'QWARK', '188.9'],
['Radium', 'RADS', '24.38'],
['Reddcoin', 'RDD', '465,000'],
['Riecoin', 'RIC', '867.4'],
['Ripple', 'XRP', '4,565'],
['Rubycoin', 'RBY', '118.47'],
['Safeexchange', 'SEC', '28,500'],
['8Bit', '8BIT', '457.25'],
['Salus', 'SLS', '33.25'],
['Scotcoin', 'SCOT', '5,158'],
['Shadowcash', 'SDC', '36.44'],
['Shift', 'SHIFT', '688.2'],
['SiaCoin', 'SC', '665,000'],
['SiberianChervonets', 'SIB', '213.75'],
['SingularDTV', 'SNGLS', '598.5'],
['SoarCoin', 'SOAR', '2,692.6'],
['SolarCoin', 'SLR', '105.03'],
['SongCoin', 'SONG', '58,698'],
['Spreadcoin', 'SPR', '199.5'],
['Startcoin', 'START', '650.8'],
['Stealthcoin', 'XST', '9,980'],
['Steem', 'STEEM', '18.52'],
['SteemDollars', 'SBD', '56.1'],
['StellarLumens', 'XLM', '6,045'],
['StorjCoinX', 'SJCX', '219.5'],
['Stratis', 'STRAT', '997.5'],
['Stress', 'STS', '50,000'],
['SuperNET', 'UNITY', '18.15'],
['Swarm', 'SWARM', '13,300'],
['Sync', 'SYNC', '.73'],
['Synereo', 'AMP', '113.8'],
['SysCoin', 'SYS', '1956'],
['Terra', 'TERRA', '14,627'],
['TeslaCoilCoin', 'TESLA', '15.3'],
['Ubiq', 'UBQ', '991.43'],
['Unobtanium', 'UNO', '2.28'],
['UtaCoin', 'UTA', '156.8'],
['Vcash', 'XVC', '410.7'],
['Vericoin', 'VRC', '255.1'],
['Vertcoin', 'VTC', '261.9'],
['Viacoin', 'VIA', '8,008.8'],
['Voxels', 'VOX', '165.46'],
['Waves', 'WAVES', '85.5'],
['WildBeastBlock', 'WBB', '26.27'],
['WoodCoin', 'LOG', '525.3'],
['WorldGoldCoin', 'WGC', '1,000,000'],
['Worldcoin', 'WDC', '1,247'],
['XCurrency', 'XC', '119.5'],
['Xaurum', 'XAUR', '299.25'],
['YoGold', 'YOG', '28.5'],
['Yocoin', 'YOC', '3,507'],
['ZCash', 'ZEC', '6.315'],
['ZCoin', 'XZC', '6.65'],
['ZClassic', 'ZCL', '10.71']]

h.sort(key=lambda x: x[0])

def calc_portfolio_value():    
    success=0
    fail=0
    total=0
    for c in h:
        req="https://api.cryptonator.com/api/ticker/"+c[1]+"-"+"usd"
        with urllib.request.urlopen(req) as url:
            data = json.loads(url.read().decode())
            if len(data['error'])==0:
                success+=1
                print(data['ticker'])
                p=data['ticker']['price']
                c.append(p)
                worth=float(p)*float(c[2].replace(',',''))
                c.append(worth)
                total+=worth
            else:
                fail+=1
                print('could not get data for',c[1])
                c.append('NO_DATA')
                c.append('NO_DATA')
    return (h,success,fail,total)

table=calc_portfolio_value()
    
def print_table():
    print('found data for',table[1],'coins and did NOT find data for',table[2],'coins, for total value of $',float(str(table[3])[:10]))
    for c in table[0]:
        if c[3]!='NO_DATA':
            print(c[0],c[1].rjust(25-len(c[0])),'    ',float(c[2][:5].replace(',','')),'    ',"%.5f" % float(str(c[3])[:7]),'    ',float(str(c[4])[:7]))
        else:
            print(c[0],c[1].rjust(25-len(c[0])),'    ',float(c[2][:5].replace(',','')),'    ','NO_DATA','    ','NO_DATA')
    prices=[i[2] for i in table[0]]
    worths=[i[3] for i in table[0]]
    return (prices,worths)
     
out=print_table()


