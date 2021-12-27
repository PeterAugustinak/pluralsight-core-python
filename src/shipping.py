import iso6346


class ShippingContainer:

    next_serial = 1337

    # manipulating class attributes
    # not the best way
    @staticmethod
    def _generate_serial_static():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    # correct way
    @classmethod
    def _generate_serial_class(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    # alternative constructors
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, *items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=self.owner_code,
            serial=ShippingContainer._generate_serial_class()
        )
