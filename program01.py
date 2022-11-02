# -*- coding: utf-8 -*-

"""
Consideriamo la codifica dei numeri romani e la modifica suggerita da 
Randall Munroe nel suo blog XKCD.
Nella codifica dei numeri romani:
- non esiste lo zero
- si usano le lettere 'IVXLCDM' che corrispondono ai valori decimali
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- i numeri si scrivono da sinistra a destra cominciando con i valori più alti 
  (migliaia, centinaia, decine, unità)
- i valori delle lettere si sommano, tranne quando sono seguiti da lettere di peso maggiore, 
  nel qual caso si sottraggono
- si possono usare al massimo 3 lettere consecutive uguali per le lettere 'IXCM'
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- per rappresentare i valori che hanno cifra decimale 4 o 9 si usa la sottrazione 
  dalla lettera seguente
  Es. 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

Nel suo blog XKCD, invece, Randall Munroe codifica i numeri romani con i corrispondenti numeri arabi: 
si concatenano i numeri arabi ottenuti sostituendo a ciascuna lettera il valore corrispondente.  
Es.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Chiamiamo questa codifica "formato XKCD".

Obiettivo dello homework è decodificare una lista di stringhe che rappresentano
numeri romani nel formato XKCD, e tornare i K valori maggiori in ordine decrescente.

Implementate quindi le seguenti funzioni:
"""

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    '''
    # INSERISCI QUI IL TUO CODICE
    # "1000100100010100110"
    result = []
    #for value in xkcd_values:
        #result.append(decode_value(value))
    result = list(map(decode_value, xkcd_values))

    #return result[:k].sort(reverse=True)
    result.sort(reverse=True)
    return result[:k]

def decode_value(xkcd : str ) -> int:
    '''
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente
    
    Esempio: '10010010010100511' -> 397
    '''
    # INSERISCI QUI IL TUO CODICE

    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))

def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    Esempio: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''



    # INSERISCI QUI IL TUO CODICE

    xkcd = str(int(xkcd))
    value_list = []
    num = xkcd[0]
    xkcd = xkcd[1:]
    for idx, x in enumerate(xkcd):
        if x != '0':
            value_list.append(int(num))
            num = ''

        num += x

        if idx >= len(xkcd) - 1:
            value_list.append(int(num))

    return value_list


def list_of_weights_to_number(weigths : list[int] ) -> int:
    '''
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante
    
    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    # INSERISCI QUI IL TUO CODICE
    weight_result = 0
    previous_one = 0

    for element in weigths:

        if element > previous_one:
            weight_result -= previous_one
            weight_result += element - previous_one

        else:
            weight_result += element

        previous_one = element

    return weight_result


###################################################################################
if __name__ == '__main__':
    print(xkcd_to_list_of_weights('00000000000000000000000000000000000000000000000000000000000000000000000000000000101011'))
    # inserisci qui i tuoi test

    #print(list_of_weights_to_number([1000, 100, 1000, 10, 100, 1, 10]))
    #print(decode_XKCD_tuple(('1000100100010100110', '100010001050015', '50010010050101015'), 2))
    #print(decode_value('10010010010100511'))
    #print(xkcd_to_list_of_weights('10010010010100511'))
    #print('10010010010100511', decode_value('10010010010100511'), '(397?)')