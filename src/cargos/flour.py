from cargo import Cargo

cargo = Cargo(
    id="flour",
    type_name="string(STR_CARGO_NAME_FLOUR)",
    unit_name="string(STR_CARGO_NAME_FLOUR)",
    type_abbreviation="string(STR_CID_FLOUR)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED, CC_POWDERIZED)", # NOT UPDATED FOR FRAX
    cargo_label="BAKE",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FLOUR)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(3, 6),
    sprites_complete=True,
)
