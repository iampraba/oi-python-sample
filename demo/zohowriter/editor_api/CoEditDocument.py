from controllers.ClientSideException import ZOIException
from controllers.Operations import CoEditDocument
from controllers.RestClient import ZOIRestClient


def configure():
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

        # Used for demonstration only
        from controllers.RestClient import ZOIConfigUtil
        for key in ZOIConfigUtil.config_prop_dict:
            print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_1():
    try:
        oi_demo_obj = CoEditDocument.get_instance()

        oi_demo_obj.set_callback_settings("save_format", "docx")
        oi_demo_obj.set_callback_settings("save_url", "https://domain.com/save.php")
        oi_demo_obj.set_callback_settings("http_method_type", "post")
        oi_demo_obj.set_callback_settings("timeout", 120000)
        '''
            "save_url_params"
                If you wish to customize the above default keys or add some extra data that you need to 
            send back during save call, you can make use of the 'save_url_params' key of 'callback_settings' parameter.
                For more details regarding usage of save_url_params, 
            Visit https://www.zoho.com/officeplatform/integrator/api/v1/zoho-writer-create-document.html#saveurl_params
        '''
        save_url_params = {
            "file": "$content",
            "extension": "$format",
            "document_name": "$filename",
            "key1": "hgbb83h8ghejd92002jfnd",  # additional_user_key
            "key2": "p0oiu9ytr8e7sa65dfghj4",  # additional_user_key...
        }
        oi_demo_obj.set_callback_settings("save_url_params", save_url_params)

        oi_demo_obj.set_document_defaults("track_changes", "disabled")

        oi_demo_obj.set_editor_settings("unit", "in")
        oi_demo_obj.set_editor_settings("language", "en")
        oi_demo_obj.set_editor_settings("view", "pageview")

        oi_demo_obj.set_permissions("document.export", True)
        oi_demo_obj.set_permissions("document.print", True)
        oi_demo_obj.set_permissions("document.edit", True)
        oi_demo_obj.set_permissions("review.changes.resolve", False)
        oi_demo_obj.set_permissions("review.comment", False)
        oi_demo_obj.set_permissions("collab.chat", True)
        oi_demo_obj.set_permissions("document.pausecollaboration", False)
        oi_demo_obj.set_permissions("document.fill", True)

        oi_demo_obj.set_document_info("document_name", "Untitled")
        # oi_demo_obj.set_document_info("document_id", document_id)

        # oi_demo_obj.set_user_info("user_id", user_id)
        oi_demo_obj.set_user_info("display_name", "Guest")

        oi_demo_obj.set_ui_options("save_button", "show")
        oi_demo_obj.set_ui_options("chat_panel", "show")

        # Link used for demonstration purposes only
        oi_demo_obj.set_url("https://file-examples-com.github.io/uploads/2017/02/file-sample_500kB.docx")

        response = oi_demo_obj.co_edit_document()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_2():
    try:
        oi_demo_obj = CoEditDocument.get_instance()

        oi_demo_obj.set_bulk_callback_settings(
            save_format="docx",
            save_url="https://domain.com/save.php",
            save_url_params={
                "file": "$content",
                "extension": "$format",
                "document_name": "$filename",
                "key1": "hgbb83h8ghejd92002jfnd",  # additional_user_key
                "key2": "p0oiu9ytr8e7sa65dfghj4",  # additional_user_key...
            },
            http_method_type="post",
            timeout=120000,
            retries=None
        )
        oi_demo_obj.set_bulk_document_defaults(
            track_changes="disabled"
        )
        oi_demo_obj.set_bulk_editor_settings(
            unit="in",
            language="en",
            view="pageview"
        )
        oi_demo_obj.set_bulk_permissions(
            document_export=True,
            document_print=True,
            document_edit=True,
            review_changes_resolve=False,
            review_comment=False,
            collab_chat=True,
            document_pausecollaboration=False,
            document_fill=True
        )
        oi_demo_obj.set_bulk_document_info(
            # document_id=document_id,
            document_name="Untitled"
        )
        oi_demo_obj.set_bulk_user_info(
            # user_id=user_id,
            display_name="Guest"
        )
        oi_demo_obj.set_bulk_ui_options(
            save_button="show",
            chat_panel="show"
        )

        oi_demo_obj.upload_document("document", "../../files/ZohoWriter.docx")

        response = oi_demo_obj.co_edit_document()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def sample_3():
    try:
        oi_demo_obj = CoEditDocument.get_instance()

        callback_settings = {
            "save_format": "docx",
            "save_url": "https://domain.com/save.php",
            "http_method_type": "post",
            "timeout": 120000,
            "save_url_params": {
                "file": "$content",
                "extension": "$format",
                "document_name": "$filename",
                "key1": "hgbb83h8ghejd92002jfnd",  # additional_user_key
                "key2": "p0oiu9ytr8e7sa65dfghj4",  # additional_user_key...
            }
        }
        oi_demo_obj.set_bulk_callback_settings(callback_settings)

        document_defaults = {
            "track_changes": "disabled"
        }
        oi_demo_obj.set_bulk_document_defaults(document_defaults)

        editor_settings = {
            "unit": "in",
            "language": "en",
            "view": "pageview"
        }
        oi_demo_obj.set_bulk_editor_settings(editor_settings)

        permissions = {
            "document.export": True,
            "document.print": True,
            "document.edit": True,
            "review.changes.resolve": False,
            "review.comment": False,
            "collab.chat": True,
            "document.pausecollaboration": False,
            "document.fill": True
        }
        oi_demo_obj.set_bulk_permissions(permissions)

        document_info = {
            # "document_id": document_id,
            "document_name": "Untitled",
        }
        oi_demo_obj.set_bulk_document_info(document_info)

        user_info = {
            # "user_id": user_id,
            "display_name": "Guest"
        }
        oi_demo_obj.set_bulk_user_info(user_info)

        ui_options = {
            "save_button": "show",
            "chat_panel": "show"
        }
        oi_demo_obj.set_bulk_ui_options(ui_options)

        oi_demo_obj.upload_document("document", "../../files/ZohoWriter.docx")

        response = oi_demo_obj.co_edit_document()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


if __name__ == '__main__':
    configure()
    print()
    sample_1()
    print()
    sample_2()
    print()
    sample_3()
