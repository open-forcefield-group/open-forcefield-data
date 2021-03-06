# Utility functions for use in all scripts here

from openforcefield.typing.engines.smirnoff import ForceField

SMIRNOFF = ForceField("test_forcefields/smirnoff99Frosst.offxml")


def find_smirnoff_params(ff) -> set:
    """Creates a set of all the smirnoff params, given a forcefield object. Loops over Bonds, Angles, ProperTorsions, ImproperTorsions, vdW only."""
    smirnoff_ids = set()

    handlers = ["Bonds", "Angles", "ProperTorsions", "ImproperTorsions", "vdW"]
    for handler in handlers:
        phandler = ff.get_parameter_handler(handler)
        for p in phandler.parameters:
            smirnoff_ids.add(p.id)

    return smirnoff_ids


def order_param_id(pid: str) -> (str, int):
    """Orders parameter ids by type then number. IDs match [a-z][0-9]+[a-z]? """
    if pid[-1].isdigit():
        return (pid[0], int(pid[1:]))
    else:
        return (pid[0], int(pid[1:-1]), pid[-1])
