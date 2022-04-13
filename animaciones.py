import streamlit as st
st.title ("Particulas elementales")
from sympy import 
import heppackv0 as hep
s,theta=symbols('s theta',real=True)
p=symbols('p',positive=True)
u,t,s=symbols('u t s',real=True)
p1=[p,0,0,0]
p2=[p,0,pi,pi]
p3=[p,0,theta,0]
p4=[p,0,pi-theta,pi]
sCM=4*p*p;sCM
tCM=-sCM*sin(theta/2)^2;tCM
uCM=-sCM*cos(theta/2)^2;uCM
