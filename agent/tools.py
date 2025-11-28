
import os

from toolbox_core import auth_methods
from toolbox_langchain import ToolboxClient

TOOLBOX_URL = os.getenv("TOOLBOX_URL", default="http://127.0.0.1:5000")


async def initialize_tools():

    auth_token_provider = auth_methods.aget_google_id_token(TOOLBOX_URL)
    client = ToolboxClient(
        TOOLBOX_URL, client_headers={"Authorization": auth_token_provider}
    )

    tools = await client.aload_toolset("bcel_products")

    return tools
