from project import menu, initialization, selection, Recorder


def test_initialization():
    assert initialization() == 'Welcome to expense recorder \n ================================= \n Initializing...'

def test_menu():
    assert menu() == '''Press: \n 1: Enter a new expense. \n 2: Enter a new income. \n 3: View the expenses. \n 4: Erase a expense. \n 5: Download a csv file with the expenses. \n 6: Exit. \n ================================= '''


def test_selection():
    recorder = Recorder(100)
    assert selection(6, recorder) == 'Program finished'