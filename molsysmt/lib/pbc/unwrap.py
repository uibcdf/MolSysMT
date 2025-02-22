import numba as nb
import numpy as np
from .box_is_orthogonal import box_is_orthogonal_single_structure
from ..make_numba_signature import make_numba_signature
from ..math import inverse_matrix_3x3, dot_product

arguments=[nb.float64[:,:,:], # coordinates
           nb.float64[:,:,:], # box
          ]
output=None
@nb.njit(make_numba_signature(arguments, output), cache=True)
def unwrap(coordinates, box):

    n_structures, n_atoms = coordinates.shape[:-1]

    orthogonal = box_is_orthogonal_single_structure(box[0,:,:])

    if orthogonal:

        for ii in range(n_structures-1):
            tmp_box=np.diag(box[ii,:,:])
            for jj in range(n_atoms):
                delta = coordinates[ii+1,jj,:]-coordinates[ii,jj,:]
                delta[0]=delta[0]-tmp_box[0]*round(delta[0]/tmp_box[0])
                delta[1]=delta[1]-tmp_box[1]*round(delta[1]/tmp_box[1])
                delta[2]=delta[2]-tmp_box[2]*round(delta[2]/tmp_box[2])
                coordinates[ii+1,jj,:]=coordinates[ii,jj,:]+delta

    else:

        vaux = np.empty((3), dtype=float)

        for ii in range(n_structures-1):
            tmp_box=box[ii,:,:]
            tmp_inv_box=inverse_matrix_3x3(tmp_box)
            for jj in range(n_atoms):
                delta = coordinates[ii+1,jj,:]-coordinates[ii,jj,:]
                vaux[0]=tmp_inv_box[0,0]*delta[0]+tmp_inv_box[1,0]*delta[1]+tmp_inv_box[2,0]*delta[2]
                vaux[1]=                              tmp_inv_box[1,1]*delta[1]+tmp_inv_box[2,1]*delta[2]
                vaux[2]=                                                            tmp_inv_box[2,2]*delta[2]
                vaux[0]=vaux[0]-round(vaux[0])
                vaux[1]=vaux[1]-round(vaux[1])
                vaux[2]=vaux[2]-round(vaux[2])
                delta[0]=tmp_box[0,0]*vaux[0]+tmp_box[1,0]*vaux[1]+tmp_box[2,0]*vaux[2]
                delta[1]=                     tmp_box[1,1]*vaux[1]+tmp_box[2,1]*vaux[2]
                delta[2]=                                          tmp_box[2,2]*vaux[2]
                vmin=delta
                dmin=dot_product(delta,delta)
                for kk in [-1,0,1]:
                    vaux=delta+ii*tmp_box[0,:]
                    for ll in [-1,0,1]:
                        vaux2=vaux+ll*tmp_box[1,:]
                        for mm in [-1,0,1]:
                            vaux3=vaux2[:]+mm*tmp_box[2,:]
                            dd=dot_product(vaux3,vaux3)
                            if dmin>dd:
                                vmin=vaux3
                                dmin=dd
                coordinates[ii+1,jj,:]=coordinates[ii,jj,:]+delta

    pass

