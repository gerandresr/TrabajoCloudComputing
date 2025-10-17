# ------------------------------------- DATA GETTERS ------------------------------------------------
def add_technical_indicators(var:str, df):
    import pandas as pd
    # Create all technical indicators at once for better performance
    ma_30 = df[var].rolling(window=30).mean()
    ma_360 = df[var].rolling(window=360).mean()
    std_30 = df[var].rolling(window=30).std()
    std_360 = df[var].rolling(window=360).std()
    high_30 = df[var].rolling(window=30).max()
    high_360 = df[var].rolling(window=360).max()
    low_30 = df[var].rolling(window=30).min()
    low_360 = df[var].rolling(window=360).min()
    range_30 = high_30 - low_30
    range_360 = high_360 - low_360
    zscore = (df[var] - ma_30) / std_30
    delta = df[var].diff()
    
    # Create new dataframe with all indicators
    new_cols = pd.DataFrame({
        f'{var}_MA_30': ma_30,
        f'{var}_MA_360': ma_360,
        f'{var}_STD_30': std_30,
        f'{var}_STD_360': std_360,
        f'{var}_HIGH_30': high_30,
        f'{var}_HIGH_360': high_360,
        f'{var}_LOW_30': low_30,
        f'{var}_LOW_360': low_360,
        f'{var}_Range_30': range_30,
        f'{var}_Range_360': range_360,
        f'{var}_ZScore': zscore,
        f'{var}_Delta': delta
    })

    # Concatenate with df_master
    df = pd.concat([df, new_cols], axis=1)
    return df

def add_tpm_category(df_macro):
    ranges_tpm_cl = [df_macro["tpm_cl"].min() + (i) * (df_macro["tpm_cl"].max() - df_macro["tpm_cl"].min()) / 3 for i in range(4)]
    ranges_tpm_us = [df_macro["tpm_us"].min() + (i) * (df_macro["tpm_us"].max() - df_macro["tpm_us"].min()) / 3 for i in range(4)]
    
    def category_tpm(tpm,ranges):
        if tpm <= ranges[1]:
            return 0 # Baja
        elif tpm <= ranges[2]:
            return 1 # Media
        else:
            return 2 # Alta
        #Agregamos columnas binarias de is in category
    df_macro["tpm_cl_cat"] = df_macro["tpm_cl"].apply(lambda x: category_tpm(x, ranges_tpm_cl))
    df_macro["tpm_us_cat"] = df_macro["tpm_us"].apply(lambda x: category_tpm(x, ranges_tpm_us))
    for cat in range(3):
        df_macro[f'tpm_cl_is_{cat}'] = (df_macro["tpm_cl_cat"] == cat).astype(int)
        df_macro[f'tpm_us_is_{cat}'] = (df_macro["tpm_us_cat"] == cat).astype(int)
    return df_macro

def add_tpm_changes(df_macro):
    df_macro["tpm_cl_change"] = df_macro["tpm_cl"].diff().fillna(0).apply(lambda x: 1 if x != 0 else 0)
    df_macro["tpm_us_change"] = df_macro["tpm_us"].diff().fillna(0).apply(lambda x: 1 if x != 0 else 0)
    return df_macro

def new_max(df_macro):
    df_macro["new_max_sp500"] = (df_macro["sp500"] == df_macro["sp500"].cummax()).astype(int)
    df_macro["new_max_ipsa"] = (df_macro["ipsa"] == df_macro["ipsa"].cummax()).astype(int)
    df_macro["new_max_usdclp"] = (df_macro["usdclp"] == df_macro["usdclp"].cummax()).astype(int)
    return df_macro

def diff_tasas(df_macro):
    df_macro["tpm_diff"] = df_macro["tpm_cl"] - df_macro["tpm_us"]
    df_macro["tpm_diff_pos"] = (df_macro["tpm_diff"] > 0).astype(int)
    return df_macro

def add_macro_indicators(df_macro):
    df_macro = add_tpm_category(df_macro)
    df_macro = add_tpm_changes(df_macro)
    df_macro = new_max(df_macro)
    df_macro = diff_tasas(df_macro)
    return df_macro

def get_technical_dataframe(ruta : str = "./db_data_bbg.db"): # type: ignore
    import pandas as pd
    import numpy as np
    import conexion_a_db as db

    lista_tablas = ["monedas","commodities","equity","cds", "sofr", "clpcam"]

    # Conseguir dataframes de la base de datos
    dfs = {tabla: db.Descargar_DF(ruta, tabla) for tabla in lista_tablas}

    df_clp = dfs["monedas"][dfs["monedas"]["Pais"] == "CLP"].copy()
    df_dxy = dfs["monedas"][dfs["monedas"]["Pais"] == "DXY"].copy()
    
    df_clpcam_5y = dfs["clpcam"][dfs["clpcam"]["Tenor"] == "5y"].copy()
    df_sofr_5y = dfs["sofr"][dfs["sofr"]["Tenor"] == "5y"].copy()

    df_wti = dfs["commodities"][dfs["commodities"]["Pais"] == "WTI"].copy()
    df_cobre = dfs["commodities"][dfs["commodities"]["Pais"] == "Cobre"].copy()

    df_cds_clp_5y = dfs["cds"][dfs["cds"]["Pais"] == "Chile"].copy()
    df_vix = dfs["equity"][dfs["equity"]["Pais"] == "Usa Vix"].copy()

    df_final = df_clp[["Fecha", "Valor"]].rename(columns={"Valor": "usdclp"})
    df_final = df_final.merge(df_dxy[["Fecha", "Valor"]].rename(columns={"Valor": "dxy"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_clpcam_5y[["Fecha", "Valor"]].rename(columns={"Valor": "spc_5y"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_sofr_5y[["Fecha", "Valor"]].rename(columns={"Valor": "sofr_5y"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_cobre[["Fecha", "Valor"]].rename(columns={"Valor": "cobre"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_wti[["Fecha", "Valor"]].rename(columns={"Valor": "wti"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_cds_clp_5y[["Fecha", "Valor"]].rename(columns={"Valor": "cds_clp_5y"}), on="Fecha", how="outer")
    df_final = df_final.merge(df_vix[["Fecha", "Valor"]].rename(columns ={"Valor": "vix"}), on="Fecha", how="outer")
    df_final = df_final.sort_values(by="Fecha").reset_index(drop=True)

    numeric_cols = [col for col in df_final.columns if col != "Fecha"]
    df_final[numeric_cols] = df_final[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Limpiamos las Fechas repetidas, tomando siempre el último valor.
    df_final = df_final.drop_duplicates(subset=["Fecha"], keep="last").reset_index(drop=True)
    # Hacemos ffill para completar los NaN. En los fines de semana
    base_columns = [col for col in df_final.columns if col != "Fecha"]
    for var in base_columns:
        df_final = add_technical_indicators(var, df_final)
    df_final = df_final.ffill()
    df_final = df_final.dropna(axis=1, how="all")
    df_final = df_final.dropna().reset_index(drop=True)
    return df_final

def get_macro_dataframe(ruta:str = "./db_data_bbg.db"):

    import pandas as pd
    import numpy as np
    import conexion_a_db as db

    lista_tablas = ["inflacion", "tpm", "ipc", "equity", "monedas"]

    # Conseguir dataframes de la base de datos
    # Cargar dataframes en un diccionario en lugar de usar vars()
    dfs = {tabla: db.Descargar_DF(ruta, tabla) for tabla in lista_tablas}

    # Mantener df_inflacion completo para los merges posteriores
    df_inflacion = dfs["inflacion"]

    # Filtrar y copiar data necesaria
    df_tpm_cl = dfs["tpm"][dfs["tpm"]["Pais"] == "Chile"].copy()
    df_tpm_us = dfs["tpm"][dfs["tpm"]["Pais"] == "Usa"].copy()
    df_ipc_cl = dfs["ipc"][dfs["ipc"]["Pais"] == "Chile"].copy()
    df_ipc_us = dfs["ipc"][dfs["ipc"]["Pais"] == "Usa"].copy()
    df_sp500 = dfs["equity"][dfs["equity"]["Pais"] == "Usa S&P"].copy()
    df_ipsa = dfs["equity"][dfs["equity"]["Pais"] == "Chile IPSA"].copy()
    df_clp = dfs["monedas"][dfs["monedas"]["Pais"] == "CLP"].copy()

    df_macro_final = df_inflacion[df_inflacion["Pais"] == "Chile"][["Fecha", "Valor"]].rename(columns={"Valor": "inflacion_cl"})
    df_macro_final = df_macro_final.merge(df_inflacion[df_inflacion["Pais"] == "Usa"][["Fecha", "Valor"]].rename(columns={"Valor": "inflacion_us"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_tpm_cl[["Fecha", "Valor"]].rename(columns={"Valor": "tpm_cl"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_tpm_us[["Fecha", "Valor"]].rename(columns={"Valor": "tpm_us"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_ipc_cl[["Fecha", "Valor"]].rename(columns={"Valor": "ipc_cl"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_ipc_us[["Fecha", "Valor"]].rename(columns={"Valor": "ipc_us"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_sp500[["Fecha", "Valor"]].rename(columns={"Valor": "sp500"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_ipsa[["Fecha", "Valor"]].rename(columns={"Valor": "ipsa"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.merge(df_clp[["Fecha", "Valor"]].rename(columns={"Valor": "usdclp"}), on="Fecha", how="outer")
    df_macro_final = df_macro_final.sort_values(by="Fecha").reset_index(drop=True)

    numeric_cols = [col for col in df_macro_final.columns if col != "Fecha"]
    df_macro_final[numeric_cols] = df_macro_final[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Dropeamos las fechas repetidas, tomando siempre el último valor.
    df_macro_final = df_macro_final.drop_duplicates(subset=["Fecha"], keep="last").reset_index(drop=True)

    df_macro_final[["inflacion_cl", "inflacion_us", "tpm_cl", "tpm_us", "ipc_cl", "ipc_us"]] = df_macro_final[["inflacion_cl", "inflacion_us", "tpm_cl", "tpm_us", "ipc_cl", "ipc_us"]].ffill()
    df_macro_final = df_macro_final.dropna(axis=1, how="all")
    df_macro_final = df_macro_final.dropna().reset_index(drop=True)

    df_macro_final = add_macro_indicators(df_macro_final)
    df_macro_final = df_macro_final.dropna(axis=1, how="all")
    df_macro_final = df_macro_final.dropna().reset_index(drop=True)
    return df_macro_final

def get_saved_preds(ruta:str):
    # Asumimos que esta guardado en formato json
    import pandas as pd
    import os

    if not os.path.isdir(ruta):
        return pd.DataFrame()
    archivos = [f for f in os.listdir(ruta) if f.endswith(".json")]
    dfs = []
    for archivo in archivos:
        df = pd.read_json(os.path.join(ruta, archivo))
        dfs.append(df)
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)
