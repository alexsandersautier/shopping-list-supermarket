from decouple import config
from datetime import datetime

# right_user = config('USERAPP')
# right_password = config('PASSWORD')

months = {
    1: 'Jan',
    2: 'Fev',
    3: 'Mar',
    4: 'Abr',
    5: 'Mai',
    6: 'Jun',
    7: 'Jul',
    8: 'Ago',
    9: 'Set',
    10: 'Out',
    11: 'Nov',
    12: 'Dez'
}

class Config:

    # user = right_user
    # password = right_password
    currenty_date = f'{months[datetime.now().month]}/{datetime.now().year}'

system = Config()