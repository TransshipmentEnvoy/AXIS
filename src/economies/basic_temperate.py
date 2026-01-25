from economy import Economy

economy = Economy(
    id="BASIC_TEMPERATE",
    numeric_id=0,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acid",
        "mail",
        "alcohol",
        "aluminium",
        "goods",
        "bauxite",
        "beans",
        "biomass",
        "building_materials",
        "cement",
        "food",
        "chemicals",
        "chlorine",
        "clay",
        "coal",
        "coal_tar",
        "coke",
        "copper",
        "copper_ore",
#       "edible_oil",
        "electrical_parts",
        "engineering_supplies",
#       "ethylene",
        "explosives",
        "farm_supplies",
#       "ferrochrome",
        "fertiliser",
        "fish",
        "fruits",
        "glass",# not in xis
        "grain",
        "iron_ore",
        "limestone",
        "livestock",
        "logs",
        "milk",
        "nitrates",
        "oil",
#       "oxygen",
        "packaging",
        "paints_and_coatings",
        "paper", # delete?
        "petrol",
        "pig_iron",
#       "pipe",
        "plant_fibres", # delete?
        "plastics",# not in xis
        "pyrite_ore",
        "quicklime",
        "rare_metals",
        "recyclables",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
        "steel",
        "steel_sections", #not in xis
        "sugar_beet", #or sugarcane?
        "sulphur",
        "textiles",
        "tyres",
        "lumber",
#       "vehicle_bodies",
        "vehicle_parts",
        "vehicles",
        "wool",
        "zinc",
    ],
    # as of March 2021 this cargoflow tuning is a temporary patch up, might need more work
    cargoflow_graph_tuning={}
)
