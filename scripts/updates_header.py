from astropy.io import fits
import numpy as np
import os
def update_fits_header(zmin, zmax):

    filename = f'../data/DR14_QSO_NMF_zQSO_%03d_%03d_basis.fits'%(zmin*100, zmax*100)
    # Open the FITS file in read-write mode
    with fits.open(f'{filename}', mode='update') as hdul:
        # Access the primary header (HDU 0)
        hdr = hdul[0].header

        # Add or update the key-value pair
        hdr['AUTHOR'] = ('A.Anand', 'Data Author')
        hdr['QSOVAC'] = ('SDSS DR14', 'QSO Data')
        hdr['EIGFIT'] = ('NMF', 'Eigenspectra fit method: Zhu NMF')
        hdr['ZMIN'] = (zmin, 'minimum redshift for NMF fit')
        hdr['ZMAX'] = (zmax, 'maximum redshift for NMF fit')

        # Save changes to file
        hdul.flush()

        # Update or add a header key in the primary HDU (index 0)

    print(f'{filename} HDU0 updated..\n')

def clean_fits_structure(zmin, zmax):

    filename = f'../data/DR14_QSO_NMF_zQSO_%03d_%03d_basis.fits'%(zmin*100, zmax*100)
    temp_file  = f'../data/DR14_QSO_NMF_zQSO_%03d_%03d_basis_clean.fits'%(zmin*100, zmax*100)
    # Open original FITS file
    with fits.open(filename) as hdul:
        # Preserve primary header as-is
        primary_hdu = fits.PrimaryHDU(header=hdul[0].header)

        # Extract data
        data = hdul[1].data
        eigenvec = np.array(data['EIGENVEC'])     # shape (7171, 12)
        rest_wave = np.array(data['REST_WAVE'])   # shape (7171,)

        # Create Image HDUs for each array
        eigenvec_hdu = fits.ImageHDU(data=eigenvec, name='EIGENVEC')
        rest_wave_hdu = fits.ImageHDU(data=rest_wave, name='REST_WAVE')

        # Create new HDUList and save to new file
        hdul_new = fits.HDUList([primary_hdu, eigenvec_hdu, rest_wave_hdu])
        hdul_new.writeto(f'{temp_file}', overwrite=True)

    # Step 4: Delete original file
    os.remove(filename)

    # Step 5: Rename the cleaned file
    os.rename(temp_file, filename)

    print(f"{filename} successfully updated and cleaned.")

if __name__=='__main__':

    zmins = [0.0, 0.4, 0.8, 2.0]
    zmaxs = [1.0, 1.8, 2.8, 4.8]

    for zmin, zmax in zip(zmins, zmaxs):
        #update_fits_header(zmin, zmax)
        clean_fits_structure(zmin, zmax)
