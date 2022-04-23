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
  st.header("Quarks")
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
  st.header("Leptones")
  st.write("El centro de un átomo cargado positivamente generalmente se describe como un núcleo rodeado por una nube de electrones, esto se debe a que, al igual que en una nube, es difícil ver y saber exactamente en qué parte de los átomos se encuentra el electrón, pero podemos adivinar dónde probablemente está. Probablemente estará volando alrededor del núcleo.")
  st.write("Los electrones son como los quarks, no estamos seguros de si hay algo dentro de ellos, son un tipo de partículas llamadas leptones que tienen exactamente 1 carga negativa o una carga 0, a diferencia de las cargas parciales de los quarks.")
  st.write("Hay 6 tipos de leptones, el más común y conocido es el electrón, con carga negativa 1. Las versiones más grandes de electrones son Muon y Tau, los otros 3 leptones tienen carga 0 llamados neutrinos que son tan pequeños, son una millonésima parte del tamaño de un electrón, estos neutrinos atraviesan nuestros cuerpos entre todo el espacio vacío que existe nuestros átomos sin nosotros siquiera darnos cuenta. Los electrones son la razón principal de mucho de lo que sucede en la química y la ciencia, sin embargo, los otros 5 leptones son raros o no tienen mucho efecto.")
  st.write("Los electrones juegan un papel importante en permitir que los átomos se unan, y tener electrones adicionales o no tener suficientes es lo que hace que los imanes funcionen. Entonces, los quarks forman el núcleo de un átomo, los leptones forman los electrones de un átomo, y lo que mantiene unidas a estas partículas se le conoce como bosones.")
  st.image("https://d1kvkzjpuym02z.cloudfront.net/61313570a68662083c853e9e.png?Expires=2104061090&Signature=Fu-iLqxwRPckZqqOwqCOuW11kNFgE2VNR-Slff54Q3MHmgIc2rfBI3fbh-wXcvfBwYLucvPJeVfFDiFwxnvTxbWfrPgKpVzI5buRxr3YxTZfz2pYkzBDQlMR~rVlBFJqn3Tj3AuBCT334NJwA0hBYFLWD9XMyrWBDViWuObglOE_&Key-Pair-Id=APKAJXYWFXCDTRLR3EFA")
  
if bt3:
  st.header("Bosón de gauge")
  st.write("un bosón que media la interacción entre partículas elementales. Hay varios tipos: fotones para interacciones electromagnéticas, bosones vectoriales intermedios W y Z para interacciones débiles y gravitones para interacciones gravitatorias.")
  st.image("https://francis.naukas.com/files/2017/11/Dibujo20171126-gauge-theory-lagrangian1.png")
  
if bt4:
  st.header("Bosón de Higgs")
  st.write("Los bosones a veces se denominan partículas de fuerza, porque son los bosones los que controlan la interacción de las fuerzas físicas, como el electromagnetismo y posiblemente incluso la propia gravedad.")
  st.image("https://agencia.fapesp.br/agencia-novo/imagens/noticia/19475.jpg")
 
