def Decode(Rhymes_List,window):
    
    Rhymes_List = Rhymes_List.json()
    Rhymes_List_Refined = []
    for i in Rhymes_List:
        Rhymes_List_Refined.append(i['word'])
        #window['-OUTPUT-'].update(i['word'])
    Rhymes_List = Rhymes_List_Refined
    return Rhymes_List
def Main():
    sg.theme('DarkAmber')

    layout = [[sg.Text('Find words that rhyme with:'), sg.Text(size=(15,1))],
          [sg.Input(key='-IN-')],
          [sg.Text(''), sg.Text(size=(100,25), key='-OUTPUT-')],
          [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # Grabbing the input from the user
            word_entered=(values['-IN-'])
            #Get rhyme data list from Datamuse
            Rhymes_List = requests.get(f'https://api.datamuse.com/words?rel_rhy={word_entered}&max=100')                            
            #send the list to remove unnecessary data
            Rhymes_List = Decode(Rhymes_List, window)
            
            window['-OUTPUT-'].update(Rhymes_List)

        

    window.close()
    
#####Notes#####
    ###Short Term###
    #-strip function for that obnoxious string from datamuse OR find a way to get shorter strings from the original query list
    #-fix text size for that string(probably not permanent...need to make edits to the GUI Window
    #-create menu so that user can choose what list they want the tool to generate (rhymes,near rhymes, synonyms, etc.)
    ###----------###
    ###Long Term###
    #- 
    #- Add a "save words for later" feature so users can come back to words/ phrases that they like
    #- Add a "you've rhymed these words before" feature/analytic 
    #- Add a "your favorite words/most used words" feature/analytic
    #-
    ###---------###
#####-----#####
Main()