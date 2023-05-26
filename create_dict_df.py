import pandas as pd
country_details = {'country' : ['England' , 'Canada' , 'China' , 'India'],
                   'Area' : [789.99 , 66.6 , 898.0 , 649.90],
                    'population' : [778.99 , 545.787 , 444.3 , 232.5]
                   }
 
print(country_details)

def print_vals(key_name):
    print(country_details[key_name]);

print_vals('population')

for key in country_details.keys():
    print(f"The value corresponding to Key {key} is {country_details[key]}")

country_details_df = pd.DataFrame(country_details)
print(country_details_df)

print(type(country_details_df))

print(country_details_df.index.tolist())

country_details_df.index = [12, 13, 14, 15]

print(country_details_df)

country_details_df.index = ['Eng', 'Can', 'Chi', 'Ind']
print(country_details_df)