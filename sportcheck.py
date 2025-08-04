import streamlit as st
import datetime
import time

# ----------- Datos por día ----------- #
schedule = {
    'monday': ['Natación', 'PF', 'Running'],
    'tuesday': ['Ciclismo'],
    'wednesday': ['Natación', 'PF', 'Running'],
    'thursday': ['Ciclismo'],
    'friday': ['Natación', 'PF'],
    'saturday': ['Running'],
    'sunday': []
}

items_por_deporte = {
    'Natación': [
        '--- Elementos personales ---',
        'Bolso Natación', 'Toalla', 'Chalas', 'Cepillo de pelo', 'Secador de pelo',
        'Neceser: jabón, shampoo, acondicionador',
        '',
        '--- Elementos de entrenamiento ---',
        'Traje Baño', 'Gorro', 'Lentes', 'Aletas', 'Paletas', 'Pull boy', 'Tapones',
        '',
        '--- Ropa de cambio ---',
        'Calzón', 'Calcetines', 'Sostén', 'Pantalón', 'Polera', 'Chaleco/polerón', 'Calzado',
        '',
        '--- Suplementos ---',
        'Shaker (proteína/creatina)'
    ],
    'PF': [
        '--- Ropa deportiva ---',
        'Peto', 'Polera', 'Calzas', 'Zapatillas pesas', 'Polerón',
        '',
        '--- Higiene ---',
        'Toalla', 'Neceser', 'Secador pelo'
    ],
    'Ciclismo': [
        '--- Equipamiento ---',
        'Casco', 'Lentes', 'Ciclo computador cargado', 'Bicicleta cargada', 'Luces cargadas',
        '',
        '--- Alimentación/Hidratación ---',
        'Gel o barrita', 'Botellas', 'Sales', 'Banda cardiaca', 'Audífonos',
        '',
        '--- Ropa ciclismo ---',
        'Polera cambio', 'Peto', 'Tricota', 'Cortaviento', 'Chaqueta', 'Guantes',
        'Calza', 'Calcetas', 'Zapatillas',
        '',
        '--- Extras ---',
        'Bloqueador', 'Bandana', 'Gorro nerd horrible'
    ],
    'Running': [
        '--- Ropa deportiva ---',
        'Polera cambio', 'Zapatillas', 'Calcetas', 'Calzas', 'Peto', 'Polerón', 'Chaqueta',
        '',
        '--- Tecnología y control ---',
        'Banda cardiaca', 'Reloj cargado', 'Audífonos',
        '',
        '--- Hidratación/Comida ---',
        'Botellas', 'Sales', 'Comida'
    ]
}

# ----------- Funciones ----------- #
def get_tomorrow():
    import pytz
    tz = pytz.timezone('America/Santiago')
    now = datetime.datetime.now(tz)
    if now.hour < 5:
        target = now
    else:
        target = now + datetime.timedelta(days=1)
    return target.strftime('%A').lower()

# ----------- App ----------- #
st.set_page_config(page_title="Checklist entrenamiento", layout="centered")

st.markdown("""
    <style>
    .celebration {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: #27ae60;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2em;
        z-index: 9999;
        animation: fadein 1s ease-in-out;
    }
    @keyframes fadein {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

st.title("✅ Preparación para mañana")

dias_semana = {
    'monday': 'Lunes',
    'tuesday': 'Martes',
    'wednesday': 'Miércoles',
    'thursday': 'Jueves',
    'friday': 'Viernes',
    'saturday': 'Sábado',
    'sunday': 'Domingo'
}

selected_day = st.selectbox("📅 ¿Qué día es mañana?", options=list(dias_semana.keys()), format_func=lambda x: dias_semana[x])
st.subheader("📅 ¿Qué día es mañana?")

deportes = schedule.get(selected_day, [])

total_items = 0
completados = 0

for deporte in deportes:
    st.markdown(f"### {deporte}")
    with st.expander("Ver ítems"):
        for item in items_por_deporte[deporte]:
            if item.startswith('---'):
                st.markdown(f"**{item}**")
                continue
            if item.strip() == '':
                st.markdown("&nbsp;")
                continue
            checked = st.checkbox(f" {item}", key=f"{deporte}-{item}")
            total_items += 1
            if checked:
                completados += 1

# ----------- Celebración ----------- #
if total_items > 0 and completados == total_items:
    st.components.v1.html(
        """
        <div class='celebration'>🎉 ¡Todo listo para mañana! 🎉</div>
        """,
        height=300
    )
else:
    st.progress(completados / total_items if total_items else 0)
    st.write(f"Completado: {completados} de {total_items}")

st.caption("Hecho con amor para entrenar sin pensar 💪")
