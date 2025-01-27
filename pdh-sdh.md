### 1. Le Multiplexage Temporel Non Synchronisé (PDH)  

Dans le PDH (**Plesiochronous Digital Hierarchy**), chaque flux de données dispose de sa propre horloge interne, ce qui signifie que les horloges des différents flux ne sont pas parfaitement synchronisées. Le terme "plésiochrone" signifie que ces horloges fonctionnent à des fréquences proches mais légèrement différentes.  

#### Problèmes du PDH :  
- **Désynchronisation entre les flux** :  
  Ces légères différences d'horloge compliquent le traitement des données, notamment lors de l'assemblage ou de l'extraction d'un flux spécifique.  

- **Ajout de bits de bourrage** :  
  Pour compenser les écarts dus à la désynchronisation, il est nécessaire d’ajouter des bits de bourrage (ou de remplissage) lorsque l’on combine plusieurs flux.  

- **Démultiplexage complexe** :  
  Pour accéder à un flux de données particulier, il faut démultiplexer tout le signal agrégé. Cela rend les opérations lentes, inefficaces et peu flexibles.  

#### Exemple :  
Imaginons que nous souhaitons assembler 4 flux de données fonctionnant à 2 Mbps chacun pour créer un signal unique de 8 Mbps.  
- Les horloges des flux ne sont pas parfaitement synchronisées.  
- Il faut alors insérer des bits de bourrage pour maintenir la cohérence du signal global.  
- Pour accéder à un flux de 2 Mbps, il est nécessaire de démultiplexer entièrement le signal 8 Mbps, ce qui complique les manipulations.  

---

### 2. Le Multiplexage Temporel Synchronisé (SDH)  

Avec le SDH (**Synchronous Digital Hierarchy**), tous les flux de données utilisent une horloge centrale unique et parfaitement synchronisée. Cela élimine les problèmes de désynchronisation et simplifie la gestion des flux de données.  

#### Avantages du SDH :  

1. **Synchronisation parfaite** :  
   - Tous les flux sont alignés grâce à l'utilisation d'une horloge centrale commune.  
   - Cela évite les désynchronisations et rend inutile l’ajout de bits de bourrage.  

2. **Accès direct aux flux spécifiques** :  
   - Grâce à l'alignement parfait des flux, un ADM (**Add-Drop Multiplexer**) peut insérer ou extraire un flux spécifique sans démultiplexer l’ensemble du signal.  
   - Cela rend le SDH beaucoup plus flexible, rapide et adapté aux besoins des réseaux modernes.  

3. **Débits standardisés** :  
   - SDH utilise des débits fixes et bien définis, tels que :  
     - **STM-1 (155 Mbps)**  
     - **STM-4 (622 Mbps)**  
     - **STM-16 (2,5 Gbps)**  
   - Ces standards facilitent l’interconnexion entre différents équipements et technologies de télécommunications.
   - Les **débits en PDH sont imbriqués les uns dans les autres**, ce qui rend leur extraction et leur gestion complexes
       - 2 Mbps (E1) : Niveau de base en Europe. C'est un canal regroupant 32 canaux vocaux de 64 kbps chacun (30 canaux pour la voix + 2 canaux de signalisation et synchronisation).
       - 8 Mbps (E2) : Agrégation de 4 liens E1.
       - 34 Mbps (E3) : Agrégation de 4 liens E2.
       - 140 Mbps (E4) : Agrégation de 4 liens E3.
