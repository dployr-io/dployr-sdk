"""
MIT License
Copyright (c) 2025 Emmanuel Madehin
See LICENSE file for full license text

dployr-sdk: Python SDK for dployr

A Python client library for interacting with the Dployr API.
Provides authentication, deployment management, service control, and more.
"""

from .client_factory import create_dployr_client, TokenManager

__version__ = "2.0.0"
__all__ = ["create_dployr_client", "TokenManager"]
