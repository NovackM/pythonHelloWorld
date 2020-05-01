import unittest
from unittest import mock

# explained mocking well
# https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2


class ExternalServices():

    def call_service(self, request_params):
        return "Called Service"


class AppLogic():

    ext_services = ExternalServices()

    def do_logic(self):
        service_data = self.ext_services.call_service(["some", "items"])
        return f"{service_data} and logic was performed"


class TestSuite(unittest.TestCase):

    def test_no_mock(self):
        self.assertEqual(AppLogic().do_logic(), "Called Service and logic was performed")
    
    @mock.patch('external_depen_test.ExternalServices')
    def test_mock_good_service_call(self, mock_call_service):
        logic = AppLogic()
        logic.ext_services = mock_call_service
        mock_call_service.call_service.return_value = "Overide Service Impl"
        self.assertEqual(logic.do_logic(), "Overide Service Impl and logic was performed")

    def side_effect_function(self, requestParams):
        raise RuntimeError("Something mysterious happened")

    @mock.patch('external_depen_test.ExternalServices')
    def test_mock_bad_service_call(self, mock_call_service):
        logic = AppLogic()
        logic.ext_services = mock_call_service
        mock_call_service.call_service.side_effect = self.side_effect_function
        self.assertRaises(RuntimeError, logic.do_logic)


if __name__ == '__main__':
    unittest.main()