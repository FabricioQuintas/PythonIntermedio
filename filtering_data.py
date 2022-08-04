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


    # Itinerate through the last list created
    for worker in old_people:
        # Print it
        print(worker)


if __name__ == '__main__':
    run()