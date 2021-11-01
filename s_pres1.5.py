# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:24:59 2021

@author: Matias
"""


import pandas as pd
import sys
import os

def lectura_proveedor(path_archivo, hoja = "HDCVI"):
    """
    path_archivo    ->    Ruta de hoja de calculo del proveedor
    hoja            ->    hoja que se desea abrir. por defecto HDCVI
    retorna un df
    """ 
    
    df = pd.read_excel(path_archivo, sheet_name = hoja, header = 3, usecols=[2, 3, 4, 5, 6])
    
    
    return df


def programa(pathdata, hojas, num_cam = 1, dolar = 105, mo = 2500, viatico = 1000):
    """
    Parameters
    df           ---->    el excel hecho df
    hojas           ---->    lista con los nombres de las hojas a utilizar
    num_cam = 1     ---->    numero de camaras. por defecto 1
    dolar           ---->    valor del dolar 
    mo              ---->    Mano de obra por camara.
    
    df : dataframe de pandas as pd
    hojas : lista str
    num_cam : int
        DESCRIPTION. The default is 1.
    dolar : float, optional
        DESCRIPTION. The default is 105.
    mo : int, optional
        DESCRIPTION. The default is 2500.

    Returns
    
    imprime una tabla con una descripcion del material a comprar, descripcion valor en dolar
    valor de iva aplicado, el valor llevado a pesos argentinos y el total a cobrar
    -------
    """
    
    precio = 0.0
    
    #itero sobre cada hoja del excel
    
    for h in hojas:
    
        df = lectura_proveedor(pathdata, hoja = h)
        
        cod_materiales = {"camara":"HAC-T2A21-3,6", "dvr_disc":"XVR1A04-1TB", "fuente":"FU 12V2000", "caja_estanca":"909075B", "zapatilla":"M-2199", "balun":"VT-HD402", "plugm":"PLUG M", "plugfem":"PLUGFEM", "cable":"HRN-1024-100", "hdmi":"C-HDMI 3"}
         
        col_nombre = df.columns
        
        #itero sobre el rango de los indices y me imprime coincidencia con lista requerida
        
        for i in df.index:
        
            #------------------------------------------------------------------------------------------------------
                
            for cod_mat in cod_materiales:
                
                if df["CODIGO"][i] == cod_materiales[cod_mat]:
                    
                    print("*"*100)
                        
                    for col in col_nombre:
                            
                        print(df[col][i])
        
            #------------------------------------------------------------------------------------------------------
                
            for cod_mat in cod_materiales:
                
                if df["CODIGO"][i] == cod_materiales[cod_mat]:
                    
                    if df["CODIGO"][i] == cod_materiales["camara"]:
                        
                        precio += (float(df["GREMIO"][i]) * num_cam) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    if df["CODIGO"][i] == cod_materiales["fuente"]:
                        
                        precio += (float(df["GREMIO"][i]) * num_cam) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    if df["CODIGO"][i] == cod_materiales["caja_estanca"]:
                        
                        precio += (float(df["GREMIO"][i]) * num_cam) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    if df["CODIGO"][i] == cod_materiales["balun"]:
                        
                        precio += (float(df["GREMIO"][i]) * (num_cam + 1)) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    if df["CODIGO"][i] == cod_materiales["plugm"]:
                        
                        precio += (float(df["GREMIO"][i]) * (num_cam + 1)) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    if df["CODIGO"][i] == cod_materiales["plugfem"]:
                        
                        precio += (float(df["GREMIO"][i]) * (num_cam + 1)) + (float(df["GREMIO"][i]) * 0.21)
                        
                        break
                    
                    precio += float(df["GREMIO"][i]) + (float(df["GREMIO"][i]) * 0.21)
    
    print("\n\n")                
    print(">>>>>>>>>>>>>>>>>>>>>>>DETALLE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    print("          CANTIDAD DE MATERIALES SELECCIONADO\n")
    print("CANTIDAD DE CAMARAS 1080p: ", num_cam, "          COD   ----->", cod_materiales["camara"])
    print("UN DVR DE 8 CH DE 1080p + DISCO DE 1T   COD   ----->",cod_materiales["dvr_disc"])
    print("CANTIDAD DE PLUGM ", (num_cam+1), "                   COD   ----->", cod_materiales["plugm"])
    print("CANTIDAD DE PLUGFEM ", (num_cam+1), "                 COD   ----->", cod_materiales["plugfem"])
    print("CANTIDAD DE BALUNES ", num_cam+1, "                 COD   ----->", cod_materiales["balun"])
    print("CANTIDAD DE CAJAS ESTANCA ", num_cam, "           COD   ----->", cod_materiales["caja_estanca"])
    print("CANTIDAD DE FUENTES ", num_cam, "                 COD   ----->", cod_materiales["fuente"])
    print("CANTIDAD DE CABLE 100 mts", "              COD   ----->", cod_materiales["cable"])
    print("CABLE HDMI 3 mts                        COD   ----->",cod_materiales["hdmi"])
    print("ZAPATILLA DE 6 TOMAS                    COD   ----->",cod_materiales["zapatilla"])
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>DETALLE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    print("\n\n")
    print("-"*100)
    print("precio total USD",precio," ::: UNO O MAS VALORES PUEDEN TENER UN IVA MENOR AL 21% :::")
    print("-"*100)
    print("\n")
    print("-"*100)
    print("precio total $",round(precio*dolar,4)," ::: UNO O MAS VALORES PUEDEN TENER UN IVA MENOR AL 21% :::")
    print("-"*100)
    print("\n")
    print("-"*100)
    print("Mano de obra $",mo," por camara, total => $", mo*num_cam)
    print("-"*100)
    print("\n")
    print("-"*100)
    print("Viatico", viatico)
    print("-"*100)
    print("\n")
    print("-"*100)
    print("TOTAL $",round(precio*dolar,4) + (mo * num_cam) + int(viatico)," con Mano de Obra")
    print("-"*100)
    

if __name__ == "__main__":
    
    num_cam = 1
    
    dolar = 105
    
    mo = 2500
    
    viatico = 1000
    
    for root, folder, file in os.walk("../proveedor"):
        
        for archivo in file:
            
            pathdata = os.path.join(root,archivo)
    
    for i in sys.argv:
            
        if "num_cam" in i:
                
            n = i.split("=")
                
            num_cam = int(n[-1])
            
        if "mo" in i:
                
            m = i.split("=")
                
            mo = int(m[-1])
                
        if "dolar" in i:
                
            d = i.split("=")
                
            dolar = float(d[-1])
        
        if "viatico" in i:
                
            v = i.split("=")
                
            viatico = int(v[-1])
            
        
    hojas = ["ELECTRICIDAD", "HDCVI", "ACC. CCTV", "CONECTIVIDAD", "ACCESO"]
            
    #pathdata = "../proveedor/HURIN GREMIO NOVIEMBRE V1 2021.xlsx"
            
    programa(pathdata, hojas, num_cam, dolar, mo, viatico)
