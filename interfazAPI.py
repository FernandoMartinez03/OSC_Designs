import streamlit as st

st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
                background-color: white;
        }
        div.stButton > button:first-child {
            background-color: #ff8502 !important; /* naranja de la inclusión */
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
            padding: 10px 20px !important; /* lo hace más amplio el margen */
            border: none !important; /* si no se ve feo al seleccionar */
        }

        /* Button hover effect */
        div.stButton > button:first-child:hover {
            background-color: #d96d00 !important; /* Más naranja */
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 style="color:#df1583;">Hola, bienvenido al sistema de evaluación de OSCs.</h1>', unsafe_allow_html=True)

st.markdown(
    """ 
    <p style="color:black; font-size:18px;">
    Por favor, asegúrese de que la fecha para subir respuestas al Cognito Forms ya haya pasado.
    </p>
    
    <p style="color:black; font-size:18px;">
    Para enviar a procesar la información, de click al botón de abajo:
    </p>
    """,
    unsafe_allow_html=True
)

if st.button("Mandar a procesar"):
    st.balloons()