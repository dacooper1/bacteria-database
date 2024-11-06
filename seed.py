from models import db, csv, Bacterium, User, Favourite
from app import client
import bacdive

file = './bacteria_data/Z.csv'



def add_genus_index(file):
        with open(file, newline='') as file_a:
            file = csv.DictReader(file_a)
            data = [row for row in file]
        return data

def get_unique_species(add_genus_index):
    unique_dict = {};
    for value in add_genus_index:
        species_id = value['ID']
        species = value['species']

        if species not in unique_dict:
            unique_dict[species] = species_id
      
    unique_list = [{'id':species_id, 'species':species} for species, species_id in unique_dict.items()]
    
    return unique_list
    
def get_species_data(get_unique_species):
    species_id_values = [value['id'] for value in get_unique_species]
    unique_data = []
    for value in species_id_values:
        try:
            query = {'id':value}
            client.search(**query)
            for strain in client.retrieve(): 
                data = {'ID': strain['General']['BacDive-ID'],
                        'genus': strain['Name and taxonomic classification']['LPSN']['genus'],
                        'species':strain['Name and taxonomic classification']['LPSN']['species']
                        }
                unique_data.append(data)
        except Exception as e:
             print("Error, search not found")
             continue
    return unique_data

def create_bacterium_instance(get_species_data):
    data = []
    for value in get_species_data:
        id = value['ID']
        genus = value['genus']
        species = value['species']

        new = Bacterium(strain_id=id, genus=genus, species=species)

        data.append(new)

    return data

def add_to_database(create_bacterium_instance):
    for value in create_bacterium_instance:
        db.session.add(value)
    db.session.commit()

def create_data():
    data = add_genus_index(file)
    unique_species = get_unique_species(data)
    species_data = get_species_data(unique_species)
    bacterium_instance = create_bacterium_instance(species_data)
    add_to_database(bacterium_instance)

create_data()










     
     
     


