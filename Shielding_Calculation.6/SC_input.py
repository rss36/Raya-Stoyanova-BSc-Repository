! B3LYP pcSseg-3 NMR CPCM DefGrid3

%pal
  nprocs 4
end

%maxcore 3000

%cpcm
  epsilon 78.30
  refrac  1.3330
end

* xyz 0 1
  C         -3.1349       -0.2637       -1.2086
  C         -3.2135        0.0672        0.2702
  [...coordinates for all atoms...]
*

%eprnmr
  Nuclei = all F { shift }
end