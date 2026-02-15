dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for i in dog_breeds_available_for_adoption:
    if dog_breed_I_want in i:
        print("У них есть собака, которую я хочу!")
        break