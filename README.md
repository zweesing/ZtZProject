# ZtZProject - Chips & Circuits
### Project door Ziggy, Thomas en Zoe
### De case
Onze case is Chips & Circuits. Er zijn verschillende chips waarop verschillende gates te vinden zijn. De gates op een chip moeten verbonden worden via kabels. De gates liggen op een rooster. De verbindingen tussen gates die gelegd moeten worden heten "nets". Elke chip heeft verschillende lijsten met verbindingen die gelegd moeten worden tussen gates, "netlists". Elke chip heeft ook een lijst met daarin de coördinaten van elke gate. 

De kabels mogen alleen over roostersegmenten heenlopen, ze mogen dus niet schuin. Kabels mogen niet over elkaar heenlopen. Een kabel mag wel een andere kabel direct kruizen, maar dan komt er kortsluiting. Kortsluiting mag, maar het kost 300 kabellengte en moet dus vermeden worden. Als een kabel een andere kabel direct kruist, noem je dit een intersection. Kabels mogen wel omhoog en naar beneden gaan en in een hogere of lagere laag verder lopen. Dit kost dan wel meer kabellengte. Het doel is om voor elke netlist een zo kort mogelijke totale kabellengte te krijgen. 

### De algoritmen
**Random**
Wij zijn begonnen met het maken van een random algoritme. Dit algoritme kiest random een kant om op te gaan om bij de gate te komen waar hij heen moet. Zo ontstaat er random een kabel tussen twee gates. Dit doet hij voor alle nets in de netlist. Wij hebben ervoor gekozen om dit alleen in de x en de y richting te doen. De verschillende lagen in de z richting zijn dus nog niet geïmplementeerd. Ook intersections zijn hierbij nog niet geïmplementeerd. Als de kabel de verkeerde kant op gaat en vast komt te zitten, omdat hij niet langs andere kabels kan, loopt het algoritme vast. Het zal dan opnieuw beginnen met het proberen van een oplossing zoeken. 

**Greedy/random**


**Breadth first**


#### Reproductie




