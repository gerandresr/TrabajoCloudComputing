# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:05:43 2025

@author: grios5
"""

# from xbbg import blp
from datetime import date
import os
import conexion_a_db as db  # pip install conexion-a-db
from blp import blp
import pandas as pd
bquery = blp.BlpQuery().start()


# Crear o conectar a una base de datos
nombre_usuario = os.getlogin().lower()
if nombre_usuario == 'grios5':
    RAW = "//SRV_RECURSOS/Mesa_Dinero/Carpeta propietaria/PaginaWeb/BaseDatos/"
elif nombre_usuario in ['mparada6', 'rmacho']:
    RAW = "I:/Carpeta propietaria/PaginaWeb/BaseDatos/"

os.chdir(RAW)

folder_base = RAW+'DataBases/'

nombre_base = 'db_data_bbg.db'
# nombre_base = 'db_data_bbg_javier.db'
desde_sin_data = date(2021, 1, 1)  # en caso de que la tabla esta vacia 

# 

# ticket : field
dic_prox_tpm = {'CHOVCHOV Index': 'Chile',
               'mxonbr Index': 'Mexico',
               'BZSTSETA Index': 'Brasil',
               'FDTR Index': 'Usa',
               'EURR002W Index': 'Eurozona',
               'bojdtr Index': 'Japon',
               'chlrlpr5 Index': 'China',
               'CABROVER Index': 'Canada',
               'RBATCTR Index': 'Australia',
        }

dic_tpm = {'CHOVCHOV Index': 'Chile',
           'mxonbr Index': 'Mexico',
           'BZSTSETA Index': 'Brasil',
           'FDTR Index': 'Usa',
           'EURR002W Index': 'Eurozona',
           'bojdtr Index': 'Japon',
           'chlrlpr5 Index': 'China',
           'CABROVER Index': 'Canada',
           'RBATCTR Index': 'Australia',
    }

dic_desempleo = {'CHUETOTL Index': 'Chile',
            'MXUERATE Index': 'Mexico',
            'EHUPBR Index': 'Brasil',
            'EHUPUS Index': 'Usa',
            'UMRTEMU Index': 'Eurozona',
            'EHUPJP Index': 'Japon',
            'EHUPCN Index': 'China',
            'GRUEPR Index': 'Alemania',
            'CANLXEMR Index': 'Canada',
            'AULFUNEM Index': 'Australia',
        }

dic_clpcam = {
         'CHSWPA ICCH Curncy': '1m',  # nominal
         'CHSWPB ICCH Curncy': '2m',
         'CHSWPC ICCH Curncy': '3m',
         'CHSWPF ICCH Curncy': '6m',
         'CHSWPI ICCH Curncy': '9m',
         'CHSWP1 ICCH Curncy': '1y',
         'CHSWP1F ICCH Curncy': '1.5y',
         'CHSWP2 ICCH Curncy': '2y',
         'CHSWP3 ICCH Curncy': '3y',
         'CHSWP4 ICCH Curncy': '4y',
         'CHSWP5 ICCH Curncy': '5y',
         'CHSWP6 ICCH Curncy': '6y',
         'CHSWP7 ICCH Curncy': '7y',
         'CHSWP8 ICCH Curncy': '8y',
         'CHSWP9 ICCH Curncy': '9y',
         'CHSWP10 ICCH Curncy': '10y',
         'CHSWP12 ICCH Curncy': '12y',
         'CHSWP15 ICCH Curncy': '15y',
         'CHSWP20 ICCH Curncy': '20y',
         'CHSWP25 ICCH Curncy': '25y',
         'CHSWP30 ICCH Curncy': '30y'
         }

dic_crecimiento = {'CLIMYOYN Index': 'Chile',
                   'MXAGDPCH Index': 'Mexico',
                   'BZGDGDP4 Index': 'Brasil',
                   'EHGDUSY Index': 'Usa',
                   'EUGNEMUQ Index': 'Eurozona',
                   'JGDPQGDP Index': 'Japon',
                   'CNGDPYOY Index': 'China',
                   'GRGDPPGQ Index': 'Alemania',
                   'CAGDPYOY Index': 'Canada',
            }

dic_ipc = {'CLINNSMO Index': 'Chile',
           'MXCPCHNG Index': 'Mexico',
           'BZPIIPCM Index': 'Brasil',
           'CPI CHNG Index': 'Usa',
           'ECCPEMUM Index': 'Eurozona',
           'GRCP20MM Index': 'Alemania',
           'JNCPIMOM Index': 'Japon',
           'CNCPIMOM Index': 'China',
           'CACPICHG Index': 'Canada',
    }

dic_infla = {'CLINNSYO Index': 'Chile',
             'MXCPYOY Index': 'Mexico',
             'BZPIIPCY Index': 'Brasil',
             'CPI YOY Index': 'Usa',
             'ECCPEMUY Index': 'Eurozona',
             'GRCP20YY Index': 'Alemania',
             'JNCPIYOY Index': 'Japon',
             'CNCPIYOY Index': 'China',
             "CACPIYOY Index": "Canada",
             'ACPMYOY Index': 'Australia',
    }


dic_sofr = {
'USOSFRF BGN Curncy' : '6m',
'USOSFR1 BGN Curncy' : '1y',
'USOSFR1F BGN Curncy' : '18m',
'USOSFR2 BGN Curncy' : '2y',
'USOSFR3 BGN Curncy' : '3y',
'USOSFR5 BGN Curncy' : '4y',
'USOSFR6 BGN Curncy' : '5y',
'USOSFR7 BGN Curncy' : '6y',
'USOSFR8 BGN Curncy' : '7y',
'USOSFR9 BGN Curncy' : '8y',
'USOSFR10 BGN Curncy' : '9y',
'USOSFR12 BGN Curncy' : '10y',
'USOSFR15 BGN Curncy' : '12y',
'USOSFR20 BGN Curncy' : '15y',
'USOSFR25 BGN Curncy' : '20y',
'USOSFR30 BGN Curncy' : '25y',

}


dic_ccy = {
    'CLP Curncy': 'CLP',
    'BRL Curncy': 'BRL',
    'MXN Curncy': 'MXN',
    'COP Curncy': 'COP',
    'EUR Curncy': 'EUR',
    'GBP Curncy': 'GBP',
    'AUD Curncy': 'AUD',    
    'NZD Curncy': 'NZD',
    'CAD Curncy': 'CAD',
    'CHY Curncy': 'CHY',
    'JPY Curncy': 'JPY',
    'ZAR Curncy': 'ZAR',
    'TRY Curncy': 'TRY',   
    'DXY Curncy': 'DXY',
    }

dic_cds = {
       'CHILE CDS USD SR 5Y D14 Corp': 'Chile',
       'PERU CDS USD SR 5Y D14 Corp': 'Peru',
       'COLOM CDS USD SR 5Y D14 Corp': 'Colombia',
       'BRAZIL CDS USD SR 5Y D14 Corp': 'Brasil',
       'MEX CDS USD SR 5Y  Corp': 'Mexico',
       'AUSTLA CDS USD SR 5Y D14 Corp': "Australia",
      }

dic_acciones = {
    'IPSA Index': 'Chile IPSA',
    'IGPA Index': 'Chile IGPA',
    'IBOV Index': 'Brasil Ibovespa',
    'MEXBOL Index': 'Mexico Mexbol',
    'COLCAP Index': 'Colombia Colcap',
    'SPX Index': 'Usa S&P',
    'INDU Index': 'Usa DowJones',
    'VIX Index': 'Usa Vix',
    'SX5E Index': 'Eurozona EuroStoxx',
    'NKY Index': 'Japon Nikkei',
    'SHSZ300 Index': 'China Shanghai',   
    'DAX Index': 'Alemania DAX',
    'SPTSX Index': 'Canada S&P',
    'AS51 Index': 'Australia S&P',
    
    }

dic_comm = {
    'GCA Comdty': 'Oro',
    'CLA Comdty': 'WTI',
    'COA Comdty': 'Brent',
    'XBA Comdty': 'Gasolina',
    'NGA Comdty': 'Gas Natural',
    'W A Comdty': 'Trigo',
    'HGA Comdty': 'Cobre',
     }

dic_presidentes = {'45793Z CI Equity': 'Chile',
                   '1323Z BZ Equity': 'Brasil',
                   '3352Z US Equity': 'Usa',
                   '1426Z MM Equity': 'Mexico',
                   'PRCH CH Equity': 'China',
                   '1319293D JP Equity': 'Japon',
                   '3413Z GR Equity': 'Alemania',
                   '80710Z CN Equity': 'Canada',
                   "1525Z AU Equity": "Australia",
    }


# DESCARGO DATA DE BBG

#%% Presidentes de cada pais
# este siempre correra, los demas dependen si encuentra datos o no
presidentes = pd.DataFrame(columns=['Pais', 'Nombre'])
for i in dic_presidentes.keys():
    presidente = bquery.bds(i, "COMPANY_EXEC_OFFICERS")
    presidentes.loc[len(presidentes)] = [dic_presidentes[i], presidente.iloc[0,0]]

db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'presidentes')  # elimino tabla
db.Subir_DF(presidentes, folder_base+nombre_base, 'presidentes')  # cargo nueva

# db.Tablas_en_base(nombre_db=RAW+nombre_base)  # cargo nueva

#%% Proximos datos de tpm
# este siempre correra, los demas dependen si encuentra datos o no
prox_tpm = bquery.bdp(
    list(dic_prox_tpm.keys()),
    ["ECO_RELEASE_DT"],
)
prox_tpm = prox_tpm.rename(columns={'security': 'Pais', 'ECO_RELEASE_DT': 'Fecha'})
prox_tpm['Pais'] = prox_tpm['Pais'].replace(dic_prox_tpm)

db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'proximas_tpm')  # elimino tabla
db.Subir_DF(prox_tpm, folder_base+nombre_base, 'proximas_tpm')  # cargo nueva

#%% desempleo
# este siempre correra, los demas dependen si encuentra datos o no
desempleo = bquery.bdp(
    list(dic_desempleo.keys()),
    ["PX_LAST"],
)
desempleo = desempleo.rename(columns={'security': 'Pais', 'PX_LAST': 'Valor'})
desempleo['Pais'] = desempleo['Pais'].replace(dic_desempleo)

db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'desempleo')  # elimino tabla
db.Subir_DF(desempleo, folder_base+nombre_base, 'desempleo')  # cargo nueva

#%% crecimiento
# este siempre correra, los demas dependen si encuentra datos o no
crecimiento = bquery.bdp(
    list(dic_crecimiento.keys()),
    ["PX_LAST"],
)

crecimiento = crecimiento.rename(columns={'security': 'Pais', 'PX_LAST': 'Valor'})
crecimiento['Pais'] = crecimiento['Pais'].replace(dic_crecimiento)

db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'crecimiento')  # elimino tabla
db.Subir_DF(crecimiento, folder_base+nombre_base, 'crecimiento')  # cargo nueva


#%% inflacion yoy
#** Necesita FOR porque no todos los datos salen al mismo tiempo
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'inflacion')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_inflacion = db.Descargar_DF(folder_base+nombre_base, 'inflacion')
    des_inflacion['Fecha'] = des_inflacion['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
except:
    desde_inflacion = desde_sin_data


for i in list(dic_infla.keys()):
    try:
        dinf = des_inflacion.loc[des_inflacion.Pais==dic_infla[i]]
        desde_inflacion = max(dinf.Fecha)
    except:
        desde_inflacion = desde_sin_data

    # descargo de bbg y subo
    inflacion = bquery.bdh(
        [i],
        ['PX_LAST'],
        start_date=desde_inflacion.strftime("%Y%m%d"),
        end_date=date.today().strftime("%Y%m%d"),
    )

    inflacion = inflacion.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
    inflacion = inflacion.loc[inflacion.Fecha!=desde_inflacion]  # elimino la primera fecha porque ya esta cargada
    inflacion['Pais'] = inflacion['Pais'].replace(dic_infla)
    
    if len(inflacion) > 0:
        db.Subir_DF(inflacion, folder_base+nombre_base, 'inflacion')  # subo a la base

#%% IPC
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'ipc')  # elimino tabla
#** Necesita FOR porque no todos los datos salen al mismo tiempo
# obtengo la ultima fecha cargada
try:
    des_ipc = db.Descargar_DF(folder_base+nombre_base, 'ipc')
    des_ipc['Fecha'] = des_ipc['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
except:
    desde_ipc = desde_sin_data

for i in list(dic_ipc.keys()):
    try:
        dipc = des_ipc.loc[des_ipc.Pais==dic_infla[i]]
        desde_ipc = max(dipc.Fecha)
    except:
        desde_ipc = desde_sin_data
        
    # descargo de bbg y subo
    ipc = bquery.bdh(
        [i],
        ['PX_LAST'],
        start_date=desde_ipc.strftime("%Y%m%d"),
        end_date=date.today().strftime("%Y%m%d"),
    )

    ipc = ipc.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
    ipc = ipc.loc[ipc.Fecha!=desde_ipc]  # elimino la primera fecha porque ya esta cargada
    ipc['Pais'] = ipc['Pais'].replace(dic_ipc)
    
    if len(ipc) > 0:
        db.Subir_DF(ipc, folder_base+nombre_base, 'ipc')  # subo a la base

#%% Tasas de Politicas monetarias
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'tpm')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_tpm = db.Descargar_DF(folder_base+nombre_base, 'tpm')
    des_tpm['Fecha'] = des_tpm['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    desde_tpm = max(des_tpm['Fecha'])
except:
    desde_tpm = desde_sin_data
    
# descargo de bbg y subo
tpm = bquery.bdh(
    list(dic_tpm.keys()),
    ['PX_LAST'],
    start_date=desde_tpm.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

tpm = tpm.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
tpm = tpm.loc[tpm.Fecha!=desde_tpm]  # elimino la primera fecha porque ya esta cargada
tpm['Pais'] = tpm['Pais'].replace(dic_tpm)

if len(tpm) > 0:
    db.Subir_DF(tpm, folder_base+nombre_base, 'tpm')  # subo a la base

#%% Commodities
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'commodities')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_comm = db.Descargar_DF(folder_base+nombre_base, 'commodities')
    des_comm['Fecha'] = des_comm['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    desde_comm = max(des_comm['Fecha'])
except:
    desde_comm = desde_sin_data

# descargo de bbg y subo
comm = bquery.bdh(
    list(dic_comm.keys()),
    ['PX_LAST'],
    start_date=desde_comm.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

comm = comm.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
comm = comm.loc[comm.Fecha!=desde_comm]  # elimino la primera fecha porque ya esta cargada
comm['Pais'] = comm['Pais'].replace(dic_comm)

if len(comm) > 0:
    db.Subir_DF(comm, folder_base+nombre_base, 'commodities')  # subo a la base

#%% MONEDAS
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'monedas')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_ccy = db.Descargar_DF(folder_base+nombre_base, 'monedas')
    # clp = des_ccy.loc[des_ccy.Pais=='CLP']
    des_ccy['Fecha'] = des_ccy['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    desde_ccy = max(des_ccy['Fecha'])
except:
    desde_ccy = desde_sin_data

# descargo de bbg y subo
ccy = bquery.bdh(
    list(dic_ccy.keys()),
    ['PX_LAST'],
    start_date=desde_ccy.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

ccy = ccy.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
ccy = ccy.loc[ccy.Fecha!=desde_ccy]  # elimino la primera fecha porque ya esta cargada
ccy['Pais'] = ccy['Pais'].replace(dic_ccy)

if len(ccy) > 0:
    db.Subir_DF(ccy, folder_base+nombre_base, 'monedas')  # subo a la base

#%% EQUITY
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'equity')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_equity = db.Descargar_DF(folder_base+nombre_base, 'equity')
    des_equity['Fecha'] = des_equity['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    desde_equity = max(des_equity['Fecha'])
except:
    desde_equity = desde_sin_data
    
# descargo de bbg y subo
equity = bquery.bdh(
    list(dic_acciones.keys()),
    ['PX_LAST'],
    start_date=desde_equity.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

equity = equity.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
equity = equity.loc[equity.Fecha!=desde_equity]  # elimino la primera fecha porque ya esta cargada
equity['Pais'] = equity['Pais'].replace(dic_acciones)

if len(equity) > 0:
    db.Subir_DF(equity, folder_base+nombre_base, 'equity')  # subo a la base

#%% CDS
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'cds')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_cds = db.Descargar_DF(folder_base+nombre_base, 'cds')
    des_cds['Fecha'] = des_cds['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    des_cds = max(des_cds['Fecha'])
except:
    des_cds = desde_sin_data
    
# descargo de bbg y subo
cds = bquery.bdh(
    list(dic_cds.keys()),
    ['PX_LAST'],
    start_date=des_cds.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

cds = cds.rename(columns={'date': 'Fecha', 'security': 'Pais', 'PX_LAST': 'Valor'})
cds = cds.loc[cds.Fecha!=des_cds]  # elimino la primera fecha porque ya esta cargada
cds['Pais'] = cds['Pais'].replace(dic_cds)

if len(cds) > 0:
    db.Subir_DF(cds, folder_base+nombre_base, 'cds')  # subo a la base

#%% CLPCAM
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'clpcam')  # elimino tabla

# obtengo la ultima fecha cargada
try:
    des_clpcam = db.Descargar_DF(folder_base+nombre_base, 'clpcam')
    des_clpcam['Fecha'] = des_clpcam['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    des_clpcam = max(des_clpcam['Fecha'])
except:
    des_clpcam = desde_sin_data
    
# descargo de bbg y subo
clpcam = bquery.bdh(
    list(dic_clpcam.keys()),
    ['PX_LAST'],
    start_date=des_clpcam.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

clpcam = clpcam.rename(columns={'date': 'Fecha', 'security': 'Tenor', 'PX_LAST': 'Valor'})
clpcam = clpcam.loc[clpcam.Fecha!=des_clpcam]  # elimino la primera fecha porque ya esta cargada
clpcam['Tenor'] = clpcam['Tenor'].replace(dic_clpcam)

if len(clpcam) > 0:
    db.Subir_DF(clpcam, folder_base+nombre_base, 'clpcam')  # subo a la base

#%% sofr
# db.Eliminar_Tabla_de_DB(folder_base+nombre_base, 'sofr')  # elimino tabla
try:
    des_sofr = db.Descargar_DF(folder_base+nombre_base, 'sofr')
    des_sofr['Fecha'] = des_sofr['Fecha'].apply(lambda x: date(int(x[0:4]), int(x[5:7]), int(x[8:10])))
    des_sofr = max(des_sofr['Fecha'])
except:
    des_sofr = desde_sin_data
    
# descargo de bbg y subo
sofr = bquery.bdh(
    list(dic_sofr.keys()),
    ['PX_LAST'],
    start_date=des_sofr.strftime("%Y%m%d"),
    end_date=date.today().strftime("%Y%m%d"),
)

sofr = sofr.rename(columns={'date': 'Fecha', 'security': 'Tenor', 'PX_LAST': 'Valor'})
sofr = sofr.loc[sofr.Fecha!=des_sofr]  # elimino la primera fecha porque ya esta cargada
sofr['Tenor'] = sofr['Tenor'].replace(dic_sofr)

if len(sofr) > 0:
    db.Subir_DF(sofr, folder_base+nombre_base, 'sofr')  # subo a la base


