import json

from controllers.Utility import APIConstants


class ZOIRestClient(object):

    def __init__(self):
        self.apikey = None
        self.writer_api_base_url = None
        self.sheet_api_base_url = None
        self.show_api_base_url = None
        self.writer_api_version = None
        self.sheet_api_version = None
        self.show_api_version = None
        self.isConfigAsFile = False

    @staticmethod
    def get_instance():
        return ZOIRestClient()

    def set_apikey(self, value=None):
        if value is not None:
            self.apikey = value
        else:
            print("API Key is mandatory for Configuration")
            exit(1)

    def set_writer_api_base_url(self, value=None):
        if value is not None:
            self.writer_api_base_url = value

    def set_sheet_api_base_url(self, value=None):
        if value is not None:
            self.sheet_api_base_url = value

    def set_show_api_base_url(self, value=None):
        if value is not None:
            self.show_api_base_url = value

    def set_writer_api_version(self, value=None):
        if value is not None:
            self.writer_api_version = value

    def set_sheet_api_version(self, value=None):
        if value is not None:
            self.sheet_api_version = value

    def set_show_api_version(self, value=None):
        if value is not None:
            self.show_api_version = value

    def set_configuration(self, apikey=None, writer_api_base_url=None, sheet_api_base_url=None, show_api_base_url=None,
                          writer_api_version=None, sheet_api_version=None, show_api_version=None):
        if apikey is not None:
            self.apikey = apikey
            self.writer_api_base_url = writer_api_base_url
            self.sheet_api_base_url = sheet_api_base_url
            self.show_api_base_url = show_api_base_url
            self.writer_api_version = writer_api_version
            self.sheet_api_version = sheet_api_version
            self.show_api_version = show_api_version
        else:
            print("API Key is mandatory for Configuration")
            exit(1)

    def upload_configuration_file(self, config_file_path=None):
        if config_file_path is not None:
            with open(config_file_path) as config_file:
                config = json.load(config_file)
            if config[APIConstants.API_KEY]:
                self.isConfigAsFile = True
                self.apikey = config[APIConstants.API_KEY]
                self.writer_api_base_url = config.get(APIConstants.WRITER_API_BASEURL, None)
                self.sheet_api_base_url = config.get(APIConstants.SHEET_API_BASEURL, None)
                self.show_api_base_url = config.get(APIConstants.SHOW_API_BASEURL, None)
                self.writer_api_version = config.get(APIConstants.WRITER_API_VERSION, None)
                self.sheet_api_version = config.get(APIConstants.SHEET_API_VERSION, None)
                self.show_api_version = config.get(APIConstants.SHOW_API_VERSION, None)
            else:
                print("API Key is mandatory for Configuration")
                exit(1)
        else:
            print("Configuration file path cannot be empty!")
            exit(1)

    def initialize(self, config_dict=None):
        if config_dict is not None:
            ZOIConfigUtil.initialize(config_dict)
        else:
            ZOIConfigUtil.initialize(self.get_config_as_dict())

    def get_current_user_api_key(self):
        return self.apikey

    def get_config_as_dict(self):
        config_dict = dict()
        config_dict[APIConstants.API_KEY] = self.apikey
        config_dict[APIConstants.WRITER_API_BASEURL] = self.writer_api_base_url
        config_dict[APIConstants.SHEET_API_BASEURL] = self.sheet_api_base_url
        config_dict[APIConstants.SHOW_API_BASEURL] = self.show_api_base_url
        config_dict[APIConstants.WRITER_API_VERSION] = self.writer_api_version
        config_dict[APIConstants.SHEET_API_VERSION] = self.sheet_api_version
        config_dict[APIConstants.SHOW_API_VERSION] = self.show_api_version
        return config_dict


class ZOIConfigUtil(object):
    config_prop_dict = {}

    @staticmethod
    def get_instance():
        return ZOIConfigUtil()

    @staticmethod
    def initialize(config_dict=None):
        if config_dict is None:
            print("Configuration dictionary is mandatory to initialize RestClient")
        mandatory_keys = [APIConstants.API_KEY]

        for key in mandatory_keys:
            if key not in config_dict:
                print(key + " is mandatory")
            elif key in config_dict and (config_dict[key] is None or config_dict[key] == ""):
                print(key + " value is missing")
        ZOIConfigUtil.set_config_values(config_dict)

        # Printing Configuration Details
        for key in ZOIConfigUtil.config_prop_dict:
            print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))

    @staticmethod
    def get_writer_api_base_url():
        return ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_BASEURL] + \
               ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_VERSION]

    @staticmethod
    def get_sheet_api_base_url():
        return ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_BASEURL] + \
               ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_VERSION]

    @staticmethod
    def get_show_api_base_url():
        return ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_BASEURL] + \
               ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_VERSION]

    @staticmethod
    def set_config_values(config_dict):

        config_keys = [
            APIConstants.API_KEY, APIConstants.WRITER_API_BASEURL, APIConstants.WRITER_API_VERSION,
            APIConstants.SHEET_API_BASEURL, APIConstants.SHEET_API_VERSION, APIConstants.SHOW_API_BASEURL,
            APIConstants.SHOW_API_VERSION, APIConstants.APPLICATION_LOGFILE_PATH
        ]

        if APIConstants.WRITER_API_BASEURL not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_BASEURL] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_BASEURL] is None:
            ZOIConfigUtil.config_prop_dict[
                APIConstants.WRITER_API_BASEURL] = "https://writer.zoho.com/writer/officeapi/"

        if APIConstants.SHEET_API_BASEURL not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_BASEURL] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_BASEURL] is None:
            ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_BASEURL] = "https://sheet.zoho.com/sheet/officeapi/"

        if APIConstants.SHOW_API_BASEURL not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_BASEURL] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_BASEURL] is None:
            ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_BASEURL] = "https://show.zoho.com/show/officeapi/"

        if APIConstants.WRITER_API_VERSION not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_VERSION] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_VERSION] is None:
            ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_VERSION] = "v1/"

        if APIConstants.SHEET_API_VERSION not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_VERSION] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_VERSION] is None:
            ZOIConfigUtil.config_prop_dict[APIConstants.SHEET_API_VERSION] = "v1/"

        if APIConstants.SHOW_API_VERSION not in ZOIConfigUtil.config_prop_dict or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_VERSION] == "" or \
                ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_VERSION] is None:
            ZOIConfigUtil.config_prop_dict[APIConstants.SHOW_API_VERSION] = "v1/"

        for key in config_keys:
            if key in config_dict and config_dict[key] != "" and config_dict[key] is not None:
                ZOIConfigUtil.config_prop_dict[key] = config_dict[key].strip()

    @staticmethod
    def get_api_key():
        return ZOIConfigUtil.config_prop_dict[APIConstants.API_KEY]
