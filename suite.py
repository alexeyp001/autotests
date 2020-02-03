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
import regions
import tp_search

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
suite.addTest(loader.loadTestsFromModule(tp_search))
suite.addTest(loader.loadTestsFromModule(regions))

runner = unittest.TextTestRunner(verbosity=10)
result = runner.run(suite)


