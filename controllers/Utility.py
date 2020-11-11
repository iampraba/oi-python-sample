import random

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


class DocumentDefaults:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "zdoc",
            "http_method_type": "post",
            "retries": 0,
            "timeout": 120000
        }

    @staticmethod
    def set_default_create_document_defaults(handler_obj):
        handler_obj.document_defaults = {
            "orientation": "portrait",
            "paper_size": "Letter",
            "font_name": "Arial",
            "font_size": 12,
            "track_changes": "disabled",
            "margin":
                {
                    "left": "1in",
                    "right": "1in",
                    "top": "1in",
                    "bottom": "1in"
                }
        }

    @staticmethod
    def set_default_edit_document_defaults(handler_obj):
        handler_obj.document_defaults = {
            "track_changes": "disabled"
        }

    @staticmethod
    def set_default_editor_settings(handler_obj):
        handler_obj.editor_settings = {
            "unit": "in",
            "language": "en",
            "view": "pageview"
        }

    @staticmethod
    def set_default_permissions(handler_obj):
        handler_obj.permissions = {
            "document.export": True,
            "document.print": True,
            "document.edit": False,
            "review.changes.resolve": False,
            "review.comment": False,
            "collab.chat": True,
            "document.pausecollaboration": False,
            "document.fill": True
        }

    @staticmethod
    def set_default_document_info(handler_obj):
        handler_obj.document_info = {
            "document_name": "Untitled",
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "display_name": "Guest"
        }

    @staticmethod
    def set_default_ui_options(handler_obj):
        handler_obj.ui_options = {
            "save_button": "show",
            "chat_panel": "show"
        }

    @staticmethod
    def set_default_watermark_settings(handler_obj):
        handler_obj.watermark_settings = {
            "orientation": "diagonal",
            "font_name": "Arial",
            "font_size": 36,
            "font_color": "#000000",
            "opacity": 0.0
        }

    @staticmethod
    def set_default_webhook(handler_obj):
        handler_obj.webhook = {
            "invoke_period": "oncomplete"
        }

    @staticmethod
    def set_default_lang(handler_obj):
        handler_obj.lang = "en"

    @staticmethod
    def set_default_output_format(handler_obj):
        handler_obj.output_format = "docx"

    @staticmethod
    def set_default_output_options(handler_obj):
        handler_obj.output_options = {
            "format": "docx",
            "include_changes": "as_markups",
            "include_comments": "all"
        }

    @staticmethod
    def set_default_create_document_settings(handler_obj):
        DocumentDefaults.set_default_callback_settings(handler_obj)
        DocumentDefaults.set_default_create_document_defaults(handler_obj)
        DocumentDefaults.set_default_editor_settings(handler_obj)
        DocumentDefaults.set_default_permissions(handler_obj)
        DocumentDefaults.set_default_document_info(handler_obj)
        DocumentDefaults.set_default_user_info(handler_obj)
        DocumentDefaults.set_default_ui_options(handler_obj)

    @staticmethod
    def set_default_edit_document_settings(handler_obj):
        DocumentDefaults.set_default_callback_settings(handler_obj)
        DocumentDefaults.set_default_edit_document_defaults(handler_obj)
        DocumentDefaults.set_default_editor_settings(handler_obj)
        DocumentDefaults.set_default_permissions(handler_obj)
        DocumentDefaults.set_default_document_info(handler_obj)
        DocumentDefaults.set_default_user_info(handler_obj)
        DocumentDefaults.set_default_ui_options(handler_obj)

    @staticmethod
    def set_default_co_edit_document_settings(handler_obj):
        DocumentDefaults.set_default_callback_settings(handler_obj)
        DocumentDefaults.set_default_edit_document_defaults(handler_obj)
        DocumentDefaults.set_default_editor_settings(handler_obj)
        DocumentDefaults.set_default_permissions(handler_obj)
        DocumentDefaults.set_default_document_info(handler_obj)
        DocumentDefaults.set_default_user_info(handler_obj)
        DocumentDefaults.set_default_ui_options(handler_obj)

    @staticmethod
    def set_default_preview_document_settings(handler_obj):
        DocumentDefaults.set_default_lang(handler_obj)

    @staticmethod
    def set_default_watermark_with_text_settings(handler_obj):
        DocumentDefaults.set_default_watermark_settings(handler_obj)

    @staticmethod
    def set_default_create_template_settings(handler_obj):
        DocumentDefaults.set_default_callback_settings(handler_obj)
        DocumentDefaults.set_default_create_document_defaults(handler_obj)
        DocumentDefaults.set_default_editor_settings(handler_obj)
        DocumentDefaults.set_default_permissions(handler_obj)
        DocumentDefaults.set_default_document_info(handler_obj)
        DocumentDefaults.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_merge_and_deliver_via_webhook(handler_obj):
        DocumentDefaults.set_default_output_format(handler_obj)
        DocumentDefaults.set_default_webhook(handler_obj)

    @staticmethod
    def set_default_merge_and_download_settings(handler_obj):
        DocumentDefaults.set_default_output_format(handler_obj)

    @staticmethod
    def set_default_convert_document_settings(handler_obj):
        DocumentDefaults.set_default_output_options(handler_obj)

    @staticmethod
    def set_default_compare_document_settings(handler_obj):
        DocumentDefaults.set_default_lang(handler_obj)


class SheetDefaults:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "xlsx",
        }

    @staticmethod
    def set_default_editor_settings(handler_obj):
        handler_obj.editor_settings = {
            "language": "en",
            "country": "IN"
        }

    @staticmethod
    def set_default_permissions(handler_obj):
        handler_obj.permissions = {
            "document.export": True,
            "document.print": True,
            "document.edit": False
        }

    @staticmethod
    def set_default_document_info(handler_obj):
        handler_obj.document_info = {
            "document_name": "Untitled",
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "display_name": "Guest"
        }

    @staticmethod
    def set_default_preview_permissions(handler_obj):
        handler_obj.permissions = {
            "document.export": True,
            "document.print": True
        }

    @staticmethod
    def set_default_language(handler_obj):
        handler_obj.lang = "en"

    @staticmethod
    def set_default_create_spreadsheet_settings(handler_obj):
        SheetDefaults.set_default_callback_settings(handler_obj)
        SheetDefaults.set_default_editor_settings(handler_obj)
        SheetDefaults.set_default_permissions(handler_obj)
        SheetDefaults.set_default_document_info(handler_obj)
        SheetDefaults.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_edit_spreadsheet_settings(handler_obj):
        SheetDefaults.set_default_callback_settings(handler_obj)
        SheetDefaults.set_default_editor_settings(handler_obj)
        SheetDefaults.set_default_permissions(handler_obj)
        SheetDefaults.set_default_document_info(handler_obj)
        SheetDefaults.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_co_edit_spreadsheet_settings(handler_obj):
        SheetDefaults.set_default_edit_spreadsheet_settings(handler_obj)

    @staticmethod
    def set_default_preview_spreadsheet_settings(handler_obj):
        SheetDefaults.set_default_language(handler_obj)
        SheetDefaults.set_default_preview_permissions(handler_obj)


class ShowDefaults:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "pptx",
            "save_url": "https://zylker.com/save.php",
        }

    @staticmethod
    def set_default_editor_settings(handler_obj):
        handler_obj.editor_settings = {
            "language": "en"
        }

    @staticmethod
    def set_default_permissions(handler_obj):
        handler_obj.permissions = {
            "document.export": True,
            "document.print": True,
            "document.edit": True
        }

    @staticmethod
    def set_default_document_info(handler_obj):
        handler_obj.document_info = {
            "document_name": "Untitled",
            "document_id": random.randint(10000000, 100000000)
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "user_id": random.randint(1000000, 10000000),
            "display_name": "Guest"
        }

    @staticmethod
    def set_default_language(handler_obj):
        handler_obj.language = "en"

    @staticmethod
    def set_default_format(handler_obj):
        handler_obj.format = "pptx"

    @staticmethod
    def set_default_create_presentation_settings(handler_obj):
        ShowDefaults.set_default_callback_settings(handler_obj)
        ShowDefaults.set_default_editor_settings(handler_obj)
        ShowDefaults.set_default_permissions(handler_obj)
        SheetDefaults.set_default_document_info(handler_obj)
        SheetDefaults.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_edit_presentation_settings(handler_obj):
        ShowDefaults.set_default_create_presentation_settings(handler_obj)

    @staticmethod
    def set_default_co_edit_presentation_settings(handler_obj):
        ShowDefaults.set_default_create_presentation_settings(handler_obj)

    @staticmethod
    def set_default_preview_presentation_settings(handler_obj):
        ShowDefaults.set_default_language(handler_obj)

    @staticmethod
    def set_default_conversion_api_settings(handler_obj):
        ShowDefaults.set_default_format(handler_obj)


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
            # attachment_dict[key] = open(reqFiles[key], 'rb')
        return attachment_dict

    @staticmethod
    def create_api_supported_input_json(api_key, req_body_json=None):
        if req_body_json is None:
            req_body_json = dict()
        req_body_json[APIConstants.API_KEY] = api_key
        return req_body_json

    @staticmethod
    def raise_exception(url, message, details, content=None):
        zoi_exception = ZOIException(url, APIConstants.RESPONSECODE_INVALID_INPUT, message, APIConstants.STATUS_ERROR,
                                     details, content)
        import logging
        try:
            from controllers.ClientSideException import Logger
        except ImportError:
            from .ClientSideException import Logger
        Logger.add_log(message, logging.ERROR, zoi_exception)
        raise zoi_exception
