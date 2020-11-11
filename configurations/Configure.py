from controllers.ClientSideException import ZOIException
from controllers.RestClient import ZOIRestClient


class Configure(object):

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def configure1():
        """
        Using in-built Setters
        """
        try:
            config_obj = ZOIRestClient.get_instance()
            config_obj.set_apikey("2ae438cf864488657cc9754a27daa480")
            config_obj.set_writer_api_base_url("https://api.office-integrator.com/writer/officeapi/")
            config_obj.set_sheet_api_base_url("https://api.office-integrator.com/sheet/officeapi/")
            config_obj.set_show_api_base_url("https://api.office-integrator.com/show/officeapi/")
            config_obj.initialize()
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def configure2():
        """
        Passing the entire configuration as a dictionary
        """
        try:
            config_obj = ZOIRestClient.get_instance()
            user_config = {
                "apikey": "2ae438cf864488657cc9754a27daa480",
                "writer_api_base_url": "https://api.office-integrator.com/writer/officeapi/",
                "sheet_api_base_url": "https://api.office-integrator.com/sheet/officeapi/",
                "show_api_base_url": "https://api.office-integrator.com/show/officeapi/"
            }
            config_obj.initialize(user_config)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def configure3():
        """
        Passing the configuration file
        """
        try:
            config_obj = ZOIRestClient.get_instance()
            config_obj.upload_configuration_file("../configurations/AppConfiguration.json")
            config_obj.initialize()
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)
