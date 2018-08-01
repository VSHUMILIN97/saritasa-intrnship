import unittest
from day5.task0 import ReadOnlyDict, setup_dict_factory


class ReadOnlyDictTest(unittest.TestCase):

    def test_always_falls_on_write_without_permission(self):
        """ Test that checks whether it is possible to write,
            to dict without permissiob
        """
        funcbbox = setup_dict_factory({'mama': 'mom'})
        bbox = ReadOnlyDict({'mama': 'mom', 'otec': 'dad'})
        with self.assertRaises(ValueError) as cm:
            bbox.granddad = 'dedushka'
        with self.assertRaises(ValueError) as cm2:
            funcbbox.grandmom = 'babushka'
        self.assertEqual(str(cm.exception),
                         'Not permitted to change')
        self.assertEqual(str(cm2.exception),
                         'Not permitted to change')

    def test_extend_dictionary_on_attribute_with_permission(self):
        """ Test checks whether it is possible to extend dictionary
            using cls attributes
        """
        funcbbox = setup_dict_factory({'mama': 'mom'}, add=True)
        bbox = ReadOnlyDict({'mama': 'mom', 'otec': 'dad'}, add=True)
        funcbbox.a = 2
        bbox.b = 3
        self.assertEqual(funcbbox.a, {'a': 2})
        self.assertEqual(bbox.b, {'b': 3})
        self.assertEqual(funcbbox.user_dict, {'mama': 'mom', 'a': 2})

    def test_delete_permissions_check(self):
        """ Test checks whether it is possible to del object
        """
        funcbbox = setup_dict_factory({'mama': {'lambdaY': {1: 2}}},
                                      delete=True)
        bbox = ReadOnlyDict({'mama': 'mom', 'otec': 'dad'}, delete=True)
        del funcbbox.mama.lambdaY
        self.assertEqual({'mama': {}}, funcbbox.user_dict)
        del bbox.otec
        self.assertEqual({'mama': 'mom'}, bbox.user_dict)

    def test_change_permission_cannot_add(self):
        """ This test checks whether it is possible to add
            something with only change permission or it is not
            possible
        """
        funcbbox = setup_dict_factory({'mama': 'mom', 'otec': 'dad'},
                                      change=True)
        funcbbox.mama = 'mommy'
        self.assertEqual({'mama': 'mommy'}, funcbbox.mama)
        with self.assertRaises(ValueError) as cm:
            funcbbox.uncle = 'Benz'
        self.assertEqual(str(cm.exception), 'Not permitted to add')
