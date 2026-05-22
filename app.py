from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dados COMPLETOS da tabela periódica (todos os 118 elementos)
TABELA_PERIODICA = {
    # Período 1
    1: {"nome": "Hidrogênio", "simbolo": "H", "massa": "1.008", "grupo": "Não-metal", "camadas": [1], "posicao": {"linha": 1, "coluna": 1}},
    2: {"nome": "Hélio", "simbolo": "He", "massa": "4.0026", "grupo": "Gás Nobre", "camadas": [2], "posicao": {"linha": 1, "coluna": 18}},
    
    # Período 2
    3: {"nome": "Lítio", "simbolo": "Li", "massa": "6.94", "grupo": "Metal Alcalino", "camadas": [2, 1], "posicao": {"linha": 2, "coluna": 1}},
    4: {"nome": "Berílio", "simbolo": "Be", "massa": "9.012", "grupo": "Metal Alcalino Terroso", "camadas": [2, 2], "posicao": {"linha": 2, "coluna": 2}},
    5: {"nome": "Boro", "simbolo": "B", "massa": "10.81", "grupo": "Metaloide", "camadas": [2, 3], "posicao": {"linha": 2, "coluna": 13}},
    6: {"nome": "Carbono", "simbolo": "C", "massa": "12.011", "grupo": "Não-metal", "camadas": [2, 4], "posicao": {"linha": 2, "coluna": 14}},
    7: {"nome": "Nitrogênio", "simbolo": "N", "massa": "14.007", "grupo": "Não-metal", "camadas": [2, 5], "posicao": {"linha": 2, "coluna": 15}},
    8: {"nome": "Oxigênio", "simbolo": "O", "massa": "15.999", "grupo": "Não-metal", "camadas": [2, 6], "posicao": {"linha": 2, "coluna": 16}},
    9: {"nome": "Flúor", "simbolo": "F", "massa": "18.998", "grupo": "Halogênio", "camadas": [2, 7], "posicao": {"linha": 2, "coluna": 17}},
    10: {"nome": "Neônio", "simbolo": "Ne", "massa": "20.180", "grupo": "Gás Nobre", "camadas": [2, 8], "posicao": {"linha": 2, "coluna": 18}},
    
    # Período 3
    11: {"nome": "Sódio", "simbolo": "Na", "massa": "22.990", "grupo": "Metal Alcalino", "camadas": [2, 8, 1], "posicao": {"linha": 3, "coluna": 1}},
    12: {"nome": "Magnésio", "simbolo": "Mg", "massa": "24.305", "grupo": "Metal Alcalino Terroso", "camadas": [2, 8, 2], "posicao": {"linha": 3, "coluna": 2}},
    13: {"nome": "Alumínio", "simbolo": "Al", "massa": "26.982", "grupo": "Metal", "camadas": [2, 8, 3], "posicao": {"linha": 3, "coluna": 13}},
    14: {"nome": "Silício", "simbolo": "Si", "massa": "28.086", "grupo": "Metaloide", "camadas": [2, 8, 4], "posicao": {"linha": 3, "coluna": 14}},
    15: {"nome": "Fósforo", "simbolo": "P", "massa": "30.974", "grupo": "Não-metal", "camadas": [2, 8, 5], "posicao": {"linha": 3, "coluna": 15}},
    16: {"nome": "Enxofre", "simbolo": "S", "massa": "32.06", "grupo": "Não-metal", "camadas": [2, 8, 6], "posicao": {"linha": 3, "coluna": 16}},
    17: {"nome": "Cloro", "simbolo": "Cl", "massa": "35.45", "grupo": "Halogênio", "camadas": [2, 8, 7], "posicao": {"linha": 3, "coluna": 17}},
    18: {"nome": "Argônio", "simbolo": "Ar", "massa": "39.95", "grupo": "Gás Nobre", "camadas": [2, 8, 8], "posicao": {"linha": 3, "coluna": 18}},
    
    # Período 4
    19: {"nome": "Potássio", "simbolo": "K", "massa": "39.098", "grupo": "Metal Alcalino", "camadas": [2, 8, 8, 1], "posicao": {"linha": 4, "coluna": 1}},
    20: {"nome": "Cálcio", "simbolo": "Ca", "massa": "40.078", "grupo": "Metal Alcalino Terroso", "camadas": [2, 8, 8, 2], "posicao": {"linha": 4, "coluna": 2}},
    21: {"nome": "Escândio", "simbolo": "Sc", "massa": "44.956", "grupo": "Metal de Transição", "camadas": [2, 8, 9, 2], "posicao": {"linha": 4, "coluna": 3}},
    22: {"nome": "Titânio", "simbolo": "Ti", "massa": "47.867", "grupo": "Metal de Transição", "camadas": [2, 8, 10, 2], "posicao": {"linha": 4, "coluna": 4}},
    23: {"nome": "Vanádio", "simbolo": "V", "massa": "50.942", "grupo": "Metal de Transição", "camadas": [2, 8, 11, 2], "posicao": {"linha": 4, "coluna": 5}},
    24: {"nome": "Cromo", "simbolo": "Cr", "massa": "51.996", "grupo": "Metal de Transição", "camadas": [2, 8, 13, 1], "posicao": {"linha": 4, "coluna": 6}},
    25: {"nome": "Manganês", "simbolo": "Mn", "massa": "54.938", "grupo": "Metal de Transição", "camadas": [2, 8, 13, 2], "posicao": {"linha": 4, "coluna": 7}},
    26: {"nome": "Ferro", "simbolo": "Fe", "massa": "55.845", "grupo": "Metal de Transição", "camadas": [2, 8, 14, 2], "posicao": {"linha": 4, "coluna": 8}},
    27: {"nome": "Cobalto", "simbolo": "Co", "massa": "58.933", "grupo": "Metal de Transição", "camadas": [2, 8, 15, 2], "posicao": {"linha": 4, "coluna": 9}},
    28: {"nome": "Níquel", "simbolo": "Ni", "massa": "58.693", "grupo": "Metal de Transição", "camadas": [2, 8, 16, 2], "posicao": {"linha": 4, "coluna": 10}},
    29: {"nome": "Cobre", "simbolo": "Cu", "massa": "63.546", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 1], "posicao": {"linha": 4, "coluna": 11}},
    30: {"nome": "Zinco", "simbolo": "Zn", "massa": "65.38", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 2], "posicao": {"linha": 4, "coluna": 12}},
    31: {"nome": "Gálio", "simbolo": "Ga", "massa": "69.723", "grupo": "Metal", "camadas": [2, 8, 18, 3], "posicao": {"linha": 4, "coluna": 13}},
    32: {"nome": "Germânio", "simbolo": "Ge", "massa": "72.630", "grupo": "Metaloide", "camadas": [2, 8, 18, 4], "posicao": {"linha": 4, "coluna": 14}},
    33: {"nome": "Arsênio", "simbolo": "As", "massa": "74.922", "grupo": "Metaloide", "camadas": [2, 8, 18, 5], "posicao": {"linha": 4, "coluna": 15}},
    34: {"nome": "Selênio", "simbolo": "Se", "massa": "78.971", "grupo": "Não-metal", "camadas": [2, 8, 18, 6], "posicao": {"linha": 4, "coluna": 16}},
    35: {"nome": "Bromo", "simbolo": "Br", "massa": "79.904", "grupo": "Halogênio", "camadas": [2, 8, 18, 7], "posicao": {"linha": 4, "coluna": 17}},
    36: {"nome": "Criptônio", "simbolo": "Kr", "massa": "83.798", "grupo": "Gás Nobre", "camadas": [2, 8, 18, 8], "posicao": {"linha": 4, "coluna": 18}},
    
    # Período 5
    37: {"nome": "Rubídio", "simbolo": "Rb", "massa": "85.468", "grupo": "Metal Alcalino", "camadas": [2, 8, 18, 8, 1], "posicao": {"linha": 5, "coluna": 1}},
    38: {"nome": "Estrôncio", "simbolo": "Sr", "massa": "87.62", "grupo": "Metal Alcalino Terroso", "camadas": [2, 8, 18, 8, 2], "posicao": {"linha": 5, "coluna": 2}},
    39: {"nome": "Ítrio", "simbolo": "Y", "massa": "88.906", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 9, 2], "posicao": {"linha": 5, "coluna": 3}},
    40: {"nome": "Zircônio", "simbolo": "Zr", "massa": "91.224", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 10, 2], "posicao": {"linha": 5, "coluna": 4}},
    41: {"nome": "Nióbio", "simbolo": "Nb", "massa": "92.906", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 12, 1], "posicao": {"linha": 5, "coluna": 5}},
    42: {"nome": "Molibdênio", "simbolo": "Mo", "massa": "95.95", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 13, 1], "posicao": {"linha": 5, "coluna": 6}},
    43: {"nome": "Tecnécio", "simbolo": "Tc", "massa": "98", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 13, 2], "posicao": {"linha": 5, "coluna": 7}},
    44: {"nome": "Rutênio", "simbolo": "Ru", "massa": "101.07", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 15, 1], "posicao": {"linha": 5, "coluna": 8}},
    45: {"nome": "Ródio", "simbolo": "Rh", "massa": "102.91", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 16, 1], "posicao": {"linha": 5, "coluna": 9}},
    46: {"nome": "Paládio", "simbolo": "Pd", "massa": "106.42", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 18, 0], "posicao": {"linha": 5, "coluna": 10}},
    47: {"nome": "Prata", "simbolo": "Ag", "massa": "107.87", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 18, 1], "posicao": {"linha": 5, "coluna": 11}},
    48: {"nome": "Cádmio", "simbolo": "Cd", "massa": "112.41", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 18, 2], "posicao": {"linha": 5, "coluna": 12}},
    49: {"nome": "Índio", "simbolo": "In", "massa": "114.82", "grupo": "Metal", "camadas": [2, 8, 18, 18, 3], "posicao": {"linha": 5, "coluna": 13}},
    50: {"nome": "Estanho", "simbolo": "Sn", "massa": "118.71", "grupo": "Metal", "camadas": [2, 8, 18, 18, 4], "posicao": {"linha": 5, "coluna": 14}},
    51: {"nome": "Antimônio", "simbolo": "Sb", "massa": "121.76", "grupo": "Metaloide", "camadas": [2, 8, 18, 18, 5], "posicao": {"linha": 5, "coluna": 15}},
    52: {"nome": "Telúrio", "simbolo": "Te", "massa": "127.60", "grupo": "Metaloide", "camadas": [2, 8, 18, 18, 6], "posicao": {"linha": 5, "coluna": 16}},
    53: {"nome": "Iodo", "simbolo": "I", "massa": "126.90", "grupo": "Halogênio", "camadas": [2, 8, 18, 18, 7], "posicao": {"linha": 5, "coluna": 17}},
    54: {"nome": "Xenônio", "simbolo": "Xe", "massa": "131.29", "grupo": "Gás Nobre", "camadas": [2, 8, 18, 18, 8], "posicao": {"linha": 5, "coluna": 18}},
    
    # Período 6
    55: {"nome": "Césio", "simbolo": "Cs", "massa": "132.91", "grupo": "Metal Alcalino", "camadas": [2, 8, 18, 18, 8, 1], "posicao": {"linha": 6, "coluna": 1}},
    56: {"nome": "Bário", "simbolo": "Ba", "massa": "137.33", "grupo": "Metal Alcalino Terroso", "camadas": [2, 8, 18, 18, 8, 2], "posicao": {"linha": 6, "coluna": 2}},
    57: {"nome": "Lantânio", "simbolo": "La", "massa": "138.91", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 18, 9, 2], "posicao": {"linha": 6, "coluna": 3}},
    58: {"nome": "Cério", "simbolo": "Ce", "massa": "140.12", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 19, 9, 2], "posicao": {"linha": 8, "coluna": 4}},  # Linha separada
    59: {"nome": "Praseodímio", "simbolo": "Pr", "massa": "140.91", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 21, 8, 2], "posicao": {"linha": 8, "coluna": 5}},
    60: {"nome": "Neodímio", "simbolo": "Nd", "massa": "144.24", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 22, 8, 2], "posicao": {"linha": 8, "coluna": 6}},
    61: {"nome": "Promécio", "simbolo": "Pm", "massa": "145", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 23, 8, 2], "posicao": {"linha": 8, "coluna": 7}},
    62: {"nome": "Samário", "simbolo": "Sm", "massa": "150.36", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 24, 8, 2], "posicao": {"linha": 8, "coluna": 8}},
    63: {"nome": "Európio", "simbolo": "Eu", "massa": "151.96", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 25, 8, 2], "posicao": {"linha": 8, "coluna": 9}},
    64: {"nome": "Gadolínio", "simbolo": "Gd", "massa": "157.25", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 25, 9, 2], "posicao": {"linha": 8, "coluna": 10}},
    65: {"nome": "Térbio", "simbolo": "Tb", "massa": "158.93", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 27, 8, 2], "posicao": {"linha": 8, "coluna": 11}},
    66: {"nome": "Disprósio", "simbolo": "Dy", "massa": "162.50", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 28, 8, 2], "posicao": {"linha": 8, "coluna": 12}},
    67: {"nome": "Hólmio", "simbolo": "Ho", "massa": "164.93", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 29, 8, 2], "posicao": {"linha": 8, "coluna": 13}},
    68: {"nome": "Érbio", "simbolo": "Er", "massa": "167.26", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 30, 8, 2], "posicao": {"linha": 8, "coluna": 14}},
    69: {"nome": "Túlio", "simbolo": "Tm", "massa": "168.93", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 31, 8, 2], "posicao": {"linha": 8, "coluna": 15}},
    70: {"nome": "Itérbio", "simbolo": "Yb", "massa": "173.05", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 32, 8, 2], "posicao": {"linha": 8, "coluna": 16}},
    71: {"nome": "Lutécio", "simbolo": "Lu", "massa": "174.97", "grupo": "Lantanídeo", "camadas": [2, 8, 18, 32, 9, 2], "posicao": {"linha": 6, "coluna": 4}},
    
    # Continuar período 6 (Háfnio até Radônio)
    72: {"nome": "Háfnio", "simbolo": "Hf", "massa": "178.49", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 10, 2], "posicao": {"linha": 6, "coluna": 5}},
    73: {"nome": "Tântalo", "simbolo": "Ta", "massa": "180.95", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 11, 2], "posicao": {"linha": 6, "coluna": 6}},
    74: {"nome": "Tungstênio", "simbolo": "W", "massa": "183.84", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 12, 2], "posicao": {"linha": 6, "coluna": 7}},
    75: {"nome": "Rênio", "simbolo": "Re", "massa": "186.21", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 13, 2], "posicao": {"linha": 6, "coluna": 8}},
    76: {"nome": "Ósmio", "simbolo": "Os", "massa": "190.23", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 14, 2], "posicao": {"linha": 6, "coluna": 9}},
    77: {"nome": "Irídio", "simbolo": "Ir", "massa": "192.22", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 15, 2], "posicao": {"linha": 6, "coluna": 10}},
    78: {"nome": "Platina", "simbolo": "Pt", "massa": "195.08", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 17, 1], "posicao": {"linha": 6, "coluna": 11}},
    79: {"nome": "Ouro", "simbolo": "Au", "massa": "196.97", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 18, 1], "posicao": {"linha": 6, "coluna": 12}},
    80: {"nome": "Mercúrio", "simbolo": "Hg", "massa": "200.59", "grupo": "Metal", "camadas": [2, 8, 18, 32, 18, 2], "posicao": {"linha": 6, "coluna": 13}},
    81: {"nome": "Tálio", "simbolo": "Tl", "massa": "204.38", "grupo": "Metal", "camadas": [2, 8, 18, 32, 18, 3], "posicao": {"linha": 6, "coluna": 14}},
    82: {"nome": "Chumbo", "simbolo": "Pb", "massa": "207.2", "grupo": "Metal", "camadas": [2, 8, 18, 32, 18, 4], "posicao": {"linha": 6, "coluna": 15}},
    83: {"nome": "Bismuto", "simbolo": "Bi", "massa": "208.98", "grupo": "Metal", "camadas": [2, 8, 18, 32, 18, 5], "posicao": {"linha": 6, "coluna": 16}},
    84: {"nome": "Polônio", "simbolo": "Po", "massa": "209", "grupo": "Metaloide", "camadas": [2, 8, 18, 32, 18, 6], "posicao": {"linha": 6, "coluna": 17}},
    85: {"nome": "Astato", "simbolo": "At", "massa": "210", "grupo": "Halogênio", "camadas": [2, 8, 18, 32, 18, 7], "posicao": {"linha": 6, "coluna": 18}},
    86: {"nome": "Radônio", "simbolo": "Rn", "massa": "222", "grupo": "Gás Nobre", "camadas": [2, 8, 18, 32, 18, 8], "posicao": {"linha": 6, "coluna": 19}},
    
    # Período 7 (Actinídeos)
    87: {"nome": "Frâncio", "simbolo": "Fr", "massa": "223", "grupo": "Metal Alcalino", "camadas": [2, 8, 18, 32, 18, 8, 1], "posicao": {"linha": 7, "coluna": 1}},
    88: {"nome": "Rádio", "simbolo": "Ra", "massa": "226", "grupo": "Metal Alcalino Terroso", "camadas": [2, 8, 18, 32, 18, 8, 2], "posicao": {"linha": 7, "coluna": 2}},
    89: {"nome": "Actínio", "simbolo": "Ac", "massa": "227", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 18, 9, 2], "posicao": {"linha": 7, "coluna": 3}},
    90: {"nome": "Tório", "simbolo": "Th", "massa": "232.04", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 18, 10, 2], "posicao": {"linha": 9, "coluna": 4}},
    91: {"nome": "Protactínio", "simbolo": "Pa", "massa": "231.04", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 20, 9, 2], "posicao": {"linha": 9, "coluna": 5}},
    92: {"nome": "Urânio", "simbolo": "U", "massa": "238.03", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 21, 9, 2], "posicao": {"linha": 9, "coluna": 6}},
    93: {"nome": "Netúnio", "simbolo": "Np", "massa": "237", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 22, 9, 2], "posicao": {"linha": 9, "coluna": 7}},
    94: {"nome": "Plutônio", "simbolo": "Pu", "massa": "244", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 24, 8, 2], "posicao": {"linha": 9, "coluna": 8}},
    95: {"nome": "Amerício", "simbolo": "Am", "massa": "243", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 25, 8, 2], "posicao": {"linha": 9, "coluna": 9}},
    96: {"nome": "Cúrio", "simbolo": "Cm", "massa": "247", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 25, 9, 2], "posicao": {"linha": 9, "coluna": 10}},
    97: {"nome": "Berquélio", "simbolo": "Bk", "massa": "247", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 27, 8, 2], "posicao": {"linha": 9, "coluna": 11}},
    98: {"nome": "Califórnio", "simbolo": "Cf", "massa": "251", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 28, 8, 2], "posicao": {"linha": 9, "coluna": 12}},
    99: {"nome": "Einstênio", "simbolo": "Es", "massa": "252", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 29, 8, 2], "posicao": {"linha": 9, "coluna": 13}},
    100: {"nome": "Férmio", "simbolo": "Fm", "massa": "257", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 30, 8, 2], "posicao": {"linha": 9, "coluna": 14}},
    101: {"nome": "Mendelévio", "simbolo": "Md", "massa": "258", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 31, 8, 2], "posicao": {"linha": 9, "coluna": 15}},
    102: {"nome": "Nobélio", "simbolo": "No", "massa": "259", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 32, 8, 2], "posicao": {"linha": 9, "coluna": 16}},
    103: {"nome": "Laurêncio", "simbolo": "Lr", "massa": "266", "grupo": "Actinídeo", "camadas": [2, 8, 18, 32, 32, 8, 3], "posicao": {"linha": 7, "coluna": 4}},
    
    # Elementos superpesados
    104: {"nome": "Rutherfórdio", "simbolo": "Rf", "massa": "267", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 10, 2], "posicao": {"linha": 7, "coluna": 5}},
    105: {"nome": "Dúbnio", "simbolo": "Db", "massa": "268", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 11, 2], "posicao": {"linha": 7, "coluna": 6}},
    106: {"nome": "Seabórgio", "simbolo": "Sg", "massa": "269", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 12, 2], "posicao": {"linha": 7, "coluna": 7}},
    107: {"nome": "Bóhrio", "simbolo": "Bh", "massa": "270", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 13, 2], "posicao": {"linha": 7, "coluna": 8}},
    108: {"nome": "Hássio", "simbolo": "Hs", "massa": "277", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 14, 2], "posicao": {"linha": 7, "coluna": 9}},
    109: {"nome": "Meitnério", "simbolo": "Mt", "massa": "278", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 15, 2], "posicao": {"linha": 7, "coluna": 10}},
    110: {"nome": "Darmstádtio", "simbolo": "Ds", "massa": "281", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 16, 2], "posicao": {"linha": 7, "coluna": 11}},
    111: {"nome": "Roentgênio", "simbolo": "Rg", "massa": "282", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 17, 2], "posicao": {"linha": 7, "coluna": 12}},
    112: {"nome": "Copernício", "simbolo": "Cn", "massa": "285", "grupo": "Metal de Transição", "camadas": [2, 8, 18, 32, 32, 18, 2], "posicao": {"linha": 7, "coluna": 13}},
    113: {"nome": "Nihônio", "simbolo": "Nh", "massa": "286", "grupo": "Metal", "camadas": [2, 8, 18, 32, 32, 18, 3], "posicao": {"linha": 7, "coluna": 14}},
    114: {"nome": "Fleróvio", "simbolo": "Fl", "massa": "289", "grupo": "Metal", "camadas": [2, 8, 18, 32, 32, 18, 4], "posicao": {"linha": 7, "coluna": 15}},
    115: {"nome": "Moscóvio", "simbolo": "Mc", "massa": "290", "grupo": "Metal", "camadas": [2, 8, 18, 32, 32, 18, 5], "posicao": {"linha": 7, "coluna": 16}},
    116: {"nome": "Livermório", "simbolo": "Lv", "massa": "293", "grupo": "Metal", "camadas": [2, 8, 18, 32, 32, 18, 6], "posicao": {"linha": 7, "coluna": 17}},
    117: {"nome": "Tenessino", "simbolo": "Ts", "massa": "294", "grupo": "Halogênio", "camadas": [2, 8, 18, 32, 32, 18, 7], "posicao": {"linha": 7, "coluna": 18}},
    118: {"nome": "Oganesson", "simbolo": "Og", "massa": "294", "grupo": "Gás Nobre", "camadas": [2, 8, 18, 32, 32, 18, 8], "posicao": {"linha": 7, "coluna": 19}},
}

NOMES_CAMADAS = ['K', 'L', 'M', 'N', 'O', 'P', 'Q']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/elementos', methods=['GET'])
def get_elementos():
    elementos_lista = []
    for num, dados in TABELA_PERIODICA.items():
        elementos_lista.append({
            'AtomicNumber': str(num),
            'Symbol': dados['simbolo'],
            'Name': dados['nome'],
            'AtomicMass': dados['massa'],
            'GroupBlock': dados['grupo'],
            'Position': dados['posicao']
        })
    
    return jsonify({
        'Table': {
            'Row': [{'Cell': [e['AtomicNumber'], e['Symbol'], e['Name'], e['AtomicMass'], e['GroupBlock'], e['Position']]} for e in elementos_lista],
            'Columns': {'Column': ['AtomicNumber', 'Symbol', 'Name', 'AtomicMass', 'GroupBlock', 'Position']}
        }
    })

@app.route('/api/elemento/<int:numero_atomico>', methods=['GET'])
def get_elemento(numero_atomico):
    if numero_atomico not in TABELA_PERIODICA:
        return jsonify({'erro': 'Elemento não encontrado'}), 404
    
    dados = TABELA_PERIODICA[numero_atomico]
    
    camadas = []
    for i, num_eletrons in enumerate(dados['camadas']):
        if num_eletrons > 0 and i < len(NOMES_CAMADAS):
            camadas.append({
                'camada': NOMES_CAMADAS[i],
                'eletrons': num_eletrons,
                'nivel': i + 1
            })
    
    return jsonify({
        'success': True,
        'atomic_number': numero_atomico,
        'nome': dados['nome'],
        'simbolo': dados['simbolo'],
        'massa_atomica': dados['massa'],
        'grupo': dados['grupo'],
        'camadas_eletronicas': camadas,
        'total_eletrons': sum(dados['camadas']),
        'configuracao': ' • '.join([f"{c['camada']}: {c['eletrons']}" for c in camadas])
    })

if __name__ == '__main__':
    app.run(debug=True)