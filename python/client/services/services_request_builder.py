from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.error import Error
    from .item.with_service_item_request_builder import WithServiceItemRequestBuilder
    from .services_get_response import ServicesGetResponse

class ServicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /services
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ServicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/services{?limit*,offset*}", path_parameters)
    
    def by_service_id(self,service_id: str) -> WithServiceItemRequestBuilder:
        """
        Gets an item from the ApiSdk.services.item collection
        param service_id: Service ID
        Returns: WithServiceItemRequestBuilder
        """
        if service_id is None:
            raise TypeError("service_id cannot be null.")
        from .item.with_service_item_request_builder import WithServiceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["serviceId"] = service_id
        return WithServiceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ServicesRequestBuilderGetQueryParameters]] = None) -> Optional[ServicesGetResponse]:
        """
        Retrieve a list of services (Viewer+ required)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.error import Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": Error,
            "403": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_get_response import ServicesGetResponse

        return await self.request_adapter.send_async(request_info, ServicesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ServicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a list of services (Viewer+ required)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ServicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServicesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServicesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ServicesRequestBuilderGetQueryParameters():
        """
        Retrieve a list of services (Viewer+ required)
        """
        # Maximum number of services to return
        limit: Optional[int] = None

        # Number of services to skip
        offset: Optional[int] = None

    
    @dataclass
    class ServicesRequestBuilderGetRequestConfiguration(RequestConfiguration[ServicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

