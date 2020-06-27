import unittest

from krunner_keepassxc import __version__
from krunner_keepassxc.dhcrypto import dhcrypto
from .dhcrypto_reference import dhcryptoss

class Tests(unittest.TestCase):

	def test_version(self):
		self.assertEqual(__version__, '1.0.0')

	def test_crypto(self):
		crypto1 = dhcrypto()
		crypto2 = dhcrypto()
		crypto1.set_server_public_key(bytearray(crypto2.pubkey_as_bytes()))
		crypto2.set_server_public_key(bytearray(crypto1.pubkey_as_bytes()))

		self.assertEqual(crypto1.aes_key, crypto2.aes_key)

		secret = "a secret message"
		result1 = crypto1.encrypt_message(secret)
		result2 = crypto2.decrypt_message(result1)
		self.assertEqual(result2, secret)

	def test_crypto_ss(self):

		crypto = dhcrypto()
		crypto.pkey = 147566589851476177870810964496093990934306790047078165572566230176527840758765675034603131144606182367924651223102171984891386850386435996534792108338145371539000265217100821932875981501307453173931859149567579535962260168103300170942754359672285525300978843650330965329270964780811226675432026346246133222303
		crypto.pubkey = 164230467356653606922423559802908377728996834007263510352224394641063801575952010268826445746182985516837916562687718863677429945387908863624420464850481869713818376415548626751974410461326141004646198388634983917959881458176760161383493455754970214337579235821486867280451394242765668071523386904795147174731
		crypto.set_server_public_key(b'\xa1c\xa0\xa1nR\xce\xc7}\xc4;i\x05\x88J%\xf2.\xe4#\x80@N\x048\xfa \xb0\xb8l\xe3\x0e\xb5P\xee\xca`\x9f\xf0\x1f9\xd9f\xa3\xfc\xd5]\xc4\xe7\xbbX\xea!R\xd6\r\xb7]\xe7M=\xad\xb7\xa3\x95\x0b]\xf0\xbf\t\x86\xeaZ\xecZu\xb5\xbds\xc4\x95\x1fF"\x9d\xf79\x1d2\xb5\xcd\x89:\x91\xf4\xf3\xf7|W\x80\xfe#f\xb3P\x89\xebX\xce\x84\xb5\x8b\x83\xfd\x01\x06rl\x0fU\x92{\x86\x02\xecI\xc8#')

		cryptoss = dhcryptoss()
		cryptoss.pkey = 147566589851476177870810964496093990934306790047078165572566230176527840758765675034603131144606182367924651223102171984891386850386435996534792108338145371539000265217100821932875981501307453173931859149567579535962260168103300170942754359672285525300978843650330965329270964780811226675432026346246133222303
		cryptoss.pubkey = 164230467356653606922423559802908377728996834007263510352224394641063801575952010268826445746182985516837916562687718863677429945387908863624420464850481869713818376415548626751974410461326141004646198388634983917959881458176760161383493455754970214337579235821486867280451394242765668071523386904795147174731
		cryptoss.set_server_public_key(b'\xa1c\xa0\xa1nR\xce\xc7}\xc4;i\x05\x88J%\xf2.\xe4#\x80@N\x048\xfa \xb0\xb8l\xe3\x0e\xb5P\xee\xca`\x9f\xf0\x1f9\xd9f\xa3\xfc\xd5]\xc4\xe7\xbbX\xea!R\xd6\r\xb7]\xe7M=\xad\xb7\xa3\x95\x0b]\xf0\xbf\t\x86\xeaZ\xecZu\xb5\xbds\xc4\x95\x1fF"\x9d\xf79\x1d2\xb5\xcd\x89:\x91\xf4\xf3\xf7|W\x80\xfe#f\xb3P\x89\xebX\xce\x84\xb5\x8b\x83\xfd\x01\x06rl\x0fU\x92{\x86\x02\xecI\xc8#')

		self.assertEqual(crypto.aes_key, cryptoss.aes_key)


	def test_crypto_server(self):
		crypto1 = dhcrypto()
		crypto1.pkey = 147566589851476177870810964496093990934306790047078165572566230176527840758765675034603131144606182367924651223102171984891386850386435996534792108338145371539000265217100821932875981501307453173931859149567579535962260168103300170942754359672285525300978843650330965329270964780811226675432026346246133222303
		crypto1.pubkey = 164230467356653606922423559802908377728996834007263510352224394641063801575952010268826445746182985516837916562687718863677429945387908863624420464850481869713818376415548626751974410461326141004646198388634983917959881458176760161383493455754970214337579235821486867280451394242765668071523386904795147174731
		crypto1.set_server_public_key(b"\xb9t\\\x17&\x86\x1bN\xd8\xa8\xea\x88\xda\xd6\xba\xc8\r\x01E\xa5\x9b\x97\xa5\xe6Y(\x02\xa9U\x1a\xeb\xf9x\xf3\xf5\xec'\xb6@\xb0l\x19\xa9\xed.\xe7\x99U\x01\xc16W\xf8\x90\xdb\x04\xf8\x18\xc2!\xbe\x89&.\xa5\x80^\xff\xaa\x92`\xfea\x07\xb9\x9a\xfaD_S\x9a\x8f{\x01\xe7ZY\xdd\x05\x16\xe2\xe5D\x17\xb0\x05&\xddH\xea\xd0\x82\x93\xda\x8c\xe2\xa2\x8b\x13\x7fJ\xc9\x8c\x0e\x97\x1b\x060%\x03;@\xd68,\xb9\xe2@")
		result1 = crypto1.decrypt_message(('', b'~\xd7\x96\xbc\x12\x1aWT\xc1\xa3\x9d*\xd8\x18\xde\xb8', b"p/@\xc3'v\x12\xc8\xd8\xa4\xad\xdfP\xb3*5;j@\xc4*\xcfL'\xb1G\x96\xdeo\\p\xe9"))
		self.assertEqual(result1, 'kanji漢字かんじ')
		crypto2 = dhcryptoss()
		crypto2.pkey = 147566589851476177870810964496093990934306790047078165572566230176527840758765675034603131144606182367924651223102171984891386850386435996534792108338145371539000265217100821932875981501307453173931859149567579535962260168103300170942754359672285525300978843650330965329270964780811226675432026346246133222303
		crypto2.pubkey = 164230467356653606922423559802908377728996834007263510352224394641063801575952010268826445746182985516837916562687718863677429945387908863624420464850481869713818376415548626751974410461326141004646198388634983917959881458176760161383493455754970214337579235821486867280451394242765668071523386904795147174731
		crypto2.set_server_public_key(b"\xb9t\\\x17&\x86\x1bN\xd8\xa8\xea\x88\xda\xd6\xba\xc8\r\x01E\xa5\x9b\x97\xa5\xe6Y(\x02\xa9U\x1a\xeb\xf9x\xf3\xf5\xec'\xb6@\xb0l\x19\xa9\xed.\xe7\x99U\x01\xc16W\xf8\x90\xdb\x04\xf8\x18\xc2!\xbe\x89&.\xa5\x80^\xff\xaa\x92`\xfea\x07\xb9\x9a\xfaD_S\x9a\x8f{\x01\xe7ZY\xdd\x05\x16\xe2\xe5D\x17\xb0\x05&\xddH\xea\xd0\x82\x93\xda\x8c\xe2\xa2\x8b\x13\x7fJ\xc9\x8c\x0e\x97\x1b\x060%\x03;@\xd68,\xb9\xe2@")
		result2 = crypto2.decrypt_message(('', b'~\xd7\x96\xbc\x12\x1aWT\xc1\xa3\x9d*\xd8\x18\xde\xb8', b"p/@\xc3'v\x12\xc8\xd8\xa4\xad\xdfP\xb3*5;j@\xc4*\xcfL'\xb1G\x96\xdeo\\p\xe9"))
		self.assertEqual(result2, 'kanji漢字かんじ')
		self.assertEqual(result1, result2)

if __name__ == '__main__':
	unittest.main()
