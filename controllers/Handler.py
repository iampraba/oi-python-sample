import json

from controllers.APIHelper import APIRequest
from controllers.ClientSideException import ZOIException
from controllers.RestClient import ZOIConfigUtil
from controllers.Utility import APIConstants, CommonUtil


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
        super().__init__()
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

            from controllers.RestClient import ZOIConfigUtil
            from controllers.Utility import CommonUtil
            api_handler_init.request_body = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key(),
                                                                                       input_json)
            if self.editor_obj.document is not None:
                api_handler_init.request_files = self.editor_obj.document

            api_response = APIRequest(api_handler_init).get_api_response()
            api_response.data = self.editor_obj
            return api_response
        except ZOIException as ex:
            raise ex

    def sheet_show_request_handler(self):
        try:
            api_handler_init = APIHandler()

            api_handler_init.request_api_end_point = self.editor_obj.api_end_point
            api_handler_init.request_method = APIConstants.REQUEST_METHOD_POST

            input_json = self.get_sheet_show_object_as_json()

            api_handler_init.request_body = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key(),
                                                                                       input_json)
            if self.editor_obj.document is not None:
                api_handler_init.request_files = self.editor_obj.document

            api_response = APIRequest(api_handler_init).get_api_response()
            api_response.data = self.editor_obj
            return api_response
        except ZOIException as ex:
            raise ex

    def delete_request_handler(self):
        try:
            api_handler_init = APIHandler()

            api_handler_init.request_api_end_point = self.editor_obj.api_end_point
            api_handler_init.request_method = APIConstants.REQUEST_METHOD_DELETE

            api_handler_init.request_params = CommonUtil.create_api_supported_input_json(ZOIConfigUtil.get_api_key())

            api_response = APIRequest(api_handler_init).get_api_response()
            api_response.data = self.editor_obj
            return api_response
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
        if self.editor_obj.output_options is not None:
            writer_json_obj["output_options"] = json.dumps(self.editor_obj.output_options)

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
        if self.editor_obj.url is not None and self.editor_obj.isURL:
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

        # Checking Dictionary entries
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

        # Checking String entries
        if self.editor_obj.language is not None:
            sheet_show_json_obj["language"] = self.editor_obj.language
        if self.editor_obj.format is not None:
            sheet_show_json_obj["format"] = self.editor_obj.format

        # Checking URL entries
        if self.editor_obj.url is not None and self.editor_obj.isURL:
            sheet_show_json_obj["url"] = self.editor_obj.url

        return sheet_show_json_obj
