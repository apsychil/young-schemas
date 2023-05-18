from tabulate import tabulate

def test():
    """Este código se puede sintetizar mucho más... Una función que tenga como parámetros esquema y una lista con todas las preguntas
    """
    preguntas = [
    "1. Las personas no han estado ahí para satisfacer mis necesidades emocionales.",
    "2. No he recibido amor y atención.",
    "3. La mayor parte del tiempo, no he tenido a nadie que me brinde consejo y apoyo emocional.",
    "4. La mayor parte del tiempo, no he tenido a nadie que me cuide, que comparta conmigo, o que se preocupe profundamente por todo lo que me pasa.",
    "5. Por mucho tiempo de mi vida, no he tenido a nadie que quisiera estar estrechamente ligado a mí, y compartir mucho tiempo conmigo.",
    "6. En general, las personas no han estado ahí para darme calidez, apoyo y afecto.",
    "7. Por mucho tiempo de mi vida no he sentido que sea especial para nadie.",
    "8. La mayor parte del tiempo no he tenido a nadie que realmente me escuche, me comprenda o esté sintonizado con mis verdaderas necesidades y sentimientos.",
    "9. Rara vez he tenido una persona fuerte que me brinde consejos sabios o dirección cuando no estoy seguro de qué hacer.",
    "10. Me preocupa que las personas a quienes quiero mueran pronto, aun cuando existen muy pocas razones médicas que sustenten mi preocupación.",
    "11. Me descubro a mí mismo(a) aferrándome a las personas de quienes estoy cerca, porque temo que me abandonen.",
    "12. Me preocupa que las personas a quienes me siento cercano me dejen o me abandonen.",
    "13. Siento que me falta una base estable de apoyo emocional.",
    "14. No siento que las relaciones interpersonales importantes vayan a durar. Tengo la expectativa que ellas se acabarán.",
    "15. Me siento adicto(a) a parejas que no pueden estar ahí para mí en forma comprometida.",
    "16. Al final, estaré solo(a).",
    "17. Cuando siento que alguien que me importa está tratando de alejarse de mí, me desespero.",
    "18. Algunas veces estoy tan preocupado(a) de que las personas vayan a abandonarme, que termino alejándolas.",
    "19. Me aflijo cuando alguien me deja solo(a), aun por un corto período de tiempo.",
    "20. No puedo contar con que las personas que me apoyan estén presentes en forma consistente.",
    "21. No me permito acercarme de verdad a otras personas, ya que no puedo estar seguro(a) de que estarán ahí para siempre.",
    "22. Pareciera que las personas importantes en mi vida siempre están yendo y viniendo.",
    "23. Me preocupa muchísimo que las personas a quienes quiero encuentren a alguien más a quien prefieran, y me dejen.",
    "24. Las personas que han estado cerca de mí han sido muy impredecibles, unas veces están disponibles y cariñosas conmigo y al minuto están enojadas, molestas, peleando, etc.",
    "25. Necesito tanto a las otras personas que me preocupo acerca de la posibilidad de perderlas.",
    "26. Me siento tan indefenso(a) si no tengo personas que me protejan, que me preocupa mucho perderlas.",
    "27. No puedo ser yo mismo(a) o expresar lo que en realidad siento, porque las personas me abandonarán.",
    "28. Siento que las personas se aprovecharán de mí.",
    "29. Con frecuencia siento que tengo que protegerme de otras personas.",
    "30. Siento que no puedo bajar la guardia en presencia de otras personas, porque de otra manera van a herirme intencionalmente.",
    "31. Si alguien se comporta muy amable conmigo, asumo que esa persona debe estar buscando algo.",
    "32. Es sólo cuestión de tiempo antes de que alguien me traicione.",
    "33. La mayoría de las personas sólo piensan en sí mismas.",
    "34. Me da una gran dificultad confiar en la gente.",
    "35. Sospecho mucho de las intenciones de las otras personas.",
    "36. Las otras personas muy rara vez son honestas; generalmente no son lo que parecen.",
    "37. Usualmente estoy en la búsqueda de las verdaderas intenciones de los demás.",
    "38. Si pienso que alguien va a herirme, trato de herirla(o) primero.",
    "39. Normalmente las personas me tienen que demostrar mucho antes de que yo pueda confiar en ellas.",
    "40. Les pongo 'pruebas' a los demás para ver si me están diciendo la verdad y si son bien intencionados.",
    "41. Me identifico con la creencia 'controla o serás controlado'.",
    "42. Me enojo cuando pienso en las distintas formas en que he sido maltratado(a) por las otras personas a lo largo de mi vida.",
    "43. A lo largo de mi vida, aquellas personas cercanas a mí se han aprovechado o me han usado para sus propósitos.",
    "44. He sido abusado(a) sexual, emocional o físicamente por personas importantes en mi vida.",
    "45. No encajo.",
    "46. Soy fundamentalmente diferente de las otras personas.",
    "47. No pertenezco; soy un solitario.",
    "48. Me siento alejado de otras personas.",
    "49. Me siento aislado y sólo(a).",
    "50. Siempre me siento ajeno a los grupos.",
    "51. Nadie en realidad me comprende.",
    "52. Mi familia siempre fue diferente de las otras familias que nos rodeaban.",
    "53. Algunas veces me siento como si fuera un extraterrestre.",
    "54. Si desapareciera mañana, nadie lo notaría.",
    "55. Ninguna persona a quien yo deseara podría amarme si viera mis defectos.",
    "56. Nadie a quien yo quisiera desearía permanecer cerca de mí si conociera mi verdadero yo.",
    "57. Yo soy inherentemente imperfecto y defectuoso.",
    "58. No importa qué tanto lo intente, siento que no seré capaz de conseguir una persona significativa que me respete o que sienta que soy valioso.",
    "59. No merezco el respeto, la atención y el amor de los demás.",
    "60. Siento que no soy digno de ser amado.",
    "61. Soy demasiado inaceptable en muchos aspectos básicos como para revelarme ante otras personas.",
    "62. Si los demás se dieran cuenta de mis defectos básicos, no podría darles la cara.",
    "63. Cuando le gusto a las personas, siento que las estoy engañando.",
    "64. Con frecuencia me descubro a mí mismo atraído por personas muy críticas o que me rechazan.",
    "65. Tengo secretos muy personales que no quiero que las personas cercanas a mí los descubran.",
    "66. Es culpa mía que mis padres no pudieran amarme lo suficiente.",
    "67. No permito que las personas conozcan mi verdadero yo.",
    "68. Uno de mis mayores miedos es que mis defectos queden al descubierto.",
    "69. No puedo entender cómo alguien podría amarme.",
    "70. No soy sexualmente atractivo.",
    "71. Soy demasiado gordo.",
    "72. Soy feo.",
    "73. No soy capaz de mantener una conversación normal.",
    "74. Soy soso y aburrido en situaciones sociales.",
    "75. Personas que considero valiosas no se relacionarían conmigo, por mi posición social (por ejemplo, ingresos, nivel educativo, carrera, entre otros).",
    "76. Nunca sé qué decir en situaciones sociales.",
    "77. Las personas no quieren incluirme en sus grupos.",
    "78. Soy demasiado consciente de mí mismo cuando estoy con otras personas.",
    "79. Casi nada de lo que hago en mi trabajo (o estudio) es tan bueno como lo pueden hacer otras personas.",
    "80. Soy incompetente cuando de logros se trata.",
    "81. La mayoría de las personas son más capaces que yo en las áreas de trabajo y logro.",
    "82. Soy un fracaso.",
    "83. No soy tan talentoso como la mayoría de personas en su trabajo.",
    "84. No soy tan inteligente como la mayoría de las personas en lo que se refiere al trabajo (o estudio).",
    "85. Estoy avergonzado por mis inadecuaciones y fracasos en la esfera del trabajo.",
    "86. Con frecuencia me siento avergonzado cuando estoy con otras personas, ya que yo no estoy a su nivel en términos de logros.",
    "87. Con frecuencia comparo mis logros con los de los demás y siento que ellos son mucho más exitosos.",
    "88. No me siento capaz de valerme por mí mismo en la vida diaria.",
    "89. Necesito que otras personas me ayuden a sostenerme.",
    "90. No siento que pueda enfrentar bien la vida por mí mismo.",
    "91. Creo que otras personas pueden ocuparse mejor de mí que lo que yo mismo lo hago.",
    "92. Tengo problemas emprendiendo nuevas tareas, aparte de mi trabajo, a menos que tenga a alguien que me guíe.",
    "93. Me veo a mí mismo como una persona dependiente cuando del funcionamiento de la vida diaria se trata.",
    "94. Echo a perder todo lo que intento aún cosas por fuera del trabajo o la escuela.",
    "95. Soy incapaz en la mayoría de los aspectos de mi vida.",
    "96. Si confío en mi propio juicio en situaciones cotidianas, tomaré malas decisiones.",
    "97. Me falta sentido común.",
    "98. En las situaciones cotidianas, no se puede confiar en mi juicio.",
    "99. No me siento seguro de mi habilidad para resolver problemas cotidianos cuando estos se presentan.",
    "100. Siento que necesito a alguien en quien pueda confiar para darme consejo sobre los problemas prácticos.",
    "101. Me siento más como un niño que como un adulto cuando se trata de las responsabilidades cotidianas.",
    "102. Encuentro agobiantes las responsabilidades de la vida cotidiana",
    "103. No puedo escapar al sentimiento de que algo malo está a punto de pasar.",
    "104. Siento que un desastre (natural, delictivo, financiero o médico) podría golpearme en cualquier momento.",
    "105. Me preocupa volverme un indigente o vago.",
    "106. Me preocupa ser atacado.",
    "107. Siento que debo tener mucho cuidado con el dinero porque de otra manera podría terminar sin nada, en la ruina.",
    "108. Tomo grandes precauciones para evitar enfermarme o herirme.",
    "109. Me preocupa perder todo mi dinero y volverme indigente.",
    "110. Me preocupa estar desarrollando una enfermedad grave aún cuando nada serio haya sido diagnosticado por un médico.",
    "111. Soy una persona temerosa.",
    "112. Me preocupa mucho la cantidad de cosas malas que ocurren en el mundo: contaminación, crímenes, entre otros.",
    "113. Con frecuencia siento que podría enloquecerme.",
    "114. Con frecuencia siento que voy a tener un ataque de ansiedad.",
    "115. Con frecuencia me preocupa llegar a tener un ataque al corazón, aún cuando hay muy poca evidencia médica para estarlo.",
    "116. Siento que el mundo es un lugar peligroso.",
    "117. No parezco haber sido capaz de separarme de mis padres del mismo modo que otras personas de mi edad parecen haberlo hecho.",
    "118. Mis padres y yo tendemos a involucrarnos demasiado en la vida y problemas de cada uno.",
    "119. Es muy difícil tanto para mis padres como para mí, callar detalles íntimos sin sentirnos traicionados o culpables.",
    "120. Mis padres y yo tenemos que hablarnos casi a diario o de otra manera alguno se sentirá culpable, lastimado, decepcionado o solo.",
    "121. Con frecuencia siento que no tengo una identidad separada de mis padres o mi compañero(a).",
    "122. Con frecuencia siento como si mis padres estuvieran viviendo a través mío o que no tengo una vida propia.",
    "123. Es muy difícil para mí tomar distancia de las personas con quienes intim o. Me da dificultad conservar un sentido de mí mismo separado de ellas.",
    "124. Estoy tan involucrado con mis padres o compañero(a) que en realidad no sé quién soy o qué quiero.",
    "125. Tengo dificultades en separar mi punto de vista u opinión de las de mis padres o compañero(a).",
    "126. Con frecuencia siento que no tengo intimidad cuando se trata de mis padres o compañero(a).",
    "127. Siento que mis padres se sienten o se sentirían muy lastimados y ofendidos si yo viviera solo por mis propios medios, lejos de ellos.",
    "128. Permito que otras personas hagan lo que quieran, porque temo las consecuencias.",
    "129. Pienso que si hago lo que quiero, sólo estaría buscando problemas.",
    "130. Siento que no tengo otra opción que rendirme a los deseos de otras personas, o de otra manera ellos se vengarán o me rechazarán de alguna forma.",
    "131. En relaciones interpersonales, yo dejo que la otra persona tome la delantera.",
    "132. Siempre he permitido que otros tomen decisiones por mí, de tal forma que en realidad no se lo que quiero para mí mismo.",
    "133. Siento que las principales decisiones de mi vida no fueron mías realmente.",
    "134. Me preocupa mucho complacer a otros, para que no me rechacen.",
    "135. Me cuesta mucho trabajo exigir que mis derechos sean respetados y que mis sentimientos sean tenidos en cuenta.",
    "136. Recrimino a las personas de maneras sutiles en lugar de mostrar mi enojo.",
    "137. Voy mucho más lejos que la mayoría de las personas para evitar confrontaciones.",
    "138. Pongo las necesidades de los demás antes que las mías o de otra manera me siento culpable.",
    "139. Me siento culpable cuando traiciono o decepciono a otras personas.",
    "140. Le doy más a los demás de lo que recibo a cambio.",
    "141. Usualmente soy el (la) que termino cuidando a las personas a quienes tengo cerca.",
    "142. Podría soportarlo casi todo si amara a alguien.",
    "143. Soy una buena persona porque pienso en los demás más que en mí mismo.",
    "144. En el trabajo, soy el (la) que usualmente se ofrece voluntariamente a hacer tareas extras o dar tiempo extra.",
    "145. No importa que tan ocupada(o) esté, siempre puedo encontrar tiempo para otros.",
    "146. Puedo conformarme con muy poco, ya que mis necesidades son mínimas.",
    "147. Solo soy feliz cuando los demás a mi alrededor están felices.",
    "148. Estoy tan ocupada(o) haciendo cosas por las personas que me son importantes, que tengo muy poco tiempo para mí.",
    "149. Siempre he sido quien escucha los problemas de todo el mundo.",
    "150. Estoy más cómodo(a) dando un regalo que recibiéndolo.",
    "151. Los demás me ven demasiado entregado a otros y no lo suficiente a mí mismo.",
    "152. No importa cuánto de, nunca es suficiente.",
    "153. Si hago lo que yo quiero, me siento muy incómodo(a).",
    "154. Me es muy difícil pedir a otros ayuda cuando tengo necesidades.",
    "155. Me preocupa perder el control de mis acciones.",
    "156. Me preocupa seriamente causarle daño físico o emocional a alguien, si mi enojo me hace perder el control.",
    "157. Siento que tengo que controlar mis impulsos o emociones, o es probable que ocurra algo malo.",
    "158. Hay mucha cantidad de ira y resentimiento creciendo al interior mío, y no soy capaz de expresarlo.",
    "159. Estoy demasiado conciente de mostrar mis sentimientos positivos hacia los demás (mostrar consideración, afecto, que los demás me importan).",
    "160. Encuentro embarazoso expresar mis sentimientos a los demás.",
    "161. Encuentro difícil ser cálido y espontáneo.",
    "162. Me controlo a mí mismo(a), tanto que los demás creen que yo no tengo emociones.",
    "163. La gente me ve como reconcentrado emocionalmente (cerrado, hermético).",
    "164. Tengo que ser el (la) mejor en lo que haga.",
    "165. Me esfuerzo por mantener casi todo en perfecto orden.",
    "166. Tengo que parecer el (la), mejor, la mayor parte del tiempo.",
    "167. Trato de hacer lo mejor. No puedo conformarme con los suficientemente bueno.",
    "168. Tengo tanto para hacer, que casi no tengo tiempo para relajarme.",
    "169. Casi nada de lo que haga es lo suficientemente bueno; siempre puedo hacerlo mejor.",
    "170. Tengo que cumplir con todas mis responsabilidades.",
    "171. Siento que existe constante presión en cuanto a logro y llevar las cosas a cabo.",
    "172. Mis relaciones interpersonales sufren porque yo exijo mucho.",
    "173. Mi salud está sufriendo porque ejerzo demasiada presión para hacer las cosas bien.",
    "174. Con frecuencia sacrifico placer y felicidad para alcanzar mis propios estándares.",
    "175. Cuando cometo errores, me merezco fuertes críticas.",
    "176. No me permito desatenderme de los errores o tener excusas que los justifiquen.",
    "177. Soy una persona muy competitiva.",
    "178. Le doy un gran énfasis al dinero y al estatus.",
    "179. En términos de mi ejecución, tengo que ser siempre el número uno.",
    "180. Me cuesta aceptar un 'no' como respuesta cuando quiero algo de las demás personas.",
    "181. A menudo me enojo y me irrito si no puedo conseguir lo que quiero.",
    "182. Soy especial y no tendría por qué aceptar muchas de las restricciones que tienen las demás personas.",
    "183. Odio sentirme restringido que se me impida hacer lo que quiero.",
    "184. Siento que no tengo porqué seguir las reglas normales y otras convenciones que las personas tienen.",
    "185. Tengo la sensación de que lo que ofrezco es más especial que lo que ofrecen las otras personas.",
    "186. Usualmente pongo mis necesidades por encima de las otras personas.",
    "187. Con frecuencia estoy tan involucrado(a) en mis propias prioridades, que no tengo tiempo para darle a la familia o a los amigos.",
    "188. A menudo la gente me dice que soy controlador(a) de la manera como se hacen las cosas.",
    "189. Me irrito mucho cuando las personas no hacen lo que les pido.",
    "190. No puedo tolerar que otras personas me digan lo que tengo que hacer.",
    "191. Tengo gran dificultad para convencerme de dejar de beber, de fumar, de comer en exceso u otros problemas de comportamiento.",
    "192. Parece que no puedo disciplinarme a mí mismo(a) para completar tareas rutinarias o aburridas.",
    "193. Con frecuencia me dejo llevar por mis impulsos y expreso emociones que me generan problemas o hieren a otras personas.",
    "194. Si yo no consigo una meta, me frustro fácilmente y la abandono.",
    "195. Es para mí muy difícil sacrificar la satisfacción inmedia t a para alcanzar una meta a largo plazo.",
    "196. A menudo me pasa que una vez empiezo a sentirme enojado ya no puedo controlarlo.",
    "197. Tiendo a hacer las cosas en exceso aún cuando sé que son malas para mí.",
    "198. Me aburro fácilmente.",
    "199. Cuando las tareas se vuelven difíciles, normalmente no puedo perseverar para completarlas.",
    "200. No me puedo controlar en nada por mucho tiempo.",
    "201. No me puedo forzar a hacer las cosas que no disfruto, aún cuando sé que son por mi bien.",
    "202. Pierdo mi paciencia a la menor ofensa.",
    "203. Rara vez he sido capaz de cumplir lo que he dicho.",
    "204. Casi nunca me privo de mostrarle a las personas cómo me siento en realidad, sin importar lo que me pueda costar.",
    "205. Con frecuencia hago cosas impulsivamente y luego me arrepiento."
    ]
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
    print("\n"*3)
    print("*************")
    print("Resultados:")
    print("*************")
    print("\n"*2)
    
    if deprivacion_emocional_total > 16.56:
        esquema_deprivacion_emocional = "ACTIVADO"
    else:
        esquema_deprivacion_emocional = "DESACTIVADO"
    print(f'Tu puntuación fue de {deprivacion_emocional_total}, (Media = 16.65). Tienes el esquema de Deprivación Emocional {esquema_deprivacion_emocional}.\n')

    if abandono_inestabilidad_total > 37.57:
        esquema_abandono_inestabilidad = "ACTIVADO"
    else:
        esquema_abandono_inestabilidad = "DESACTIVADO"
    print(f'Tu puntuación fue de {abandono_inestabilidad_total}, (Media = 37.57). Tienes el esquema de Abandono/Inestabilidad {esquema_abandono_inestabilidad}.\n')

    if desconfianza_abuso_total > 37.81:
        esquema_desconfianza_abuso = "ACTIVADO"
    else:
        esquema_desconfianza_abuso = "DESACTIVADO"
    print(f'Tu puntuación fue de {desconfianza_abuso_total}, (Media = 37.81). Tienes el esquema de Desconfianza/Abuso {esquema_desconfianza_abuso}.\n')

    if aislamiento_social_total > 21.41:
        esquema_aislamiento_social = "ACTIVADO"
    else:
        esquema_aislamiento_social = "DESACTIVADO"
    print(f'Tu puntuación fue de {aislamiento_social_total}, (Media = 21.41). Tienes el esquema de Aislamiento Social {esquema_aislamiento_social}.\n')

    if verguenza_defectuosidad_total > 25.5:
        esquema_verguenza_defectuosidad = "ACTIVADO"
    else:
        esquema_verguenza_defectuosidad = "DESACTIVADO"
    print(f'Tu puntuación fue de {verguenza_defectuosidad_total}, (Media = 25.5). Tienes el esquema de Verguenza/Defectuosidad {esquema_verguenza_defectuosidad}.\n')

    if indeseabilidad_social_total > 15.42:
        esquema_indeseabilidad_social = "ACTIVADO"
    else:
        esquema_indeseabilidad_social = "DESACTIVADO"
    print(f'Tu puntuación fue de {indeseabilidad_social_total}, (Media = 15.42). Tienes el esquema de Indeseabilidad Social {esquema_indeseabilidad_social}.\n')

    if fracaso_total > 14.01:
        esquema_fracaso = "ACTIVADO"
    else:
        esquema_fracaso = "DESACTIVADO"
    print(f'Tu puntuación fue de {fracaso_total}, (Media = 14.01). Tienes el esquema de Fracaso {esquema_fracaso}.\n')

    if dependencia_incompetencia_total > 25.08:
        esquema_dependencia_incompetencia = "ACTIVADO"
    else:
        esquema_dependencia_incompetencia = "DESACTIVADO"
    print(f'Tu puntuación fue de {dependencia_incompetencia_total}, (Media = 25.08). Tienes el esquema de Dependencia/Incompetencia {esquema_dependencia_incompetencia}.\n')

    if vulnerabilidad_al_dano_total > 29.33:
        esquema_vulnerabilidad_al_dano = "ACTIVADO"
    else:
        esquema_vulnerabilidad_al_dano = "DESACTIVADO"
    print(f'Tu puntuación fue de {vulnerabilidad_al_dano_total}, (Media = 29.33). Tienes el esquema de Vulnerabilidad al daño {esquema_vulnerabilidad_al_dano}.\n')

    if entrampamiento_total > 19.59:
        esquema_entrampamiento = "ACTIVADO"
    else:
        esquema_entrampamiento = "DESACTIVADO"
    print(f'Tu puntuación fue de {entrampamiento_total}, (Media = 19.59). Tienes el esquema de Entrampamiento {esquema_entrampamiento}.\n')

    if subyugacion_total > 21.49:
        esquema_subyugacion = "ACTIVADO"
    else:
        esquema_subyugacion = "DESACTIVADO"
    print(f'Tu puntuación fue de {subyugacion_total}, (Media = 21.49). Tienes el esquema de Subyugación {esquema_subyugacion}.\n')

    if autosacrificio_total > 41.21:
        esquema_autosacrificio = "ACTIVADO"
    else:
        esquema_autosacrificio = "DESACTIVADO"
    print(f'Tu puntuación fue de {autosacrificio_total}, (Media = 41.21). Tienes el esquema de Autosacrificio {esquema_autosacrificio}.\n')

    if inhibicion_emocional_total > 21.49:
        esquema_inhibicion_emocional = "ACTIVADO"
    else:
        esquema_inhibicion_emocional = "DESACTIVADO"
    print(f'Tu puntuación fue de {inhibicion_emocional_total}, (Media = 21.49). Tienes el esquema de Inhibición Emocional {esquema_inhibicion_emocional}.\n')

    if estandares_flexibles_total > 39.6:
        esquema_estandares_flexibles = "ACTIVADO"
    else:
        esquema_estandares_flexibles = "DESACTIVADO"
    print(f'Tu puntuación fue de {estandares_flexibles_total}, (Media = 39.6). Tienes el esquema de Estándares Inflexibles {esquema_estandares_flexibles}.\n')

    if egocentrismo_grandiosidad_total > 26.67:
        esquema_egocentrismo_grandiosidad = "ACTIVADO"
    else:
        esquema_egocentrismo_grandiosidad = "DESACTIVADO"
    print(f'Tu puntuación fue de {egocentrismo_grandiosidad_total}, (Media = 26.67). Tienes el esquema de Egocentrismo/Grandiosidad {esquema_egocentrismo_grandiosidad}.\n')

    if autocontrol_insuficiente_total > 34.01:
        esquema_autocontrol_insuficiente = "ACTIVADO"
    else:
        esquema_autocontrol_insuficiente = "DESACTIVADO"
    print(f'Tu puntuación fue de {autocontrol_insuficiente_total}, (Media = 34.01). Tienes el es esquema de Autocontrol/Autodisciplina insuficientes {esquema_autocontrol_insuficiente}.\n')


    print("\n"*3)
    print("*************"*3)
    print("Estos son tus resultados en mayor detalle:")
    print("*************"*3)
    print("\n"*2)
    table = [
        ["Deprivación emocional", deprivacion_emocional_total, "1 a 9", 7.58, 8.98, 16.56, 24.14],
        ["Abandono/Inestabilidad", abandono_inestabilidad_total, "10 a 27", 13.83, 23.74, 37.57, 51.4],
        ["Desconfianza/Abuso", desconfianza_abuso_total, "28 a 44", 13.93, 23.88, 37.81, 51.74],
        ["Aislamiento social", aislamiento_social_total, "45 a 54", 8.48, 12.93, 21.41, 29.89],
        ["Verguenza/Defectuosidad", verguenza_defectuosidad_total, "55 a 69", 9.92, 15.58, 25.5, 35.42],
        ["Indeseabilidad social", indeseabilidad_social_total, "70 a 78", 5.28, 10.14, 15.42, 20.7],
        ["Fracaso", fracaso_total, "79 a 87", 5.52, 8.49, 14.01, 19.53],
        ["Dependencia/Incompetencia", dependencia_incompetencia_total, "88 a 102", 8.3, 16.78, 25.08, 33.38],
        ["Vulnerabilidad al daño", vulnerabilidad_al_dano_total, "103 a 116", 10.27, 19.06, 29.33, 39.6],
        ["Entrampamiento", entrampamiento_total, "117 a 127", 7.57, 12.02, 19.59, 27.16],
        ["Subyugación", subyugacion_total, "128 a 137", 6.41, 14.55, 21.49, 28.43],
        ["Autosacrificio", autosacrificio_total, "138 a 154", 13.55, 27.66, 41.21, 54.76],
        ["Inhibición emocional", inhibicion_emocional_total, "155 a 163", 6.94, 14.55, 21.49, 28.43],
        ["Estándares inflexibles", estandares_flexibles_total, "164 a 179", 12.11, 27.49, 39.6, 51.71],
        ["Egocentrismo/Grandiosidad", egocentrismo_grandiosidad_total, "180 a 190", 9.35, 17.32, 26.67, 36.05],
        ["Autocontrol/Autodisciplina insuficientes", autocontrol_insuficiente_total, "191 a 205", 11.11, 22.9, 34.01, 45.12],
    ]
    
    #Imprimir la tabla de resultados
    print(tabulate(table, headers = ["Esquema", "Resultados del cuestionario", "Preguntas", "DS", "LI", "Media " , "LS"]))
    print("\n"*5)
    print("Recuerda que la validez de estos resultados se basan en el siguiente estudio: https://www.redalyc.org/articulo.oa?id=80537307")
    print("Para más información sobre la Terapia de Esquemas puedes consultar: Young, J. E., Klosko, J. S., & Weishaar, M. E. (2003). Schema therapy: A practitioner's guide. Guilford Press. https://psycnet.apa.org/record/2003-00629-000")
    print("\n"*5)



if __name__ == "__main__":
   print("\n")
   print("*************"*4)
   print("Bienvenido al Cuestionario de Esquemas de Jeffrey E. Young")
   print("*************"*4)
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