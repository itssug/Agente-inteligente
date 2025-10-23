# main.pygit 
from datetime import datetime, timedelta
from agente_inteligente import AgenteInteligente
import time
import heapq

agente = AgenteInteligente()


 #PRIORIZACIÓN DE CASOS SEGÚN NIVEL DE RIESGO
print("\n=== PRIORIZACIÓN DE CASOS DE NNA ===")

cases = [
    {'id': 'C1', 'nombre': 'Juan Pérez', 'riesgo_salud': 0.9, 'riesgo_psicologico': 0.4,
     'abandono_previos': True, 'edad': 1, 'condiciones_vulnerables': True},
    {'id': 'C2', 'nombre': 'María López', 'riesgo_salud': 0.3, 'riesgo_psicologico': 0.8,
     'abandono_previos': False, 'edad': 6, 'condiciones_vulnerables': False},
    {'id': 'C3', 'nombre': 'Andrés Quispe', 'riesgo_salud': 0.6, 'riesgo_psicologico': 0.7,
     'abandono_previos': True, 'edad': 4, 'condiciones_vulnerables': True},
    {'id': 'C4', 'nombre': 'Valeria Mamani', 'riesgo_salud': 0.2, 'riesgo_psicologico': 0.3,
     'abandono_previos': False, 'edad': 2, 'condiciones_vulnerables': True},
]

casos_prioritarios = agente.priorizar_casos(cases)
for idx, c in enumerate(casos_prioritarios, 1):
    print(f"{idx}. {c['case']['nombre']} (Score: {c['score']})")




 #CHATBOT PARA PREGUNTAS FRECUENTES

print("\n=== CHATBOT DE ORIENTACIÓN A ADOPTANTES ===")

agente.chatbot = agente.chatbot.__class__([
    ("¿Qué documentos necesito para iniciar la adopción?", "Debe presentar su certificado de nacimiento, cédula de identidad, formulario RUANI y certificado de antecedentes."),
    ("¿Cuánto dura el proceso?", "El tiempo promedio de adopción es de 6 a 12 meses, dependiendo de la documentación y evaluación social."),
    ("¿Se puede adoptar como persona soltera?", "Sí, las adopciones monoparentales están permitidas y se evalúan de manera individual."),
])

preguntas = [
    "Qué documentos se requieren para adoptar?",
    "Cuánto dura todo el proceso?",
    "Puedo adoptar si soy soltera?"
]
for p in preguntas:
    print(f"Pregunta: {p}")
    print("Respuesta:", agente.responder_pregunta(p))
    print()

#  CLASIFICACIÓN AUTOMÁTICA DE DOCUMENTOS

print("\n=== CLASIFICACIÓN DE DOCUMENTOS ===")

agente.doc_classifier.train([
    ("Certificado de nacimiento original con sello oficial", "válido"),
    ("Evaluación psicológica firmada por profesional acreditado", "válido"),
    ("Fotocopia sin firma ni sello", "inválido"),
    ("Documento escaneado ilegible", "inválido"),
])

docs_prueba = [
    "Certificado de nacimiento firmado por juez",
    "Evaluación psicológica sin sello",
    "Fotocopia legible con firma y sello",
]

for d in docs_prueba:
    print(f"Documento: '{d}' → Clasificación:", agente.clasificar_documento(d))

# =====================================================
#  MOTOR DE RECOMENDACIONES ADOPTANTE - NNA
# =====================================================
print("\n=== MOTOR DE RECOMENDACIONES ADOPTANTE - NNA ===")

adoptante = {
    'nombre': 'Familia Quispe',
    'edad_min': 2,
    'edad_max': 7,
    'idiomas': ['es', 'aym'],
    'tipos_adopcion': ['nacional', 'monoparental'],
    'disponibilidad': True,
    'tags_sociales': ['rural']
}

nna_list = [
    {'id': 'NNA001', 'nombre': 'Diego', 'edad': 3, 'idiomas': ['es'], 'tipo_adopcion': 'nacional',
     'disponibilidad': True, 'tags_sociales': ['rural']},
    {'id': 'NNA002', 'nombre': 'Sofía', 'edad': 6, 'idiomas': ['es', 'que'], 'tipo_adopcion': 'internacional',
     'disponibilidad': True, 'tags_sociales': ['urbano']},
    {'id': 'NNA003', 'nombre': 'Luis', 'edad': 5, 'idiomas': ['es', 'aym'], 'tipo_adopcion': 'nacional',
     'disponibilidad': True, 'tags_sociales': ['rural']},
]

recomendaciones = agente.preseleccionar(adoptante, nna_list)
print(f"Recomendaciones para {adoptante['nombre']}:")
for r in recomendaciones:
    print(f" - {r['id']} ({r['nombre']})")

#  PROGRAMACIÓN DE RECORDATORIOS AUTOMÁTICOS
print("\n=== PROGRAMACIÓN DE RECORDATORIOS ===")

when1 = datetime.utcnow() + timedelta(seconds=3)
when2 = datetime.utcnow() + timedelta(seconds=5)

agente.programar_recordatorio(when1, "Reunión con familia adoptante Pérez - 10:00 AM", {"nombre": "Trabajadora Social 1"})
agente.programar_recordatorio(when2, "Entrega de informes mensuales al SEDEGES Central", {"nombre": "Trabajadora Social 2"})

print("Esperando recordatorios...")
time.sleep(6)
recordatorios = agente.scheduler.due()
print("Recordatorios vencidos:")
for r in recordatorios:
    print(f" - {r['message']} | Destinatario: {r['dest']['nombre']}")