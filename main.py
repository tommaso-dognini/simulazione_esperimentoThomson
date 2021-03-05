import matplotlib.pyplot as plt
from PIL import Image
import matplotlib as mpl
import streamlit as st
import numpy as np


# titolo della pagina
st.markdown("<h1 style='text-align: center; color: #191970;'>Esperimento di J.J. Thomson</h1>",
            unsafe_allow_html=True)

# titolo e pagina laterale
st.sidebar.title('Menù\n')
pagina = st.sidebar.radio('', ['HOME', 'SIMULAZIONE','CODICE SORGENTE'], index=0)
if pagina == 'HOME':
    
    st.write('''
    ## Abstract \n
    The aim of this experiment is to calculate the ratio between the charge of the electron and its mass, using the
     data obtained from the reproduction of Thomson's experiment.
    
    ## J.J. Thomson: la storia dietro la scoperta degli elettroni \n
    Mentre Thomson frequentava l’Owen’s collage suo padre morì, e non potendo pagare le spese del college cercò di ricavare i soldi
     dalle borse di studio della scuola.\n
    Nel 1884, all’età di 24 anni, si candida e viene sorprendentemente eletto come capo dell’istituto di ricerca di Cavendish, ove, aiutato da un’equipe di 8 assistenti,
     conduce diversi esperimenti anche grazie alla facilità con cui riesce a reperire materiali e strumenti, permettendo una ricerca più veloce ed efficace. Egli stesso,
      trovandosi in questa situazione dichiarerà di sentirsi come “un pescatore che ritrovatosi per caso in un posto cerca di pescare un pesce più grosso delle sue possibilità”. Secondo l’autobiografia di Thomson,
       la scoperta dell’elettrone è nata dal tentativo di spiegare la discrepanza fra il comportamento dei raggi catodici quando immersi in campi magnetici e quando soggetti all’azione di forze elettrostatiche. 

    ## La storia dell’elettrone da Faraday a Thomson \n
    - 1833: M. Faraday ipotizza l’esistenza di un “atomo di elettricità” sulla base delle leggi dell’elettrolisi.
    - 1869: W. Hittorf studiando la scarica elettrica nei gas scopre i raggi catodici, utilizzati successivamente da Thomson per perseguire lo scopo del suo esperimento.
    - 1874: Primo tentativo di calcolo approssimativo della carica di questo “atomo di elettricità”, ad opera di G. J. Stoney, il quale fornisce una stima del valore della carica elementare utilizzando una sua precedente stima del valore del numero di Avogadro.
    - 1891: Stoney inventa il nome “elettrone” per designare l’atomo di elettricità, concetto rilanciato 10 anni prima da H. Helmholtz.
    - 1897: J. J. Thomson dimostra che i raggi catodici sono particelle cariche negativamente e ne determina il rapporto massa/carica. Dal suo esperimento, Thomson evince che la particella è circa 1000 volte più leggera dell’atomo di H, dato che si ottiene assumendo come valore della carica quella misurata per gli ioni nell’elettrolisi. 
    - 1899: Misura della carica dell’elettrone grazie alla scoperta dell’allievo di Thomson, Wilson, il quale scopre che gli ioni prodotti ionizzando le molecole d’aria mediante raggi ultravioletti agiscono in appropriate condizioni da nuclei di condensazione delle goccioline d’acqua.
    - 1913: Millikan calcola con più precisione il valore della carica dell’elettrone, sostituendo le goccioline d’acqua con goccioline d’olio.
    \n
    ## Descrizione dell’esperimento \n
    Lo scopo dell’esperimento di Thomson era quello di studiare e comprendere il comportamento dell’atomo di elettricità, precedentemente definito da Stoney “elettrone”.  A riguardo erano diverse le teorie e gli esperimenti con i quali diversi fisici avevano tentato di descrivere il comportamento di questa ipotetica nuova particella, comportamento che ancora non era chiaro a causa delle forti divergenze dei risultati sperimentali pubblicati fino ad allora. Tra questi, i più contrastanti, che hanno poi portato Thomson ad ideare il suo esperimento, furono quelli di Hertz e quelli di Perrin. Il primo sosteneva infatti che i raggi catodici non subivano alcuna deflessione in presenza di forze elettriche e quindi che la loro natura non era quella di particelle cariche. Al contrario, Perrin poté affermare, a seguito di diversi esperimenti, che tali raggi erano portatori di cariche elettriche negative. L’evidente contraddizione nei due risultati indusse Thomson a considerare nuovamente entrambi gli esperimenti e a cercare, ideando un nuovo esperimento, di trarre una conclusione che smentisse la tesi dell’uno confermando quella dell’altro.
    Thomson, convinto della correttezza delle affermazioni di Perrin, ipotizzò che l’esperimento di Hertz poteva aver dato un risultato errato: egli sapeva infatti che i tubi per i raggi catodici utilizzati da Hertz funzionavano solo se in presenza di aria pertanto ipotizzò che questa ionizzandosi, diventasse conduttrice creando un effetto analogo alla quello della gabbia di Faraday.
    Egli scoprì inoltre che, facendo passare il raggio catodico attraverso un anodo positivo con un foro al centro, si otteneva un raggio collimato e quindi più potente. In questo modo fu per lui possibile abbassare drasticamente la quantità di aria necessaria, aspirandola dal tubo, diminuendo quindi l’influenza di quest’ultima sull’esperimento.  Modificando quindi l’sperimento di Hertz sulla base delle sue ipotesi diede vita ad un nuovo esperimento che gli permise di osservare come il fascio di elettroni prodotto dal filamento e sparato nel tubo catodico subisca una deflessione verso la piastra positiva, confermando la teoria di Perrin.
    Scoprì poi che i raggi catodici potevano attraversare il metallo; Egli ipotizzò che ciò fosse possibile purché le particelle si muovessero ad una velocità molto elevata. Stante che le particelle si muovano sia per l’azione della forza elettrica che della forza magnetica, Thomson introdusse un campo magnetico di intensità tale da bilanciare la forza elettrostatica, e osservare quindi rettilinea la direzione del raggio.
    Sapendo che la forza elettrostatica dipende dalla carica della particella, dalla sua velocità e dall’intensità del campo magnetico, e sapendo inoltre che la forza magnetica è il prodotto fra la carica della particella e dal campo, Thomson poté calcolare la velocità della particella, definita come il rapporto fra il campo magnetico e il campo elettrico. La velocità così calcolata ha un valore di circa 2,6*10^4 m/s qualsiasi sia la forza elettrica o magnetica applicata (purché sia bilanciata). Successivamente, Thomson rimosse il campo magnetico lasciando applicata solo la forza elettrostatica, e osservò che il raggio seguiva una traiettoria simile a quella di un proiettile lanciato orizzontalmente. Sapendo che la forza di gravità relativa alle particelle contenute nei raggi catodici è così piccola da poter essere trascurata, e conoscendo la velocità delle particelle, calcolata precedentemente, poté calcolare il tempo impiegato dalle particelle per raggiungere la fine del tubo da lui utilizzato, e di conseguenza la loro accelerazione. Sostituendo il valore trovato nella formula $F=ma = qE$, calcolò il rapporto fra la carica della particella e la sua massa (uguale ad a/E), scoprendo che esso rimaneva costante per qualsiasi sostanza venisse utilizzata per l’elettrodo e qualsiasi gas venisse utilizzato per riempire il tubo. Poté quindi provare l’esistenza di particelle fondamentali, equi presenti in tutti gli oggetti, gli elettroni.
    \n
    ## Il sistema utilizzato \n
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
    L'effetto termoionico (o effetto termoelettronico) consiste nell'emissione indotta termicamente di particelle cariche (elettroni o ioni, "termoioni" da cui il nome), da parte di un materiale, a volte un metallo riscaldato ad alta temperatura, per esempio a seguito del passaggio di una corrente elettrica.
    L'emissione degli elettroni avviene come conseguenza dell'aumento della loro energia cinetica, osservato come aumento della temperatura, che permette loro di vincere la forza che li trattiene vincolati agli atomi del materiale. La particella emessa tenderà a rimanere in prossimità della superficie emettitrice, la quale si sarà caricata di una carica opposta nel segno ma uguale in modulo al totale delle cariche emesse. 
    Quando gli elettroni assumono un energia maggiore del lavoro che occorrerebbe fare per estrarli, allora essi potrebbero essere in grado di lasciare la superficie metallica. Non tutti gli elettroni con un tale quantità di energia però sono in grado di fuoriuscire dal metallo; Infatti, possono essere estratti solo quelli che si trovano in prossimità della superficie e che si stanno muovendo nel verso uscente da essa

    ''')

    #CALCOLO TEORICO E DEFINIZION DEL RAPPORTO EM
    st.write(''' 
    ## Calcolo teorico e definizione del rapporto e/m \n

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
    ## Misurazioni e calcoli sperimentali
    \nIn questo esperimento i risultati ottenuti sono stati registrati attraverso una fotografia del sistema raffigurante la traiettoria in forma di raggio luminoso degli elettroni all’interno del condensatore.
    Pertanto per poter procedere con l’analisi dei dati e quindi con il calcolo del rapporto $e/m$ è necessario estrapolare dalla fotografia le informazioni sul moto degli elettroni (coppia di coordinate *x,y*) e misurare le condizioni iniziali a cui il fascio di elettroni è sottoposto.
    
    \n**Misurazione delle condizioni iniziali**
    \nCon il termine condizioni iniziali si intendono tutti quei fattori che concorrono nel calcolo del rapporto $e/m$ attraverso l’equazione della traiettoria precedentemente trovata e che rimangono, a meno di variazioni volontarie, costanti durante il corso dell’esperimento. Questi fattori sono:
    ''')
    st.write('''
    - La differenza di potenziale $\Delta V$ applicata alle armature del condensatore.
	- La differenza di potenziale $\Delta V_2$ applicata alle estremità del filamento metallico (che funge da acceleratore per gli elettroni) e quindi la velocità orizzontale (perché il fascio è collimato da una piastra metallica) con cui gli elettroni sono immessi nel condensatore
	- La distanza d tra le armature del condensatore
    ''')
    st.write('''
    ***D.D.P. tra le armature del condensatore: ***
    In questo esperimento sono state effettuate due misurazioni applicando d.d.p. differenti alle armature del condensatore:
    ''')
    img_tabelladdp = Image.open('img//tabelladdp.jpg')
    st.image(img_tabelladdp,width=700)

    st.write('''
    ***D.D.P tra le estremità del filamento, velocità orizzontale iniziale: ***
    Il $\Delta V_2$ applicato tra le estremità del filamento metallico in questo esperimento è stato mantenuto costante a 4000V.  Tale differenza di potenziale come illustrato precedentemente permette di accelerare gli elettroni prodotti dal filamento per effetto termoionico e quindi di migliorare l’osservazione del fascio degli stessi. 
    Tra i fattori che concorrono al calcolo del rapporto $e/m$  c’è la velocita orizzontale iniziale degli elettroni, $v_0$, che dipende dal potenziale $\Delta V_2$. Per calcolare tale velocità, in questo esperimento, è stato utilizzato un procedimento semplificato che in realtà porta ad un risultato approssimato che si discosta da quello
     che si otterrebbe seguendo il corretto procedimento teorico.  In particolare, è stato tralasciato, per semplicità, un passaggio che però risulta fondamentale in quanto senza di esso Thomson non avrebbe potuto ottenere i risultati che ha ottenuto. La semplificazione attuata si basa sul fatto che per semplicità non è stato considerato l’effetto del campo magnetico ed è stata utilizzata come costante nota (anche se per Thomson non lo era e per questo ha dovuto utilizzare un campo magnetico come è spiegato in: descrizione dell’esperimento) la carica dell’elettrone. Seguendo questo procedimento risulta infatti semplice calcolare la velocità orizzontale iniziale degli elettroni, $v_0$, infatti si può affermare che l’energia cinetica di ciascuna particella è uguale al lavoro da essa compiuta all’interno del condensatore.
    Quindi:    
    ''')
    st.latex(r'\Delta K = e\Delta V \rightarrow \frac{1}{2}mv_0^2 =e\Delta V')
    st.latex(r'\text{Quindi: } v_0^2 = \frac{2e\Delta V}{m}=1,4*10^{15} \frac{m}{s}')
    st.write('''
    con $v_i =0$ e $v_f=v_0$ \n
    ***Distanza d tra le armature del condensatore: ***
    Per poter calcolare l’intensità del campo elettrico uniforme all’interno del condensatore data la differenza di potenziale tra le sue armature è necessario conoscere la distanza tra di esse. Infatti:
    ''')
    st.latex(r'E = \frac{\Delta V}{d}')
    st.write('''
    In questo esperimento il sistema utilizzato integra all’interno del condensatore piano una scala graduata che facilita l’operazione di registrazione e di misurazione di *d* e delle coordinate *x,y* del moto. In particolare, la scala graduata ha come unità di misura 1cm e pertanto la distanza tra le armature risulta di 6,0 cm. 
    ''')
    st.write('''
    **Analisi della fotografia: calcolo delle coordinate x,y**\n 
    ***Metodo utilizzato: ***
    Per poter eseguire l’analisi dei dati è necessario estrapolare dalla fotografia un determinato numero di coppie di coordinate *x,y* di punti appartenenti alla traiettoria degli elettroni in modo da poter verificare che il rapporto $e/m$  sia effettivamente costante. Tuttavia, procedere calcolando n volte il rapporto $e/m$   per ogni punto di coordinate $x_n,y_n$ implicherebbe l’utilizzo di una media semplice dei vari risultati ottenuti e quindi un’approssimazione insufficientemente precisa e che non terrebbe conto degli errori sperimentali commessi nel raccogliere i dati. 
    Infatti, non essendo gli errori sperimentali quantificabili precisamente, a causa del metodo di raccolta dati utilizzato, non sarebbe possibile calcolare un errore relativo sulla misura finale. Pertanto in questo esperimento si è deciso di utilizzare n punti del fascio di elettroni e mediante le loro coordinate *x,y* calcolare l’equazione della linea di tendenza polinomiale di secondo 2° (la traiettoria ideale è una parabola come precedentemente dimostrato) in modo da ottenere  una buona approssimazione e di non dover considerare i singoli errori ma bensì l’imprecisione generale delle misurazioni quantificabile mediante l’indice R^2 della linea di tendenza cosi trovata.
     Inoltre, così facendo, l’equazione della linea di tendenza trovata (che coincide con una ideale traiettoria parabolica che più si avvicina a quella calcolabile teoricamente) permette di identificare con precisione, scelto adeguatamente il sistema di riferimento, le radici dell’equazione e l’intercetta all’origine della parabola che dal punto di vista fisico coincidono con lo spazio *x* percorso in orizzontale nel condensatore e la deflessione verticale *y* subita dal fascio di elettroni. 
    Dati quindi *x* e *y* è possibile scrivere l’equazione della traiettoria degli elettroni nella forma sopra citata e quindi quantificare il rapporto $e/m$ .
    ''')
    st.write("\n*In questo esperimento l’analisi grafica della fotografia è stata effettuata tramite geometra.*\n")

    st.write('''
    ***Fattore di scala dell’analisi grafica: ***
    Procedendo come spiegato è necessario però considerare che le misure di *x,y* ottenute tramite l’analisi grafica della fotografia non hanno un significato reale a meno che normalizzate utilizzando il corretto fattore di scala. Infatti, si può dedurre facilmente lo zoom utilizzato nella fotografia la posizione della fotocamera rispetto al sistema fotografato (errore di parallasse dovuto al non perfetto allineamento con la normale al piano del condensatore) potrebbero portare a una parziale distorsione delle dimensioni dell’immagine che pertanto risulterebbero ingrandite o rimpicciolite rispetto alla realtà di un determinato fattore. Per ottenere quindi un risultato finale veritiero è necessario calcolare tale fattore di scala e normalizzare tramite esso tutte le misure estrapolate dalla fotografia. Tuttavia, è con i giusti accorgimenti è possibile evitare tale operazione e quindi anche gli errori sperimentali ad essa annessi. Infatti, se si prelevano tutte le misure dalla stessa fotografia e quindi si fa in modo che tutte siano affette dallo stesso fattore di scala è possibile fare il seguente ragionamento:\n    
    ''')
    st.latex(r'K_{fattore di scala}=\frac{x_{vituale}}{x_{reale}} \text{       quindi     }  x_r= \frac{x_v}{K}')
    st.write("Se si analizza la formula finale da utilizzare per quantificare $e/m$ si nota che: \n")
    st.latex(r'\frac{e}{m}=\frac{2ydv_0^2}{x^2\Delta V} \text{   moltiplicando per K le dimensioni virtuali    } \frac{e}{m}=\frac{2yKdKv_0^2}{(xK)^2\Delta V }')
    st.latex(r'\text{Quindi:    } \frac{e}{m}=\frac{2ydv_0^2K^2}{x^2\Delta V K^2}')
    st.write("Si nota quindi come, se le misure affette da K sono tutte, quindi *x,y* e anche *d*,allora il fattore di scala si semplifica e pertanto non è necessario normalizzare le misure precedentemente calcolate.")

    st.write('''
    ***Scelta del sistema di riferimento: ***\n
    *In questo esperimento l’analisi grafica della fotografia è stata effettuata tramite Geogebra.*\n
    Anche la scelta del sistema di riferimento è importante ed ha la sua influenza sulla precisione del risultato finale. Si consiglia per questo, dato che il fattore di scala non influenza il risultato finale, di ingrandire l’immagine il giusto, in modo che risulti più semplice e accurata la scelta dei punti della traiettoria. Inoltre, si consiglia di posizionare l’immagine all’interno del sistema di riferimento cartesiano di Geogebra in modo che l’origine degli assi coincida con 
    l’intersezione degli assi della scala graduata posta all’interno del condensatore. Si consiglia inoltre di ruotare l’immagine o modificarla nel caso in cui questa raffiguri il sistema dell’esperimento storto o inclinato: non interessa l’orientamento dell’immagine ma il giusto allineamento tra gli assi cartesiani di Geogebra e la scala graduata dell’immagine.
    ''')
    st.write(" ## Analisi dei risultati ottenuti \n ")
    st.write("### Osservazione 1")
    img_osservazione1 = Image.open('img//osservazione1.jpg')
    st.image(img_osservazione1,width=800)

    st.write("Ulteriori dati utilizzati per il calcolo: \n")
    img_datioss1 = Image.open('img//datioss1.jpg')
    st.image(img_datioss1,width=200)
    
    st.write("Rapporto $e/m$ ottenuto: \n")
    st.latex(r'\frac{e}{m} = \frac{2ydv_0^2}{x^2\Delta V} = 1,72*10^{11}\frac{C}{kg}')

    st.write("### Osservazione 2")
    
    img_osservazione2 = Image.open('img//osservazione2.jpg')
    st.image(img_osservazione2,width=800)

    st.write("Ulteriori dati utilizzati per il calcolo: \n")
    img_datioss2 = Image.open('img//datioss2.jpg')
    st.image(img_datioss2,width=200)

    st.write("Rapporto $e/m$ ottenuto: \n")
    st.latex(r'\frac{e}{m} = \frac{2ydv_0^2}{x^2\Delta V} = 1,90*10^{11}\frac{C}{kg}')

    st.write('''
    *In entrambe le osservazioni i valori di *x* e *y* utilizzati sono stati calcolati tramite l’equazione della traiettoria (linea di tendenza) uno come soluzione accettabile dell’equazione e l’altro come intercetta all’origine della parabola. Il valore di $d$ è invece stato calcolato facendo una media aritmetica di 3 misurazioni (virtuali) in modo da ottenere un valore più preciso ed esatto.*\n
    ''')
    st.write('''
    I risultati ottenuti sono comparabili ma non perfettamente coincidenti infatti si nota come il rapporto ottenuto dalla seconda osservazione, con d.d.p. di 500V sia maggiore di quello atteso e di quello ottenuto nella prima osservazione. Concludere che tale differenza sia dovuta ad errori sperimentali e alla possibile imprecisione nel raccogliere i dati in quanto con un potenziale minore applicato alle armature del condensatore la deflessione verticale risulta minore e pertanto l’errore, 
    nonostante sia simile a quello della prima osservazione, diventa percentualmente maggiore.\n

    In conclusione, si può affermare che i risultati ottenuti sono comparabili tra loro e con un livello di precisione accettabile per questo esperimento. Infatti, analizzando singolarmente ogni osservazione si nota che il coefficiente di determinazione $R^2$ delle linee di tendenza ottenute è prossimo a 1 (0,997 nel caso di d.d.p. 1000V e 0,996 nel caso si d.d.p. 500V)
     il cui significato è di esprimere la variabilità dei dati e quindi la correttezza del modello statistico utilizzato; quanto più esso tende ad 1 tanto più il modello utilizzato risulta preciso e affidabile. Tale precisione conferma quindi il comportamento del moto degli elettroni che ci si attendeva ossia quello di un moto simile a quello di un proiettile (come aveva osservato Thomson) e di tipo parabolico dovuto all’interazione degli elettroni, 
     in quanto carichi, con il campo elettrico prodotto dal condensatore. Entrambe le osservazioni hanno inoltre permesso di confermare non solo che gli elettroni siano particelle cariche ma anche che la loro carica è di segno negativo in quanto in entrambe le osservazioni la deflessione verticale avviene nella direzione della piastra positiva del condensatore. In fine, comparando i risultati dei rapporti $e/m$ ottenuti dalle due osservazioni è possibile anche confermare che questo rimane costante e quindi che indipendentemente dalle condizioni iniziali le particelle 
     osservate mantengono invariate la loro carica e massa che risultano quindi esprimibili 
    attraverso un rapporto definito e costante. 
    ''')
    st.write('''
    ## Confronto con dati reali \n
    Conoscendo ad oggi con elevata precisione la massa e la carica di un elettrone è possibile verificare la correttezza dei risultati ottenuti calcolando il rapporto con i dati reali:\n
    ''')
    st.latex(r'\frac{e}{m} = \frac{1,602*10^{-19}}{9,109*10^{-31}} = 1,759*10^{11}\frac{C}{kg}')
    st.write('''
    È possibile affermare che i rapporti ottenuti dall’esperimento siano corretti e anche piuttosto precisi, in particolare il rapporto ottenuto dalla prima osservazione.\n
    ''')
    st.write('''
    ## Conclusioni\n
    Dal punto di vista storico, grazie al suo esperimento, Thomson è riuscito a chiarire l’esistenza degli elettroni, e affermare che:
    -	Gli elettroni sono ovunque e sono più di mille volte più piccoli dell’atomo di idrogeno
    -	Gli oggetti assumono carica positiva poiché essi cedono elettroni, mentre gli oggetti negativi presentano un sovraffollamento di elettroni;
    -	La corrente è definita come il flusso di elettroni dal polo negativo al polo positivo;\n
    Thomson elaborò anche la teoria del “Plum Pudding”, la quale ipotizzava che gli elettroni negativi fossero immersi in una regione positiva. Questa ipotesi venne poi smentita successivamente da un allievo di Thomson, chiamato Hernest Rutherford, il quale conducendo esperimenti con le radiazioni confutò inavvertitamente l’ipotesi del maestro.\n
    Come si può evincere dall’analisi dei dati precedentemente elaborata, il rapporto fra la carica dell’elettrone e la sua massa rimane costante indipendentemente dalle condizioni iniziali, confermando i dati attesi.

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
             'lastra -', horizontalalignment='left')

    # plt.grid()
    # plt.legend()

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # calcolo del rapporto em
    y = traiettoria[1]
    x = traiettoria[0]
    em = (2*y[-1]*10**-2*v0*d/(ddp*(x[-1]*10**-2)**2))*10**-11

    st.write("### Risultato della simulazione\n")
    st.latex(r'e/m =   %s *10^{11} C/kg' %em.round(3))

if pagina =='CODICE SORGENTE':
    st.write('''
    In questa pagina è possibile consultare il codice sorgente di questa applicazione web, esso è inoltre scaricabile e modificabile attraverso il menù in alto a destra che rimanda alla repository GitHub di Tommaso Dognini.\n
    \n
    https://github.com/tommaso-dognini/simulazione_esperimentoThomson/blob/master/main.py 
    ''')
    st.write("Link per scaricare la relazione completa in formato pdf\n")