import pandas as pd
import numpy as np


def nom_rept():
    voy = pd.read_excel('data_syll.xlsx', sheet_name='voyelles')
    con = pd.read_excel('data_syll.xlsx', sheet_name='consonnes')
    mix = pd.read_excel('data_syll.xlsx', sheet_name='mixtes')

    nb_syll = np.random.randint(2) + 1

    nom = []
    i = 0
    for i in range(nb_syll):
        nb_con = con['lett_con'].size
        rand_con = np.random.randint(nb_con)
        nom.append(con['lett_con'].to_numpy()[rand_con])

        nb_voy = voy['lett_voy'].size
        rand_voy = np.random.randint(nb_voy)
        nom.append(voy['lett_voy'].to_numpy()[rand_voy])

    nb_con = con['lett_con'].size
    rand_con = np.random.randint(nb_con)
    nom.append(con['lett_con'].to_numpy()[rand_con])

    nb_voy = voy['lett_voy'].size
    rand_voy = np.random.randint(nb_voy)
    nom.append(voy['lett_voy'].to_numpy()[rand_voy])

    nom.append('x')

    i = 0
    aff = ""
    for i in range(len(nom)):
        aff += nom[i]
    return (aff)
