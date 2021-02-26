from nlpsandboxclient import client

from openapi_server.models.tool import Tool  # noqa: E501
from ..config import Config
from ..models import License, ToolDependencies


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501

    :rtype: Tool
    """
    tool = Tool(
        name="phi-deidentifier",
        version="1.0.0",
        license=License.APACHE_2_0,
        repository="github:nlpsandbox/phi-deidentifier",
        description="NLP Sandbox PHI Deidentifier",
        author="The NLP Sandbox Team",
        author_email="thomas.schaffter@sagebionetworks.org",
        url="https://github.com/nlpsandbox/phi-deidentifier",
        tool_type="nlpsandbox:phi-deidentifier",
        tool_api_version="1.0.0"
    )
    return tool, 200


def get_tool_dependencies():  # noqa: E501
    """Get tool dependencies

    Get the dependencies of this tool # noqa: E501


    :rtype: ToolDependencies
    """
    config = Config()
    tool_dependencies = []
    for hostname in (
        config.date_annotator_api_url,
        config.person_name_annotator_api_url,
        config.physical_address_annotator_api_url
    ):
        tool_dependencies.append(client.get_tool(host=hostname).to_dict())
    return ToolDependencies(tool_dependencies=tool_dependencies)
