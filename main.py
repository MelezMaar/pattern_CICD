import pytest
import scenario.scenario_01.tests.test_scenario_01 as scenario_01
#
options_for_test: str = "id001"
retcode = pytest.main(["-s", "-v", "-m", options_for_test])
#retcode = pytest.main()

#scenario_01.devise_for_test()
