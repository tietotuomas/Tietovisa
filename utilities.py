def get_feedback(points):
    message_number = 0
    feedback_limit = [0, 0.2, 0.4, 0.6, 0.8, 1]
    feedback = ["Hups... vaikeita kysymyksiä?", "No... olisihan se huonomminkin voinut mennä.", \
        "Ei huono, kyllä tällä luokalta pääsee.", "Vähintäänkin tyydyttävä tulos!", \
        "Wau, kiitettävä suoritus!", "No, terve! Ethän vain huijannut?"]
    while message_number < len(feedback) and points > feedback_limit[message_number]:
        message_number += 1
    return feedback[message_number]

def get_ordinal(id):
    ordinal = ""
    ordinals = ["ensimmäinen", "toinen", "kolmas", "neljäs", "viides", "kuudes",\
                            "seitsemäs", "kahdeksas", "yhdeksäs", "kymmenes"]         
    if id <= 10:
        for i in range (1, 10):
            if i == id:
                ordinal = ordinals[i-1]
    else:
        ordinal = str(id) + "."
    
    return ordinal
    