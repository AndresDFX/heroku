from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

doc = """
Your app description
"""

# ******************************************************************************************************************** #
# ***                                                           UTILITY
# ******************************************************************************************************************** #

def make_radiohorizontal_button(label, choices):
    return models.IntegerField(
        choices=choices,
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

def makefield_urn_decision():
    return models.StringField(
    initial='')

def makefield_string(label, choices):
    return models.StringField(
        label=label,
        choices=choices,
        widget=widgets.RadioSelect
    )

def makefield_integer():
    return models.IntegerField(initial=0)

def makefield_urnz_question(label):
    return models.StringField(
        label=label,
        widget=widgets.TextArea
)

def make_field(label):
    return models.StringField(
        choices=[
            ['Fuertemente en desacuerdo', ""],
            ['En desacuerdo', ""],
            ['Ligeramente en desacuerdo', ""],
            ['Ni de acuerdo, ni en desacuerdo', ""],
            ['De acuerdo', ""],
            ['Fuertemente de acuerdo', ""],
        ],
        label=label,
        widget=widgets.RadioSelect,
    )

def make_field2(label):
    return models.IntegerField(
        choices=[-2,-1,0,1,2],
        label=label,
    )

# ******************************************************************************************************************** #
# ***                                                           CHOICES
# ******************************************************************************************************************** #

#################### STAGE 1 #######################
choices_gen_instructions1 = [
    [1,'2 UM'], 
    [2,'0 UM'],
    [3,'8 UM'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions2 = [
    [1,'10 UM'], 
    [2,'8 UM'],
    [3,'6 UM'],
    [4,'Ninguna de las anteriores']
]

choices_gen_instructions3 = [
    [1,'$1400 (7 UM x 10 respuestas x $20)'], 
    [2,'$0 (7 UM x 10 respuestas x $0) 8 '],
    [3,'$2000 (10 UM x 10 respuestas x $20)'],
    [4,'Ninguna de las anteriores' ]
]


#################### STAGE 2 #######################
choices_gen_instructions4 = [
    [1,'$1,000'], 
    [2,'$3,000'],
    [3,'$5,000']
]

choices_gen_instructions5 = [
    [1,'$2,000'], 
    [2,'$6,000'],
    [3,'$9,000']
]

# ******************************************************************************************************************** #
# ***                                                       CLASS APPLICATION
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'informality_experiment_B1'
    players_per_group = None
    fixed_payment = 5000
    num_rounds = 20

    #STAGE 1
    coin_value = 20 # default: 20
    rate_error = 2 # default: 2
    min_length_textarea = 50 # default: 50
    max_length_textarea = 200 # default: 200
    num_seconds_stage_1 = 60 # default: 60
    urn_z_token_min_random = 2
    urn_z_token_max_random = 8
    urn_y_token_min_random = 0
    urn_y_token_max_random = 8

    images_per_phase = 25
    images_max_phase1 = images_per_phase
    images_max_phase2 = images_per_phase*2
    images_max_phase3 = images_per_phase*3
    images_max_phase4 = images_per_phase*4 
    images_names_questions = [
        '1_1_1_4',
        '1_1_2_5',
        '1_1_3_6',
        '1_1_4_2',
        '1_1_5_4',
        '1_2_1_2',
        '1_2_2_6',
        '1_2_3_3',
        '1_2_4_3',
        '1_2_5_1',
        '1_3_1_4',
        '1_3_2_3',
        '1_3_3_5',
        '1_3_4_2',
        '1_3_5_3',
        '1_4_1_1',
        '1_4_2_2',
        '1_4_3_2',
        '1_4_4_4',
        '1_4_5_5',
        '1_5_1_4',
        '1_5_2_4',
        '1_5_3_2',
        '1_5_4_2',
        '1_5_5_1',
        '2_6_1_2',
        '2_6_2_4',
        '2_6_3_2',
        '2_6_4_5',
        '2_6_5_2',
        '2_7_1_3',
        '2_7_2_1',
        '2_7_3_2',
        '2_7_4_5',
        '2_7_5_3',
        '2_8_1_4',
        '2_8_2_3',
        '2_8_3_4',
        '2_8_4_2',
        '2_8_5_1',
        '2_9_1_4',
        '2_9_2_4',
        '2_9_3_6',
        '2_9_4_5',
        '2_9_5_1',
        '2_10_1_2',
        '2_10_2_3',
        '2_10_3_3',
        '2_10_4_4',
        '2_10_5_3',
        '3_11_1_2',
        '3_11_2_3',
        '3_11_3_3',
        '3_11_4_4',
        '3_11_5_2',
        '3_12_1_3',
        '3_12_2_2',
        '3_12_3_2',
        '3_12_4_3',
        '3_12_5_2',
        '3_13_1_3',
        '3_13_2_2',
        '3_13_3_2',
        '3_13_4_4',
        '3_13_5_1',
        '3_14_1_2',
        '3_14_2_2',
        '3_14_3_2',
        '3_14_4_4',
        '3_14_5_2',
        '3_15_1_3',
        '3_15_2_2',
        '3_15_3_3',
        '3_15_4_2',
        '3_15_5_4',
        '4_16_1_2',
        '4_16_2_2',
        '4_16_3_4',
        '4_16_4_5',
        '4_16_5_3',
        '4_17_1_2',
        '4_17_2_2',
        '4_17_3_4',
        '4_17_4_3',
        '4_17_5_2',
        '4_18_1_3',
        '4_18_2_1',
        '4_18_3_3',
        '4_18_4_5',
        '4_18_5_2',
        '4_19_1_4',
        '4_19_2_3',
        '4_19_3_3',
        '4_19_4_1',
        '4_19_5_2',
        '4_20_1_3',
        '4_20_2_2',
        '4_20_3_6',
        '4_20_4_2',
        '4_20_5_5',
        '4_20_5_5'
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    round_counter = makefield_integer()
    payment_total = makefield_integer()

# ******************************************************************************************************************** #
# *** STAGE 1
# ******************************************************************************************************************** #
    last_decision_phase = makefield_urn_decision()
    last_token_value_phase = makefield_integer()
    last_answer_correct_phase = makefield_integer()
    payment_phase_1 = makefield_integer()
    payment_phase_2 = makefield_integer()
    payment_phase_3 = makefield_integer()
    payment_phase_4 = makefield_integer()
    payment_stage_1 = makefield_integer()
    decision_phase_1 = makefield_urn_decision()
    decision_phase_2 = makefield_urn_decision()
    decision_phase_3 = makefield_urn_decision()
    decision_phase_4 = makefield_urn_decision()
    answer_correct_phase1 = makefield_integer()
    answer_correct_phase2 = makefield_integer()
    answer_correct_phase3 = makefield_integer()
    answer_correct_phase4 = makefield_integer()

    ############################### Consent #########################
    accepts_terms = models.BooleanField()
    num_temporal = models.IntegerField(
        label="Por favor, ingrese el numero de identificaci??n temporal que le lleg?? en el correo de invitaci??n")

    ############################ Instructions #######################
    question_1_stage1_instructions = makefield_string(
        '1. ??Cu??l es el valor m??nimo de las monedas de la Urna Z?',
        choices_gen_instructions1
    )

    question_2_stage1_instructions = makefield_string(
        '2.	??Cu??l es el valor m??nimo de las monedas de la de la Urna Y?',
        choices_gen_instructions1
    )

    question_3_stage1_instructions = makefield_string(
        '3.	??Cu??l es el valor m??ximo de las monedas de la Urna Y?',
        choices_gen_instructions2
    )

    question_4_stage1_instructions = makefield_string(
        '4.	Si para las rondas 6-10 escoges la urna Z y sale al azar una moneda de 7 UM, ??cu??ntos pesos ganar??s por 10 respuestas correctas?',
        choices_gen_instructions3
    )

    num_entered = models.IntegerField(
        label="Por favor indique el n??mero de inconsistencias que logr?? identificar dentro del texto:",
        initial=0, 
    )

    ############################ PHASE 1 ############################
    question_1_phase1_urnz = makefield_urnz_question('??Cu??ntenos c??mo se ha sentido en esta actividad hasta ahora y por qu???')
    question_2_phase1_urnz = makefield_urnz_question('??C??mo define usted la incertidumbre?')
    question_3_phase1_urnz = makefield_urnz_question('??Cu??l cree usted que es el principal problema del pa??s?')
    
    ############################ PHASE 2 ############################
    question_1_phase2_urnz = makefield_urnz_question('??De qu?? cree usted que se trata esta actividad que est?? realizando?')
    question_2_phase2_urnz = makefield_urnz_question('??A qu?? cree usted que se dedica la C??mara de Comercio?')
    question_3_phase2_urnz = makefield_urnz_question('??Cu??l cree usted que es el principal problema que enfrenta el Valle del Cauca?')

    ############################ PHASE 3 ############################
    question_1_phase3_urnz = makefield_urnz_question('Cu??ntenos sobre alguna encuesta que usted haya respondido recientemente ??para qu?? era? ??le pareci?? entretenida?')
    question_2_phase3_urnz = makefield_urnz_question('??A qu?? cree usted que se dedica el Ministerio de Industria, Comercio y Turismo?')
    question_3_phase3_urnz = makefield_urnz_question('??Cu??l cree usted que es el principal problema que enfrenta Suram??rica?')

    ############################ PHASE 4 ############################
    question_1_phase4_urnz = makefield_urnz_question('??Cu??ntas veces ha escogido usted la Urna Z en esta actividad? ??Por qu?? la ha escogido?')
    question_2_phase4_urnz = makefield_urnz_question('??En qu?? se le parecen las decisiones que usted est?? tomando en esta encuesta con las decisiones que usted toma diariamente?')
    question_3_phase4_urnz = makefield_urnz_question('Si pudiera aconsejar a otras personas que est??n realizando esta encuesta sobre la urna que deben elegir, ??qu?? les dir??a?')
    

# ******************************************************************************************************************** #
# *** STAGE 2
# ******************************************************************************************************************** #
    payment_stage_2 = makefield_integer()
    flip_value = models.FloatField(initial=0.0)

    amount_inversion = models.IntegerField(
        label="Por favor, indica el monto que invertir??s en el activo de riesgo (sin puntos o comas)", 
        min=0, 
        max=5000
    )

# ******************************************************************************************************************** #
# *** Encuesta sociodemogr??fica
# ******************************************************************************************************************** #
    edad = models.IntegerField(label='??Cu??ntos a??os cumplidos tiene?')
    ciudad = models.StringField(label='??En qu?? ciudad vive actualmente?')

    rol_hogar = models.StringField(
        label='??Cu??l es su rol en su hogar? (Por favor, escoja una opci??n)',
        choices=['Padre / Madre', 'Espos@', 'Hij@', 'Otro']
    )

    estado_civil = models.StringField(
        label='??Cu??l es su estado civil? (Por favor, escoja una opci??n)',
        choices=['Soltero', 'Casado', 'Uni??n libre', 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='??Cu??ntos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos f??sicos, usted es o se reconoce como:(Por favor, escoja una opci??n)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco', 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='??En cu??l de los siguientes grupos se identifica usted?(Por favor, escoja una opci??n)',
        choices=['Cat??lico', 'Cristiano', 'Testigo de Jehov??', 'Ateo', 'Agn??stico', 'Jud??o', 'Musulm??n', 'Hinduista', 'Otro', 'Prefiero no decir' ]
    )

    estudios = models.StringField(
        label='??Cu??l es el m??ximo nivel de estudios alcanzado a la fecha? (Por favor, escoja una opci??n)',
        choices=[
            'Primaria incompleta',
            'Primaria completa',
            'B??sica secundaria (9?? grado completo)',
            'Media secundaria (11?? grado completo)',
            'T??cnico incompleto',
            'T??cnico completo',
            'Tecnol??gico incompleto',
            'Tecnol??gico completo',
            'Pregrado incompleto',
            'Pregrado completo',
            'Postgrado incompleto',
            'Posgrado completo'
        ]
    )

    actividad_actual = models.StringField(
        label='Actualmente, ??cu??l es su actividad principal? (Por favor, escoja una opci??n)',
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar', 'Buscar trabajo' ,'Otra actividad']
    )

    esta_laborando = models.BooleanField(
        label='??Se encuentra usted laborando actualmente? (Por favor, escoja una opci??n)',
        choices=[
            [True, "S??"],
            [False, "No"],
        ]
    )

    ingreso_mensual = models.StringField(
        label='??Cu??l es su nivel aproximado de ingresos mensuales (incluya mesadas, subsidios y remesas)?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'M??s de 5.000.001',
            'Prefiero no decir'
        ]
    )

    gasto_mensual = models.StringField(
        label='??Cu??l es su nivel aproximado de gastos mensuales?',
        choices=[
            'De 1 a $200.000',
            'De $200.001 a $400.000',
            'De $400.001 a $700.000',
            'De $700.001 a $1.000.000',
            'De $1.000.001 a $2.000.000',
            'De $2.000.001 a $5.000.000',
            'M??s de 5.000.001',
            'Prefiero no decir'
        ]
    )

    #Esacala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5,6,7,8,9,10], label= "")

    Estabilidad = models.IntegerField(choices=[1,2,3,4,5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situaci??n.')
    Independencia = models.IntegerField(choices=[1,2,3,4,5], label='Autonom??a de tomar las decisiones propias.')
    Descanso = models.IntegerField(choices=[1,2,3,4,5], label='Reposar fuerzas a trav??s de un estado inactivo')
    Lucro = models.IntegerField(choices=[1,2,3,4,5], label='Ganancia o provecho de alg??n actividad u objeto.')
    Protecci??n = models.IntegerField(choices=[1,2,3,4,5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla3_pregunta1 = make_field2 ('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2 ('Comprar a vendedores ambulantes')
    encuesta_tabla3_pregunta3 = make_field2 ('Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta4 = make_field2 ('Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')
    encuesta_tabla3_pregunta5 = make_field2 ('No cotizar al sistema de pensiones')
    encuesta_tabla3_pregunta6 = make_field2 ('No aportar al sistema de salud')
    encuesta_tabla3_pregunta7 = make_field2 ('No tener cuenta bancaria')
    encuesta_tabla3_pregunta8 = make_field2 ('Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)')
    encuesta_tabla3_pregunta9 = make_field2 ('Usar transportes alternativos como piratas o mototaxis')
    encuesta_tabla3_pregunta10 = make_field2 ('Vender cosas o hacer negocios de manera informal')
    encuesta_tabla3_pregunta11 = make_field2 ('No votar')
    encuesta_tabla3_pregunta12 = make_field2 ('Ir a eventos pol??ticos para conseguir empleo/beneficios personales')
    encuesta_tabla3_pregunta13 = make_field2 ('Comprar productos sin factura')
    encuesta_tabla3_pregunta14 = make_field2 ('No recoger los desechos de las mascotas')
    encuesta_tabla3_pregunta15 = make_field2 ('Subarrendar una habitaci??n')

