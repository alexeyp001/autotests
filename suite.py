import unittest
import otchetnost_new
import elpodpis_new
import ofd_new
import cto_new
import dokument_new
import vetis_new
import edi_new
import kontr_new
import OdinC_new

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(otchetnost_new))
suite.addTest(loader.loadTestsFromModule(elpodpis_new))
suite.addTest(loader.loadTestsFromModule(ofd_new))
suite.addTest(loader.loadTestsFromModule(cto_new))
suite.addTest(loader.loadTestsFromModule(dokument_new))
suite.addTest(loader.loadTestsFromModule(OdinC_new))
suite.addTest(loader.loadTestsFromModule(vetis_new))
suite.addTest(loader.loadTestsFromModule(edi_new))
suite.addTest(loader.loadTestsFromModule(kontr_new))

runner = unittest.TextTestRunner(verbosity=8)
result = runner.run(suite)


