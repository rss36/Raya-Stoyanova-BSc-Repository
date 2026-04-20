# Raya-Stoyanova-BSc-Repository
Computational Data for BSc

This repository holds the computational data for the BSc dissertation, *Investigating ¹⁹F NMR Tags for Protein Conformational Changes* (University of Edinburgh, 2026, supervised by Dr Christopher Coxon).

Full methods are in Section 4.3 of the dissertation. This is just a short guide navigation guide.

The folders are numbered by pipeline step:

- `S-ethyl_Model_Co-ordinates.1` — cartesian co-ordinates of starting structures 
- `CREST_Conformational_Sampling.3` — conformer generation scripts, and relevant cartesian co-ordinates and energies
- `Conformational_Filtering.4` — script for filtering conformers by energy and population, and resulting ensemble
- `Geometry_Optimisation.5` — DFT geometry optimisation and frequency check scripts, raw output data, cartesian co-ordinates of final structures, and of properties summary.
- `Shielding_Calculation.6` — scripts for ¹⁹F NMR shielding calculations, raw output values, and summary of data.
- `Boltzmann_Averaging.7` — Results for boltzmann averaging of shieldings
- `Experimental_Validation.8` — comparison with experimental shifts

Model numbers (31 to 38) and solvent group numbers (G1 to G6) are defined in the dissertation appendix.
