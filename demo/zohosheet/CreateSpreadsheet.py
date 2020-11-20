from controllers.ClientSideException import ZOIException
from controllers.Operations import CreateSpreadsheet
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
        oi_demo_obj = CreateSpreadsheet.get_instance()

        oi_demo_obj.set_callback_settings("save_format", "xlsx")
        oi_demo_obj.set_callback_settings("save_url", "https://zylker.com/save.php")
        oi_demo_obj.set_callback_settings("context_info", "additional doc or user info")

        oi_demo_obj.set_editor_settings("language", "en")
        oi_demo_obj.set_editor_settings("country", "IN")

        oi_demo_obj.set_permissions("document.export", True)
        oi_demo_obj.set_permissions("document.print", True)
        oi_demo_obj.set_permissions("document.edit", True)

        oi_demo_obj.set_document_info("document_name", "Untitled")
        # oi_demo_obj.set_document_info("document_id", document_id)

        oi_demo_obj.set_user_info("display_name", "Guest")

        response = oi_demo_obj.create_spreadsheet()
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
        oi_demo_obj = CreateSpreadsheet.get_instance()

        oi_demo_obj.set_bulk_callback_settings(
            save_format="xlsx",
            save_url="https://zylker.com/save.php",
            context_info="additional doc or user info"
        )

        oi_demo_obj.set_bulk_editor_settings(
            language="en",
            country="IN"
        )

        oi_demo_obj.set_bulk_permissions(
            document_export=True,
            document_print=True,
            document_edit=True
        )

        oi_demo_obj.set_bulk_document_info(
            # document_id=document_id,
            document_name="Untitled"
        )

        oi_demo_obj.set_user_info("display_name", "Guest")

        response = oi_demo_obj.create_spreadsheet()
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
        oi_demo_obj = CreateSpreadsheet.get_instance()

        callback_settings = {
            "save_format": "xlsx",
            "save_url": "https://zylker.com/save.php",
            "context_info": "additional doc or user info"
        }
        oi_demo_obj.set_bulk_callback_settings(callback_settings)

        editor_settings = {
            "language": "en",
            "country": "IN"
        }
        oi_demo_obj.set_bulk_editor_settings(editor_settings)

        permissions = {
            "document.export": True,
            "document.print": True,
            "document.edit": True
        }
        oi_demo_obj.set_bulk_permissions(permissions)

        document_info = {
            # document_id: document_id,
            "document_name": "Untitled"
        }
        oi_demo_obj.set_bulk_document_info(document_info)

        oi_demo_obj.set_user_info("display_name", "Guest")

        response = oi_demo_obj.create_spreadsheet()
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
