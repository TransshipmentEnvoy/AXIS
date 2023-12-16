from cargo import Cargo

cargo = Cargo(
    id="rare_metals",
    type_name="string(STR_CARGO_NAME_RARE_METALS)",
    unit_name="string(STR_CARGO_NAME_RARE_METALS)",
    type_abbreviation="string(STR_CID_RARE_METALS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="RAMT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_RARE_METALS)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=155,
    icon_indices=(12, 6),
    sprites_complete=True,
)
