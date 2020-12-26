from cargo import Cargo

cargo = Cargo(
    id="chromite_ore",
    type_name="string(STR_CARGO_NAME_CHROMITE_ORE)",
    unit_name="string(STR_CARGO_NAME_CHROMITE_ORE)",
    type_abbreviation="string(STR_CID_CHROMITE_ORE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK)",
    cargo_label="CHRO",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CHROMITE_ORE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=58,
    capacity_multiplier="1",
    icon_indices=(13, 2),
)
