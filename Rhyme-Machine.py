import PySimpleGUI as sg
import json
import requests


funct = {
    
    'Rhymes':['Find words that rhyme with','-SEARCH-PARAMETER-','rel_rhy'],
    'Related Words':['Find words related to','-SEARCH-PARAMETER-','ml'],
    'Similar Sound' : ['Find words that sound similar to','-SEARCH-PARAMETER-','sl'],
    'Similar Spelling' : ['Find words with a similar spelling as', '-SEARCH-PARAMETER-','sp'],
    'Synonyms' : ['Find synonyms of', '-SEARCH-PARAMETER-','rel_syn'],
    'Antonyms' : ['Find antonyms of', '-SEARCH-PARAMETER-','rel_ant']
    }

#def definitions():

def windowdisplay():
    sg.theme('DarkAmber')

    layout = [[sg.Text('Please Choose a mode:'), sg.Text(size=(15,1))],
          [sg.Button(item) for item in funct.keys()],
          [sg.Text(size=(30,1), key='-SEARCH-PARAMETER-')],
          [sg.Input(key='-WORD-')],
          [sg.Text(''),sg.Text(size=(100,25), key='-OUTPUT-')],
          [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout)
    return window, layout

#def Decode(Rhymes_List,window):
#    
#    Rhymes_List = Rhymes_List.json()
#    Rhymes_List = [word['word'] for word in Rhymes_List]
#    return Rhymes_List

decode = lambda word_list : [i['word'] for i in word_list.json()]



def main():
    
    window, layout = windowdisplay()
    opened = True
    mode = funct['Rhymes'][2]
    
    while opened:  # Event Loop
        event, values = window.read()
        print(event, values)
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            opened = False

        elif event == 'Show':
            # Grabbing the input from the user
            word_entered=(values['-WORD-'])
            #Get rhyme data list from Datamuse
            word_list = requests.get(f'https://api.datamuse.com/words?{mode}={word_entered}&max=100')
            
            #send the list to remove unnecessary data
            word_list = decode(word_list)
            
            window['-OUTPUT-'].update([item for item in word_list])

        else:
            window[funct[event][1]].update(funct[event][0])
            mode = funct[event][2]

    window.close()
main()    

