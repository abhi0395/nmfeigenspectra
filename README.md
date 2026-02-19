# Non-negative Matrix Factorization (NMF) Eigenspectra for Quasar Continuum Modeling

This repository provides NMF-based quasar eigenspectra that can be used to model and reconstruct quasar continua in large spectroscopic surveys.

The methodology used to construct these eigenvectors is described in:

- **Anand et al. (2021)**  
  https://arxiv.org/abs/2103.15842  

If you use these eigenspectra in your research, please cite this paper. You should also cite the original NMF-based quasar spectral decomposition work:

- **Zhu (2016)**  
  https://arxiv.org/abs/1612.06037  

---

## Installation

To download the eigenspectra files, clone the repository:

```bash
git clone https://github.com/abhi0395/nmfeigenspectra.git
```

---

## Available Data

The current repository currently hosts:

- **SDSS DR14-based quasar NMF eigenspectra**

These eigenspectra can be used to construct continua for SDSS-like quasar spectra (e.g., DESI).

---

## Future Releases

In future updates, the repository will also include NMF eigenspectra built from:

- DESI DR1 / DR2  
- 4MOST  
- WEAVE  

---

## File Structure

Each survey has its own directory structure. Please refer to:

`${survey}/README.md`

for details on file naming conventions, redshift binning, and data formats.

---

## Acknowledgment

If you use these eigenspectra in your research, please cite the relevant papers listed above.

Thank you for your interest.

Abhijeet Anand  
IUCAA Pune