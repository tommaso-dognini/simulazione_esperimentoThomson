import matplotlib.pyplot as plt
from PIL import Image
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
    ### Abstract \n
    The aim of this experiment is to calculate the ratio between the charge of the electron and its mass, using the
     data obtained from the reproduction of Thomson's experiment.
    
    ### J.J. Thomson: la storia dietro la scoperta degli elettroni \n
    Mentre Thomson frequentava l’Owen’s collage suo padre morì, e non potendo pagare le spese del college cercò di ricavare i soldi
     dalle borse di studio della scuola.\n
    Nel 1884, all’età di 24 anni, si candida e viene sorprendentemente eletto come capo dell’istituto di ricerca di Cavendish, ove, aiutato da un’equipe di 8 assistenti,
     conduce diversi esperimenti anche grazie alla facilità con cui riesce a reperire materiali e strumenti, permettendo una ricerca più veloce ed efficace. Egli stesso,
      trovandosi in questa situazione dichiarerà di sentirsi come “un pescatore che ritrovatosi per caso in un posto cerca di pescare un pesce più grosso delle sue possibilità”. Secondo l’autobiografia di Thomson,
       la scoperta dell’elettrone è nata dal tentativo di spiegare la discrepanza fra il comportamento dei raggi catodici quando immersi in campi magnetici e quando soggetti all’azione di forze elettrostatiche. 

    ### La storia dell’elettrone da Faraday a Thomson \n
    - 1833: M. Faraday ipotizza l’esistenza di un “atomo di elettricità” sulla base delle leggi dell’elettrolisi.
    - 1869: W. Hittorf studiando la scarica elettrica nei gas scopre i raggi catodici, utilizzati successivamente da Thomson per perseguire lo scopo del suo esperimento.
    - 1874: Primo tentativo di calcolo approssimativo della carica di questo “atomo di elettricità”, ad opera di G. J. Stoney, il quale fornisce una stima del valore della carica elementare utilizzando una sua precedente stima del valore del numero di Avogadro.
    - 1891: Stoney inventa il nome “elettrone” per designare l’atomo di elettricità, concetto rilanciato 10 anni prima da H. Helmholtz.
    - 1897: J. J. Thomson dimostra che i raggi catodici sono particelle cariche negativamente e ne determina il rapporto massa/carica. Dal suo esperimento, Thomson evince che la particella è circa 1000 volte più leggera dell’atomo di H, dato che si ottiene assumendo come valore della carica quella misurata per gli ioni nell’elettrolisi. 
    - 1899: Misura della carica dell’elettrone grazie alla scoperta dell’allievo di Thomson, Wilson, il quale scopre che gli ioni prodotti ionizzando le molecole d’aria mediante raggi ultravioletti agiscono in appropriate condizioni da nuclei di condensazione delle goccioline d’acqua.
    - 1913: Millikan calcola con più precisione il valore della carica dell’elettrone, sostituendo le goccioline d’acqua con goccioline d’olio.
    \n
    ### Descrizione dell’esperimento \n
    Lo scopo dell’esperimento di Thomson era quello di studiare e comprendere il comportamento dell’atomo di elettricità, precedentemente definito da Stoney “elettrone”.  A riguardo erano diverse le teorie e gli esperimenti con i quali diversi fisici avevano tentato di descrivere il comportamento di questa ipotetica nuova particella, comportamento che ancora non era chiaro a causa delle forti divergenze dei risultati sperimentali pubblicati fino ad allora. Tra questi, i più contrastanti, che hanno poi portato Thomson ad ideare il suo esperimento, furono quelli di Hertz e quelli di Perrin. Il primo sosteneva infatti che i raggi catodici non subivano alcuna deflessione in presenza di forze elettriche e quindi che la loro natura non era quella di particelle cariche. Al contrario, Perrin poté affermare, a seguito di diversi esperimenti, che tali raggi erano portatori di cariche elettriche negative. L’evidente contraddizione nei due risultati indusse Thomson a considerare nuovamente entrambi gli esperimenti e a cercare, ideando un nuovo esperimento, di trarre una conclusione che smentisse la tesi dell’uno confermando quella dell’altro.
    Thomson, convinto della correttezza delle affermazioni di Perrin, ipotizzò che l’esperimento di Hertz poteva aver dato un risultato errato: egli sapeva infatti che i tubi per i raggi catodici utilizzati da Hertz funzionavano solo se in presenza di aria pertanto ipotizzò che questa ionizzandosi, diventasse conduttrice creando un effetto analogo alla quello della gabbia di Faraday.
    Egli scoprì inoltre che, facendo passare il raggio catodico attraverso un anodo positivo con un foro al centro, si otteneva un raggio collimato e quindi più potente. In questo modo fu per lui possibile abbassare drasticamente la quantità di aria necessaria, aspirandola dal tubo, diminuendo quindi l’influenza di quest’ultima sull’esperimento.  Modificando quindi l’sperimento di Hertz sulla base delle sue ipotesi diede vita ad un nuovo esperimento che gli permise di osservare come il fascio di elettroni prodotto dal filamento e sparato nel tubo catodico subisca una deflessione verso la piastra positiva, confermando la teoria di Perrin.
    Scoprì poi che i raggi catodici potevano attraversare il metallo; Egli ipotizzò che ciò fosse possibile purché le particelle si muovessero ad una velocità molto elevata. Stante che le particelle si muovano sia per l’azione della forza elettrica che della forza magnetica, Thomson introdusse un campo magnetico di intensità tale da bilanciare la forza elettrostatica, e osservare quindi rettilinea la direzione del raggio.
    Sapendo che la forza elettrostatica dipende dalla carica della particella, dalla sua velocità e dall’intensità del campo magnetico, e sapendo inoltre che la forza magnetica è il prodotto fra la carica della particella e dal campo, Thomson poté calcolare la velocità della particella, definita come il rapporto fra il campo magnetico e il campo elettrico. La velocità così calcolata ha un valore di circa 2,6*10^4 m/s qualsiasi sia la forza elettrica o magnetica applicata (purché sia bilanciata). Successivamente, Thomson rimosse il campo magnetico lasciando applicata solo la forza elettrostatica, e osservò che il raggio seguiva una traiettoria simile a quella di un proiettile lanciato orizzontalmente. Sapendo che la forza di gravità relativa alle particelle contenute nei raggi catodici è così piccola da poter essere trascurata, e conoscendo la velocità delle particelle, calcolata precedentemente, poté calcolare il tempo impiegato dalle particelle per raggiungere la fine del tubo da lui utilizzato, e di conseguenza la loro accelerazione. Sostituendo il valore trovato nella formula $F=ma = qE$, calcolò il rapporto fra la carica della particella e la sua massa (uguale ad a/E), scoprendo che esso rimaneva costante per qualsiasi sostanza venisse utilizzata per l’elettrodo e qualsiasi gas venisse utilizzato per riempire il tubo. Poté quindi provare l’esistenza di particelle fondamentali, equi presenti in tutti gli oggetti, gli elettroni.
    \n
    ### Il sistema utilizzato \n
    ''')

    img_sistema = Image.open('img//sistema.jpg')
    st.image(img_sistema,width=600, caption='Schema del sistema utilizzato')

    st.write(''' 
    ***I generatori***
    - Il generatore 1 crea una differenza potenziale tra le armature del condensatore;
    - Il generatore 2 riscalda il filamento con conseguente effetto termoionico; 
    - Il generatore 3 funziona da acceleratore per gli elettroni prodotti infatti crea una differenza di potenziale tra gli estremi del filamento necessaria per mettere in movimento gli elettroni verso il condensatore ad una velocità adeguata (senza di esso il moto degli elettroni sarebbe troppo lento);

    ***I voltmetri***
    - Il voltmetro 1 quantifica la differenza di potenziale sulle piastre del condensatore, mentre il voltmetro 2 quantifica quella sul filamento.

    ***Il condensatore piano***\n
    Il condensatore piano posto all’interno di una sfera di vetro di raggio 12.5 cm è utilizzato per creare un campo elettrico uniforme E perpendicolare al moto degli elettroni. Tra le due piastre del condensatore vi è una scala graduata utilizzata per calcolare l’angolo di deflessione del fascio degli elettroni soggetti alla forza attrattiva della piastra positiva.  All’interno della sfera vi è un gas a bassa pressione necessario per visualizzare la traiettoria degli elettroni sotto forma di raggio luminoso dovuto ad una interazione lieve (che non perturba l’esperimento e i risultati) tra esso e gli elettroni.

    \n
    ### L'origine degli elettroni: l'effetto termoionico \n
    ''')

    #CALCOLO TEORICO E DEFINIZION DEL RAPPORTO EM
    st.write(''' 
    ### Calcolo teorico e definizione del rapporto e/m \n

    L’intero esperimento si basa sullo studio e sull’osservazione del comportamento degli elettroni. Infatti, ipotizzando (come aveva fatto Perrin) che questi siano carichi negativamente, l’intento di Thomson era quello di osservare il loro comportamento dinamico all’interno di un campo elettrico in modo da poter stabilire il segno e la quantità di carica posseduta da ogni ipotetica particella. A questo è dovuto l’utilizzo di un condensatore piano posto all’interno della sfera di vetro, infatti, è noto che all’interno di un condensatore il campo elettrico è costante. Tale proprietà rende quindi un condensatore piano perfetto per i fini dell’esperimento e permette di operare attraverso calcoli piuttosto semplici grazie alle sue diverse proprietà. In particolare, sfruttando la relazione $\Delta V =Ed$ , risulta piuttosto semplice descrivere, data la differenza di potenziale applicata alle armature del condensatore, l’intensità del campo elettrico al suo interno. Infine, sfruttando la definizione di forza elettrica di una particella in un campo elettrico costante, $F=qE$, e il secondo principio della dinamica, $F=ma$ , è possibile scrivere e calcolare il rapporto tra la carica e
     la massa di ciascuna particella, noto il comportamento delle stesse all’interno di un campo elettrico (traiettoria, cioè *x,y* in funzione del tempo). 
    \n
    Pertanto, fissato un sistema di riferimento, è possibile scrive la traiettoria del moto degli elettroni all’interno del condensatore scomponendo il moto nelle sue due componenti, quella orizzontale e quella verticale e risolvendo il sistema delle leggi orarie in funzione del tempo.  
    ''')
    st.latex(r'{\begin{cases}y= \frac{1}{2}at^2 \\ x=v_0 t \end{cases} => y = \frac{1}{2}a\frac{x^2}{v_0^2}}')
    st.write('''
    Data quindi l’equazione generale della traiettoria, sfruttando le relazioni prima citate è possibile scrivere l’accelerazione degli elettroni in funzione del loro carica *e* e massa *m* e dell’intensità del campo elettrico *E*. Infatti
    \n
    ''')
    st.latex(r'F=ma=qe \leftrightarrow a=\frac{eE}{m}')
    st.write('''
    con $q=e$ carica elettrone\n
    Quindi l’equazione della traiettoria risulta: \n
    ''')
    st.latex(r'y= \frac{1}{2}\frac{eE}{m v_0^2}x^2')
    st.write('''
    Poiché sperimentalmente è spesso più comodo misure la differenza di potenziale applicata alle armature del condensatore piuttosto che il campo elettrico al suo interno, è possibile, data la relazione $\Delta V = Ed$, scrivere il campo elettrico in funzione della differenza di potenziale e della distanza delle sue armature. Pertanto\n
    ''')
    st.latex(r'E=\frac{\Delta V}{d} \rightarrow a=\frac{ed}{m\Delta V}\frac{1}{v_0^2}')
    st.write('''
    Quindi, ricavando sperimentalmente la coppia delle coordinate *x,y* di un determinato numero di punti sulla traiettoria degli elettroni e conoscendo i valori di $d,\Delta V$ e di $v_0$ è possibile mediante l’equazione della traiettoria ottenuta precedentemente calcolare il rapporto $e/m$  e verificare che questo rimanga invariato per ogni punto della traiettoria e quindi per ogni particella del fascio luminoso che la rappresenta.
    \nInfine, per poter affermare con certezza la correttezza del risultato ottenuto, è necessario ripetere lo stesso procedimento ma variando le condizioni iniziali come per esempio la d.d.p. tra le armature del condensatore. In questo modo, se il rapporto calcolato risulta costante pur variando le condizioni iniziali, si è dimostrato che le particelle oggetto di studio, gli elettroni, possiedo una quantità di carica e una massa specifica che stanno tra loro in un rapporto definito e costante.
    ''')

    #MISURAZIONE E CALCOLI SPERIMENTALI
    st.write('''
    ### Misurazioni e calcoli sperimentali
    \nIn questo esperimento i risultati ottenuti sono stati registrati attraverso una fotografia del sistema raffigurante la traiettoria in forma di raggio luminoso degli elettroni all’interno del condensatore.
    Pertanto per poter procedere con l’analisi dei dati e quindi con il calcolo del rapporto $e/m$ è necessario estrapolare dalla fotografia le informazioni sul moto degli elettroni (coppia di coordinate *x,y*) e misurare le condizioni iniziali a cui il fascio di elettroni è sottoposto.
    
    \n**Misurazione delle condizioni iniziali**\n
    Con il termine condizioni iniziali si intendono tutti quei fattori che concorrono nel calcolo del rapporto $e/m$ attraverso l’equazione della traiettoria precedentemente trovata e che rimangono, a meno di variazioni volontarie, costanti durante il corso dell’esperimento. Questi fattori sono:

    -   La differenza di potenziale $\Delta V$ applicata alle armature del condensatore
	-   La differenza di potenziale $\Delta V_2$ applicata alle estremità del filamento metallico (che funge da acceleratore per gli elettroni) e quindi la velocità orizzontale (perché il fascio è collimato da una piastra metallica) con cui gli elettroni sono immessi nel condensatore
	-   La distanza d tra le armature del condensatore

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
