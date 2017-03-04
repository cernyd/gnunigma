from gui import Root
from enigma.components import TestEnigma, unittest, EnigmaFactory, EnigmaM4
from cfg_handler import Config


config = Config('config.xml')
config.focus_buffer('globals')
config.find('font')
font = list(config.find('font').values())
bg = config.find('bg')['color']
enigma_cfg = config.find('enigma_defaults')
root = Root(enigma_cfg, Config('config.xml'), bg, font)


# Main unittest before running, could warn about potential flaws
if config.find(['unit_tests'])['startup_test'] == "True":
    TestEnigma.model = enigma_cfg['model']
    TestEnigma.cfg_path = ['config.xml']
    unittest.main(exit=False, verbosity=2)


if __name__ == '__main__':
    root.mainloop()
