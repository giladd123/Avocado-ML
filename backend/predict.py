from tensorflow import keras
import pandas as pd
model = keras.models.load_model('./backend/model/')

REGIONS = ['Albany', 'Atlanta', 'BaltimoreWashington', 'Boise',
                  'Boston', 'BuffaloRochester', 'California', 'Charlotte',
                  'Chicago', 'CincinnatiDayton', 'Columbus', 'DallasFtWorth',
                  'Denver', 'Detroit', 'GrandRapids', 'GreatLakes',
                  'HarrisburgScranton', 'HartfordSpringfield', 'Houston',
                  'Indianapolis', 'Jacksonville', 'LasVegas', 'LosAngeles',
                  'Louisville', 'MiamiFtLauderdale', 'Midsouth', 'Nashville',
                  'NewOrleansMobile', 'NewYork', 'Northeast',
                  'NorthernNewEngland', 'Orlando', 'Philadelphia',
                  'PhoenixTucson', 'Pittsburgh', 'Plains', 'Portland',
                  'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke',
                  'Sacramento', 'SanDiego', 'SanFrancisco', 'Seattle',
                  'SouthCarolina', 'SouthCentral', 'Southeast', 'Spokane',
                  'StLouis', 'Syracuse', 'Tampa', 'TotalUS', 'West',
                  'WestTexNewMexico']

YEARS = [2015, 2016, 2017, 2018]

TYPES = ['conventional', 'organic']

def get_prediciton(input):
    ans = check_req(input)
    if ans:
        return ans
    avocado = format_df(input)
    price = model.predict(avocado, verbose = 0)
    
    return price[0]

def format_df(input):
    df = format_req(input)
    print(df["year"])
    avocado = makeAvocadoWithCategory(
	df,
	['year', 'region','type'])
    print(avocado.columns)
    return avocado

def format_req(input):
    input = dict(input)
    reg = input["region"]
    for region in REGIONS:
        if region != reg:
            input.update({f"region_{region}" : 0})
    
    y = input["year"]
    for year in YEARS:
        if year != y:
            input.update({f"year_{year}" : 0})
    
    t = input["type"]
    for type in TYPES:
        if type != t:
            input.update({f"type_{type}" : 0})
    
    for keys in input:
        input[keys] = [input[keys]]
    


    df = pd.DataFrame(input)
    return df

def makeAvocadoWithCategory(data, categoryColumns):

	#allFields = categoryColumns + fieldsToKeep
	
    dfCategories = [ pd.get_dummies(data[column], prefix=column) for column in categoryColumns ]
    data = pd.concat([data] + dfCategories, axis=1)
    data = data.drop(columns=categoryColumns)

    return data



def check_req(input):
    errors = ""
    

    if input["region"] not in REGIONS:
        errors += "Region not supported\n"
    
    if input["type"] not in TYPES:
        errors+= "Type should be conventional or organic\n"
    
    if input["year"] not in YEARS:
        errors += "Year should be between 2015 and 2018"
    
    return errors
    
