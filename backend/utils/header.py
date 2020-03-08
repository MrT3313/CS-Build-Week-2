# ENV
from decouple import config

# __ MAIN __
TOKEN = config('TOKEN')
header = {
    'Authorization': 'Token '+ TOKEN,
    'Content-Type': 'application/json'
}
