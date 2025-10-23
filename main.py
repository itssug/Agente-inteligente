# main.py
from datetime import datetime, timedelta
from agente_inteligente import AgenteInteligente
import time

agente = AgenteInteligente()

# Recomendaciones
adoptante = {'edad_min': 2, 'edad_max': 6, 'idiomas': ['es', 'aym'], 'tipos_adopcion': ['nacional','monoparental'], 'disponibilidad': True, 'tags_sociales': ['rural']}
nna_list = [
    {'id': 'NNA001','edad':3,'idiomas':['es'],'tipo_adopcion':'nacional','disponibilidad':True,'tags_sociales':['rural']},
    {'id': 'NNA002','edad':7,'idiomas':['es'],'tipo_adopcion':'internacional','disponibilidad':True,'tags_sociales':['urbano']}
]
print("Recomendaciones:", agente.preseleccionar(adoptante, nna_list))

# 2Priorización
cases = [{'id':'C1','riesgo_salud':0.9,'riesgo_psicologico':0.2,'abandono_previos':True,'edad':1,'condiciones_vulnerables':True}]
print("Casos Prioritarios:", agente.priorizar_casos(cases))

#  Clasificador documentos
agente.doc_classifier.train([
    ("Certificado de nacimiento original", "valido"),
    ("Fotocopia borrosa sin sello", "invalido")
])
print("Documento:", agente.clasificar_documento("Certificado de nacimiento firmado"))

#  Chatbot
agente.chatbot = agente.chatbot.__class__([
    ("¿Qué documentos necesito?", "Debe presentar su certificado de nacimiento, CI y formulario de solicitud."),
])
print("Chatbot:", agente.responder_pregunta("Qué documentos se requieren?"))

# Recordatorios
when = datetime.utcnow() + timedelta(seconds=2)
agente.programar_recordatorio(when, "Entrega de informes mañana", {"nombre": "Trabajadora Social"})
print("Esperando recordatorios...")
time.sleep(3)
print("Recordatorios vencidos:", agente.scheduler.due())
