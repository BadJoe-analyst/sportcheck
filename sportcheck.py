import streamlit as st
import datetime

# ----------- Datos por día ----------- #
schedule = {
    'lunes': ['Natación', 'PF', 'Running'],
    'martes': ['Ciclismo'],
    'miércoles': ['Natación', 'PF', 'Running'],
    'jueves': ['Ciclismo'],
    'viernes': ['Natación', 'PF'],
    'sábado': ['Running'],
    'domingo': []
}

items_por_deporte = {
    'Natación': [
        'Bolso Natación', 'Toalla', 'Chalas', 'Cepillo de pelo', 'Secador de pelo',
        'Neceser: jabón, shampoo, acondicionador', 'Traje Baño', 'Gorro', 'Lentes',
        'Aletas', 'Paletas', 'Pull boy', 'Tapones',
        'Calzón', 'Calcetines', 'Sostén', 'Pantalón', 'Polera', 'Chaleco/polerón', 'Calzado',
        'Shaker (proteína/creatina)'
    ],
    'PF': [
        'Peto', 'Polera', 'Calzas', 'Zapatillas pesas', 'Polerón', 'Toalla', 'Neceser', 'Secador pelo'
    ],
    'Ciclismo': [
        'Casco', 'Lentes', 'Ciclo computador cargado', 'Bicicleta cargada', 'Luces cargadas',
        'Gel o barrita', 'Botellas', 'Sales', 'Banda cardiaca', 'Audífonos',
        'Polera cambio', 'Peto', 'Tricota', 'Cortaviento', 'Chaqueta', 'Guantes',
        'Calza', 'Calcetas', 'Zapatillas', 'Bloqueador', 'Bandana', 'Gorro nerd horrible'
    ],
    'Running': [
        'Polera cambio', 'Zapatillas', 'Calcetas', 'Calzas', 'Peto', 'Polerón', 'Chaqueta',
        'Banda cardiaca', 'Reloj cargado', 'Botellas', 'Sales', 'Comida', 'Audífonos'
    ]
}

# ----------- Funciones ----------- #
def get_tomorrow():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    return tomorrow.strftime('%A').lower()

# ----------- App ----------- #
st.set_page_config(page_title="Checklist entrenamiento", layout="centered")

st.title("✅ Preparación para mañana")

tomorrow = get_tomorrow()
dia = tomorrow.capitalize()
st.subheader(f"📅 Mañana es {dia}")

deportes = schedule.get(tomorrow, [])

total_items = 0
completados = 0

for deporte in deportes:
    st.markdown(f"### {deporte}")
    with st.expander("Ver ítems"):
        for item in items_por_deporte[deporte]:
            checked = st.checkbox(item, key=f"{deporte}-{item}")
            total_items += 1
            if checked:
                completados += 1

# ----------- Celebración ----------- #
if total_items > 0 and completados == total_items:
    st.markdown(
        """
        <style>
            body {
                background-color: #27ae60 !important;
            }
        </style>
        <h2 style='color:white;text-align:center;'>🎉 ¡Todo listo para mañana! 🎉</h2>
        """,
        unsafe_allow_html=True
    )
else:
    st.progress(completados / total_items if total_items else 0)
    st.write(f"Completado: {completados} de {total_items}")

st.caption("Hecho con amor para entrenar sin pensar 💪")
