# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class Service(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, version=None, license=None, repository=None, description=None, author=None, author_email=None, url=None):  # noqa: E501
        """Service - a model defined in OpenAPI

        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param version: The version of this Service.  # noqa: E501
        :type version: str
        :param license: The license of this Service.  # noqa: E501
        :type license: str
        :param repository: The repository of this Service.  # noqa: E501
        :type repository: str
        :param description: The description of this Service.  # noqa: E501
        :type description: str
        :param author: The author of this Service.  # noqa: E501
        :type author: str
        :param author_email: The author_email of this Service.  # noqa: E501
        :type author_email: str
        :param url: The url of this Service.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'name': str,
            'version': str,
            'license': str,
            'repository': str,
            'description': str,
            'author': str,
            'author_email': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'license': 'license',
            'repository': 'repository',
            'description': 'description',
            'author': 'author',
            'author_email': 'authorEmail',
            'url': 'url'
        }

        self._name = name
        self._version = version
        self._license = license
        self._repository = repository
        self._description = description
        self._author = author
        self._author_email = author_email
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Service':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Service of this Service.  # noqa: E501
        :rtype: Service
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Service.

        The service name  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.

        The service name  # noqa: E501

        :param name: The name of this Service.
        :type name: str
        """
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this Service.

        The version of the service (SemVer string)  # noqa: E501

        :return: The version of this Service.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Service.

        The version of the service (SemVer string)  # noqa: E501

        :param version: The version of this Service.
        :type version: str
        """
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501
        if version is not None and not re.search(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$', version):  # noqa: E501
            raise ValueError("Invalid value for `version`, must be a follow pattern or equal to `/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$/`")  # noqa: E501

        self._version = version

    @property
    def license(self):
        """Gets the license of this Service.

        The license of this service (spdx.org/licenses Identifier)  # noqa: E501

        :return: The license of this Service.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Service.

        The license of this service (spdx.org/licenses Identifier)  # noqa: E501

        :param license: The license of this Service.
        :type license: str
        """
        allowed_values = ["afl-3.0", "apache-2.0", "artistic-2.0", "bsl-1.0", "bsd-2-clause", "bsd-3-clause", "bsd-3-clause-clear", "cc", "cc0-1.0", "cc-by-4.0", "cc-by-sa-4.0", "wtfpl", "ecl-2.0", "epl-1.0", "epl-2.0", "eupl-1.1", "agpl-3.0", "gpl", "gpl-2.0", "gpl-3.0", "lgpl", "lgpl-2.1", "lgpl-3.0", "isc", "lppl-1.3c", "ms-pl", "mit", "mpl-2.0", "osl-3.0", "postgresql", "ofl-1.1", "ncsa", "unlicense", "zlib"]  # noqa: E501
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"
                .format(license, allowed_values)
            )

        self._license = license

    @property
    def repository(self):
        """Gets the repository of this Service.

        The place where the code lives  # noqa: E501

        :return: The repository of this Service.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Service.

        The place where the code lives  # noqa: E501

        :param repository: The repository of this Service.
        :type repository: str
        """

        self._repository = repository

    @property
    def description(self):
        """Gets the description of this Service.

        A short, one-sentence summary of the service  # noqa: E501

        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Service.

        A short, one-sentence summary of the service  # noqa: E501

        :param description: The description of this Service.
        :type description: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def author(self):
        """Gets the author of this Service.

        The author of the service  # noqa: E501

        :return: The author of this Service.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Service.

        The author of the service  # noqa: E501

        :param author: The author of this Service.
        :type author: str
        """

        self._author = author

    @property
    def author_email(self):
        """Gets the author_email of this Service.

        The email address of the author  # noqa: E501

        :return: The author_email of this Service.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this Service.

        The email address of the author  # noqa: E501

        :param author_email: The author_email of this Service.
        :type author_email: str
        """

        self._author_email = author_email

    @property
    def url(self):
        """Gets the url of this Service.

        The URL to the homepage of the service  # noqa: E501

        :return: The url of this Service.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Service.

        The URL to the homepage of the service  # noqa: E501

        :param url: The url of this Service.
        :type url: str
        """

        self._url = url