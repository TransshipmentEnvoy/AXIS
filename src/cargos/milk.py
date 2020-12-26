from cargo import Cargo

cargo = Cargo(
    id="milk",
    type_name="string(STR_CARGO_NAME_MILK)",
    unit_name="string(STR_CARGO_NAME_MILK)",
    type_abbreviation="string(STR_CID_MILK)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.1",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_LIQUID, CC_REFRIGERATED)",
    cargo_label="MILK",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_MILK)",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=146,
    icon_indices=(13, 0),
)
