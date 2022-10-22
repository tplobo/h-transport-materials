import h_transport_materials as htm


def test_pre_exp_can_be_quantity():
    prop = htm.Diffusivity(
        D_0=1 * htm.ureg.cm**2 * htm.ureg.second**-1,
        E_D=0.5,
    )

    assert prop.pre_exp == 1e-4


def test_act_energy_can_be_quantity():
    prop = htm.Diffusivity(
        D_0=1,
        E_D=0.5 * htm.ureg.kJ * htm.ureg.mol**-1,
    )
    assert prop.act_energy != 0.5


def test_fit_with_units_data_y():
    """Checks that units are taken into account in data_y"""
    my_prop_ref = htm.Diffusivity(
        data_T=[1, 2, 3] * htm.ureg.K,
        data_y=[1, 2, 3] * htm.ureg.m**2 * htm.ureg.s**-1,
    )

    my_prop_other_units = htm.Diffusivity(
        data_T=[1, 2, 3] * htm.ureg.K,
        data_y=[1, 2, 3] * htm.ureg.cm**2 * htm.ureg.s**-1,
    )

    assert my_prop_other_units.pre_exp != my_prop_ref.pre_exp
    assert my_prop_other_units.act_energy != my_prop_ref.act_energy


def test_fit_with_units_data_T():
    """Checks that units are taken into account in data_T"""
    my_prop_ref = htm.Diffusivity(
        data_T=[1, 2, 3] * htm.ureg.K,
        data_y=[1, 2, 3] * htm.ureg.m**2 * htm.ureg.s**-1,
    )

    my_prop_other_units = htm.Diffusivity(
        data_T=htm.ureg.Quantity([1, 2, 3], htm.ureg.degC),
        data_y=[1, 2, 3] * htm.ureg.m**2 * htm.ureg.s**-1,
    )

    assert my_prop_other_units.pre_exp != my_prop_ref.pre_exp
    assert my_prop_other_units.act_energy != my_prop_ref.act_energy
