from flask import Flask
import random
app = Flask(__name__)
lista_fatti = [
    "le persone possono passare troppo tempo sui social media e sui messenger, riducendo il tempo che trascorrono nel mondo reale. Inoltre, questo porta alla dipendenza da aggiornamenti costanti di notizie e messaggi",
    "le persone possono subire ricatti e ciberbullismo",
    "le persone possono diventare dipendenti dalli smartphone"
]
@app.route("/")
def ciao_mondo():
    return f"""<html>
<head>
    <title>PaperSite: il miglior sito di papere</title>
</head>
<body>
    <h1>le papere sono il miglior animale mai concepito nella storia dell'universo osservabile conosciuto</h1>
    <p>volete immmergervi in questo mondo paperoso?? (ovvio che si)</p>
    <h2>ecco perchè dovete farlo PER FORZA</h2>
             <ul>
                   <li>le papere sono carine</li>
                   <li>le papere sono belle</li>
                   <li>e ricordati di visitare spesso il sito per questo!</li>                   
             </ul>
    <h1>e che stai aspettando li? Vai ed esplora il nostro sito</h1>   
    <iframe width="110" height="200" src="https://www.myinstants.com/instant/mac-quack-83896/embed/" frameborder="0" scrolling="no"></iframe>
     <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6XKaHclHkoFkISbj79pCMniWyB_6C5gOrQg&s" alt="Image 1">
     <a href="/paperG">vedi belle foto!!!!!!!!</a>
     <a href="/paperD">scopri di più sul tuo animale preferito!!!!!!!!!!</a>
     <a href="/paperM">meme approvati dalla papercommunity</a>
</body>
</html>"""
@app.route("/paperG")
def ofgaf():
    return f"""
<img src="https://i.pinimg.com/236x/8a/60/f1/8a60f1cdde1419046905ee7b351635fb.jpg" alt="Image 2">
<img src="https://www.rivista20.com/wp-content/uploads/2023/08/papera-e-oca-760x466.jpeg" alt="Image 3">
<img src="https://media.gettyimages.com/id/157187144/it/foto/anatra-curiose.jpg?s=612x612&w=gi&k=20&c=KW88H2nuJwR2vyEMzRiQktihJdNJXevmWfSHXlrSUNY=" alt="Image 4"> 
<img src="https://st3.depositphotos.com/9880800/12928/i/450/depositphotos_129283178-stock-photo-domestic-ducks-on-green-grass.jpg" alt="Image 5">
<img src="https://preview.redd.it/cosa-ne-pensate-delle-papere-v0-im98nyv6ro1g1.jpeg?width=640&crop=smart&auto=webp&s=f06f75cce857fe503074df42314b18fd28c751a9" alt="Image 6">
<img src="https://www.shutterstock.com/image-photo/papere-che-sguazzano-nello-stagno-260nw-2572759961.jpg" alt="Image 7"> 
<img src="https://images.sbito.it/api/v1/sbt-ads-images-pro/images/e4/e41a15b6-2d07-4c43-badd-a6c6debd4ac0?rule=gallery-desktop-2x-auto" alt="Image 8">
<img src="https://static8.depositphotos.com/1004032/874/i/450/depositphotos_8747074-stock-photo-duck-male-on-lake-shore.jpg" alt="Image 9">
"""
@app.route("/paperD")
def hgso():
    return f"""
<h3>Anatra (o anitra, dal latino anas) è il nome comune di un importante numero di uccelli anseriformi, generalmente migratori, appartenenti alla famiglia degli anatidi.

Si tratta di una definizione priva di valore sistematico, in quanto raggruppa specie appartenenti a svariati generi e sottofamiglie diverse; in linea generale il termine "anatra" si applica alle specie di Anseriformi di dimensioni inferiori e con spiccato dimorfismo sessuale, in contrapposizione ad oca, che definisce al contrario specie di grande mole e prive di dimorfismo.

Abitudini
Le anatre hanno abitudini diverse a seconda della specie, ma sono, assai più delle oche, legate all'acqua; tutte le specie sono infatti ottime nuotatrici. Gli ambienti più frequentati dalle anatre sono gli stagni e i laghi, ma possono trovarsi anche lungo le coste marine, i piccoli corsi d'acqua o addirittura le fontane e i laghetti artificiali dei parchi urbani. Alcune specie sono appositamente allevate nei giardini quali uccelli ornamentali, in virtù della colorazione variopinta, soprattutto dei maschi.

Le specie più spiccatamente acquatiche non hanno un buon coordinamento dei movimenti sulla terraferma; altre si trovano invece a proprio agio in entrambi gli ambienti.[1]


Anatre nel Tevere, 11 settembre 1992
Alimentazione
Anche il nutrimento delle anatre dipende dalla specie e dalle abitudini: quelle che vivono negli stagni hanno generalmente un'alimentazione prevalentemente vegetariana e raccolgono il cibo sulla terraferma o poco al disotto della superficie dell'acqua, immergendo solo la testa, il collo e parte del corpo, restando con il posteriore in posizione verticale; quelle marine o che abitano in laghi estesi e profondi sono invece tuffatrici e si nutrono anche di pesci. Le specie esclusivamente piscivore hanno becchi dal bordo seghettato, atti a trattenere la preda.

Tassonomia
L'anatra non è una specie monofiletica. La maggior parte delle razze deriva infatti dal germano reale, ma esistono varietà che discendono invece dall'anatra muta; molti incroci industriali utilizzati per la produzione di carne e di foie gras sono incroci sterili tra le due specie precedenti.

La sottofamiglia dei Tadornini si colloca a metà strada tra anatre e oche: gli uccelli che vi appartengono hanno infatti, come le anatre, colori brillanti e abitudini strettamente acquatiche, ma hanno grande mole e dimorfismo sessuale molto ridotto (vedasi volpoca e casarca).

Distribuzione
Le varie specie di anatre, anche grazie alle abitudini migratorie, abitano molte aree del globo.

Europa e area mediterranea
In Europa e nell'area mediterranea si possono incontrare le seguenti specie:

l'alzavola (Anas crecca)
la canapiglia (Mareca strepera)
il codone (Anas acuta)
il fischione (Mareca penelope)
il germano reale (Anas platyrhynchos)
la marzaiola (Spatula querquedula)
il mestolone (Spatula clypeata)
la moretta (Aythya fuligula)
la moretta grigia (Aythya marila)
la moretta tabaccata (Aythya nyroca)
il moriglione (Aythya ferina)
lo smergo maggiore (Mergus merganser)
lo smergo minore (Mergus serrator)
l'anatra muta (Cairina Moschata)
Asia
Tra le specie presenti in Asia:

l'alzavola asiatica (Sibirionetta formosa)
l'anatra mandarina (Aix galericulata)
la moretta dal collare (Aythya collaris)
Nord America
Tra le specie presenti in Nord America:

il fischione americano (Mareca americana)
la marzaiola americana (Spatula discors)

Due Anas platyrhynchos Anatre - Puerto Ayora- Galápagos.

Testa di anatra comune
Le anatre nella cultura

Un'anatra mandarina

Dendrocygna bicolor
L'anatra è un animale piuttosto comune nella letteratura e nell'arte, spesso antropomorfizzato. Fra gli esempi più celebri possiamo ricordare:

le rappresentazioni sia plastiche sia disegnative testimoniate nella protostoria europea, tanto nella ceramica quanto nella bronzistica; tra le raffigurazioni più complesse della semplice paperella incisa o modellata, si ricordano gli schemi della cosiddetta barca solare e delle due teste ("protomi") contrapposte;
la celebre fiaba Il brutto anatroccolo di Hans Christian Andersen (nella quale tuttavia, nonostante il titolo, il protagonista non è un'anatra perché si scoprirà essere un cigno);
dalla fiaba "Il brutto anatroccolo", in spagnolo "El patito feo", nasce la telenovela argentina chiamata Il mondo di Patty in Italia;
la fiaba musicale Pierino e il lupo di Sergei Prokofiev, dove l'anatra è rappresentata dall'oboe.
numerosi personaggi di Walt Disney, tra cui Paperino, Qui, Quo, Qua, Paperina e Paperon de' Paperoni;
uno dei personaggi più amati dei cartoni animati Warner Brothers, Daffy Duck;
la mascotte dell'università dell'Oregon.
Gastronomia
La carne di anatra è molto apprezzata come alimento quindi il volatile è soggetto ad allevamento per scopo gastronomico ovunque nel mondo. Particolarmente preferita in Francia: è famosa la cottura di ali, cosce e petto d'anatra nel grasso del volatile stesso, piatto noto come confit de canard, così com'è celebre la preparazione culinaria del petto di anatra ossia il magret nonché del fegato ossia il foie gras. Altre pietanze preparate con la carne di questo uccello sono: anatra alla pressa, anatra all'arancia, anatra laccata alla pechinese, turducken.


Contribuisci a migliorarla integrando se possibile le informazioni all'interno dei paragrafi della voce e rimuovendo quelle inappropriate.
Per molto tempo si è creduto che il verso dell'anatra non producesse l'eco. Tale fatto è stato smentito da studi specifici che hanno dimostrato che il verso produce un'eco come qualunque altro suono, ma che tale eco è solitamente difficile da rilevare a causa delle sue peculiarità timbriche.[2]
L'anatra, per tenersi le uniche parti del corpo scoperte (becco e zampe) al caldo, le inserisce sotto l'ala.
  </h3>
"""
@app.route("/paperM")
def fdsu():
    return f"""
<iframe width="110" height="200" src="https://www.myinstants.com/instant/fahhhhhhhhhhhhhh-3525/embed/" frameborder="0" scrolling="no"></iframe>
<iframe width="110" height="200" src="https://www.myinstants.com/instant/vine-boom-sound-70972/embed/" frameborder="0" scrolling="no"></iframe>
<iframe width="110" height="200" src="https://www.myinstants.com/instant/fluffing-a-duck-26903/embed/" frameborder="0" scrolling="no"></iframe>

"""
app.run(debug=True)
