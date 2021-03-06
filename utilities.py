from random import choice

def get_feedback(points):
    message_list = 0
    feedback_limit = [0, 0.2, 0.4, 0.6, 0.8, 1]
    feedback = [["... vaikeita kysymyksiä?", "...oliko keskittyminen hukassa?"], \
        ["No... olisihan se huonomminkin voinut mennä.", "Ei mennyt kuin Strömsössä."], \
        ["Ei huono, ehkä tällä luokalta päässee.", "Ihan kohtuullinen esitys."], \
        ["Vähintäänkin tyydyttävä tulos!", "Ei hassummin!", "Tavattoman kelpo tulos!"], \
        ["Wau, kiitettävä suoritus!", "Fantastista tekemistä!", "Upeaa, aihepiiri selvästi hallussa!"], \
        ["No, terve! Ethän vain huijannut?", "Suorastaan timanttista!", "Mestarisuoritus!"]]
    while message_list < len(feedback) and points > feedback_limit[message_list]:
        message_list += 1
    return choice(feedback[message_list])

def get_ordinal(id):
    ordinal = ""
    ordinals = ["ensimmäinen", "toinen", "kolmas", "neljäs", "viides", "kuudes",\
                            "seitsemäs", "kahdeksas", "yhdeksäs", "kymmenes"]     
    if id <= 10:
        for i in range (1, 11):
            if i == id:
                ordinal = ordinals[i-1]
    else:
        ordinal = str(id) + "."
    return ordinal

def get_random_message():
    messages = ['Jukupätkä', 'Huppista', '"To err is human"', 'Voi pentele']
    return choice(messages)
    