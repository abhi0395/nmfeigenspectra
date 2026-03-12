# Validation Tests

This directory contains pytest tests to validate the integrity and consistency of FITS files in the repository.

## Quick Start

Install test dependencies:
```bash
pip install -r test/requirements.txt
```

Run all tests:
```bash
pytest test/test_validation.py -v
```

## What Gets Tested

### File Naming

- Files follow the pattern: `SURVEY_z_zmin_zmax_(eigenspectra).fits`
- Redshift bounds are valid (zmin < zmax)

### FITS Structure

- Files can be opened without errors
- Contains at least 3 HDUs
- Required extensions: `EIGENVEC` and `REST_WAVE`
- Required header keywords: `METHOD`, `ZMIN`, `ZMAX`, `AUTHOR`, `LAMSTART`, `NORMSTAT`, `LAMEND`

### Data Integrity

- EIGENVEC is 2D, REST_WAVE is 1D
- Shapes are compatible (columns of EIGENVEC match length of REST_WAVE)
- No NaN or inf values in data arrays
- Redshift bounds in headers match the filename

### Documentation

- Each survey directory contains a `README.md`

## Running Specific Tests

```bash
# Test only naming conventions
pytest test_validation.py -v

```