DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# Function to show list
def showResult(show_list):
    print("*** Starting ***")
    for item in show_list:
        print(item)
    print("*** Done ***")

def run():
    # For all DATA, take all worker name which his lenguage is "python"
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # For all DATA, take workers that work in "Platzi"
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Take the data of people with an age of 18 or higher
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # Put in the list, the name of each person in "adults"
    adults = list(map(lambda worker: worker["name"], adults))

    # To the data, insert a new key "old"
    # That if the person is older than 70 will return True, and if not False
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # Reto:
        # Crear las listas "all_python_devs" y "all_Platzi_workers" usando una combinación de filter y map
        # Crear la lista "old_people" y "adults" con list comprehension

    # Filter the data of people that his language is python and Map in "python_devs" only his name
    python_devs = list(filter(lambda worker: worker["language"] == "python", DATA)) # Filter
    python_devs = list(map(lambda worker: worker["name"], python_devs)) # Map
    # Print this data
    showResult(python_devs)

    # Filter the data of people that his "organization" is "Platzi" then, Map in "platzi_devs" only his name
    platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA)) # Filter
    platzi_workers = list(map(lambda worker: worker["name"], platzi_workers)) # Map
    # Print this data
    showResult(platzi_workers)

    # Save worker "name" in DATA if his "age" is 18 or higher.
    adults_list = [worker["name"] for worker in DATA if worker["age"] >= 18]
    # Print this data
    showResult(adults_list)

    # Add to each worker, True or False, if his age is higher than 70 or not
    old_people_list = [worker | {"old": worker["age"] > 70} for worker in DATA]
    # Print it
    showResult(old_people_list)

if __name__ == '__main__':
    run()