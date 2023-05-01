# Funciones necesarias para extraer los comentarios, analizarlos y 
# mostrarlos en pantalla
from pysentimiento import create_analyzer # libreria para analizar los comentarios
from google_play_scraper import Sort, reviews, app # libreria para extrar comentarios de Play Store

#Función para obtener los comentarios de la Play Store
def obtener_comentarios(appId,totalComentarios):
    comentarios = []
    resultados, continuation_token = reviews(
    appId,
    lang='es', # defaults to 'en'
    country='mx', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=totalComentarios, # defaults to 100
    )
# Obtener el nombre de la aplicación por el app ID que fue ingresado
    resultado_nombre = app(
    appId,
    lang='es', # defaults to 'en'
    country='mx' # defaults to 'us'
    )
# Agregar comentarios y nombre de la app en arreglo
# en la primera posición se agrega el nombre de aplicación
# despues se agregan los comentarios obtenidos
    comentarios.append(resultado_nombre["title"])
    for resultado in resultados:
        comentarios.append(resultado["content"])
    return comentarios

#Función para obtener la polaridad de cada comentario y agregarlo en arreglo
def polaridades(comentarios, total_comentarios):
    polaridad = []
    analyzer = create_analyzer(task="sentiment", lang="es")
    for i in range (1, total_comentarios+1):
        pol = analyzer.predict(comentarios[i]).output
        polaridad.append(pol)
    return polaridad

#Función para contabilizar cuantos son positivos, negativos, neutros y agregar resultados en arreglo                
def polaridad_total(polaridades):
    resultados_polaridad = []
    positivo = 0
    negativo = 0
    neutro = 0
    for polaridad in polaridades:
        if polaridad == "POS":
            positivo += 1
        elif polaridad == "NEU":
            neutro += 1
        elif polaridad == "NEG":
            negativo += 1
    resultados_polaridad.append(positivo)
    resultados_polaridad.append(neutro)
    resultados_polaridad.append(negativo) 
    return resultados_polaridad

# función para contabilizar y predecir la emoción de cada comentario y obtener los resultados en un arreglo
def emocion(comentarios):
    emociones = []
    joy = 0
    others = 0
    surprise = 0
    sadness = 0
    fear = 0
    anger = 0
    disgust = 0
    emotion_analyzer = create_analyzer(task="emotion", lang="es")
    for comentario in comentarios:
        resultado = emotion_analyzer.predict(comentario)
        emociones.append(resultado.output)
        if resultado.output == "joy":
            joy+=1
        elif resultado.output == "others":
            others+=1
        elif resultado.output == "surprise":
            surprise+=1
        elif resultado.output == "sadness":
            sadness+=1
        elif resultado.output == "fear":
            fear+=1
        elif resultado.output == "anger":
            anger+=1
        elif resultado.output == "disgust":
            disgust+=1
#Función para detectar el sentimiento que fue mas frecuente y mostrarlo como resultado, asi como traducirlas al español    
    emociones_resultados = {
        'Alegría': joy,
        'No definido': others,
        'Sorpresa': surprise,
        'Trsiteza': sadness,
        'Miedo': fear,
        'Enojo': anger,
        'Disgusto': disgust
    }
    valores = list(emociones_resultados.values())
    llaves = list(emociones_resultados.keys())
    return llaves[valores.index(max(valores))]  
