from cargo import Cargo

cargo = Cargo(
    id="cleaning_agents",
    type_name="string(STR_CARGO_NAME_CLEANING_AGENTS)",
    unit_name="string(STR_CARGO_NAME_CLEANING_AGENTS)",
    type_abbreviation="string(STR_CID_CLEANING_AGENTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_PIECE_GOODS)",
    cargo_label="SOAP",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CLEANING_AGENTS)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(9, 5),
)
