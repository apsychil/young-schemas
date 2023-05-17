def test():
    """Este código se puede sintetizar mucho más... Una función que tenga como parámetros esquema y una lista con todas las preguntas
    """
    preguntas = [
    "Las personas no han estado ahí para satisfacer mis necesidades emocionales.",
    "No he recibido amor y atención.",
    "La mayor parte del tiempo, no he tenido a nadie que me brinde consejo y apoyo emocional.",
    "La mayor parte del tiempo, no he tenido a nadie que me cuide, que comparta conmigo, o que se preocupe profundamente por todo lo que me pasa.",
    "Por mucho tiempo de mi vida, no he tenido a nadie que quisiera estar estrechamente ligado a mí, y compartir mucho tiempo conmigo.",
    "En general, las personas no han estado ahí para darme calidez, apoyo y afecto.",
    "Por mucho tiempo de mi vida no he sentido que sea especial para nadie.",
    "La mayor parte del tiempo no he tenido a nadie que realmente me escuche, me comprenda o esté sintonizado con mis verdaderas necesidades y sentimientos.",
    "Rara vez he tenido una persona fuerte que me brinde consejos sabios o dirección cuando no estoy seguro de qué hacer.",
    "Me preocupa que las personas a quienes quiero mueran pronto, aun cuando existen muy pocas razones médicas que sustenten mi preocupación.",
    "Me descubro a mí mismo(a) aferrándome a las personas de quienes estoy cerca, porque temo que me abandonen.",
    "Me preocupa que las personas a quienes me siento cercano me dejen o me abandonen.",
    "Siento que me falta una base estable de apoyo emocional.",
    "No siento que las relaciones interpersonales importantes vayan a durar. Tengo la expectativa que ellas se acabarán.",
    "Me siento adicto(a) a parejas que no pueden estar ahí para mí en forma comprometida.",
    "Al final, estaré solo(a).",
    "Cuando siento que alguien que me importa está tratando de alejarse de mí, me desespero.",
    "Algunas veces estoy tan preocupado(a) de que las personas vayan a abandonarme, que termino alejándolas.",
    "Me aflijo cuando alguien me deja solo(a), aun por un corto período de tiempo.",
    "No puedo contar con que las personas que me apoyan estén presentes en forma consistente.",
    "No me permito acercarme de verdad a otras personas, ya que no puedo estar seguro(a) de que estarán ahí para siempre.",
    "Pareciera que las personas importantes en mi vida siempre están yendo y viniendo.",
    "Me preocupa muchísimo que las personas a quienes quiero encuentren a alguien más a quien prefieran, y me dejen.",
    "Las personas que han estado cerca de mí han sido muy impredecibles, unas veces están disponibles y cariñosas conmigo y al minuto están enojadas, molestas, peleando, etc.",
    "Necesito tanto a las otras personas que me preocupo acerca de la posibilidad de perderlas.",
    "Me siento tan indefenso(a) si no tengo personas que me protejan, que me preocupa mucho perderlas.",
    "No puedo ser yo mismo(a) o expresar lo que en realidad siento, porque las personas me abandonarán.",
    "Siento que las personas se aprovecharán de mí.",
    "Con frecuencia siento que tengo que protegerme de otras personas.",
    "Siento que no puedo bajar la guardia en presencia de otras personas, porque de otra manera van a herirme intencionalmente.",
    "Si alguien se comporta muy amable conmigo, asumo que esa persona debe estar buscando algo.",
    "Es sólo cuestión de tiempo antes de que alguien me traicione.",
    "La mayoría de las personas sólo piensan en sí mismas.",
    "Me da una gran dificultad confiar en la gente.",
    "Sospecho mucho de las intenciones de las otras personas.",
    "Las otras personas muy rara vez son honestas; generalmente no son lo que parecen.",
    "Usualmente estoy en la búsqueda de las verdaderas intenciones de los demás.",
    "Si pienso que alguien va a herirme, trato de herirla(o) primero.",
    "Normalmente las personas me tienen que demostrar mucho antes de que yo pueda confiar en ellas.",
    "Les pongo 'pruebas' a los demás para ver si me están diciendo la verdad y si son bien intencionados.",
    "Me identifico con la creencia 'controla o serás controlado'.",
    "Me enojo cuando pienso en las distintas formas en que he sido maltratado(a) por las otras personas a lo largo de mi vida.",
    "A lo largo de mi vida, aquellas personas cercanas a mí se han aprovechado o me han usado para sus propósitos.",
    "He sido abusado(a) sexual, emocional o físicamente por personas importantes en mi vida.",
    "No encajo.",
    "Soy fundamentalmente diferente de las otras personas.",
    "No pertenezco; soy un solitario.",
    "Me siento alejado de otras personas.",
    "Me siento aislado y sólo(a).",
    "Siempre me siento ajeno a los grupos.",
    "Nadie en realidad me comprende.",
    "Mi familia siempre fue diferente de las otras familias que nos rodeaban.",
    "Algunas veces me siento como si fuera un extraterrestre.",
    "Si desapareciera mañana, nadie lo notaría.",
    "Ninguna persona a quien yo deseara podría amarme si viera mis defectos.",
    "Nadie a quien yo quisiera desearía permanecer cerca de mí si conociera mi verdadero yo.",
    "Yo soy inherentemente imperfecto y defectuoso.",
    "No importa qué tanto lo intente, siento que no seré capaz de conseguir una persona significativa que me respete o que sienta que soy valioso.",
    "No merezco el respeto, la atención y el amor de los demás.",
    "Siento que no soy digno de ser amado.",
    "Soy demasiado inaceptable en muchos aspectos básicos como para revelarme ante otras personas.",
    "Si los demás se dieran cuenta de mis defectos básicos, no podría darles la cara.",
    "Cuando le gusto a las personas, siento que las estoy engañando.",
    "Con frecuencia me descubro a mí mismo atraído por personas muy críticas o que me rechazan.",
    "Tengo secretos muy personales que no quiero que las personas cercanas a mí los descubran.",
    "Es culpa mía que mis padres no pudieran amarme lo suficiente.",
    "No permito que las personas conozcan mi verdadero yo.",
    "Uno de mis mayores miedos es que mis defectos queden al descubierto.",
    "No puedo entender cómo alguien podría amarme.",
    "No soy sexualmente atractivo.",
    "Soy demasiado gordo.",
    "Soy feo.",
    "No soy capaz de mantener una conversación normal.",
    "Soy soso y aburrido en situaciones sociales.",
    "Personas que considero valiosas no se relacionarían conmigo, por mi posición social (por ejemplo, ingresos, nivel educativo, carrera, entre otros).",
    "Nunca sé qué decir en situaciones sociales.",
    "Las personas no quieren incluirme en sus grupos.",
    "Soy demasiado consciente de mí mismo cuando estoy con otras personas.",
    "Casi nada de lo que hago en mi trabajo (o estudio) es tan bueno como lo pueden hacer otras personas.",
    "Soy incompetente cuando de logros se trata.",
    "La mayoría de las personas son más capaces que yo en las áreas de trabajo y logro.",
    "Soy un fracaso.",
    "No soy tan talentoso como la mayoría de personas en su trabajo.",
    "No soy tan inteligente como la mayoría de las personas en lo que se refiere al trabajo (o estudio).",
    "Estoy avergonzado por mis inadecuaciones y fracasos en la esfera del trabajo.",
    "Con frecuencia me siento avergonzado cuando estoy con otras personas, ya que yo no estoy a su nivel en términos de logros.",
    "Con frecuencia comparo mis logros con los de los demás y siento que ellos son mucho más exitosos.",
    "No me siento capaz de valerme por mí mismo en la vida diaria.",
    "Necesito que otras personas me ayuden a sostenerme.",
    "No siento que pueda enfrentar bien la vida por mí mismo.",
    "Creo que otras personas pueden ocuparse mejor de mí que lo que yo mismo lo hago.",
    "Tengo problemas emprendiendo nuevas tareas, aparte de mi trabajo, a menos que tenga a alguien que me guíe.",
    "Me veo a mí mismo como una persona dependiente cuando del funcionamiento de la vida diaria se trata.",
    "Echo a perder todo lo que intento aún cosas por fuera del trabajo o la escuela.",
    "Soy incapaz en la mayoría de los aspectos de mi vida.",
    "Si confío en mi propio juicio en situaciones cotidianas, tomaré malas decisiones.",
    "Me falta sentido común.",
    "En las situaciones cotidianas, no se puede confiar en mi juicio.",
    "No me siento seguro de mi habilidad para resolver problemas cotidianos cuando estos se presentan.",
    "Siento que necesito a alguien en quien pueda confiar para darme consejo sobre los problemas prácticos.",
    "Me siento más como un niño que como un adulto cuando se trata de las responsabilidades cotidianas.",
    "Encuentro agobiantes las responsabilidades de la vida cotidiana",
    "No puedo escapar al sentimiento de que algo malo está a punto de pasar.",
    "Siento que un desastre (natural, delictivo, financiero o médico) podría golpearme en cualquier momento.",
    "Me preocupa volverme un indigente o vago.",
    "Me preocupa ser atacado.",
    "Siento que debo tener mucho cuidado con el dinero porque de otra manera podría terminar sin nada, en la ruina.",
    "Tomo grandes precauciones para evitar enfermarme o herirme.",
    "Me preocupa perder todo mi dinero y volverme indigente.",
    "Me preocupa estar desarrollando una enfermedad grave aún cuando nada serio haya sido diagnosticado por un médico.",
    "Soy una persona temerosa.",
    "Me preocupa mucho la cantidad de cosas malas que ocurren en el mundo: contaminación, crímenes, entre otros.",
    "Con frecuencia siento que podría enloquecerme.",
    "Con frecuencia siento que voy a tener un ataque de ansiedad.",
    "Con frecuencia me preocupa llegar a tener un ataque al corazón, aún cuando hay muy poca evidencia médica para estarlo.",
    "Siento que el mundo es un lugar peligroso.",
    "No parezco haber sido capaz de separarme de mis padres del mismo modo que otras personas de mi edad parecen haberlo hecho.",
    "Mis padres y yo tendemos a involucrarnos demasiado en la vida y problemas de cada uno.",
    "Es muy difícil tanto para mis padres como para mí, callar detalles íntimos sin sentirnos traicionados o culpables.",
    "Mis padres y yo tenemos que hablarnos casi a diario o de otra manera alguno se sentirá culpable, lastimado, decepcionado o solo.",
    "Con frecuencia siento que no tengo una identidad separada de mis padres o mi compañero(a).",
    "Con frecuencia siento como si mis padres estuvieran viviendo a través mío o que no tengo una vida propia.",
    "Es muy difícil para mí tomar distancia de las personas con quienes intim o. Me da dificultad conservar un sentido de mí mismo separado de ellas.",
    "Estoy tan involucrado con mis padres o compañero(a) que en realidad no sé quién soy o qué quiero.",
    "Tengo dificultades en separar mi punto de vista u opinión de las de mis padres o compañero(a).",
    "Con frecuencia siento que no tengo intimidad cuando se trata de mis padres o compañero(a).",
    "Siento que mis padres se sienten o se sentirían muy lastimados y ofendidos si yo viviera solo por mis propios medios, lejos de ellos.",
    "Permito que otras personas hagan lo que quieran, porque temo las consecuencias.",
    "Pienso que si hago lo que quiero, sólo estaría buscando problemas.",
    "Siento que no tengo otra opción que rendirme a los deseos de otras personas, o de otra manera ellos se vengarán o me rechazarán de alguna forma.",
    "En relaciones interpersonales, yo dejo que la otra persona tome la delantera.",
    "Siempre he permitido que otros tomen decisiones por mí, de tal forma que en realidad no se lo que quiero para mí mismo.",
    "Siento que las principales decisiones de mi vida no fueron mías realmente.",
    "Me preocupa mucho complacer a otros, para que no me rechacen.",
    "Me cuesta mucho trabajo exigir que mis derechos sean respetados y que mis sentimientos sean tenidos en cuenta.",
    "Recrimino a las personas de maneras sutiles en lugar de mostrar mi enojo.",
    "Voy mucho más lejos que la mayoría de las personas para evitar confrontaciones.",
    "Pongo las necesidades de los demás antes que las mías o de otra manera me siento culpable.",
    "Me siento culpable cuando traiciono o decepciono a otras personas.",
    "Le doy más a los demás de lo que recibo a cambio.",
    "Usualmente soy el (la) que termino cuidando a las personas a quienes tengo cerca.",
    "Podría soportarlo casi todo si amara a alguien.",
    "Soy una buena persona porque pienso en los demás más que en mí mismo.",
    "En el trabajo, soy el (la) que usualmente se ofrece voluntariamente a hacer tareas extras o dar tiempo extra.",
    "No importa que tan ocupada(o) esté, siempre puedo encontrar tiempo para otros.",
    "Puedo conformarme con muy poco, ya que mis necesidades son mínimas.",
    "Solo soy feliz cuando los demás a mi alrededor están felices.",
    "Estoy tan ocupada(o) haciendo cosas por las personas que me son importantes, que tengo muy poco tiempo para mí.",
    "Siempre he sido quien escucha los problemas de todo el mundo.",
    "Estoy más cómodo(a) dando un regalo que recibiéndolo.",
    "Los demás me ven demasiado entregado a otros y no lo suficiente a mí mismo.",
    "No importa cuánto de, nunca es suficiente.",
    "Si hago lo que yo quiero, me siento muy incómodo(a).",
    "Me es muy difícil pedir a otros ayuda cuando tengo necesidades.",
    "Me preocupa perder el control de mis acciones.",
    "Me preocupa seriamente causarle daño físico o emocional a alguien, si mi enojo me hace perder el control.",
    "Siento que tengo que controlar mis impulsos o emociones, o es probable que ocurra algo malo.",
    "Hay mucha cantidad de ira y resentimiento creciendo al interior mío, y no soy capaz de expresarlo.",
    "Estoy demasiado conciente de mostrar mis sentimientos positivos hacia los demás (mostrar consideración, afecto, que los demás me importan).",
    "Encuentro embarazoso expresar mis sentimientos a los demás.",
    "Encuentro difícil ser cálido y espontáneo.",
    "Me controlo a mí mismo(a), tanto que los demás creen que yo no tengo emociones.",
    "La gente me ve como reconcentrado emocionalmente (cerrado, hermético).",
    "Tengo que ser el (la) mejor en lo que haga.",
    "Me esfuerzo por mantener casi todo en perfecto orden.",
    "Tengo que parecer el (la), mejor, la mayor parte del tiempo.",
    "Trato de hacer lo mejor. No puedo conformarme con los suficientemente bueno.",
    "Tengo tanto para hacer, que casi no tengo tiempo para relajarme.",
    "Casi nada de lo que haga es lo suficientemente bueno; siempre puedo hacerlo mejor.",
    "Tengo que cumplir con todas mis responsabilidades.",
    "Siento que existe constante presión en cuanto a logro y llevar las cosas a cabo.",
    "Mis relaciones interpersonales sufren porque yo exijo mucho.",
    "Mi salud está sufriendo porque ejerzo demasiada presión para hacer las cosas bien.",
    "Con frecuencia sacrifico placer y felicidad para alcanzar mis propios estándares.",
    "Cuando cometo errores, me merezco fuertes críticas.",
    "No me permito desatenderme de los errores o tener excusas que los justifiquen.",
    "Soy una persona muy competitiva.",
    "Le doy un gran énfasis al dinero y al estatus.",
    "En términos de mi ejecución, tengo que ser siempre el número uno.",
    "Me cuesta aceptar un 'no' como respuesta cuando quiero algo de las demás personas.",
    "A menudo me enojo y me irrito si no puedo conseguir lo que quiero.",
    "Soy especial y no tendría por qué aceptar muchas de las restricciones que tienen las demás personas.",
    "Odio sentirme restringido que se me impida hacer lo que quiero.",
    "Siento que no tengo porqué seguir las reglas normales y otras convenciones que las personas tienen.",
    "Tengo la sensación de que lo que ofrezco es más especial que lo que ofrecen las otras personas.",
    "Usualmente pongo mis necesidades por encima de las otras personas.",
    "Con frecuencia estoy tan involucrado(a) en mis propias prioridades, que no tengo tiempo para darle a la familia o a los amigos.",
    "A menudo la gente me dice que soy controlador(a) de la manera como se hacen las cosas.",
    "Me irrito mucho cuando las personas no hacen lo que les pido.",
    "No puedo tolerar que otras personas me digan lo que tengo que hacer.",
    "Tengo gran dificultad para convencerme de dejar de beber, de fumar, de comer en exceso u otros problemas de comportamiento.",
    "Parece que no puedo disciplinarme a mí mismo(a) para completar tareas rutinarias o aburridas.",
    "Con frecuencia me dejo llevar por mis impulsos y expreso emociones que me generan problemas o hieren a otras personas.",
    "Si yo no consigo una meta, me frustro fácilmente y la abandono.",
    "Es para mí muy difícil sacrificar la satisfacción inmediata para alcanzar una meta a largo plazo.",
    "A menudo me pasa que una vez empiezo a sentirme enojado ya no puedo controlarlo.",
    "Tiendo a hacer las cosas en exceso aún cuando sé que son malas para mí.",
    "Me aburro fácilmente.",
    "Cuando las tareas se vuelven difíciles, normalmente no puedo perseverar para completarlas.",
    "No me puedo controlar en nada por mucho tiempo.",
    "No me puedo forzar a hacer las cosas que no disfruto, aún cuando sé que son por mi bien.",
    "Pierdo mi paciencia a la menor ofensa.",
    "Rara vez he sido capaz de cumplir lo que he dicho.",
    "Casi nunca me privo de mostrarle a las personas cómo me siento en realidad, sin importar lo que me pueda costar.",
    "Con frecuencia hago cosas impulsivamente y luego me arrepiento."
    ]
    pregunta_range = range(0,206)
    deprivacion_emocional_total = 0
    for pregunta in preguntas[0:10]:
        while True:
            try:
                deprivacion_emocional = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if deprivacion_emocional < 1 or deprivacion_emocional > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        deprivacion_emocional_total += deprivacion_emocional
            
            
    abandono_inestabilidad_total = 0
    for pregunta in preguntas[10:28]:
        while True:
            try:
                abandono_inestabilidad = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if abandono_inestabilidad < 1 or abandono_inestabilidad > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        abandono_inestabilidad_total += abandono_inestabilidad  
            
    desconfianza_abuso_total = 0
    for pregunta in preguntas[28:45]:
        while True:
            try:
                desconfianza_abuso = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if desconfianza_abuso < 1 or desconfianza_abuso > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        desconfianza_abuso_total += desconfianza_abuso
        
    aislamiento_social_total = 0
    for pregunta in preguntas[45:55]:
        while True:
            try:
                aislamiento_social = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if aislamiento_social < 1 or aislamiento_social > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        aislamiento_social_total += aislamiento_social
        
    verguenza_defectuosidad_total = 0
    for pregunta in preguntas[55:70]:
        while True:
            try:
                verguenza_defectuosidad = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if verguenza_defectuosidad < 1 or verguenza_defectuosidad > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        verguenza_defectuosidad_total += verguenza_defectuosidad
        
    indeseabilidad_social_total = 0
    for pregunta in preguntas[70:79]:
        while True:
            try:
                indeseabilidad_social = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if indeseabilidad_social < 1 or indeseabilidad_social > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        indeseabilidad_social_total += indeseabilidad_social
        
    fracaso_total = 0
    for pregunta in preguntas[79:88]:
        while True:
            try:
                fracaso = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if fracaso < 1 or fracaso > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        fracaso_total += fracaso
        
    dependencia_incompetencia_total = 0
    for pregunta in preguntas[88:103]:
        while True:
            try:
                dependencia_incompetencia = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if dependencia_incompetencia < 1 or dependencia_incompetencia > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        dependencia_incompetencia_total += dependencia_incompetencia
        
    vulnerabilidad_al_dano_total = 0
    for pregunta in preguntas[103:117]:
        while True:
            try:
                vulnerabilidad_al_dano = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if vulnerabilidad_al_dano < 1 or vulnerabilidad_al_dano > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        vulnerabilidad_al_dano_total += vulnerabilidad_al_dano
        
    entrampamiento_total = 0
    for pregunta in preguntas[117:128]:
        while True:
            try:
                entrampamiento = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if entrampamiento < 1 or entrampamiento > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        entrampamiento_total += entrampamiento
        
    subyugacion_total = 0
    for pregunta in preguntas[128:138]:
        while True:
            try:
                subyugacion = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if subyugacion < 1 or subyugacion > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        subyugacion_total += subyugacion
        
    autosacrificio_total = 0
    for pregunta in preguntas[138:155]:
        while True:
            try:
                autosacrificio = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if autosacrificio < 1 or autosacrificio > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        autosacrificio_total += autosacrificio
        
    inhibicion_emocional_total = 0
    for pregunta in preguntas[158:164]:
        while True:
            try:
                inhibicion_emocional = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if inhibicion_emocional < 1 or inhibicion_emocional > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        inhibicion_emocional_total += inhibicion_emocional
        
    estandares_flexibles_total = 0
    for pregunta in preguntas[164:180]:
        while True:
            try:
                estandares_flexibles = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if estandares_flexibles < 1 or estandares_flexibles > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        estandares_flexibles_total += estandares_flexibles
        
        
    egocentrismo_grandiosidad_total = 0
    for pregunta in preguntas[180:191]:
        while True:
            try:
                egocentrismo_grandiosidad = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if egocentrismo_grandiosidad < 1 or egocentrismo_grandiosidad > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        egocentrismo_grandiosidad_total += egocentrismo_grandiosidad
        
        
    autocontrol_insuficiente_total = 0
    for pregunta in preguntas[191:]:
        while True:
            try:
                autocontrol_insuficiente = int(input(f"\n{pregunta}\nMi respuesta (1-6): "))
                if autocontrol_insuficiente < 1 or autocontrol_insuficiente > 6:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido entre 1 y 6.")
        autocontrol_insuficiente_total += autocontrol_insuficiente

    #Imprimir resultados
    print("*************")
    print("\nResultados:")
    print("*************")
    if deprivacion_emocional_total > 16.56:
        print(f'Tu puntuación fue de {deprivacion_emocional_total}, que está por encima de la media de 16.65. Esto significa que tienes el esquema de Deprivación Emocional ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {deprivacion_emocional_total}, que está por debajo o en la media de 16.65. Esto significa que tienes el esquema de Deprivación Emocional DESACTIVADO.\n')

    if abandono_inestabilidad_total > 37.57:
        print(f'Tu puntuación fue de {abandono_inestabilidad_total}, que está por encima de la media de 37.57. Esto significa que tienes el esquema de Abandono/Inestabilidad ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {abandono_inestabilidad_total}, que está por debajo o en la media de 37.57. Esto significa que tienes el esquema de Abandono/Inestabilidad DESACTIVADO.\n')

    if desconfianza_abuso_total > 37.81:
        print(f'Tu puntuación fue de {desconfianza_abuso_total}, que está por encima de la media de 37.81. Esto significa que tienes el esquema de Desconfianza/Abuso ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {desconfianza_abuso_total}, que está por debajo o en la media de 37.81. Esto significa que tienes el esquema de Desconfianza/Abuso DESACTIVADO.\n')

    if aislamiento_social_total > 21.41:
        print(f'Tu puntuación fue de {aislamiento_social_total}, que está por encima de la media de 21.41. Esto significa que tienes el esquema de Aislamiento Social ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {aislamiento_social_total}, que está por debajo o en la media de 21.41. Esto significa que tienes el esquema de Aislamiento Social DESACTIVADO.\n')

    if verguenza_defectuosidad_total > 25.5:
        print(f'Tu puntuación fue de {verguenza_defectuosidad_total}, que está por encima de la media de 25.5. Esto significa que tienes el esquema de Verguenza/Defectuosidad ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {verguenza_defectuosidad_total}, que está por debajo o en la media de 25.5. Esto significa que tienes el esquema de Verguenza/Defectuosidad DESACTIVADO.\n')

    if indeseabilidad_social_total > 15.42:
        print(f'Tu puntuación fue de {indeseabilidad_social_total}, que está por encima de la media de 15.42. Esto significa que tienes el esquema de Indeseabilidad Social ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {indeseabilidad_social_total}, que está por debajo o en la media de 15.42. Esto significa que tienes el esquema de Indeseabilidad Social DESACTIVADO.\n')

    if fracaso_total > 14.01:
        print(f'Tu puntuación fue de {fracaso_total}, que está por encima de la media de 14.01. Esto significa que tienes el esquema de Fracaso ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {fracaso_total}, que está por debajo o en la media de 14.01. Esto significa que tienes el esquema de Fracaso DESACTIVADO.\n')

    if dependencia_incompetencia_total > 25.08:
        print(f'Tu puntuación fue de {dependencia_incompetencia_total}, que está por encima de la media de 25.08. Esto significa que tienes el esquema de Dependencia/Incompetencia ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {dependencia_incompetencia_total}, que está por debajo o en la media de 25.08. Esto significa que tienes el esquema de Dependencia/Incompetencia DESACTIVADO.\n')

    if vulnerabilidad_al_dano_total > 29.33:
        print(f'Tu puntuación fue de {vulnerabilidad_al_dano_total}, que está por encima de la media de 29.33. Esto significa que tienes el esquema de Vulnerabilidad al daño ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {vulnerabilidad_al_dano_total}, que está por debajo o en la media de 29.33. Esto significa que tienes el esquema de Vulnerabilidad al daño DESACTIVADO.\n')

    if entrampamiento_total > 19.59:
        print(f'Tu puntuación fue de {entrampamiento_total}, que está por encima de la media de 19.59. Esto significa que tienes el esquema de Entrampamiento ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {entrampamiento_total}, que está por debajo o en la media de 19.59. Esto significa que tienes el esquema de Entrampamiento DESACTIVADO.\n')

    if subyugacion_total > 21.49:
        print(f'Tu puntuación fue de {subyugacion_total}, que está por encima de la media de 21.49. Esto significa que tienes el esquema de Subyugación ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {subyugacion_total}, que está por debajo o en la media de 21.49. Esto significa que tienes el esquema de Subyugación DESACTIVADO.\n')

    if autosacrificio_total > 41.21:
        print(f'Tu puntuación fue de {autosacrificio_total}, que está por encima de la media de 41.21. Esto significa que tienes el esquema de Autosacrificio ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {autosacrificio_total}, que está por debajo o en la media de 41.21. Esto significa que tienes el esquema de Autosacrificio DESACTIVADO.\n')

    if inhibicion_emocional_total > 21.49:
        print(f'Tu puntuación fue de {inhibicion_emocional_total}, que está por encima de la media de 21.49. Esto significa que tienes el esquema de Inhibición Emocional ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {inhibicion_emocional_total}, que está por debajo o en la media de 21.49. Esto significa que tienes el esquema de Inhibición Emocional DESACTIVADO.\n')

    if estandares_flexibles_total > 39.6:
        print(f'Tu puntuación fue de {estandares_flexibles_total}, que está por encima de la media de 39.6. Esto significa que tienes el esquema de Estándares Inflexibles ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {estandares_flexibles_total}, que está por debajo o en la media de 39.6. Esto significa que tienes el esquema de Estándares Inflexibles DESACTIVADO.\n')

    if egocentrismo_grandiosidad_total > 26.67:
        print(f'Tu puntuación fue de {egocentrismo_grandiosidad_total}, que está por encima de la media de 26.67. Esto significa que tienes el esquema de Egocentrismo/Grandiosidad ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {egocentrismo_grandiosidad_total}, que está por debajo o en la media de 26.67. Esto significa que tienes el esquema de Egocentrismo/Grandiosidad DESACTIVADO.\n')

    if autocontrol_insuficiente_total > 34.01:
        print(f'Tu puntuación fue de {autocontrol_insuficiente_total}, que está por encima de la media de 34.01. Esto significa que tienes el esquema de Autocontrol/Autodisciplina insuficientes ACTIVADO.\n')
    else:
        print(f'Tu puntuación fue de {autocontrol_insuficiente_total}, que está por debajo o en la media de 34.01. Esto significa que tienes el esquema de Autocontrol/Autodisciplina insuficientes DESACTIVADO.\n')


    print("*************")
    print("\nEstos son tus resultados en formato de tabla:")
    print("*************")
    datos = [
        ("Esquema", "Resultados del cuestionario", "Preguntas", "DS", "LI", "Media", "LS"),
        ("Deprivación emocional", deprivacion_emocional_total, "1 a 9", 7.58, 8.98, 16.56, 24.14),
        ("Abandono/Inestabilidad", abandono_inestabilidad_total, "10 a 27", 13.83, 23.74, 37.57, 51.4),
        ("Desconfianza/Abuso", desconfianza_abuso_total, "28 a 44", 13.93, 23.88, 37.81, 51.74),
        ("Aislamiento social", aislamiento_social_total, "45 a 54", 8.48, 12.93, 21.41, 29.89),
        ("Verguenza/Defectuosidad", verguenza_defectuosidad_total, "55 a 69", 9.92, 15.58, 25.5, 35.42),
        ("Indeseabilidad social", indeseabilidad_social_total, "70 a 78", 5.28, 10.14, 15.42, 20.7),
        ("Fracaso", fracaso_total, "79 a 87", 5.52, 8.49, 14.01, 19.53),
        ("Dependencia/Incompetencia", dependencia_incompetencia_total, "88 a 102", 8.3, 16.78, 25.08, 33.38),
        ("Vulnerabilidad al daño", vulnerabilidad_al_dano_total, "103 a 116", 10.27, 19.06, 29.33, 39.6),
        ("Entrampamiento", entrampamiento_total, "117 a 127", 7.57, 12.02, 19.59, 27.16),
        ("Subyugación", subyugacion_total, "128 a 137", 6.41, 14.55, 21.49, 28.43),
        ("Autosacrificio", autosacrificio_total, "138 a 154", 13.55, 27.66, 41.21, 54.76),
        ("Inhibición emocional", inhibicion_emocional_total, "155 a 163", 6.94, 14.55, 21.49, 28.43),
        ("Estándares inflexibles", estandares_flexibles_total, "164 a 179", 12.11, 27.49, 39.6, 51.71),
        ("Egocentrismo/Grandiosidad", egocentrismo_grandiosidad_total, "180 a 190", 9.35, 17.32, 26.67, 36.05),
        ("Autocontrol/Autodisciplina insuficientes", autocontrol_insuficiente_total, "191 a 205", 11.11, 22.9, 34.01, 45.12),
    ]
    
    #Imprimir la tabla de resultados
    for fila in datos:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*fila))
    print("\n"*5)
    print("Recuerda que la validez de estos resultados se basan en el siguiente estudio: https://www.redalyc.org/articulo.oa?id=80537307")
    print("\n"*5)



if __name__ == "__main__":
   print("*************"*3)
   print("Bienvenido al Cuestionario de Esquemas de Jeffrey Young")
   print("*************"*3)
   print("\n")
   print("""INSTRUCCIONES: Encontrará aquí una serie de afirmaciones enumeradas que una persona podría usar para describirse a sí misma. Por favor lea cada frase y decida qué tan bien le describe. Cuando no esté seguro(a), base su respuesta más en lo que usted siente en lugar de lo que piensa que sea correcto. Elija el puntaje de 1 a 6 que mejor lo(a) describa, según la siguiente escala:\n""")
   print("""
    1.   Completamente falso de mí. 								
    2.   La mayor parte falso de mí.  								
    3.   Ligeramente más verdadero que falso.      								
    4.   Moderadamente verdadero de mí.								
    5.   La mayor parte verdadero de mí.								
    6.   Me describe perfectamente.								
    """)
   print("\nLas preguntas se muestran a continuación:\n")
   test()