import requests

from ClientSideException import ZOIException


class HTTPConnector(object):

    @staticmethod
    def get_instance(url, params, headers, body, method):
        """
        :param url:
        :param params:
        :param headers:
        :param body:
        :param method:
        :return:
        """
        return HTTPConnector(url, params, headers, body, method)

    def __init__(self, url, params, headers, body, method):
        self.url = url
        self.req_headers = headers
        self.req_method = method
        self.req_params = params
        self.req_body = body
        self.file = None

    def trigger_request(self):
        response = None

        # For Testing these temporary print statements are included!!!
        # print(self.url)
        # print(self.req_headers)
        # print(self.req_method)
        # print(self.req_params)
        # print(self.req_body)
        # print(self.file)

        if self.req_method == APIConstants.REQUEST_METHOD_GET:
            response = requests.get(self.url, headers=self.req_headers, params=self.req_params, allow_redirects=False)
        elif self.req_method == APIConstants.REQUEST_METHOD_PUT:
            response = requests.put(self.url, data=self.req_body, params=self.req_params,
                                    headers=self.req_headers, allow_redirects=False)
        elif self.req_method == APIConstants.REQUEST_METHOD_POST:
            if self.file is None:
                response = requests.post(self.url, data=self.req_body, params=self.req_params,
                                         headers=self.req_headers, allow_redirects=False)
            else:
                response = requests.post(self.url, files=self.file, headers=self.req_headers, allow_redirects=False,
                                         data=self.req_body)
        elif self.req_method == APIConstants.REQUEST_METHOD_DELETE:
            response = requests.delete(self.url, headers=self.req_headers, params=self.req_params,
                                       allow_redirects=False)
        return response

    @staticmethod
    def get_request_params_as_string(params):
        mapAsString = ''
        for key in params:
            mapAsString += key + '=' + params[key]
        return mapAsString

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def add_http_header(self, key, value):
        self.req_headers.put(key, value)

    def get_http_headers(self):
        return self.req_headers

    def set_http_request_method(self, method):
        self.req_method = method

    def get_http_request_method(self):
        return self.req_method

    def set_request_body(self, reqBody):
        self.req_body = reqBody

    def get_request_body(self):
        return self.req_body

    def add_http_request_params(self, key, value):
        self.req_params.put(key, value)

    def get_http_request_params(self):
        return self.req_params

    def set_file(self, file_content):
        self.file = file_content


class APIConstants:
    REQUEST_METHOD_POST = "POST"
    REQUEST_METHOD_GET = "GET"
    REQUEST_METHOD_DELETE = "DELETE"
    REQUEST_METHOD_PUT = "PUT"

    OAUTH_HEADER_PREFIX = "Zoho-oauthtoken "
    AUTHORIZATION = "Authorization"

    CODE_SUCCESS = "SUCCESS"

    STATUS_SUCCESS = "success"
    STATUS_ERROR = "error"
    INVALID_ID_MSG = "The given id seems to be invalid."
    INVALID_DATA = "INVALID_DATA"
    NO_CONTENT = "No Content"
    NOT_MODIFIED = "Not Modified"
    MESSAGE = "message"
    CODE = "code"
    STATUS = "status"
    DETAILS = "details"

    # POSSIBLE MANDATORY PARAMETERS
    API_KEY = "apikey"
    APPLICATION_LOGFILE_PATH = "applicationLogFilePath"
    CALLBACK_SETTINGS = "callback_settings"
    DATA = "data"
    DOCUMENT = "document"
    URL = "url"
    WATERMARK_SETTINGS = "watermark_settings"
    FORMAT = "format"
    DOCUMENT_1 = "document1"
    DOCUMENT_2 = "document2"
    URL_1 = "url1"
    URL_2 = "url2"
    SESSION_ID = "session_id"
    DOCUMENT_ID = "document_id"
    MERGE_DATA = "merge_data"
    MERGE_DATA_CSV_CONTENT = "merge_data_csv_content"
    MERGE_DATA_JSON_CONTENT = "merge_data_json_content"
    MERGE_DATA_CSV_URL = "merge_data_csv_url"
    MERGE_DATA_JSON_URL = "merge_data_json_url"
    FILE_CONTENT = "file_content"
    PASSWORD = "password"
    FILE_URL = "file_url"
    OUTPUT_FORMAT = "output_format"
    WEBHOOK = "webhook"
    MERGE_TO = "merge_to"

    # OPTIONAL PARAMETERS
    DOCUMENT_DEFAULTS = "document_defaults"
    EDITOR_SETTINGS = "editor_settings"
    PERMISSIONS = "permissions"
    DOCUMENT_INFO = "document_info"
    USER_INFO = "user_info"
    UI_OPTIONS = "ui_options"
    LANGUAGE = "lang"
    TITLE = "title"

    # API-SPECIFIC REQUIRED PARAMETERS
    CREATE_DOCUMENT = [API_KEY, CALLBACK_SETTINGS, DOCUMENT_DEFAULTS, EDITOR_SETTINGS, PERMISSIONS, DOCUMENT_INFO,
                       USER_INFO, UI_OPTIONS]
    EDIT_DOCUMENT = [API_KEY, CALLBACK_SETTINGS, DOCUMENT, URL, DOCUMENT_DEFAULTS, EDITOR_SETTINGS, PERMISSIONS,
                     DOCUMENT_INFO, USER_INFO, UI_OPTIONS]
    PREVIEW_DOCUMENT = [API_KEY, DOCUMENT, URL, LANGUAGE]
    WATERMARK_WITH_TEXT = [API_KEY, DOCUMENT, URL, WATERMARK_SETTINGS]
    CREATE_TEMPLATE = [API_KEY, CALLBACK_SETTINGS, MERGE_DATA_CSV_CONTENT, MERGE_DATA_JSON_CONTENT, DOCUMENT, URL,
                       DOCUMENT_DEFAULTS, EDITOR_SETTINGS, PERMISSIONS, DOCUMENT_INFO, USER_INFO]
    GET_FIELDS = [API_KEY, FILE_CONTENT, FILE_URL]
    MERGE_AND_DELIVER_VIA_WEBHOOK = [API_KEY, OUTPUT_FORMAT, FILE_CONTENT, FILE_URL, WEBHOOK, MERGE_TO,
                                     MERGE_DATA,
                                     MERGE_DATA_CSV_CONTENT, MERGE_DATA_JSON_CONTENT, MERGE_DATA_CSV_URL,
                                     MERGE_DATA_JSON_URL, PASSWORD]
    MERGE_AND_DOWNLOAD = [API_KEY, OUTPUT_FORMAT, FILE_CONTENT, FILE_URL, MERGE_DATA, MERGE_DATA_CSV_CONTENT,
                          MERGE_DATA_JSON_CONTENT, MERGE_DATA_CSV_URL, MERGE_DATA_JSON_URL, PASSWORD]
    CONVERSION = [API_KEY, DOCUMENT, URL, FORMAT]
    COMPARISON = [API_KEY, DOCUMENT_1, DOCUMENT_2, URL_1, URL_2, TITLE, LANGUAGE]

    WRITER_API_BASEURL = "writer_api_base_url"
    SHEET_API_BASEURL = "sheet_api_base_url"
    SHOW_API_BASEURL = "show_api_base_url"
    WRITER_API_VERSION = "writer_api_version"
    SHEET_API_VERSION = "sheet_api_version"
    SHOW_API_VERSION = "show_api_version"
    DOCUMENT_TYPE = "document_type"

    RESPONSECODE_OK = 200
    RESPONSECODE_CREATED = 201
    RESPONSECODE_ACCEPTED = 202
    RESPONSECODE_NO_CONTENT = 204
    RESPONSECODE_MOVED_PERMANENTLY = 301
    RESPONSECODE_MOVED_TEMPORARILY = 302
    RESPONSECODE_NOT_MODIFIED = 304
    RESPONSECODE_BAD_REQUEST = 400
    RESPONSECODE_AUTHORIZATION_ERROR = 401
    RESPONSECODE_FORBIDDEN = 403
    RESPONSECODE_NOT_FOUND = 404
    RESPONSECODE_METHOD_NOT_ALLOWED = 405
    RESPONSECODE_REQUEST_ENTITY_TOO_LARGE = 413
    RESPONSECODE_UNSUPPORTED_MEDIA_TYPE = 415
    RESPONSECODE_TOO_MANY_REQUEST = 429
    RESPONSECODE_INTERNAL_SERVER_ERROR = 500
    RESPONSECODE_INVALID_INPUT = 0

    FAULTY_RESPONSE_CODES = [RESPONSECODE_NO_CONTENT, RESPONSECODE_NOT_FOUND, RESPONSECODE_AUTHORIZATION_ERROR,
                             RESPONSECODE_BAD_REQUEST, RESPONSECODE_FORBIDDEN, RESPONSECODE_INTERNAL_SERVER_ERROR,
                             RESPONSECODE_METHOD_NOT_ALLOWED, RESPONSECODE_MOVED_PERMANENTLY,
                             RESPONSECODE_MOVED_TEMPORARILY, RESPONSECODE_REQUEST_ENTITY_TOO_LARGE,
                             RESPONSECODE_TOO_MANY_REQUEST, RESPONSECODE_UNSUPPORTED_MEDIA_TYPE,
                             RESPONSECODE_NOT_MODIFIED]


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

        try:
            from RestClient import ZOIRestClient
        except ImportError:
            from .RestClient import ZOIRestClient

        for key in mandatory_keys:
            if key not in config_dict:
                print(key + " is mandatory")
            elif key in config_dict and (config_dict[key] is None or config_dict[key] == ""):
                print(key + " value is missing")
        ZOIConfigUtil.set_config_values(config_dict)
        print(ZOIConfigUtil.config_prop_dict)

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
            ZOIConfigUtil.config_prop_dict[APIConstants.WRITER_API_BASEURL] = "https://writer.zoho.com/writer/officeapi/"

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


class CommonUtil:

    @staticmethod
    def TrueFalseUtility(value):
        if isinstance(value, str):
            return value.lower()
        elif isinstance(value, bool):
            if value:
                return "true"
            else:
                return "false"

    @staticmethod
    def ListDictionaryUtility(settings, input_dictionary):
        for setting, dict_key in zip(settings, input_dictionary.keys()):
            input_dictionary[dict_key] = setting
        return input_dictionary

    @staticmethod
    def create_api_supported_attachments_dictionary(reqFiles):
        attachment_dict = dict()
        for key in reqFiles.keys():
            with open(reqFiles[key], 'rb') as f:
                attachment_dict[key] = f.read()
            f.close()
            # attachment_dict[key] = open(reqFiles[key], 'rb')
        return attachment_dict

    @staticmethod
    def create_api_supported_input_json(api_key, reqBodyJson=None):
        if reqBodyJson is None:
            reqBodyJson = dict()
        reqBodyJson[APIConstants.API_KEY] = api_key
        return reqBodyJson

    @staticmethod
    def raise_exception(url, message, details, content=None):
        zoi_exception = ZOIException(url, APIConstants.RESPONSECODE_INVALID_INPUT, message, APIConstants.STATUS_ERROR,
                                     details, content)
        import logging
        try:
            from ClientSideException import Logger
        except ImportError:
            from .ClientSideException import Logger
        Logger.add_log(message, logging.ERROR, zoi_exception)
        raise zoi_exception
