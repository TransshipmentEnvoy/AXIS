from cargo import Cargo

cargo = Cargo(
    id="meat",
    type_name="string(STR_CARGO_NAME_MEAT)",
    unit_name="string(STR_CARGO_NAME_MEAT)",
    type_abbreviation="string(STR_CID_MEAT)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_REFRIGERATED)", # NOT UPDATED FOR FRAX
    cargo_label="MEAT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_MEAT)",
    penalty_lowerbound="0",
    single_penalty_length="18",
    price_factor=138,
    capacity_multiplier="1",
    icon_indices=(14, 5),
    sprites_complete=True,
)
