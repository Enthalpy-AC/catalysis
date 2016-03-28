'''Module with abstract classes for object and subobjects for frame_parser.'''

from abc import ABCMeta, abstractproperty

from catalysis_globals import Invalid


class JSONClass(object):
    '''An abstract JSON class, filled with the generic methods used to select
    proper function to run.

    colon_dict : Dictionary of keyword arguments to use when a function is
    called using a default value. If a keyword is not in this dictionary,
    it cannot be called using colon syntax.
    last_method : False when inactive, and a dict with a function name and the
    current value of the last method otherwise. Used for line continuation.
    base_exclude : A set of attributes to be excluded from base's
    redefining.'''

    __metaclass__ = ABCMeta

    colon_dict = {}
    last_method = False
    base_exclude = set()

    @abstractproperty
    def attribute(self):
        '''The key corresponding to the list in trial data with this kind of
        object.'''
        pass

    @abstractproperty
    def key_to_method(self):
        '''The dictionary that hashes a user-input attribute name to the
        function that sets that attribute.'''
        pass

    @property
    def base_dict(self):
        '''The dictionary of default values. Should be overriden by most
        properties.'''
        raise Invalid("defaults unsupported")

    def redefine(self, name, value):
        '''Call row function (specified by name), passing the value.'''
        try:
            func = self.key_to_method[name]
        except KeyError:
            raise Invalid("attr name", name)
        func(value)

    def append(self, value):
        '''Run redefine on the last function, with the old value, a newline,
        and then the value to append. The line continuation function.'''
        try:
            self.redefine(self.last_method["name"],
                          self.last_method["value"] + "\n" + value)
        except TypeError:
            raise Invalid("no continuation")

    def base(self, base):
        '''Run colon_redef on all applicable attributes.'''
        try:
            base = self.base_dict[base.lower()]
        except KeyError:
            raise Invalid("attr val", base)
        for name in self.colon_dict:
            if name not in self.base_exclude:
                self.key_to_method[name](base[name], **self.colon_dict[name])

    def colon_redef(self, name, base):
        '''Take the given base, transform it into a dictionary of values for a
        given typical JSON row, and use that for the applicable function.'''
        try:
            base = self.base_dict[base.lower()]
        except KeyError:
            raise Invalid("attr val", base)
        name = name.lower()
        if name in self.colon_dict:
            self.key_to_method[name](base[name], **self.colon_dict[name])
            # name in self.colon_dict => name in base & self.key_to_method
        elif name in self.key_to_method:
            raise Invalid("no default attr", name)
        else:
            raise Invalid("attr name", name)


class JSONRow(JSONClass):
    '''A JSON object representing a second-level JSON object in v6 trial_data.

    chain: A list of JSON_Row objects of the same type.
    sub_set: The set of subobjects that this row can take.

    An instance will also have:
    base_dict: A dictionary from which to draw default values.'''

    __metaclass__ = ABCMeta

    chain = [0]
    sub_set = set()

    def chain_init(self, default):
        '''Add this object's value to chain, passing in the given default
        arguments. Return the last component of the chain. Only call in an init
        function. Must create a new object rather than call the append method,
        so each subclass has their own chain.'''
        base = {"id": len(self.__class__.chain)}
        base.update(default)
        self.__class__.chain = self.__class__.chain + [base]
        return self.__class__.chain[-1]

    @abstractproperty
    def base_dict(self):
        '''Dictionary of default values. All rows should override this.'''
        pass
    