# ZtZProject - Chips & Circuits
### Project door Ziggy, Thomas en Zoe
### De case
Onze case is Chips & Circuits. Er zijn verschillende chips waarop verschillende gates te vinden zijn. De gates op een chip moeten verbonden worden via kabels. De gates liggen op een rooster. De verbindingen tussen gates die gelegd moeten worden heten "nets". Elke chip heeft verschillende lijsten met verbindingen die gelegd moeten worden tussen gates, "netlists". Elke chip heeft ook een lijst met daarin de coördinaten van elke gate. 

De kabels mogen alleen over roostersegmenten heenlopen, ze mogen dus niet schuin. Kabels mogen niet over elkaar heenlopen. Een kabel mag wel een andere kabel direct kruizen, maar dan komt er kortsluiting. Kortsluiting mag, maar het kost 300 kabellengte en moet dus vermeden worden. Als een kabel een andere kabel direct kruist, noem je dit een intersection. Kabels mogen wel omhoog en naar beneden gaan en in een hogere of lagere laag verder lopen. Dit kost dan wel meer kabellengte. Het doel is om voor elke netlist een zo kort mogelijke totale kabellengte te krijgen. 

### De algoritmen
**Random**
Wij zijn begonnen met het maken van een random algoritme. Dit algoritme kiest random een kant om op te gaan om bij de gate te komen waar hij heen moet. Zo ontstaat er random een kabel tussen twee gates. Dit doet hij voor alle nets in de netlist. Wij hebben ervoor gekozen om dit alleen in de x en de y richting te doen. De verschillende lagen in de z richting zijn dus nog niet geïmplementeerd. Ook intersections zijn hierbij nog niet geïmplementeerd. Als de kabel de verkeerde kant op gaat en vast komt te zitten, omdat hij niet langs andere kabels kan, loopt het algoritme vast. Het zal dan opnieuw beginnen met het proberen van een oplossing zoeken. 

**Greedy/random**
Het greedy/random algoritme probeert in eerste instantie de best mogelijke stappen (greedy) te zetten om bij de juiste gate te komen. Als hij vast komt te zitten, zal hij proberen een random kant op te gaan om verder te komen. Als dit ook niet lukt zal hij proberen een intersection te maken. Als dat ook niet lukt dan stopt het programma. 

**Breadth first**


**Breadth first extended**


### Reproductie
Om de algoritmen aan te roepen kan je onze main.py gebruiken. Door python main.py --help als commando in te typen, zie je precies welke commando's je kan geven om resultaten te verkrijgen. Hier ook nog een kleine samenvatting:

--algorithm + het algoritme dat je wil aanroepen. Type greedy voor greedy/random, random, type breadth voor het breadth first algoritme en type breadthext voor het extended breath first algoritme. 
--chip + de chip die je wil proberen op te lossen. Dit kan een chip zijn tussen de 0 en 2. Default staat hij op chip 0.
--netlist + de netlist die je wil proberen op te lossen. Dit kan een netlist zijn tussen de 1 en 3. Default staat hij op 1.
--iteration + de hoeveelheid oplossingen die je wil genereren. Default laat hij je 1 oplossing zien.
--sorted + True of False, of je wil dat de netlist gesorteerd is of niet. Default staat sorted op False. 

Een voorbeeld:
python main.py --algorithm greedy --chip 1 -- netlist 1 --iteration 2 --sorted True

Dit zal twee oplossingen van chip 1 netlist 1 voor greedy proberen te zoeken met een gesorteerde netlist.



