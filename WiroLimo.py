
import streamlit as st
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Logo de la empresa (cambia la URL a la de tu imagen PNG)
logo_url = "imagenes WiroLimo/logo.png"

# Coloca el logo en la parte superior del sidebar
st.sidebar.image(logo_url, use_column_width=True)


# Sidebar para la navegación
st.sidebar.title("Our menu")
pagina_seleccionada = st.sidebar.selectbox("Select a page", ["Homepage", "Sports Events Services", "Airport Services", "About Us"])


#----------------------------------------------------------------------------------------------------
if pagina_seleccionada == "Homepage":
#----------------------------------------------------------------------------------------------------    
    # st.header("Bienvenido a nuestro sitio web de transporte de limosinas")
    # Puedes agregar contenido adicional para la página de inicio aquí.

        #Título de la página
    # st.title(" Welcome to WiroLimo Transport  ")

    st.markdown(
        "<h1 style='text-align:center; color: black;'>Welcome to WiroLimo Transport</h1>",
        unsafe_allow_html=True,
        )   
   
    # Cargar las imágenes
    image1 = Image.open("imagenes WiroLimo/SUV.png")
    image2 = Image.open("imagenes WiroLimo/Sedan.png")


    # Dividir el diseño en dos columnas
    col1, col2 = st.columns(2)

    # Mostrar la primera imagen en la columna izquierda
    with col1:
        st.image(image1, caption="SUV fleet", use_column_width=True)
        # Comentario para la primera imagen
        parrafo1="Don't skimp on space or comfort. Choose our 7-passenger SUV and experience a luxurious ride every journey. Book your trip today and discover the elegance and practicality we offer."
        st.markdown(
            f"<p style='text-align:justify; font-family: cursive; font-style: italic; color: green;'>{parrafo1}</p>",
            unsafe_allow_html=True,
        )
    # Mostrar la segunda imagen en la columna derecha
    with col2:
        st.image(image2, caption="Sedan fleet", use_column_width=True)
        # Comentario para la segunda imagen
        parrafo2="Our sedan vehicles are ideal for city trips, business meetings, outings with friends or any occasion when you need comfortable and stylish transportation."
        st.markdown(
            f"<p style='text-align:justify; font-family: cursive; font-style: italic; color: green;'>{parrafo2}</p>",
            unsafe_allow_html=True,
        )

#---------------------------------------------------------------------------------------------------
#REDES SOCIALES
    # Define una función para mostrar la barra de redes sociales
    def mostrar_barra_redes_sociales():
        st.markdown(
            """
            <style>
            .redes-sociales {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background-color: blue; /* Cambia el color de fondo de la barra */
                padding: 10px;
                text-align: center;
            }
            .redes-sociales a {
                color: #fff; /* Cambia el color del texto de los enlaces */
                text-decoration: none;
                margin: 0 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="redes-sociales">
                <a href="https://www.facebook.com/tucuenta" target="_blank">Facebook</a>
                <a href="https://twitter.com/tucuenta" target="_blank">Twitter</a>
                <a href="https://www.instagram.com/tucuenta" target="_blank">Instagram</a>
                <!-- Agrega más enlaces a tus redes sociales aquí -->
            </div>
            """,
            unsafe_allow_html=True
        )

    # Llama a la función para mostrar la barra de redes sociales
    mostrar_barra_redes_sociales()

#-----------------------------------------------------------------------------------------------------    
elif pagina_seleccionada == "Sports Events Services":
# ------------------------------------------------------------------------------------------------

    tarifas_eventos = {
        "Flushing Stadium (Mets or Tennis)": {"Sedan": 90.00, "SUV": 130.00},
        "Yankee Stadium": {"Sedan": 110.00, "SUV": 140.00},
        "Barclays Center": {"Sedan": 90.00, "SUV": 145.00},
        "Meadowlands": {"Sedan": 130.00, "SUV": 160.00},
        "Prudential Center": {"Sedan": 130.00, "SUV": 160.00},
        "Atlantic City": {"Sedan": 460.00, "SUV": 535.00},
    }

    # Función para enviar correo electrónico
    def enviar_correo(destinatario, hora_servicio, evento, vehiculo):
        # Configurar el servidor SMTP
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = "tluivaniri@gmail.com"
        smtp_password = "ryvk ptuq ahvh paeh"

        # Crear el mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = destinatario
        msg['Subject'] = "Confirmación de servicio"

        # Cuerpo del mensaje
        mensaje = f"Gracias por reservar un servicio para el evento en {evento} en un {vehiculo} a las {hora_servicio}."
        msg.attach(MIMEText(mensaje, 'plain'))

        # Iniciar conexión con el servidor SMTP y enviar el correo
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, destinatario, msg.as_string())
            server.quit()
            st.success("Correo electrónico enviado con éxito")
        except Exception as e:
            st.error(f"Error al enviar el correo electrónico: {str(e)}")

    # Interfaz de usuario de Streamlit
    st.title("Reservation - Sport venues from/to Manhattan (including tolls)")

    # Selección de evento deportivo
    evento = st.selectbox("Seleccione el evento deportivo:", list(tarifas_eventos.keys()))

    # Selección de vehículo
    vehiculo = st.radio("Seleccione el tipo de vehículo:", ["Sedan", "SUV"])

    # Calcular tarifa
    tarifa = tarifas_eventos[evento][vehiculo]

    # Mostrar la tarifa
    st.write(f"Rate for the event in {evento} in {vehiculo}: ${tarifa:.2f}")

    # Formulario de reserva
    st.subheader("Reserva de Servicio")
    email = st.text_input("Ingrese su correo electrónico:")
    hora_servicio = st.time_input("Seleccione la hora del servicio:")

    # Botón para enviar reserva
    if st.button("Enviar reserva"):
        if email and hora_servicio:
            enviar_correo(email, hora_servicio.strftime("%H:%M"), evento, vehiculo)
        else:
            st.warning("Por favor, complete todos los campos.")

       
#----------------------------------------------------------------------------------------------------
elif pagina_seleccionada == "Airport Services":
#-------------------------------------------------------------------------------------------------
     
    tarifas_aeropuertos = {
        "LGA - LaGuardia Airport": {"Sedan": 85.00, "SUV": 120.00},
        "JFK - John F. Kennedy International Airport": {"Sedan": 110.00, "SUV": 150.00},
        "EWR - Newark Liberty International Airport": {"Sedan": 130.00, "SUV": 160.00},
        "TEB - Teterboro Airport": {"Sedan": 145.00, "SUV": 175.00},
        "HPN - Westchester County Airport": {"Sedan": 165.00, "SUV": 210.00},
        "ISP - Long Island MacArthur Airport": {"Sedan": 195.00, "SUV": 245.00},
    }

    # Función para enviar correo electrónico
    def enviar_correo(destinatario, hora_servicio, aeropuerto, vehiculo):
        # Configurar el servidor SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = "lvuianiri@gmail.com"
        smtp_password = "ryvk ptuq ahvh paeh"

        # Crear el mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = destinatario
        msg['Subject'] = "Confirmación de servicio"

        # Cuerpo del mensaje
        mensaje = f"Gracias por reservar un servicio desde {aeropuerto} en un {vehiculo} a las {hora_servicio}."
        msg.attach(MIMEText(mensaje, 'plain'))

        # Iniciar conexión con el servidor SMTP y enviar el correo
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, destinatario, msg.as_string())
            server.quit()
            st.success("Correo electrónico enviado con éxito")
        except Exception as e:
            st.error(f"Error al enviar el correo electrónico: {str(e)}")

    # Interfaz de usuario de Streamlit
    st.title("Reservation - Airports from/to Manhattan, Downtown up to 100th street (including tolls")

    # Selección de aeropuerto
    aeropuerto = st.selectbox("Seleccione el aeropuerto:", list(tarifas_aeropuertos.keys()))

    # Selección de vehículo
    vehiculo = st.radio("Seleccione el tipo de vehículo:", ["Sedan", "SUV"])

    # Calcular tarifa
    tarifa = tarifas_aeropuertos[aeropuerto][vehiculo]

    # Mostrar la tarifa
    st.write(f"Tarifa desde {aeropuerto} en {vehiculo}: ${tarifa:.2f}")

    # Formulario de reserva
    st.subheader("Reserva de Servicio")
    email = st.text_input("Ingrese su correo electrónico:")
    hora_servicio = st.time_input("Seleccione la hora del servicio:")

    # Botón para enviar reserva
    if st.button("Enviar reserva"):
        if email and hora_servicio:
            enviar_correo(email, hora_servicio.strftime("%H:%M"), aeropuerto, vehiculo)
        else:
            st.warning("Por favor, complete todos los campos.")




#-------------------------------------------------------------------------------------------------
elif pagina_seleccionada == "About Us":
#-------------------------------------------------------------------------------------------------
    
    st.header("About us")
    # Agrega información sobre tu empresa y su historia aquí.
       
    # Cargar la imágen
    image1 = Image.open("imagenes WiroLimo/AvionAuto.png")
    
    # Dividir el diseño en dos columnas
    col1, col2 = st.columns(2)

    # Mostrar la primera imagen en la columna izquierda
    with col1:
        st.image(image1, caption="Fleet", use_column_width=True)
        

    # Mostrar la segunda imagen en la columna derecha
    with col2:
              # Eslogan y texto publicitario
        st.markdown(
        "<h1 style='text-align:center; color: blue;'>¡Travel in style!</h1>",
        unsafe_allow_html=True,
        )   
        texto1="Our timely and high quality service is what we are known for. WiroLimo Inc. has been operating since 2003.."
        texto2 = "Short haul excursions to Philadelphia, Connecticut, Boston or surrounding areas. Fast and reliable transportation services to and from any New York airport."

        # Agregar un texto centrado con una fuente y color personalizados
        st.markdown(
            f"<p style='text-align:justify; font-family: cursive; font-style: italic; color: blue;'>{texto1}</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p style='text-align:justify; font-family: cursive; font-style: italic; color: blue;'>{texto2}</p>",
            unsafe_allow_html=True,
        )

#---------------------------------------------------------------------------------------------------
#REDES SOCIALES
    # Define una función para mostrar la barra de redes sociales
    def mostrar_barra_redes_sociales():
        st.markdown(
            """
            <style>
            .redes-sociales {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background-color: blue; /* Cambia el color de fondo de la barra */
                padding: 10px;
                text-align: center;
            }
            .redes-sociales a {
                color: #fff; /* Cambia el color del texto de los enlaces */
                text-decoration: none;
                margin: 0 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="redes-sociales">
                <a href="https://www.facebook.com/tucuenta" target="_blank">Facebook</a>
                <a href="https://twitter.com/tucuenta" target="_blank">Twitter</a>
                <a href="https://www.instagram.com/tucuenta" target="_blank">Instagram</a>
                <!-- Agrega más enlaces a tus redes sociales aquí -->
            </div>
            """,
            unsafe_allow_html=True
        )

    # Llama a la función para mostrar la barra de redes sociales
    mostrar_barra_redes_sociales()
