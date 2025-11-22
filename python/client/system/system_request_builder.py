from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .doctor.doctor_request_builder import DoctorRequestBuilder
    from .domain.domain_request_builder import DomainRequestBuilder
    from .info.info_request_builder import InfoRequestBuilder
    from .install.install_request_builder import InstallRequestBuilder
    from .register.register_request_builder import RegisterRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder

class SystemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /system
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SystemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/system", path_parameters)
    
    @property
    def doctor(self) -> DoctorRequestBuilder:
        """
        The doctor property
        """
        from .doctor.doctor_request_builder import DoctorRequestBuilder

        return DoctorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain(self) -> DomainRequestBuilder:
        """
        The domain property
        """
        from .domain.domain_request_builder import DomainRequestBuilder

        return DomainRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def install(self) -> InstallRequestBuilder:
        """
        The install property
        """
        from .install.install_request_builder import InstallRequestBuilder

        return InstallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def register(self) -> RegisterRequestBuilder:
        """
        The register property
        """
        from .register.register_request_builder import RegisterRequestBuilder

        return RegisterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    

