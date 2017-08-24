class DictValidator:

    def __init__(self):
        directives = [seg.strip().replace("\n", "").strip() for seg in self.__doc__.split("@")]
        v_name = "__SPEC_%s" % (self.__class__.__name__.upper())
        globals().update({
            v_name: self,
        })
        self.directives = directives
        self.allow_extra_params = False
        self.obligatory_keys = set(self.SAMPLE.keys())

    def is_instance(self, val):
        Adiff = set(val.keys()) - self.obligatory_keys
        Bdiff = self.obligatory_keys - set(val.keys())

        if len(Adiff) == 0 and len(Bdiff) == 0:
            print("val is a %s" % self.__class__.__name__)
            return True
        elif self.allow_extra_params and len(Adiff):
            print("val extends on %s with %s" % (self.__class__.__name__, kdiff))
            return True
        else:
            if Adiff:
                print("val is not %s. Unreconized %s" % (self.__class__.__name__, Adiff))

            if Bdiff:
                print("val is not %s, Missing %s" % (self.__class__.__name__, Bdiff))

            return False

class Customer(DictValidator):
    """
        @allow-additional-keys
        @optionals: Phone.
        @cpf: Mask(999.999.999-99)
    """

    SAMPLE = {
        "Cpf": "091.072.366-46",
        "Name": "joao maia",
        "Email": "joaoeduardocm@gmail.com",
        "Phone": "(31) 99265-1026",
        "Bank": "banco_do_brasil"
    }


ASDWQE = {
    "Cpf": "091.072.366-46",
    "Name": "joao maia",
    "Email": "joaoeduardocm@gmail.com",
    "Phone": "(31) 99265-1026"
}


globals()["Customer"]()
print(globals())

__SPEC_CUSTOMER.is_instance(ASDWQE)
