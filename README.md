# Conformational Landscape of Cytochrome P450 Reductase Interactions
This repository contains data generated and used in the publication [Conformational Landscape of Cytochrome P450 Reductase Interactions](https://www.doi.org/10.3390/ijms22031023 "DOI: 10.3390/ijms22031023").

The repository contains the following data:

- cpr contains data of the CPR (without redox partner)
  - cpr\_height contains raw data used to plot the distance between the CPR and the membrane
  - cpr\_inc\_salt contains analysis files of the three replica performed with increased ionic strength
  - cpr\_r243a contains analysis files of the three replica performed with Arg243 mutated to Ala
  - gly\_flip contains csv files used to plot the psi and phi angles of Gly141
  - other contains raw data to plot the radius of gyration and interflavin distance
  - rmsd contains the raw RMSDs of the simulations with varying redox states
  - rmsf contains the raw RMSFs of the simulations with varying redox states

- cyp\_cpr\_complex contains data of the CYP2D6-CPR complex
  - apo\_1 to apo\_5 contain data of the unliganded complex (five replica)
  - paracetamol1 to paracetamol5 contain data of the complex with paracetamol bound to the binding site of CYP2D6 (five replica)
  - promethazin1 to promethazin5 contain data of the complex with promethazine bound to the binding site of CYP2D6 (five replica)
  - tramadol1 to tramadol5 contain data of the complex with tramadol bound to the binding site of CYP2D6 (five replica)
  - Note: Data regarding tunnel analysis are not included due to a size restriction of the repository. They can be requested from the authors.

- metadynamics contains analysis files of the well-tempered metadynamics simulation

Note: Some directories are called "SID" or "SEA". This stands for Schrödinger's Simulation Interaction Diagram and Simulation Event Analysis tools, respectively.
