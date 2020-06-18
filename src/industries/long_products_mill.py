from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='long_products_mill',
                             accept_cargos_with_input_ratios=[('STCB', 4), ('ACID', 2), ('SOAP', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types_with_output_ratios=[('STSE', 3), ('RBAR', 2), ('STWR', 2), ('ENSP', 1)], # balance is deliberate, steel sections need to feed wharf, vehicle chain is already well supplied
                             prob_in_game='3',
                             prob_map_gen='5',
                             map_colour='43',
                             name='string(STR_IND_LONG_PRODUCTS_MILL)',
                             nearby_station_name='string(STR_STATION_HEAVY_INDUSTRY_2)',
                             fund_cost_multiplier='120',
                             intro_year=1832)


industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='long_products_mill_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    type='hard_standing_dirt',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -33)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 31, -31, 0)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 31, -31, 0)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(500, 60, 64, 51, -31, -21)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id='long_products_mill_spritelayout_shed_sw_ne_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_shed_sw_ne_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_shed_se_nw_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_shed_se_nw_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_small_shed_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_small_shed_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_tanks',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_7',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='long_products_mill_spritelayout_gantry',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='long_products_mill_industry_layout_1',
    layout=[(0, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (0, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (0, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_2'),
            (0, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_2'),
            (1, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (1, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (1, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            (1, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_gantry'),
            (2, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (2, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (2, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            (2, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_gantry'),
            (3, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_sw_ne_1'),
            (3, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_small_shed_2'),
            (3, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            (3, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            (4, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_tanks'),
            (4, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_small_shed_1'),
            (4, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            (4, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            ]
)

industry.add_industry_layout(
    id='long_products_mill_industry_layout_2',
    layout=[(0, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (0, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (0, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (0, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (0, 4, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_tanks'),
            (1, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (1, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (1, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_1'),
            (1, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_small_shed_2'),
            (1, 4, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_small_shed_1'),
            (2, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_2'),
            (2, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            (2, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            (2, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            (2, 4, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_7'),
            (3, 0, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_shed_se_nw_2'),
            (3, 1, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_gantry'),
            (3, 2, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_gantry'),
            (3, 3, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            (3, 4, 'long_products_mill_tile_1', 'long_products_mill_spritelayout_6'),
            ]
)