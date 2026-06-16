# Mapping-of-Organelle-Heterogeneity
This repository contains the data and python notebooks to recapitulate the results from our Day et al. 2026 paper.

System Requirements:
All scripts are python 3 code implemented in jupyter notebooks. We use windows with anaconda or miniconda.
For training the variational autoencoder, we worked in google colab and used an A100 GPU for the training task.

These scripts are all self contained. Your conda environment needs to have all of the libraries listed at the top of the script.
We used mamba for library installations (because it's faster than conda installs) and separated the work into different environments for the basic analysis and machine learning work. For any places where a csv file needs to be read in, make sure that the file location is set correctly based on where you downloaded the data and scripts.

The data for Figures 3 and 4 could not be loaded into this Github Repo. Instead, they can be found in our Dryad repository with the raw data from this work.
