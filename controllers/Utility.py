from controllers.ClientSideException import ZOIException


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
    INVALID_DATA = "INVALID_DATA"
    INVALID_ID_MSG = "The given id seems to be invalid."
    NO_CONTENT = "No Content"
    NOT_MODIFIED = "Not Modified"
    MESSAGE = "message"
    CODE = "code"
    STATUS = "status"

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

    RESPONSE_CODE_OK = 200
    RESPONSE_CODE_CREATED = 201
    RESPONSE_CODE_ACCEPTED = 202
    RESPONSE_CODE_NO_CONTENT = 204
    RESPONSE_CODE_MOVED_PERMANENTLY = 301
    RESPONSE_CODE_MOVED_TEMPORARILY = 302
    RESPONSE_CODE_NOT_MODIFIED = 304
    RESPONSE_CODE_BAD_REQUEST = 400
    RESPONSE_CODE_AUTHORIZATION_ERROR = 401
    RESPONSE_CODE_FORBIDDEN = 403
    RESPONSE_CODE_NOT_FOUND = 404
    RESPONSE_CODE_METHOD_NOT_ALLOWED = 405
    RESPONSE_CODE_REQUEST_ENTITY_TOO_LARGE = 413
    RESPONSE_CODE_UNSUPPORTED_MEDIA_TYPE = 415
    RESPONSE_CODE_TOO_MANY_REQUEST = 429
    RESPONSE_CODE_INTERNAL_SERVER_ERROR = 500
    RESPONSE_CODE_INVALID_INPUT = 0

    FAULTY_RESPONSE_CODES = [RESPONSE_CODE_NO_CONTENT, RESPONSE_CODE_NOT_FOUND, RESPONSE_CODE_AUTHORIZATION_ERROR,
                             RESPONSE_CODE_BAD_REQUEST, RESPONSE_CODE_FORBIDDEN, RESPONSE_CODE_INTERNAL_SERVER_ERROR,
                             RESPONSE_CODE_METHOD_NOT_ALLOWED, RESPONSE_CODE_MOVED_PERMANENTLY,
                             RESPONSE_CODE_MOVED_TEMPORARILY, RESPONSE_CODE_REQUEST_ENTITY_TOO_LARGE,
                             RESPONSE_CODE_TOO_MANY_REQUEST, RESPONSE_CODE_UNSUPPORTED_MEDIA_TYPE,
                             RESPONSE_CODE_NOT_MODIFIED]


class CommonUtil:

    @staticmethod
    def true_false_utility(value):
        if isinstance(value, str):
            return value.lower()
        elif isinstance(value, bool):
            if value:
                return "true"
            else:
                return "false"

    @staticmethod
    def create_api_supported_attachments_dictionary(req_files):
        attachment_dict = dict()
        for key in req_files.keys():
            with open(req_files[key], 'rb') as f:
                attachment_dict[key] = f.read()
            f.close()
        return attachment_dict

    @staticmethod
    def create_api_supported_input_json(api_key, req_body_json=None):
        if req_body_json is None:
            req_body_json = dict()
        req_body_json[APIConstants.API_KEY] = api_key
        return req_body_json

    @staticmethod
    def raise_exception(url, message, details, content=None):
        zoi_exception = ZOIException(url, APIConstants.RESPONSE_CODE_INVALID_INPUT, message, APIConstants.STATUS_ERROR,
                                     details, content)
        import logging
        try:
            from controllers.ClientSideException import Logger
        except ImportError:
            from .ClientSideException import Logger
        Logger.add_log(message, logging.ERROR, zoi_exception)
        raise zoi_exception
