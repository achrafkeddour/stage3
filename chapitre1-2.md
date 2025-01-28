
### **Chapitre 1 : Analyse des besoins**
1. **Présentation du projet** :  
   - Décrire l’objectif général de ton simulateur de réseau IP/MPLS (visualisation des routes, labels, tests de performance, etc.).  
   - Identifier les acteurs principaux :  
     - **Administrateur réseau** : Configure le réseau et simule les pannes.  
     - **Système** : Gère les routes, les labels, et les métriques réseau.  

2. **Fonctionnalités principales** :  
   - Gestion des nœuds et des liens du réseau.  
   - Simulation des routes MPLS avec attribution de labels.  
   - Visualisation graphique des résultats.  
   - Simulation de pannes et mesure des performances.  

3. **Contraintes** :  
   - Interface minimaliste en HTML/CSS (pas de JavaScript).  
   - Backend en Flask avec des bibliothèques réseau Python.  
   - Système extensible pour intégrer des bibliothèques comme GNS3 à l’avenir.  

---

### **Chapitre 2 : Conception du logiciel**
#### **2.1 Langage de modélisation UML**
- **Introduction** :  
  Définir ce qu’est un langage de modélisation (outil pour représenter les systèmes informatiques).  
  Expliquer pourquoi UML est un standard efficace (reconnu, structuré, flexible).  

- **UML et ses types de diagrammes** :  
  Parler des diagrammes structurels (comme le diagramme de classe) et comportementaux (cas d’utilisation, séquences, activités).  

---

#### **2.2 Diagrammes utilisés**
1. **Diagramme de cas d’utilisation** :  
   Décrire les interactions principales entre les acteurs (administrateur réseau) et le système (configuration, simulation, visualisation).  

2. **Diagramme de classes** :  
   Représenter les classes principales :  
   - **Node** (Nœud) : ID, nom, état.  
   - **Link** (Lien) : Bande passante, latence, état (actif/inactif).  
   - **MPLSRoute** : Labels, chemin, métriques.  

3. **Diagramme de séquence** :  
   Montrer comment un administrateur configure un réseau ou lance une simulation.  

4. **Diagramme d’activité** :  
   Décrire les étapes du processus de simulation (ex. : création des nœuds, calcul des routes, visualisation des résultats).  

---

#### **2.3 Conception avec diagrammes**
- Inclure les diagrammes UML pour chaque section décrite ci-dessus.  
- Ajouter des explications pour les plus complexes (si nécessaire).  
