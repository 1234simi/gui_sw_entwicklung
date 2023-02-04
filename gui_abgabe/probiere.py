# dicty_real = {'md5_1': {'name_neu': 'name_alt'}}
# dicty_real['md5_1']['counter'] = 0
#
#
# dicty_real['md5_2'] = {'name_neu_2': 'name_alt_2'}
# dicty_real['md5_2']['counter'] =  0
#
#
# dicty_real['md5_3'] = {'name_neu_3': 'name_alt_3', 'counter': 0}
#



import time
import numpy as np

def dicty():



    anzahl = 1000011


    start_create = time.time()
    dicty_real = {}
    dicty_viel_vorgekommen = {}
    for i in range(anzahl):
        name_neu = 'name_test_' + str(i)
        name_alt = 'name_alt_' + str(i + 10)
        md5 = i + 1
        abs_pfad = '/home/dev/' + str(i)
        dicty_real.update({md5: {name_neu: name_alt, 'count': 0, 'abs_pfad': abs_pfad}})

    end_create = time.time()


    md5_to_search = [anzahl - 3, 12, 344]

    # search the key

    start_search_key = time.time()
    print()
    for entry in md5_to_search:
        if not dicty_real.get(entry):
            print('unique entry!')
        else:
            dicty_real.get(entry)['count'] += 11
            print(f'found {entry} @ {list(dicty_real.get(entry).keys())[0]}')
            count_b4 = dicty_real.get(entry)['count']
            print(f'\tcount b4: {count_b4}')
            if count_b4 > 3:
                print('\tsehr viel vorgekommen!')
                dicty = {entry: dicty_real.get(entry)}
                dicty_viel_vorgekommen.update(dicty)
            else:
                print('\tnoch nicht so viel vorgekommen')

            dicty_real.get(entry)['count'] += 1

    end_search_key = time.time()

    print()


    for key, value in dicty_viel_vorgekommen.items():
        print(f'{key}:')
        for key_2, value_2 in value.items():
            print(f'\t{key_2} --> {value_2}')


    #
    #
    # start_counter_value = time.time()
    # counter_found = 0
    #
    # for i in range(len(dicty_real.values())):
    #     counter = list(dicty_real.values())[i]['count']
    #     if counter >= 3:
    #         counter_found += 1
    #         print('jo')
    #
    # end_counter_value = time.time()
    # print()
    # print(f'counter found: {counter_found}')


    dauer_create = end_create - start_create
    dauer_search_key = end_search_key -start_search_key
    # dauer_counter_val = end_counter_value -start_counter_value
    print()
    print(f'took {np.round(dauer_create, 2)} s for creating')
    print(f'took {np.round(dauer_search_key, 2)} s for searching the key')
    # print(f'took {np.round(dauer_counter_val, 2)} s for searching the values')

    # if dicty_real.values() > 10:
    #     print('f')

    # print()
    # for key, value in dicty_real.items():
    #     print(f'{key}:')
    #     for key_2, value_2 in value.items():
    #         print(f'\t{key_2} --> {value_2}')




















