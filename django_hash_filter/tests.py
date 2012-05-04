from django.template import Template, Context
from django.test import TestCase

class DjangoHashFilterTests(TestCase):

    def hash_tester_assert_equal(self, test_list, good_list, method):
        # Using max below ensures we go through both lists
        # However, if the lists are not equal length, this raises an exception
        for test_content, result in zip(test_list, good_list):
            t = Template('{%% load hash_filter %%}{{ test_content|hash:"%s" }}' % method)
            rendered = t.render(Context(locals())).strip()
            self.assertEqual(rendered, result,
                msg="%s test failed, produced '%s', should produce '%s'" % (method, rendered, result))

    def hash_tester_assert_not_equal(self, test_list, bad_list, method):
        # Using max below ensures we go through both lists
        # However, if the lists are not equal length, this raises an exception
        for test_content, result in zip(test_list, bad_list):
            t = Template('{%% load hash_filter %%}{{ test_content|hash:"%s" }}' % method)
            rendered = t.render(Context(locals())).strip()
            self.assertNotEqual(rendered, result,
                msg="%s test failed, produced '%s', should not produce '%s'" % (method, rendered, result))

    def test_md5(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('c097f083fc56015a47ab023002567786',
                       'bb649c83dd1ea5c9d9dec9a18df0ffe9',
                       'fc78245428fa1237d1976b7557693849')

        self.hash_tester_assert_equal(test_list, good_list, "md5")
        self.hash_tester_assert_not_equal(test_list, test_list, "md5")

    def test_sha1(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('7f895bd3aae3068c62ac77d1f7ff2041da707685',
                       '531b07a0f5b66477a21742d2827176264f4bbfe2',
                       'ad4687f31967a48f30245f837a69bfb96da0db66')

        self.hash_tester_assert_equal(test_list, good_list, "sha1")
        self.hash_tester_assert_not_equal(test_list, test_list, "sha1")

    def test_sha224(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('c42dca5447a75d600145a1fa38f98c47aea9af2ff1f8c94145c9c352',
                       'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2',
                       '2c752c821d0035490529f3b4977f84b4a1605919421d2b3c821534a2')

        self.hash_tester_assert_equal(test_list, good_list, "sha224")
        self.hash_tester_assert_not_equal(test_list, test_list, "sha224")

    def test_sha256(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('c7b4b678b227f6dfb8feedbb5f04e9293c20692af74a7d7f407a262bbad555e2',
                       '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406',
                       '33c88d091b89934bef56cc7c6e72dcded85c1dbb3673e00c36709f51045497eb')

        self.hash_tester_assert_equal(test_list, good_list, "sha256")
        self.hash_tester_assert_not_equal(test_list, test_list, "sha256")

    def test_sha384(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('47e712109f0a829416b4b45709f912f4f18f3a4e65a2a1a03fb094a73825029a9f376ddd470fea29d81b424b964cab25',
                       '213f861faafc19445f10c569f56c7540c5b6bbe10435353d930e351b49861d9a0f95f33efe355220c248b24d85e1e179',
                       'b492d6e80b14cfcad4e8252cb698ebedd05a294d16b07b738cf66e32648da72742c8d7487c0be806f6d972c43c07b8d0')

        self.hash_tester_assert_equal(test_list, good_list, "sha384")
        self.hash_tester_assert_not_equal(test_list, test_list, "sha384")

    def test_sha512(self):
        test_list = ('sekr1t',
                     'Nobody inspects the spammish repetition',
                     'say cheese')
        good_list = ('83de3d4c51b14b78156d12608cbd743c41988105bc3be2d60527503070c9f295cd4e1d260d88130f4092c5bc12e1183a5628354eaaecff003a3f8d707d89e15e',
                       'd0f4c14c48ad4837905ea7520cc4af700f6433ce0985e6bb87b6b4617cb944abf814bd53964ddbf55b41e5812b3afe90890c0a4db75cb04367e139fd62eab2e1',
                       'b0b87e6ac01d3baa8561a3da27bd5a09d13702d775b98c662b8637fa6def978596e031367363725ddb5f5ab138d69e7da9535d418f14f13923c733bdbf5de5db')

        self.hash_tester_assert_equal(test_list, good_list, "sha512")
        self.hash_tester_assert_not_equal(test_list, test_list, "sha512")
