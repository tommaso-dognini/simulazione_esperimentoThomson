import matplotlib.pyplot as plt
import matplotlib as mpl
import streamlit as st
import numpy as np


# titolo della pagina
st.markdown("<h1 style='text-align: center; color: #b30000;'>Esperimento di J.J. Thomson</h1>",
            unsafe_allow_html=True)

# titolo e pagina laterale
st.sidebar.title('Menù\n')
pagina = st.sidebar.radio('', ['HOME', 'SIMULAZIONE', 'LINK UTILI'], index=0)
if pagina == 'HOME':
    st.write('''
    text
    
    
    ''')


if pagina == 'SIMULAZIONE':
    st.write('''
        In questa pagina è possibile simulare l'esperimento di Thomson\n
        \n ## Parametri della simulazione
        \nE' possibile regolare i paramentri della simulazione
        
        \n ### Condizioni iniziali
    ''')
    ddp = st.number_input('D.D.P. tra armature condensatore [V]',step =1, value=1000)
    v0_input = st.number_input('Velocità iniziale degli elettroni [(*10^15)m/s]',step=0.1, value = 1.4)
    st.write('''### Dimensioni del condensatore \n ''')
    d_input = st.number_input('Distanza d tra le armature del condensatore [cm]',step=0.1, value = 6.0)
    l_input = st.number_input('Lunghezza l del condensatore [cm]',step=0.1, value = 10.0)
    # CALCOLO DELLA TRAIETTORIA
    def calcolaTraiettoria(campoE, v0, d, l, dati_elettrone, x):
        y = []
        for xs in x:
            y.append((0.5*dati_elettrone[0]*campoE *
                      xs**2/(dati_elettrone[1]*v0))*10**2)

        return (x*10**2, y)

    # informazioni su elettrone x il calcolo
    dati_elettrone = [1.602*10**-19, 9.109*10**-31]  # carica, massa


    v0 = v0_input*10**15  # ms

    # porto dimensioni condensatore  in m 
    d = d_input*10**-2  # m
    l = l_input*10**-2  # m

    # calcolo campo elettrico
    campoE = ddp/d

    x = np.linspace(0, l, int(l*100))
    traiettoria = calcolaTraiettoria(campoE, v0, d, l, dati_elettrone, x)

    # CREAZIONE DEL GRAFICO
    armatura1 = []
    armatura2 = []

    # definisco le rette per armature del condesatore
    for n in range(0, x.size):
        armatura1.append((d/2)*10**2)
        armatura2.append((-d/2)*10**2)

    plt.style.use('seaborn')
    plt.title('\n Traiettoria elettroni \n', fontsize='20')
    plt.plot(x*10**2, armatura1, label='lastra +', color='red', linewidth=5)
    plt.plot(x*10**2, armatura2, label='lastra -', color='red', linewidth=5)

    plt.plot(traiettoria[0], traiettoria[1], color='black')
    plt.xlabel("x (cm)")
    plt.ylabel("y (cm)")

    # testo per indicare lastra + e lastra -
    plt.text((l*10**2 - 1), ((d/2)*10**2 - 0.5),
             'lastra +', horizontalalignment='left')
    plt.text((l*10**2 - 1), - ((d/2)*10**2 - 0.5),
             'lastra +', horizontalalignment='left')

    # plt.grid()
    # plt.legend()
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # calcolo del rapporto em
    y = traiettoria[1]
    x = traiettoria[0]
    em = (2*y[-1]*10**-2*v0*d/(ddp*(x[-1]*10**-2)**2))*10**-11
