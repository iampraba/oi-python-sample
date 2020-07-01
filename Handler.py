import json

from ClientSideException import ZOIException
from Utility import APIConstants


class APIHandler(object):

    def __init__(self):
        self.request_api_end_point = None
        self.request_body = None
        self.request_files = None
        self.request_headers = None
        self.request_params = None
        self.request_method = None

    def add_param(self, key, value):
        if self.request_params is None:
            self.request_params = dict()
        self.request_params[key] = value

    def add_header(self, key, value):
        if self.request_headers is None:
            self.request_headers = dict()
        self.request_headers[key] = value


class ZOIAPIHandler(APIHandler):

    def __init__(self, editorobj):
        self.editor_obj = editorobj

    @staticmethod
    def get_instance(editorobj):
        return ZOIAPIHandler(editorobj)

    def writer_request_handler(self):
        try:
            api_handler_init = APIHandler()

            api_handler_init.request_api_end_point = self.editor_obj.api_end_point
            api_handler_init.request_method = APIConstants.REQUEST_METHOD_POST

            input_json = self.get_writer_object_as_json()

            try:
                from Utility import ZOIConfigUtil, CommonUtil
            except ImportError:
                from .Utility import ZOIConfigUtil, CommonUtil
            api_handler_init.request_body = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key(), input_json)
            if self.editor_obj.document is not None:
                api_handler_init.request_files = self.editor_obj.document
            try:
                from Request import APIRequest
            except ImportError:
                from .Request import APIRequest
            apiResponse = APIRequest(api_handler_init).get_api_response()
            apiResponse.data = self.editor_obj
            return apiResponse
        except ZOIException as ex:
            raise ex

    def sheet_show_request_handler(self):
        try:
            api_handler_init = APIHandler()

            api_handler_init.request_api_end_point = self.editor_obj.api_end_point
            api_handler_init.request_method = APIConstants.REQUEST_METHOD_POST

            input_json = self.get_sheet_show_object_as_json()

            try:
                from Utility import ZOIConfigUtil, CommonUtil
            except ImportError:
                from .Utility import ZOIConfigUtil, CommonUtil
            api_handler_init.request_body = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key(), input_json)
            if self.editor_obj.document is not None:
                api_handler_init.request_files = self.editor_obj.document
            try:
                from Request import APIRequest
            except ImportError:
                from .Request import APIRequest
            apiResponse = APIRequest(api_handler_init).get_api_response()
            apiResponse.data = self.editor_obj
            return apiResponse
        except ZOIException as ex:
            raise ex

    def delete_request_handler(self):
        try:
            api_handler_init = APIHandler()

            api_handler_init.request_api_end_point = self.editor_obj.api_end_point
            api_handler_init.request_method = APIConstants.REQUEST_METHOD_DELETE

            try:
                from Utility import ZOIConfigUtil, CommonUtil
            except ImportError:
                from .Utility import ZOIConfigUtil, CommonUtil
            api_handler_init.request_params = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key())
            try:
                from Request import APIRequest
            except ImportError:
                from .Request import APIRequest
            apiResponse = APIRequest(api_handler_init).get_api_response()
            apiResponse.data = self.editor_obj
            return apiResponse
        except ZOIException as ex:
            raise ex

    def get_writer_object_as_json(self):
        writer_json_obj = dict()

        # Checking Dictionary entries
        if self.editor_obj.callback_settings is not None:
            writer_json_obj["callback_settings"] = json.dumps(self.editor_obj.callback_settings)
        if self.editor_obj.document_defaults is not None:
            writer_json_obj["document_defaults"] = json.dumps(self.editor_obj.document_defaults)
        if self.editor_obj.editor_settings is not None:
            writer_json_obj["editor_settings"] = json.dumps(self.editor_obj.editor_settings)
        if self.editor_obj.permissions is not None:
            writer_json_obj["permissions"] = json.dumps(self.editor_obj.permissions)
        if self.editor_obj.document_info is not None:
            writer_json_obj["document_info"] = json.dumps(self.editor_obj.document_info)
        if self.editor_obj.user_info is not None:
            writer_json_obj["user_info"] = json.dumps(self.editor_obj.user_info)
        if self.editor_obj.ui_options is not None:
            writer_json_obj["ui_options"] = json.dumps(self.editor_obj.ui_options)
        if self.editor_obj.watermark_settings is not None:
            writer_json_obj["watermark_settings"] = json.dumps(self.editor_obj.watermark_settings)
        if self.editor_obj.merge_data is not None:
            writer_json_obj["merge_data"] = json.dumps(self.editor_obj.merge_data)
        if self.editor_obj.webhook is not None:
            writer_json_obj["webhook"] = json.dumps(self.editor_obj.webhook)

        # Checking String entries
        if self.editor_obj.lang is not None:
            writer_json_obj["lang"] = self.editor_obj.lang
        if self.editor_obj.output_format is not None:
            writer_json_obj["output_format"] = self.editor_obj.output_format
        if self.editor_obj.merge_to is not None:
            writer_json_obj["merge_to"] = self.editor_obj.merge_to
        if self.editor_obj.password is not None:
            writer_json_obj["password"] = self.editor_obj.password
        if self.editor_obj.format is not None:
            writer_json_obj["format"] = self.editor_obj.format
        if self.editor_obj.title is not None:
            writer_json_obj["title"] = self.editor_obj.title

        # Checking URL entries
        if self.editor_obj.isURL and self.editor_obj.url is not None:
            writer_json_obj["url"] = self.editor_obj.url
        if self.editor_obj.file_url is not None:
            writer_json_obj["file_url"] = self.editor_obj.file_url
        if self.editor_obj.merge_data_csv_url is not None:
            writer_json_obj["merge_data_csv_url"] = self.editor_obj.merge_data_csv_url
        if self.editor_obj.merge_data_json_url is not None:
            writer_json_obj["merge_data_json_url"] = self.editor_obj.merge_data_json_url
        if self.editor_obj.url1 is not None:
            writer_json_obj["url1"] = self.editor_obj.url1
        if self.editor_obj.url2 is not None:
            writer_json_obj["url2"] = self.editor_obj.url2

        return writer_json_obj

    def get_sheet_show_object_as_json(self):
        sheet_show_json_obj = dict()
        if self.editor_obj.callback_settings is not None:
            sheet_show_json_obj["callback_settings"] = json.dumps(self.editor_obj.callback_settings)
        if self.editor_obj.editor_settings is not None:
            sheet_show_json_obj["editor_settings"] = json.dumps(self.editor_obj.editor_settings)
        if self.editor_obj.permissions is not None:
            sheet_show_json_obj["permissions"] = json.dumps(self.editor_obj.permissions)
        if self.editor_obj.document_info is not None:
            sheet_show_json_obj["document_info"] = json.dumps(self.editor_obj.document_info)
        if self.editor_obj.user_info is not None:
            sheet_show_json_obj["user_info"] = json.dumps(self.editor_obj.user_info)
        if self.editor_obj.language is not None:
            sheet_show_json_obj["language"] = self.editor_obj.language
        if self.editor_obj.format is not None:
            sheet_show_json_obj["format"] = self.editor_obj.format
        return sheet_show_json_obj


class DocumentDefaultsHandler:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "docx",
            "save_url": "https://domain.com/save.php",
            "context_info": "doc or user info"
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
            "document.edit": True,
            "review.changes.resolve": True,
            "review.comment": True,
            "collab.chat": True,
            "document.pausecollaboration": False,
            "document.fill": True
        }

    @staticmethod
    def set_default_document_info(handler_obj):
        handler_obj.document_info = {
            "document_name": "New Document",
            "document_id": "20000"
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "user_id": 2000,
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
            "text": "DRAFT",
            "type": "text",
            "orientation": "diagonal",
            "font_name": "Arial",
            "font_size": 36,
            "font_color": "#000000",
            "opacity": 0.0
        }

    @staticmethod
    def set_default_webhook(handler_obj):
        handler_obj.webhook = {
            "invoke_url": "https://domain.com/xyz.php",
            "invoke_period": "oncomplete"
        }

    @staticmethod
    def set_default_merge_data(handler_obj):
        handler_obj.merge_data = {
            "data": [
                {
                    "name": "Amelia",
                    "email": "amelia@zylker.com"
                }
            ]
        }

    @staticmethod
    def set_default_lang(handler_obj):
        handler_obj.lang = "en"

    @staticmethod
    def set_default_output_format(handler_obj):
        handler_obj.add_request_body = "pdf"

    @staticmethod
    def set_default_merge_to(handler_obj):
        handler_obj.add_request_body = "separatedoc"

    @staticmethod
    def set_default_format(handler_obj):
        handler_obj.add_request_body = "docx"

    @staticmethod
    def set_default_create_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_callback_settings(handler_obj)
        DocumentDefaultsHandler.set_default_create_document_defaults(handler_obj)
        DocumentDefaultsHandler.set_default_editor_settings(handler_obj)
        DocumentDefaultsHandler.set_default_permissions(handler_obj)
        DocumentDefaultsHandler.set_default_document_info(handler_obj)
        DocumentDefaultsHandler.set_default_user_info(handler_obj)
        DocumentDefaultsHandler.set_default_ui_options(handler_obj)

    @staticmethod
    def set_default_edit_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_create_document_defaults(handler_obj)
        DocumentDefaultsHandler.set_default_edit_document_defaults(handler_obj)

    @staticmethod
    def set_default_co_edit_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_create_document_defaults(handler_obj)
        DocumentDefaultsHandler.set_default_edit_document_defaults(handler_obj)

    @staticmethod
    def set_default_preview_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_lang(handler_obj)

    @staticmethod
    def set_default_watermark_with_text_settings(handler_obj):
        DocumentDefaultsHandler.set_default_watermark_settings(handler_obj)

    @staticmethod
    def set_default_create_template_settings(handler_obj):
        DocumentDefaultsHandler.set_default_callback_settings(handler_obj)
        DocumentDefaultsHandler.set_default_create_document_defaults(handler_obj)
        DocumentDefaultsHandler.set_default_editor_settings(handler_obj)
        DocumentDefaultsHandler.set_default_permissions(handler_obj)
        DocumentDefaultsHandler.set_default_document_info(handler_obj)
        DocumentDefaultsHandler.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_merge_and_deliver_via_webhook(handler_obj):
        DocumentDefaultsHandler.set_default_output_format(handler_obj)
        DocumentDefaultsHandler.set_default_webhook(handler_obj)
        DocumentDefaultsHandler.set_default_merge_to(handler_obj)

    @staticmethod
    def set_default_merge_and_download_settings(handler_obj):
        DocumentDefaultsHandler.set_default_output_format(handler_obj)

    @staticmethod
    def set_default_convert_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_format(handler_obj)

    @staticmethod
    def set_default_compare_document_settings(handler_obj):
        DocumentDefaultsHandler.set_default_lang(handler_obj)


class SheetDefaultsHandler:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "xlsx",
            "save_url": "https://zylker.com/save.php",
            "context_info": "additional doc or user info"
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
            "document.edit": True
        }

    @staticmethod
    def set_default_preview_permissions(handler_obj):
        handler_obj.permissions = {
            "document.export": True,
            "document.print": True
        }

    @staticmethod
    def set_default_document_info(handler_obj):
        handler_obj.document_info = {
            "document_name": "New",
            "document_id": "1349"
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "display_name": "Guest"
        }

    @staticmethod
    def set_default_language(handler_obj):
        handler_obj.lang = "en"

    @staticmethod
    def set_default_create_spreadsheet_settings(handler_obj):
        SheetDefaultsHandler.set_default_callback_settings(handler_obj)
        SheetDefaultsHandler.set_default_editor_settings(handler_obj)
        SheetDefaultsHandler.set_default_permissions(handler_obj)
        SheetDefaultsHandler.set_default_document_info(handler_obj)
        SheetDefaultsHandler.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_edit_spreadsheet_settings(handler_obj):
        SheetDefaultsHandler.set_default_callback_settings(handler_obj)
        SheetDefaultsHandler.set_default_editor_settings(handler_obj)
        SheetDefaultsHandler.set_default_permissions(handler_obj)
        SheetDefaultsHandler.set_default_document_info(handler_obj)
        SheetDefaultsHandler.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_co_edit_spreadsheet_settings(handler_obj):
        SheetDefaultsHandler.set_default_edit_spreadsheet_settings(handler_obj)

    @staticmethod
    def set_default_preview_spreadsheet_settings(handler_obj):
        SheetDefaultsHandler.set_default_language(handler_obj)
        SheetDefaultsHandler.set_default_preview_permissions(handler_obj)


class ShowDefaultsHandler:

    @staticmethod
    def set_default_callback_settings(handler_obj):
        handler_obj.callback_settings = {
            "save_format": "pptx",
            "save_url": "https://domain.com/save.php",
            "context_info": "additional doc or user info"
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
            "document_name": "New",
            "document_id": "1349"
        }

    @staticmethod
    def set_default_user_info(handler_obj):
        handler_obj.user_info = {
            "user_id": "9173",
            "display_name": "Guest"
        }

    @staticmethod
    def set_default_language(handler_obj):
        handler_obj.language = "en"

    @staticmethod
    def set_default_format(handler_obj):
        handler_obj.add_request_body = "pptx"

    @staticmethod
    def set_default_create_presentation_settings(handler_obj):
        ShowDefaultsHandler.set_default_callback_settings(handler_obj)
        ShowDefaultsHandler.set_default_editor_settings(handler_obj)
        ShowDefaultsHandler.set_default_permissions(handler_obj)
        SheetDefaultsHandler.set_default_document_info(handler_obj)
        SheetDefaultsHandler.set_default_user_info(handler_obj)

    @staticmethod
    def set_default_edit_presentation_settings(handler_obj):
        ShowDefaultsHandler.set_default_create_presentation_settings(handler_obj)

    @staticmethod
    def set_default_co_edit_presentation_settings(handler_obj):
        ShowDefaultsHandler.set_default_create_presentation_settings(handler_obj)

    @staticmethod
    def set_default_preview_presentation_settings(handler_obj):
        ShowDefaultsHandler.set_default_language(handler_obj)

    @staticmethod
    def set_default_conversion_api_settings(handler_obj):
        ShowDefaultsHandler.set_default_format(handler_obj)
