# ==========================================
# Code created by Leandro Marques at 12/2018
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to assembly global matrices

# ------------------------------------------------------------------------------
# Use:
# Kxx, Kxy, Kyx, Kyy, K, M, MLump, Gx, Gy = 
# assembly.Linear2D(mesh.GL, mesh.npoints, mesh.nelem, mesh.IEN, mesh.x, mesh.y)
# ------------------------------------------------------------------------------

import sys
import numpy as np
import gaussianQuadrature
import scipy.sparse as sps
from tqdm import tqdm



def Element1D(_polynomial_option, _GL, _npoints, _nelem, _IEN, _x, _GAUSSPOINTS):
 K = sps.lil_matrix((_npoints,_npoints), dtype = float)
 M = sps.lil_matrix((_npoints,_npoints), dtype = float)
 G = sps.lil_matrix((_npoints,_npoints), dtype = float)
 
 element1D = gaussianQuadrature.Element1D(_x, _IEN, _GAUSSPOINTS)
 
 if _polynomial_option == 1:
  polynomial_order = 'Linear Element'
  
  for e in tqdm(range(0, _nelem)):
   element1D.linear(e)

   for i in range(0,_GL): 
    ii = _IEN[e][i]
  
    for j in range(0,_GL):
     jj = _IEN[e][j]

     K[ii,jj] += element1D.kx[i][j]
     M[ii,jj] += element1D.mass[i][j]
     G[ii,jj] += element1D.gx[i][j]


 elif _polynomial_option == 2:
  polynomial_order = 'Quadratic Element'

  for e in tqdm(range(0, _nelem)):
   element1D.quadratic(e)

   for i in range(0,_GL): 
    ii = _IEN[e][i]
  
    for j in range(0,_GL):
     jj = _IEN[e][j]

     K[ii,jj] += element1D.kx[i][j]
     M[ii,jj] += element1D.mass[i][j]
     G[ii,jj] += element1D.gx[i][j]



 else:
  print ""
  print " Error: Element type not found"
  print ""
  sys.exit()


 return K, M, G, polynomial_order

 



def Element2D(_simulation_option, _polynomial_option, _GL, _npoints, _nelem, _IEN, _x, _y, _GAUSSPOINTS):

 Kxx = sps.lil_matrix((_npoints,_npoints), dtype = float)
 Kxy = sps.lil_matrix((_npoints,_npoints), dtype = float)
 Kyx = sps.lil_matrix((_npoints,_npoints), dtype = float)
 Kyy = sps.lil_matrix((_npoints,_npoints), dtype = float)
 K = sps.lil_matrix((_npoints,_npoints), dtype = float)
 M = sps.lil_matrix((_npoints,_npoints), dtype = float)
 MLump = sps.lil_matrix((_npoints,_npoints), dtype = float)
 Gx = sps.lil_matrix((_npoints,_npoints), dtype = float)
 Gy = sps.lil_matrix((_npoints,_npoints), dtype = float)


 element2D = gaussianQuadrature.Element2D(_x, _y, _IEN, _GAUSSPOINTS)

 if _simulation_option == 1:
  if _polynomial_option == 1:
   polynomial_order = 'Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.linear(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 2:
   polynomial_order = 'Mini Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.mini(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
 
  elif _polynomial_option == 3:
   polynomial_order = 'Quadratic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.quadratic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 4:
   polynomial_order = 'Cubic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.cubic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]

 
  elif _polynomial_option == 0:
   polynomial_order = 'Analytic Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.analytic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
 
  else:
   print ""
   print " Error: Element type not found"
   print ""
   sys.exit()


 #Debug
 elif _simulation_option == 0:
  polynomial_order = 'Debug'

  Kxx = Kxx*1.0 
  Kxy = Kxy*1.0
  Kyx = Kyx*1.0
  Kyy = Kyy*1.0
  K =   K*1.0
  M =   M*1.0
  MLump = MLump*1.0
  Gx =  Gx*1.0 
  Gy =  Gy*1.0 
 
 return Kxx, Kxy, Kyx, Kyy, K, M, MLump, Gx, Gy, polynomial_order


#obsolete
def Mini_NS2D(_GLV, _GLP, _NV, _NP, _nelem, _IEN, _x, _y):
 
 K = sps.lil_matrix((2*_NV,2*_NV), dtype = float)
 M = sps.lil_matrix((2*_NV,2*_NV), dtype = float)
 MLump = sps.lil_matrix((2*_NV,2*_NV), dtype = float)
 Gx = sps.lil_matrix((_NV,_NP), dtype = float)
 Gy = sps.lil_matrix((_NV,_NP), dtype = float)
 Dx = sps.lil_matrix((_NP,_NV), dtype = float)
 Dy = sps.lil_matrix((_NP,_NV), dtype = float)


 mini = gaussianQuadrature.Mini(_x, _y, _IEN)

 for e in tqdm(range(0, _nelem)):
  mini.numerical(e)

  for i in range(0, _GLV): 
   ii = _IEN[e][i]
  
   for j in range(0, _GLV):
    jj = _IEN[e][j]

    #MSC 2007 pag.84
    K[ii,jj] += 2.0*mini.kxx[i][j] + mini.kyy[i][j] #K11
    K[ii,jj + _NV] += mini.kxy[i][j] #K12
    K[ii + _NV,jj] += mini.kyx[i][j] #K21
    K[ii + _NV,jj + _NV] += mini.kxx[i][j] + 2.0*mini.kyy[i][j] #K22
   
    M[ii,jj] += mini.mass[i][j]
    M[ii + _NV,jj + _NV] += mini.mass[i][j]
    
    MLump[ii,ii] += mini.mass[i][j]
    MLump[ii + _NV,ii + _NV] += mini.mass[i][j]


   for k in range(0, _GLP):
    kk = _IEN[e][k]

    G[ii,kk] += mini.gx[i][k]
    G[ii + _NV,kk] += mini.gy[i][k]

    D[kk,ii] += mini.dx[k][i]
    D[kk,ii + _NV] += mini.dy[k][i]


 return K, M, MLump, G, D




def NS2D(_simulation_option, _polynomial_option, _velocityFD, _pressureFD, _numNodes, _numVerts, _numElements, _IEN, _x, _y, _GAUSSPOINTS):

 Kxx = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 Kxy = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 Kyx = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 Kyy = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 K = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 M = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 MLump = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 Gx = sps.lil_matrix((_numNodes,_numVerts), dtype = float)
 Gy = sps.lil_matrix((_numNodes,_numVerts), dtype = float)

 KxxMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 KxyMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 KyxMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 KyyMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 KMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 MMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 MLumpMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 GxMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 GyMini = sps.lil_matrix((_numNodes,_numNodes), dtype = float)

 element2D = gaussianQuadrature.Element2D(_x, _y, _IEN, _GAUSSPOINTS)

 #obsolete
 if _simulation_option == 1:
  if _polynomial_option == 1:
   polynomial_order = 'Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.linear(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]

   
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 2:
   polynomial_order = 'Mini Element'
 
   for e in tqdm(range(0, _numElements)):
    element2D.mini(e)         # gaussian quadrature
    #element2D.analyticMini(e)  # analytic elementary matrix
 
    for i in range(0,_velocityFD): 
     ii = _IEN[e][i]
   
     for j in range(0,_velocityFD):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]

      Kxx[ii + _numNodes,jj + _numNodes] += element2D.kxx[i][j]
      Kxy[ii + _numNodes,jj + _numNodes] += element2D.kxy[i][j]
      Kyx[ii + _numNodes,jj + _numNodes] += element2D.kyx[i][j]
      Kyy[ii + _numNodes,jj + _numNodes] += element2D.kyy[i][j]
      K[ii + _numNodes,jj + _numNodes] += element2D.kxx[i][j] + element2D.kyy[i][j]
 
  
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      M[ii + _numNodes,jj + _numNodes] += element2D.mass[i][j]
      MLump[ii + _numNodes,ii + _numNodes] += element2D.mass[i][j]

      KxxMini[ii,jj] += element2D.kxx[i][j]
      KxyMini[ii,jj] += element2D.kxy[i][j]
      KyxMini[ii,jj] += element2D.kyx[i][j]
      KyyMini[ii,jj] += element2D.kyy[i][j]
      KMini[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]

      MMini[ii,jj] += element2D.mass[i][j]
      MLumpMini[ii,ii] += element2D.mass[i][j]
 
      GxMini[ii,jj] += element2D.gx[i][j]
      GyMini[ii,jj] += element2D.gy[i][j]
 

 
     for j in range(0,_pressureFD):
      jj = _IEN[e][j]
     
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 



  #obsolete
  elif _polynomial_option == 3:
   polynomial_order = 'Quadratic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.quadratic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 4:
   polynomial_order = 'Cubic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.cubic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]

 
  elif _polynomial_option == 0:
   polynomial_order = 'Analytic Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.analyticLinear(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
 
  else:
   print ""
   print " Error: Element type not found"
   print ""
   sys.exit()


 #Debug
 elif _simulation_option == 0:
  polynomial_order = 'Debug'

  Kxx = Kxx*1.0 
  Kxy = Kxy*1.0
  Kyx = Kyx*1.0
  Kyy = Kyy*1.0
  K =   K*1.0
  M =   M*1.0
  MLump = MLump*1.0
  Gx =  Gx*1.0 
  Gy =  Gy*1.0 

  KxxMini = KxxMini*1.0 
  KxyMini = KxyMini*1.0
  KyxMini = KyxMini*1.0
  KyyMini = KyyMini*1.0
  KMini =   KMini*1.0
  MMini =   MMini*1.0
  MLumpMini = MLumpMini*1.0
  GxMini =  GxMini*1.0 
  GyMini =  GyMini*1.0 
 
 
 return Kxx, Kxy, Kyx, Kyy, K, M, MLump, Gx, Gy, KxxMini, KxyMini, KyxMini, KyyMini, KMini, MMini, MLumpMini, GxMini, GyMini, polynomial_order


def AxiNS2D(_simulation_option, _polynomial_option, _velocityFD, _pressureFD, _numNodes, _numVerts, _numElements, _IEN, _x, _y, _GAUSSPOINTS):

 Kxxr   = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Kxyr   = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Kyxr   = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Kyyr   = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Kr     = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 M2r    = sps.lil_matrix((2*_numNodes,2*_numNodes), dtype = float)
 Mr     = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 M      = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 MrLump = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Gx     = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Gy     = sps.lil_matrix((_numNodes,_numNodes), dtype = float)
 Gxr    = sps.lil_matrix((_numNodes,_numVerts), dtype = float)
 Gyr    = sps.lil_matrix((_numNodes,_numVerts), dtype = float)
 M1     = sps.lil_matrix((_numVerts,_numNodes), dtype = float)

 element2D = gaussianQuadrature.Element2D(_x, _y, _IEN, _GAUSSPOINTS)

 #obsolete
 if _simulation_option == 1:
  if _polynomial_option == 1:
   polynomial_order = 'Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.linear(e)
 

    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]

   
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 2:
   polynomial_order = 'Mini Element'
 
   for e in tqdm(range(0, _numElements)):
    element2D.mini(e)         # gaussian quadrature
    #element2D.analyticMini(e)  # analytic elementary matrix

    v1 = _IEN[e][0]
    v2 = _IEN[e][1]
    v3 = _IEN[e][2]
    #r_elem = (_y[v1] + _y[v2] + _y[v3])/3.0
    r_elem = 1.0
 
    for i in range(0,_velocityFD): 
     ii = _IEN[e][i]
   
     for j in range(0,_velocityFD):
      jj = _IEN[e][j]

      M2r[ii,jj]                         += element2D.mass[i][j]*(r_elem)
      M2r[ii + _numNodes,jj + _numNodes] += element2D.mass[i][j]*(r_elem)

      Kxxr[ii,jj] += element2D.kxx[i][j]*(r_elem)
      Kxyr[ii,jj] += element2D.kxy[i][j]*(r_elem)
      Kyxr[ii,jj] += element2D.kyx[i][j]*(r_elem)
      Kyyr[ii,jj] += element2D.kyy[i][j]*(r_elem)
      Kr  [ii,jj] += (element2D.kxx[i][j] + element2D.kyy[i][j])*(r_elem)

      Mr[ii,jj]     += element2D.mass[i][j]*(r_elem)
      M [ii,jj]     += element2D.mass[i][j]
      MrLump[ii,ii] += element2D.mass[i][j]*(r_elem)
 
      Gx[ii,jj]     += element2D.gx[i][j]
      Gy[ii,jj]     += element2D.gy[i][j]
 
     for j in range(0,_pressureFD):
      jj = _IEN[e][j]
     
      Gxr[ii,jj] += element2D.gx[i][j]*(r_elem)
      Gyr[ii,jj] += element2D.gy[i][j]*(r_elem)
      M1 [jj,ii] += element2D.mass[j][i]
 



  #obsolete
  elif _polynomial_option == 3:
   polynomial_order = 'Quadratic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.quadratic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
  elif _polynomial_option == 4:
   polynomial_order = 'Cubic Element'
 
   for e in tqdm(range(0, _nelem)):
    element2D.cubic(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]

 
  elif _polynomial_option == 0:
   polynomial_order = 'Analytic Linear Element'
   
   for e in tqdm(range(0, _nelem)):
    element2D.analyticLinear(e)
 
    for i in range(0,_GL): 
     ii = _IEN[e][i]
   
     for j in range(0,_GL):
      jj = _IEN[e][j]
 
      Kxx[ii,jj] += element2D.kxx[i][j]
      Kxy[ii,jj] += element2D.kxy[i][j]
      Kyx[ii,jj] += element2D.kyx[i][j]
      Kyy[ii,jj] += element2D.kyy[i][j]
      K[ii,jj] += element2D.kxx[i][j] + element2D.kyy[i][j]
    
      M[ii,jj] += element2D.mass[i][j]
      MLump[ii,ii] += element2D.mass[i][j]
 
      Gx[ii,jj] += element2D.gx[i][j]
      Gy[ii,jj] += element2D.gy[i][j]
 
 
  else:
   print ""
   print " Error: Element type not found"
   print ""
   sys.exit()


 #Debug
 elif _simulation_option == 0:
  polynomial_order = 'Debug'

  Kxxr   = Kxxr  *1.0   
  Kxyr   = Kxyr  *1.0 
  Kyxr   = Kyxr  *1.0 
  Kyyr   = Kyyr  *1.0 
  Kr     = Kr    *1.0 
  M2r    = M2r   *1.0 
  Mr     = Mr    *1.0 
  M      = M     *1.0 
  MrLump = MrLump*1.0
  Gx     = Gx    *1.0 
  Gy     = Gy    *1.0 
  Gxr    = Gxr   *1.0 
  Gyr    = Gyr   *1.0 
  M1     = M1    *1.0 

 return Kxxr, Kxyr, Kyxr, Kyyr, Kr, M2r, Mr, M, MrLump, Gx, Gy, Gxr, Gyr, M1, polynomial_order
