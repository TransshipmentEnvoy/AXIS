incompatible_grfs = []

class DwordGrfID(object):
    """
        grfids in game and bananas are presented as dwords, so it would be more convenient all round to use the dword
        however nml wants grfids as literals, so this class stores a dword, and converts it to an *nml* literal on demand
    """
    def __init__(self, grfid):
        self.grfid_as_dword = grfid # keep the grfid around in case it's wanted for docs etc (as yet unknown)
        # split to bytes
        split = [self.grfid_as_dword[i:i+2] for i in range(0, len(self.grfid_as_dword), 2)]
        result = []
        for byte in split:
            result.append(chr(int(byte,16)))  # convert the char from the byte in base 16
        joined = repr("".join(result)) # call repr() on the result to get the literal string for nml
        no_quotes_for_nml = ''.join(joined.split("'"))
        no_x_chars_for_nml = ''.join(no_quotes_for_nml.split("x"))
        self.grfid = no_x_chars_for_nml

class LiteralGrfID(object):
    """
        store a literal grfid directly, which is convenient for nml
        but most grfids are found in the wild as dwords, in which case it's simpler to use the class for dword grfids instead ;)
    """
    def __init__(self, grfid):
        self.grfid = grfid


class IncompatibleGRF(object):
    """ simple class to hold incompatible grfs, including optional properties for extended checks """
    def __init__(self, grfid, grfname):
        self._grfid = grfid # private var for this, we'll mangle it when called as a property
        self.grfname = grfname
        incompatible_grfs.append(self)

    @property
    def grfid(self):
        return self._grfid.grfid

# add incompatible grfs here (note that some properties are optional, allowing simple or extended checks)

#IncompatibleGRF(DwordGrfID("F1250005"), "FIRS v1")
IncompatibleGRF(DwordGrfID("45480101"), "CETS")

IncompatibleGRF(LiteralGrfID(r"Meo\81"), "New Cargos")
IncompatibleGRF(LiteralGrfID(r"Meo\82"), "New Cargos Petrol + Tourists")
IncompatibleGRF(LiteralGrfID(r"Meo\91"), "ECS Town VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\92"), "ECS Basic VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\93"), "ECS Chemical VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\94"), "ECS Machinery VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\95"), "ECS Wood VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\96"), "ECS Construction VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\97"), "ECS Agricultural VectoLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"Meo\98"), "ECS Basic for Arctic")
IncompatibleGRF(LiteralGrfID(r"Meo\99"), "ECS Basic for Tropic")
IncompatibleGRF(LiteralGrfID(r"Meo\9A"), "ECS Machinery for Tropic")
IncompatibleGRF(LiteralGrfID(r"Meo\9B"), "ECS Construction Vector by Pikkabird")
IncompatibleGRF(LiteralGrfID(r"Meo\9C"), "ECS Chemical Vector II")
IncompatibleGRF(LiteralGrfID(r"SK\05\01"), "Luukland CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"JS\0A\02"), "Luukland CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"JS\0A\03"), "Luukland CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"JS\0A\04"), "Luukland CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"JS\0A\05"), "Luukland CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"EX\01\02"), "Ex CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"EX\01\03"), "Ex CitybuildeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"DD\06\01"), "UKRS Industries")
IncompatibleGRF(LiteralGrfID(r"frMI"), "Manual Industries")
IncompatibleGRF(LiteralGrfID(r"SLTU"), "Tourist Set")
IncompatibleGRF(LiteralGrfID(r"SZ\13D"), "Oil well decrease neutralizeLiteralGrfID(r")
IncompatibleGRF(LiteralGrfID(r"EH\01\01"), "Experts hard industries")
IncompatibleGRF(LiteralGrfID(r"DD\06\03"), "UKRS Brick Chain")
IncompatibleGRF(LiteralGrfID(r"DD\06\02"), "Pikka Basic Industries")
IncompatibleGRF(LiteralGrfID(r"mb\08\00"), "NewCargos by Michael Blunck")
IncompatibleGRF(LiteralGrfID(r"AL\01\01"), "Nearby Station Names")