from IPython.display import Math, display

display(Math(r"""
\tau_{ij}=\left(
\mu \left[\frac{\partial u_i}{\partial x_j}
+\frac{\partial u_j}{\partial x_i}\right]
-\delta_{ij}\left(\frac{2}{3}\mu 
\frac{\partial u_k}{\partial x_k}\right)
\right)
"""))

display(Math(r"""
p=(\gamma-1)\left(\rho E-\rho \bar{u}^2/2\right)
"""))
