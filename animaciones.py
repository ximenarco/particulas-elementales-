import streamlit as st
if st.button:
  st.title("Partículas elementales")
  st.header("Esta aplicación te enseñara un poco acerca de las partículas elementales.") 
  st.write("Las partículas elementales podrían considerarse como los ladrillos básicos de la creación, se les llama partículas elementales ya que no están constituidas por partículas más pequeñas.")
  st.image("https://upload.wikimedia.org/wikipedia/commons/0/00/Standard_Model_of_Elementary_Particles.svg")
  
with st.sidebar:
  bt1=st.button("Quarks")
  bt2=st.button("Leptones")
  bt3=st.button("Bosón de gauge")
  bt4=st.button("Bosón de Higgs")
  
if bt1:
  st.write("Son responsables de la formación y estructura de los núcleos atómicos y de las interacciones con su entorno.")
  st.write("Los quarks son un tipo de partícula que constituye la materia. Si miramos a nuestro alrededor... toda la materia que vemos está compuesta de protones y neutrones, y estas partículas están compuestas de quarks.")
  col1,col2= st.columns (2)
  with col1:
    st.markdown(''' **Arriba_(up).** Dotado de un isospín +1/2 como número cuántico.
    
    **Abajo (down).** Dotado de un isospín -1/2 como número cuántico.
    
    **Encanto (charm).** Dotado de un encanto +1 como número cuántico.
    
    **Extraño (strange).** Dotado de una extrañeza -1 como número cuántico.
    
    **Tope (top) o verdad (truth).** Dotado de una superioridad (topness) +1.
     
    **Fondo (bottom) o belleza (beauty).** Dotado de una inferioridad (bottomness) -1.  ''')
    
    
  with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Neutron_quark_structure.svg/1200px-Neutron_quark_structure.svg.png")
    
if bt2:
  st.write("Lepton, cualquier miembro de una clase de partículas subatómicas que responden solo a la fuerza electromagnética, la fuerza débil y la fuerza gravitacional y no se ven afectadas por la fuerza fuerte. Se dice que los leptones son partículas elementales; es decir, no parecen estar formados por unidades de materia más pequeñas. Los leptones pueden transportar una unidad de carga eléctrica o ser neutrales.")
  st.write("Los leptones son partículas elementales con espín 1/2 (un fermión) que no se ven afectadas por la fuerza nuclear fuerte. Son una familia de partículas diferente a la otra familia conocida de fermiones, los quarks. Los electrones son un ejemplo bien conocido que se encuentran en la materia ordinaria.")
  
if bt3:
  st.write("un bosón que media la interacción entre partículas elementales. Hay varios tipos: fotones para interacciones electromagnéticas, bosones vectoriales intermedios W y Z para interacciones débiles y gravitones para interacciones gravitatorias.")
  
if bt4:
  st.write("Los bosones a veces se denominan partículas de fuerza, porque son los bosones los que controlan la interacción de las fuerzas físicas, como el electromagnetismo y posiblemente incluso la propia gravedad.")
 
