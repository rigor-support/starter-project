import requests
import os

# Fixed


def loader():

    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    data = response.json()

    # The data returned from the API contains 10 elements in the array, this will map to 10 workers being spun up.
    results = data['results']

    pokemon_names = []
    for x in results:
        pokemon_names.append(x['name'])

    print(pokemon_names)

    return {"runner_inputs": pokemon_names}


def runner(args):

    task_index = int(os.getenv('TASK_INDEX'))
    print(task_index)
    data_to_process = args[task_index]

    print(data_to_process)
    print(
        f'Pipeline runner of index: {task_index} working on this data! {data_to_process} ... beep boop')

    return True
