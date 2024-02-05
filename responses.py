from random import choice, randint

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return 'I\'m quite a shy bot myself :P'
    elif 'hello' in lowered:
        return 'Greetings!'
    else:
        return choice(['I didn\'t quite catch that...',
                       'my beeps can\'t proccess those boops',
                       'I\'ll never see it coming (if you keep phrasing questions like that)',
                       'please stop saying dumb things, you\'re not even making sense T_T'])