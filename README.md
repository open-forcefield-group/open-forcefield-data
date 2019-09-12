# open-forcefield-data
Datasets for open forcefield parameterization and development

# General protocol for filtering ThermoML data for pure solvent data
ThermoML data compiled and filtered using ThermoPyL tool developed by Chodera Lab @ MSKCC (https://github.com/choderalab/thermopyl)

FILTER PROCEDURE:

1. Pull full ThermoML archive

2. Discard known erroneous data (j.fluid.2013.12.014 the only one I know of now)

3. Define properties of interest to pass filter

4. Allow only C, O and H atoms to pass

5. Generate SMILES formulae from component names (NIH CirPy module)

6. Apply filter for "=" and "#" to SMILES formulae (get rid of double and triple bonding)

7. Generate CAS from component names (CirPy)

8. Apply temperature and pressure filters (250 K - 400 K and 1 atm - 1000 atm)

9. Keep only liquid phase data points

10. Separate final large dataframe into subframes by property of interest
  a. Remove data with no associated uncertainties from subframes

11. Generate counts by component and journal article for all dataframes

12. Save everything as separate text .csv


# Energetic data for model systems

## Toy dataset for alkanes, alcohols, and ethers

Christopher I. Bayly developed a toy dataset of potential molecules of interest which is deposited in the "Model Systems" directory in the "AlkEthOH_distrib" subdirectory. Construction of this set is described in the README.txt there, which should be converted to md.

# Utilize All Parameters

This is an attempt to create a set of molecules that use all the parameters in
the smirnoff99Frosst force field.

# Construction of benchmarks

In the `construct_benchmarks` directory we are experimenting with filtering strategies to construct benchmark/test sets that are suitable given the chemistry we have fitted on.
