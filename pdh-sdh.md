| **Aspect**                      | **PDH (Plesiochronous Digital Hierarchy)**                          | **SDH (Synchronous Digital Hierarchy)**                          |
|----------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------|
| **Synchronisation**              | Chaque flux a sa propre horloge, ce qui entraîne de légères différences (désynchronisation). | Tous les flux partagent une horloge centrale parfaitement synchronisée. |
| **Gestion des flux**             | Complexe : il faut démultiplexer tout le signal pour extraire un flux spécifique. | Simple : accès direct à un flux spécifique grâce à l'alignement parfait des flux. |
| **Bits de bourrage**             | Nécessaire pour compenser les écarts entre les horloges.            | Inutile, car tous les flux sont synchronisés.                   |
| **Débits disponibles**           | Non standardisés, imbriqués : 2 Mbps (E1), 8 Mbps (E2), 34 Mbps (E3), 140 Mbps (E4). | Standardisés : STM-1 (155 Mbps), STM-4 (622 Mbps), STM-16 (2,5 Gbps). |
| **Flexibilité**                  | Limitée : manipulations complexes et peu adaptées aux besoins modernes. | Très flexible : insertion et extraction rapides des flux.       |
| **Complexité du matériel**       | Plus complexe en raison du démultiplexage à chaque niveau.          | Matériel simplifié grâce à la synchronisation globale.          |
| **Applications principales**     | Anciennes infrastructures de télécommunications.                   | Réseaux modernes et interconnexion internationale.              |
| **Interconnexion des équipements** | Difficile à cause des débits non standardisés.                     | Facile grâce aux débits standardisés dans le monde entier.       |
